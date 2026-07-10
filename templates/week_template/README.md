# Week template

Copy this whole folder to `weeks/week_N/` to start a new week:

```
cp -R templates/week_template weeks/week_N
```

Then:
- Rename/duplicate `talks/_talk_template.md` into one file per talk (e.g. `talks/lastname.md`).
- Add a per-talk image folder under `images/<speaker>/` for that talk's photos and figures.
- Fill in `methods.md` (stats/math/computational methods for the whole week) and `content_ideas.md` (twitter/reels/shorts) as you go.

## Layout

```
week_N/
  talks/            one .md per ARDD talk (concepts, key ideas, background, future directions)
  methods.md        statistical / mathematical / computational methods across the week
  content_ideas.md  twitter posts, reels, shorts
  images/
    <speaker>/      photos and figures for each talk
```
