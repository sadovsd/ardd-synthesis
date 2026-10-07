"""Save YouTube auto-captions for each talk as weeks/week_N/transcripts/<talk>_transcript.md.

Talks that already have a transcript are skipped.

    python scripts/get_transcripts.py                 # all weeks
    python scripts/get_transcripts.py week_6          # just some weeks
"""
import glob
import os
import re
import subprocess
import sys
import tempfile

from talks import talks

TIMESTAMP = re.compile(r"(\d+):(\d+):(\d+)\.\d+ -->")


def vtt_to_text(path):
    """Collapse YouTube's rolling captions into paragraphs, with a [mm:ss] marker about once a minute."""
    out, cur, prev, last_t, t = [], [], None, None, 0
    for ln in open(path).read().splitlines():
        m = TIMESTAMP.match(ln)
        if m:
            t = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
            continue
        if not ln.strip() or "<" in ln or ln.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        ln = ln.strip()
        if ln == prev:
            continue
        prev = ln
        if last_t is None or t - last_t >= 60:
            if cur:
                out.append(" ".join(cur))
            cur, last_t = [f"**[{t // 60:02d}:{t % 60:02d}]**"], t
        cur.append(ln)
    if cur:
        out.append(" ".join(cur))
    return "\n\n".join(out)


def main(weeks):
    tmp = tempfile.mkdtemp()
    for week_dir, stem, vid in talks(weeks):
        out = os.path.join(week_dir, "transcripts", f"{stem}_transcript.md")
        if os.path.exists(out):
            continue
        title = subprocess.run(
            [sys.executable, "-m", "yt_dlp", "--ignore-no-formats-error", "--skip-download", "--no-warnings",
             "--write-subs", "--write-auto-subs", "--sub-langs", "en-orig,en", "--sub-format", "vtt",
             "--print", "title", "--no-simulate", "-o", f"{tmp}/{vid}.%(ext)s", "--", vid],
            capture_output=True, text=True).stdout.strip().splitlines()
        vtts = glob.glob(f"{tmp}/{vid}.en-orig.vtt") or glob.glob(f"{tmp}/{vid}.en*.vtt")
        if not vtts:
            print(f"no English captions: {stem}")
            continue
        body = vtt_to_text(vtts[0])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(f"# {title[0] if title else stem}\nhttps://www.youtube.com/watch?v={vid}\n\n"
                    "_YouTube auto-generated captions (unedited — expect misheard names/terms). "
                    f"Timestamps every ~60s._\n\n{body}\n")
        print(f"saved {os.path.relpath(out, os.path.dirname(os.path.dirname(week_dir)))} ({len(body.split())} words)")


if __name__ == "__main__":
    main(sys.argv[1:] or None)
