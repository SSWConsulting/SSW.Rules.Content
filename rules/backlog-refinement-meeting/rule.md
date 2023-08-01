---
type: rule
title: Do you have a Product Backlog Refinement meeting?
uri: backlog-refinement-meeting
authors:
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair/
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
related:
  - 8-steps-to-scrum
  - defining-pbis
  - have-a-definition-of-ready
created: 2023-08-01T05:00:34.793Z
guid: e7fc1823-dc9b-4fc1-b5bd-b7ac6424c336
---


When a Scrum Team meets for Sprint Planning, they want to plan out the next week's work so they can get cracking on building an awesome Product. However, the team often runs into a roadblock when they find that the Product Backlog Items (PBIs) are lacking in basic details. This problem leads to 1 of 2 outcomes:
- **Potential Outcome 1:** Poorly defined PBIs being added to the Sprint causing problems with shaky estimates and later down the track when developers are unclear about the PBI details and how to implement them.
- **Potential Outcome 2:** A lengthy Sprint Planning meeting with only a few people engaged.



<!--endintro-->





## The Solution - Product Backlog Refinement meetings

A Product Backlog Refinement meeting can help address these issues. In this meeting, the Tech Lead and another developer refine all the PBIs. This process involves refining the PBIs in the backlog and adding a "Ready" tag or status when the PBI has met the [Definition of Ready](have-a-definition-of-ready)

To ensure the Product Backlog Refinement meeting runs. Setup a recurring meeting with the following content:

::: email-template
|          |     |
| -------- | --- |
| To:      | {{ TECH LEAD }}, {{ CHOSEN DEVELOPER }} |
| Cc:      | {{ REST OF THE SCRUM TEAM }} |
| Recurrence:      | {{ ONCE PER SPRINT }} |
| Subject: | Product Backlog Refinement –  {{ PROJECT NAME }} |
::: email-content 

This meeting is to perform Product Backlog Refinement.

Product Backlog: {{ LINK TO PRODUCT BACKLOG }}

Agenda
1. Skip all PBIs that are marked as ready already
2. Refine the top 5 PBIs that are not marked as ready. 
    - Call in the Product Owner if any feature requires requirements clarification.
3. Check if any PBIs need to be added
4. Check if any PBIs need to be deleted
    - Call in the Product Owner to double check

:::



## Benefits of Product Backlog Refinement

- **Efficient Sprint Planning**: With most PBIs already refined, the Sprint Planning meeting becomes more efficient.
- **Less time wastage**: Only the Tech Lead and another developer are required for most of refinement, so other people's time can be utilised elsewhere instead of wasted waiting around.

- **Engaged Developers**: Developers are more likely to stay engaged when meetings are shorter and more focused.
- **Well-Defined PBIs**: PBIs are well-defined before being added to the Sprint.

