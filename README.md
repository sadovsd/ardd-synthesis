# ARDD Synthesis

A personal knowledge base built from the Aging Research and Drug Discovery (ARDD) YouTube channel.

## Goals

- Use individual ARDD talks as entry points into aging biology subfields. Look more deeply into a few papers associated with each talk.
- Distill key concepts and themes from each talk in my own words.
- Keep a record of both biological and computational/mathematical methods used in each paper.
- Keep a record of data sources used in each paper.
- Potentially replicate an analysis or pipeline.
- Connect ideas across speakers — where do they agree, disagree, or talk past each other.
- Surface open questions worth exploring further.

## Structure

Work is organized by **week**. Each week collects the talks watched that week plus the methods and content ideas that came out of them.

```
weeks/
  week_0/
    talks/            one .md per ARDD talk — concepts, key ideas, background, future directions
    methods.md        statistical / mathematical / computational methods across the week
    content_ideas.md  twitter posts, reels, shorts
    images/
      <speaker>/      photos and figures for each talk
synthesis/            cross-talk / cross-week connections, added periodically
  synthesis.md
  images/
templates/
  week_template/      copy this to weeks/week_N to start a new week
```

### Starting a new week

```
cp -R templates/week_template weeks/week_N
```

Then duplicate `talks/_talk_template.md` into one file per talk, add an `images/<speaker>/` folder for that talk's figures, and fill in `methods.md` and `content_ideas.md` as you go.

## Current contents

- **[week_0](weeks/week_0/)** — Fedichev (biophysics of aging), Hoeijmakers (DNA repair & the growth–maintenance trade-off), Schumacher, Kirkland, Niedernhofer, Merad, Vaswani, Paul Robbins.

## Status

Living document. Updated as I go.
