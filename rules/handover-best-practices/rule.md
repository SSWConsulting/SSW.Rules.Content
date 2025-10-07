---
type: rule
tips: ""
title: Do you leave a project ready for the next person?
seoDescription: Make your handovers smooth and useful by planning with your successor in mind, whether you're going on leave or leaving the project permanently.
uri: handover-best-practices
authors:
  - title: Betty Bondoc
    url: https://www.ssw.com.au/people/betty-bondoc/
related:
  - bus-test
  - hand-over-projects
guid: 95b188ce-a802-4e25-b467-ae580aea89c0
---

A poorly planned handover can result in wasted time, repeated work, and confusion for the person taking over. Imagine walking into a project with no context, outdated documentation, and a scattering of files across different systems. It’s frustrating and it’s preventable.

<!--endintro-->

There’s no one-size-fits-all template for a handover. It should be tailored to your project, your role, and whether the handover is temporary (e.g. vacation) or permanent (e.g. project transition). But you should always **plan from the perspective of the person receiving the handover**.

## Ensure access is sorted early

The first blocker for any new person is access. Remove that hurdle by organizing:

* Credentials stored securely (e.g. password manager)
* Permissions to systems, tools, folders, and environments

Coordinate with sysadmins or clients in advance to avoid blockers.

## Organize files into a single source of truth

Don’t leave your successor scavenging for files. If your team doesn’t already have a designated location for handover assets, create a central folder (e.g. SharePoint or a shared drive) and include:

* Design files (e.g. Figma)
* Project documentation
* Code repositories
* Backlogs and task lists
* Secured credentials

At the root level, add a `_instructions.md` or `README` to explain the folder structure and what each file contains.

::: greybox

/Project-Handover

├── _instructions.md

├── Designs (links to Figma)

├── Docs

  └── 01_Architecture.md

├── Code (links to repos)

└── Tasks (exported backlog, priority list)

:::

::: good
Figure: Good example – A structured handover folder with an index file for guidance
:::

If your team already has a defined location (like a client-managed drive or internal system), follow that instead and just make sure your files are up to date and easy to navigate.

## Document what’s not obvious

Some things just won’t be clear by looking at files. Write down:

* Current project status and objectives
* Key decisions and why they were made
* Trade-offs, assumptions, and constraints
* Known issues, risks, and technical debt
* Outstanding or partially completed tasks

Good documentation avoids repeated questions and poor decisions.

## Turn future work into actionable tickets

Don’t leave future tasks buried in meeting notes or your memory. If follow-ups are expected from workshops, client discussions, or ongoing work, **log them now**.

Make each ticket clear and self-contained:

* Include context, relevant links (e.g. designs, documents), and rationale
* Reference key discussions or decisions in the comments
* Flag priorities with the Product Owner

This ensures nothing falls through the cracks and gives your successor a clear path forward, with everything they need in one place.

## Share recordings that matter

In some cases, a short video is more helpful than a wall of text. Add:

* Demo recordings
* Workshop walkthroughs
* Relevant meeting sessions

Label each video clearly with what it covers and why it’s useful.

## Send a mini-onboarding email

New joiners can feel overwhelmed. Help them ramp up with a structured welcome message that links them to the right places and explains what to do first.

::: email-template

| | |
| -------- | ---------------------------------- |
| To: | John |
| Subject: | Project Handover – Getting Started |

::: email-content

Hi John,

Welcome to the project! 🎉

Here’s a quick guide to help you get set up and familiar with everything:

* **Project Summary** → {{ LINK }}
* **Architecture Overview** → {{ LINK }}
* **Active Backlog / Tasks** → {{ LINK }}
* **Design Files** (Figma, etc.) → {{ LINK }}
* **Project Folder** → {{ LINK }}
* **Key Documentation** → {{ LINK }} (includes index or must-read docs)
* **Team Directory** → {{ LINK }}

Let me know if anything’s unclear or if you need help with access.

Regards,  

:::
:::

::: good
Figure: Good example – A clear onboarding email helps reduce first-day confusion
:::

## Run a handover walkthrough

Book a live session to:

* Walk through the file structure
* Show designs, workflows, or code
* Answer any questions they may have

Make it conversational, not just a reading of your notes.

## Connect them with the right people

Introduce your successor to:

* Product Owners
* Sysadmins
* Key team members

::: info
**Bonus:** Share cultural context like who’s approachable, communication norms, or anything helpful to avoid social blind spots (no bias or gossip!).
:::

---

By thinking of your handover as a **user experience** for your successor, you help ensure the transition is clear, respectful, and productive for everyone.
