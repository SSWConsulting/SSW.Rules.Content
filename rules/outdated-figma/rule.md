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

When a Figma file falls out of sync with the product, new team members (or clients) can quickly build the wrong mental model of how the app works today. A fast visual cue that says “this mock-up is stale” saves hours of rework and prompts people to validate the real experience in production.

<!--endintro-->

## Spot outdated designs fast

Follow this checklist whenever a design is no longer the source of truth:

1. **Rename the page with a `zz` prefix and the status** – e.g. `zz ⛔ Archived – Checkout (see Production)` so it sinks to the bottom of the Pages panel and instantly signals it’s not live
2. **Drop in a status banner component** – Add a top-of-frame component (e.g. a red ⚠️ callout or your design system’s "Deprecated" badge) that states “Out of date – refer to production link below”. Lock it so it cannot be hidden accidentally
3. **Link to the real experience** – Include the production URL, feature flag, or screenshots that reflect how it works today so reviewers can confirm the current behaviour
4. **Document who can update it** – Add a text block such as “Maintainers: {{ DESIGNER }} with @mentions. This answers “who do I ping for edits?” for viewers on free plans

## Keep a "Status" page at the top

Create a dedicated first page called `00 🔖 Status & Contacts` that contains:

* A legend of the icons / colours you use for **Draft**, **In progress**, **In review**, and **Archived**
* A table listing each product area with links to the current source of truth (e.g. Prod URL, Storybook, Confluence spec) and the Figma page name
* Contact details (Teams/Email) for the maintainers and a reminder that only paid editors can move things out of “Archived”

Because the Status page is at the top, newcomers land on it first and learn how to interpret the rest of the file.

## Automate reminders where you can

* Add a repeating calendar or Teams reminder every sprint to review `zz` pages and confirm whether they can be updated or removed
* Use Figma’s [description field](https://help.figma.com/hc/en-us/articles/360039222353-File-browser-in-Figma#h_01FRVW65PWEY8NKRBY8NVGP5RB) to summarize the status and link to the production build notes
* If you use design system components, publish a “Deprecated” variant so it’s visually obvious when someone drags an outdated component into a fresh mock-up

These lightweight cues make it obvious which designs are outdated while telling the team where the true behaviour lives.
