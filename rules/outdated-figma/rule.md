---
type: rule
title: Do you clearly indicate outdated Figma design files?
seoDescription: Help teammates spot outdated Figma designs by labelling the status, pointing to production as the source of truth, and naming who can update the file.
uri: outdated-figma
authors:
  - title: Tiago Araujo
    url: https://www.ssw.com.au/people/tiago-araujo
  - title: Ken Shi
    url: https://www.ssw.com.au/people/ken-shi
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
created: 2025-11-07T22:01:55.000Z
guid: 09e02bd6-5834-4e46-a5e6-aa7b5c35774e
related:
  - zz-files
---

When a Figma file falls out of sync with the product, new team members (or clients) can quickly build the wrong mental model of how the app works today. A fast visual cue that indicates the mock-up is stale saves hours of rework and prompts people to validate the real experience in production.

<!--endintro-->

## Spot outdated designs fast

When a Figma design is no longer the source of truth, make it unmistakably clear:

1. **Move outdated work to an Archive section** – Add a divider or use a clear naming pattern (e.g. a `zz` prefix) so old pages naturally sink to the bottom and stay separate from live work

2. **Add a locked status banner** – Drop a top-of-frame callout (e.g. a red ⚠️ warning or a “Deprecated” badge) that says: “Out of date — refer to production {{ LINK }}”. Lock it so it can’t be hidden

3. **Link to the production source** – Always include the real live version so there’s no confusion about where the truth lives

4. **Document who maintains it** – Add a small note like “Maintainers: {{ DESIGNER }}” so everyone knows who to @mention for updates, even on free plans

These simple cues make outdated designs obvious, prevent accidental reuse, and clearly point the team to the current production experience.
