---
type: rule
archivedreason:
title: Do you have a Bench Master?
guid: 2406ab97-055d-45a8-a90a-62764a704a16
uri: bench-master
created: 2023-08-03T13:00:00.0000000Z
authors:
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Ruby Cogan
    url: https://ssw.com.au/people/ruby-cogan
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related:
  - know-where-your-staff-are
  - streamline-approvals
redirects: []
---

In any organization that juggles multiple projects, having clear coordination and allocation of resources is essential. The role of a "Bench Master" is critical in ensuring a smooth transition for developers between client projects, minimizing downtime, and promoting ongoing learning and development.

<!--endintro-->

## What does a Bench Master do?

A Bench Master's primary responsibility is to ensure that all developers know what they are working on when they are not on client projects. In order to accomplish this, the Bench Master has these responsibilities:

1. Responsibility - This role is a Bench Masters number 1 responsibility
2. Responsibility - Allocating new employees or employees finished on a project to a Scrum team
   * The Bench Master should make the internal booking for the developer
   * Tip: Starting on a new project is costly, try not move developers too frequently
   * Customer bookings override any internal projects
   * Customer bookings should not be last minute, they should ideally be 1 day in advance
3. Responsibility - Maintaining a list of internal projects in priority order
4. Responsibility - Scrum Master for the Small Projects Team
5. Professional development - Allocating people projects based on what they want to learn
6. Coaching - The Bench Master should coach Product Champions around the Scrum ceremonies
7. Process - Across all internal projects at a high level
8. Process - Knowing the priority of internal projects
9. Process - Knowing what skills are required for each project
10. Process - Bench Backup - Keep someone in the loop for when Bench Master is unavailable
11. Process - Weekly meeting with important stakeholders to talk about priorities
12. Process - Morning meeting for anyone not on client work
    * This is for people not already assigned to an internal project or have finished work on an internal project
    * You should make sure this happens across all timezones

Some other terms that are commonly used for this type of role are:

* Bench Coordinator
* Resource Coordinator
* Operations Manager
* Allocation Manager
* Capacity Manager
* Scheduling Manager

## How do developers know what to work on?

Developers love certainty, it's important for them to know what projects they'll be working on in-between client projects. Knowing in advance what projects they'll be working on minimizes the time it takes to get up to speed on a project as they could be looped into communications for the project before they start so they have some recent context when they join.

As you can imagine there is a lot of information that would be required for a Bench Master to be effective. The following would be useful for a Bench Master to have:

* **Developers and their skills** - Your CRM likely has this information already
  * see [https://www.ssw.com.au/rules/search-employee-skills/](/search-employee-skills/)
* **Developer client bookings** - You can get this information from your staffing report,
  * see [https://www.ssw.com.au/rules/know-where-your-staff-are/](/know-where-your-staff-are/)
* **Internal projects** - It's important to know their priorities as well as tech stacks, if it's a big project, knowing the actively developed portions tech stack would be helpful
  * see [https://www.ssw.com.au/rules/report-bugs-and-suggestions/#tip-5-do-you-make-it-easy-to-find-all-the-backlog-in-your-company](/report-bugs-and-suggestions/#tip-5-do-you-make-it-easy-to-find-all-the-backlog-in-your-company)
* **Developer bench bookings** - Your staffing should be able to tell you which developers are working on which internal projects

This covers the basics of what a Bench Master would need to know, there is other factors that would influence the Bench Master's decisions such as developer personal goals. For example, if a developer wants to learn React, the Bench Master could try place the developer on a project that uses React.

![Figure: Developers can add Keen to Learn skills in CRM | Users | {{ User }} | Skills to inform the Bench Master](keen-to-learn-skills.png)

Here are some considerations the Bench Master would keep in mind for every developer:

1. Client needs - Is there any client work that tentatively needs the developer?
2. Time between now and next client?
3. Inbox count?
   * see [https://www.ssw.com.au/rules/dones-is-your-inbox-a-task-list-only/](/dones-is-your-inbox-a-task-list-only/)
4. Current skillset
5. Personal Development Time
   * Check Long Term goal tracker e.g. Trello board, anything important? Anything doable in the time between now and next client?
   * Are there any languages you want to learn? "I want to learn Blazor please" (Bench Master puts person on Blazor project)
6. Internal Projects - What is most important?
7. Internal Projects - What teams are looking for a Dev?

## What happens when the Bench Master is not available?

Ensuring seamless continuity of operations in the absence of the Bench Master is essential for [streamlining approvals](/streamline-approvals).

* The backup Bench Master should be someone who is familiar with the internal projects and the skills of the developers.
* A semi-regular catchup between the Bench Master and the backup Bench Master would be a good idea to ensure that the backup Bench Master is up to date with the current state of the bench.
* Always CC a distribution list that has the Bench Master and backup Bench Master on any emails regarding the bench.
* If the Bench Master knows they will be unavailable for a period of time they should ask the backup Bench Master to monitor the distribution list for any emails regarding the bench.

::: info
**Tip:** If you have multiple offices, consider having a backup Bench Master that covers each timezone you have an office location
:::

## Limiting the number of internal teams

Projects should be broken down according to size and scope:

* Long projects (>4 weeks) with >3 active developers should be run as a separate team. Every standalone project should have a Product Champion.
* Other projects should form a single team. This team is Scrum Mastered by the Bench Master. This allows the developers to maintain adapted process ceremonies and while still working on different products, see [Do you ensure your client projects who don't use full Scrum, at least have a "Mini-Review"?](/who-dont-use-full-scrum-should-have-a-mini-review). This team should adapt the standard Scrum emails ([Do you create a Sprint Review/Retro email?](/sprint-review-retro-email)) to send a collective email to internal stakeholders after every Sprint. This team should still do a retro as the nature of their more ad-hoc environment will help them be more effective.
