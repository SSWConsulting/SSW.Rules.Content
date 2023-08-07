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
related: 
  - know-where-your-staff-are
redirects: []

---

In any organization that juggles multiple projects, having clear coordination and allocation of resources is essential. The role of a "Bench Master" is critical in ensuring a smooth transition for developers between client projects, minimizing downtime, and promoting ongoing learning and development.

<!--endintro-->

## What does a Bench Master do?

A Bench Master's primary responsibility is to ensure that all developers know what they are working on when they are not on client projects. In order to accomplish this, the Bench Master has these responsibilities:

- Responsibility - Allocating a Scrum team to new employees or employees finished on a project
  - The Bench Master should make the internal booking for the developer
  - Developers should not be switched to new projects shorter than 4 weeks (excluding client bookings)
  - Customer bookings would override any internal project bookings
  - Customer bookings should be made at least a day in advance
- Responsibility - Maintaining a list of internal projects
- Responsibility - Scrum Master for the Small Projects Team
- Professional development - Allocating people projects based on what they want to learn
- Process - Across all internal projects at a high level
- Process - Knowing the priority of internal projects
- Process - Knowing what skills are required for each project
- Process - Bench Backup - Keep someone in the loop for when Bench Master is unavailable
- Process - Weekly meeting with important stakeholders to talk about priorities
- Process - Office specific morning meeting for anyone not on client work, 
  - This is for people not already assigned to an internal project or have finished work on an internal project

Some other terms that are commonly used for this type of role are:

- Bench Coordinator
- Resource Coordinator
- Operations Manager
- Allocation Manager
- Capacity Manager
- Scheduling Manager

## How do developers know what to work on?

Developers don't like uncertainty, it's important for them to know what projects they'll be working on in-between client projects. Knowing in advance what projects they'll be working on minimizes the time it takes to get up to speed on a project as they could be looped into communications for the project before they start so they have some recent context when they join.

As you can imagine there is a lot of information that would be required for a Bench Master to be effective. The following is a list of information that would be useful for a Bench Master to have.

- **Developers and their skills** - Your CRM likely has this information already, see https://www.ssw.com.au/rules/search-employee-skills/
- **Developer client bookings** - You can get this information from your staffing report, see https://www.ssw.com.au/rules/know-where-your-staff-are/
- **Internal projects** - It's important to know their priorities as well as tech stacks, if it's a big project, knowing the actively developed portions tech stack would be helpful
- **Developer bench bookings** - Your staffing should be able to tell you which developers are working on which internal projects

This covers the basics of what a Bench Master would need to know, there is other factors that would influence the Bench Master's decisions such as developer personal goals. For example, if a developer wants to learn react, the Bench Master could try place the developer on a project that uses react.

![Figure: Developers can add Keen to Learn skills in CRM to inform the Bench Master](keen-to-learn-skills.png)

Here's some inputs the Bench Master would consider for each developer:

- Client needs - Is there any client work that tentatively needs the developer?
- Internal Projects - What is most important? 
- Internal Projects - What teams are looking for a Dev?
- Current skillset
- Time between now and next client?
- Inbox count? see https://www.ssw.com.au/rules/dones-is-your-inbox-a-task-list-only/
- Check Long Term goal tracker e.g. Trello board, anything important? Anything doable in the time between now and next client?
- Personal Development Time 
  - e.g. Are there any languages you want to learn? "I want to learn Blazor please" (Bench Master puts person on Blazor project)

## What happens when the Bench Master is not available?

It's important to have a backup Bench Master in case the Bench Master is not available. 

- The backup Bench Master should be someone who is familiar with the internal projects and the skills of the developers. 
- A semi-regular catchup between the Bench Master and the backup Bench Master would be a good idea to ensure that the backup Bench Master is up to date with the current state of the bench.
- Always CC a distribution list that has the Bench Master and backup Bench Master on any emails regarding the bench.
- If the Bench Master knows they will be unavailable for a period of time they should ask the backup Bench Master to monitor the distribution list for any emails regarding the bench.

::: info
**Tip:** If you have multiple offices, consider having a local backup Bench Master in every office location
:::

## Limiting the number of internal teams

In order to limit the amount of teams running projects, any products that don't have large (> 3 active developers) long running (> 4 weeks) projects should form a team and work on the adhoc tasks for those products as a single team. This allows the developers to maintain adapted process ceremonies and while still working on different products, see [Do you ensure your client projects who don't use full Scrum, at least have a "Mini-Review"?](/who-dont-use-full-scrum-should-have-a-mini-review)

This team should adapt the standard scrum emails ([Do you create a Sprint Review/Retro email?](/do-you-create-a-sprint-review-retro-email)) to send a collective email to internal stakeholders after every sprint. This team should still do a retro as the nature of their more adhoc environment will help them be more effective.
