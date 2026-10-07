"""Save one screenshot per slide for each talk in weeks/week_N/presentation_screenshots/<talk>/.

Downloads the 1080p video (no audio) to a temp folder, extracts slides, removes duplicates with OCR,
writes index.md, then deletes the video. Talks that already have screenshots are skipped.
About 1.5-2 min per talk.

    python scripts/get_slides.py                      # all weeks
    python scripts/get_slides.py week_6               # just some weeks
    python scripts/get_slides.py --talk vera_gorbunova
"""
import argparse
import glob
import os
import subprocess
import sys
import tempfile
import time

import slides
from talks import talks

ap = argparse.ArgumentParser()
ap.add_argument("weeks", nargs="*", help="e.g. week_6 (default: all weeks)")
ap.add_argument("--talk", help="one talk, by note filename without .md")
args = ap.parse_args()

tmp = tempfile.mkdtemp()
for week_dir, stem, vid in talks(args.weeks or None, args.talk):
    outdir = os.path.join(week_dir, "presentation_screenshots", stem)
    if glob.glob(f"{outdir}/slide_*.jpg"):
        continue
    t0 = time.time()
    video = os.path.join(tmp, f"{vid}.mp4")
    subprocess.run([sys.executable, "-m", "yt_dlp", "-q", "--no-warnings", "-f", "137/bv*[height<=1080][ext=mp4]",
                    "-o", video, "--", vid])
    if not os.path.exists(video):
        print(f"download failed (YouTube sometimes rate-limits; rerun later): {stem}")
        continue
    try:
        slides.export(video, slides.detect(video), outdir)
        before, after = slides.dedupe(outdir)
    finally:
        os.remove(video)
    print(f"{os.path.basename(week_dir)}/{stem}: {after} slides ({before} before dedupe), {time.time() - t0:.0f}s")
