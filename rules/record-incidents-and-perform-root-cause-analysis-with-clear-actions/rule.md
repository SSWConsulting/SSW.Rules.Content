---
type: rule
title: Do you record incidents and perform root cause analysis with clear actions?
seoDescription: Ensure every high-impact incident is recorded, analysed for root cause, and followed by clear, actionable recommendations to prevent recurrence.
guid: 1f396318-534d-4a65-9559-7511edee75c1
uri: record-incidents-and-perform-root-cause-analysis-with-clear-actions
created: 2025-07-28T01:51:00.0000000Z
authors:
  - title: Nick Curran
    url: https://ssw.com.au/people/nick-curran
related:
  - continually-improve-processes
---

When high-impact incidents occur - such as website outages, data loss, or critical bugs in production - fixing the immediate issue isn't enough.

Without a structured process to capture what happened, identify the root causes, and implement improvements, the same problems can happen again. This rule defines a simple post-incident process to help teams learn from failure, prevent repeat issues, and improve software and business processes.

## Record the incident

As soon as possible, assign someone to record the key details:

* When was the issue first noticed?
* What symptoms were observed? (e.g. errors, downtime)
* Who responded, and when?
* What actions were taken?
* When and how was the incident resolved?

Capture these in a central place - if your monitoring system creates PBIs automatically, use comments in the ticket to log the incident timeline and key facts.

## Analyse the root cause

Hold a **blameless** post-incident review with everyone involved. Use structured techniques like:

* [5 Whys](https://en.wikipedia.org/wiki/Five_whys)
* [Fishbone diagram](https://en.wikipedia.org/wiki/Ishikawa_diagram)

::: info
**Tip:** Don't stop at technical causes - also consider process gaps, unclear responsibilities, or communication failures.
:::

## Document and implement recommendations

For each contributing factor, define clear and actionable recommendations:

* Describe the fix or change needed
* Link to related PRs, logs, or tasks

Each recommendation must have a dedicated PBI. The Product Owner is responsible for ensuring these PBIs are estimated, prioritised, and scheduled. Teams should review them during Sprint Planning or Backlog Refinement.

## Summary

A well-handled incident isn't just about restoring service - it's a chance to make meaningful improvements.

By recording incidents, analysing causes, and implementing clear actions, teams reduce risk, increase reliability, and turn failures into progress.
