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
---

When a Figma file falls out of sync with the product, new team members (or clients) can quickly build the wrong mental model of how the app works today. A fast visual cue that indicates the mock-up is stale saves hours of rework and prompts people to validate the real experience in production.

<!--endintro-->

## Spot outdated designs fast

Follow this checklist whenever a design is no longer the source of truth:

1. **Rename the page with a `zz` prefix and the status** – e.g. `zz ⛔ Archived – Checkout (see Production)` so it sinks to the bottom of the Pages panel and instantly signals it’s not live
2. **Drop in a status banner component** – Add a top-of-frame component (e.g. a red ⚠️ callout or your design system’s "Deprecated" badge) that states “Out of date – refer to production {{ LINK }}”. Lock this so it cannot be hidden accidentally
3. **Link to the production URL**
4. **Document who can update it** – Add a text block such as “Maintainers: {{ DESIGNER }} with @mentions. This answers “who do I ping for edits?” for viewers on free plans

These lightweight cues make it obvious which designs are outdated while telling the team where the true behaviour lives.
