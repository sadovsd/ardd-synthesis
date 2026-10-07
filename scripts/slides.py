"""Pick one frame per slide from a talk video, then clean up duplicates with OCR.

Pass 1 (detect): sample the video at 1 fps as tiny grayscale thumbnails, ignore pixels that change constantly
(speaker / camera regions), find stretches where the rest of the frame holds still for >= 3 s, and keep one
frame per distinct stretch. Slide builds collapse into the finished slide.

Pass 2 (dedupe): camera pans/zooms and a speaker walking in front of the screen fool pass 1, so OCR every
saved frame and merge neighbours with the same text (or where one's text contains the other's). Text-poor
frames (photos, camera shots) only merge when nearly pixel-identical: a leftover duplicate beats a lost slide.
Writes index.md (slide -> time -> OCR'd title).
"""
import glob
import os
import re
import subprocess
from collections import Counter

import numpy as np
from PIL import Image, ImageFilter

W, H = 160, 90


# ---------- pass 1: detect slide changes in the video ----------

def frames(video):
    p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", video, "-vf", f"fps=1,scale={W}:{H},format=gray",
                          "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    while (buf := p.stdout.read(W * H)) and len(buf) == W * H:
        yield np.frombuffer(buf, np.uint8).astype(np.float32)
    p.wait()


def detect(video, stable_diff=2.0, new_slide_diff=6.0, min_len=3):
    """Return the second of each distinct slide."""
    raw = np.stack(list(frames(video)))
    # ignore pixels that change often (speaker / camera); slide pixels only change at slide turns
    activity = (np.abs(np.diff(raw, axis=0)) > 12).mean(axis=0)
    mask = activity < 0.06
    if mask.mean() < 0.3:  # mostly moving picture: fall back to masking a bottom-right speaker inset
        mask = np.ones((H, W), bool)
        mask[int(H * .74):, int(W * .81):] = False
        mask = mask.ravel()
    f = [x[mask] for x in raw]
    segs, start = [], 0
    for i in range(1, len(f) + 1):
        if i == len(f) or np.abs(f[i] - f[i - 1]).mean() > stable_diff:
            if i - start >= min_len:
                segs.append((start, i - 1))
            start = i
    keep, last = [], None
    for _, e in segs:
        rep = f[e]  # last frame of the still stretch = fully built slide
        if last is None or np.abs(rep - last).mean() > new_slide_diff:
            keep.append(e)
        else:
            keep[-1] = e  # same slide continued (animation build) -> take the later frame
        last = rep
    return keep


def export(video, seconds, outdir):
    os.makedirs(outdir, exist_ok=True)
    for n, t in enumerate(seconds, 1):
        name = f"slide_{n:03d}_{t // 60:02d}m{t % 60:02d}s.jpg"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", video, "-frames:v", "1",
                        "-q:v", "2", os.path.join(outdir, name)], check=True)


# ---------- pass 2: OCR-based duplicate cleanup ----------

def _small(path, w=192, h=108):
    return np.asarray(Image.open(path).convert("L").resize((w, h)).filter(ImageFilter.GaussianBlur(1)), np.float32)


def pixel_dist(a, b, shift=8):
    """Fraction of pixels differing (>30 grey levels) after the best small shift and +/-5% zoom."""
    h, w = a.shape
    best = 1.0
    for z in (1.0, 1.05, 1 / 1.05):
        bz = b
        if z != 1.0:
            bz = np.asarray(Image.fromarray(b.astype(np.uint8)).resize((round(w * z), round(h * z))), np.float32)
            y0, x0 = (bz.shape[0] - h) // 2, (bz.shape[1] - w) // 2
            if z > 1:
                bz = bz[y0:y0 + h, x0:x0 + w]
            else:
                bz = np.pad(bz, ((-y0, h - bz.shape[0] + y0), (-x0, w - bz.shape[1] + x0)), mode="edge")
        for dy in range(-shift, shift + 1, 2):
            for dx in range(-shift, shift + 1, 2):
                A = a[max(dy, 0):h + min(dy, 0), max(dx, 0):w + min(dx, 0)]
                B = bz[max(-dy, 0):h + min(-dy, 0), max(-dx, 0):w + min(-dx, 0)]
                best = min(best, (np.abs(A - B) > 30).mean())
    return best


def _ocr(path):
    from ocrmac import ocrmac  # macOS Vision OCR
    res = [(t, b) for t, c, b in ocrmac.OCR(path, recognition_level="accurate").recognize() if c > 0.4]
    words = {w.lower() for t, _ in res for w in re.findall(r"[A-Za-z]{3,}", t)}
    top = sorted((r for r in res if len(r[0]) > 3), key=lambda r: -(r[1][1] + r[1][3]))  # Vision y: 1 = top
    return words, (top[0][0] if top else "")


def _same_slide(a, b, path_a, path_b):
    wa, wb = a[0], b[0]
    if len(wa) >= 4 and len(wb) >= 4:
        inter = len(wa & wb)
        return inter / len(wa | wb) >= 0.8 or inter / min(len(wa), len(wb)) >= 0.9
    return pixel_dist(_small(path_a), _small(path_b)) < 0.06


def dedupe(outdir):
    files = sorted(glob.glob(f"{outdir}/slide_*.jpg"))
    info = [_ocr(f) for f in files]
    # words on most frames (stage banner, logos, footers) say nothing about which slide it is
    freq = Counter(w for ws, _ in info for w in ws)
    common = {w for w, c in freq.items() if len(files) >= 8 and c / len(files) > 0.4}
    info = [(ws - common, t) for ws, t in info]
    keep = []
    for i in range(len(files)):
        if keep and _same_slide(info[keep[-1]], info[i], files[keep[-1]], files[i]):
            keep[-1] = i  # same slide: keep the later, more fully built frame
        else:
            keep.append(i)
    for i in set(range(len(files))) - set(keep):
        os.remove(files[i])
    rows = []
    for n, i in enumerate(keep, 1):
        ts = os.path.basename(files[i]).split("_", 2)[2][:-4]
        new = os.path.join(outdir, f"slide_{n:03d}_{ts}.jpg")
        os.rename(files[i], new)
        title = info[i][1].replace("|", "/") if len(info[i][0]) >= 4 else "_(little/no text: image or camera shot)_"
        rows.append(f"| [{n:03d}]({os.path.basename(new)}) | {ts.replace('m', ':').rstrip('s')} | {title} |")
    with open(os.path.join(outdir, "index.md"), "w") as f:
        f.write(f"# Slides: {os.path.basename(outdir)}\n\n_Auto-extracted frames; titles via OCR (may contain errors)._\n\n"
                "| # | time | title |\n|---|---|---|\n" + "\n".join(rows) + "\n")
    return len(files), len(keep)
