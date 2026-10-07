"""Find talk notes (weeks/week_*/*.md) and the YouTube video each one is about."""
import glob
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEEKS = os.path.join(REPO, "weeks")

# Notes that don't contain their YouTube link. Adding the link to the note works too.
VIDEO_ID_OVERRIDES = {
    "vadim_gladyshev": "6ZFkZG0Tr0I",
    "alexander_tyshkovskiy_2025": "pLKQcfdA5HQ",
}


def talks(weeks=None, only=None):
    """Yield (week_dir, stem, video_id) for each note with a YouTube link.

    weeks: e.g. ["week_4"] to limit to some weeks. only: a single note stem, e.g. "vera_gorbunova".
    The stem is the note's filename without .md and with spaces removed; it names the output files.
    """
    for note in sorted(glob.glob(f"{WEEKS}/week_*/*.md")):
        week_dir = os.path.dirname(note)
        if weeks and os.path.basename(week_dir) not in weeks:
            continue
        stem = os.path.basename(note).split(".md")[0].replace(" ", "")
        if only and stem != only:
            continue
        m = re.search(r"watch\?v=([A-Za-z0-9_-]{11})", open(note).read())
        vid = m[1] if m else VIDEO_ID_OVERRIDES.get(stem)
        if vid:
            yield week_dir, stem, vid
        else:
            print(f"skip (no YouTube link): {os.path.relpath(note, REPO)}")
