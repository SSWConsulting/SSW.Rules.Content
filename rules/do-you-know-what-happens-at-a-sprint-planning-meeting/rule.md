---
type: rule
title: Do you know what happens at a Sprint Planning meeting?
uri: do-you-know-what-happens-at-a-sprint-planning-meeting
authors:
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/uly
related:
  - do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint
  - do-you-conduct-an-architecture-review-after-every-sprint
  - technical-debt
  - just-enough-refactoring
redirects: []
created: 2010-05-06T04:11:55.000Z
archivedreason: null
guid: f0bf4d20-cee6-4731-b343-603cf7db3e5d

---

The work to be performed in the Sprint is planned at the Sprint Planning meeting. At the Sprint Planning meeting, the following 3 questions are answered:

* Why is this Sprint valuable?
* What can be delivered in the increment(s) resulting from the upcoming Sprint?
* How will the work needed to deliver the increment(s) be achieved?

<!--endintro-->

### Why is this Sprint valuable?

The Product Owner proposes how the product could increase its value and utility in the current Sprint. The whole Scrum Team then collaborates to define a Sprint Goal that communicates why the Sprint is valuable to stakeholders.

What can be delivered in the Increment resulting from the upcoming Sprint?

[The Architecture Review](/do-you-conduct-an-architecture-review-after-every-sprint) should be conducted every few Sprints prior to the Sprint Planning to determine any tech improvements that can be implemented in the project.

[Technical Debt](/technical-debt) should be considered prior to the Sprint Planning, as it is imperative to address it. [Just Enough Refactoring](/just-enough-refactoring) should be used to solve the debt that directly surrounds or is impacted by the features included into the Sprint.

The Product Backlog is examined and the Product Owner makes changes so that it is prioritized with bugs prioritized amongst Product Backlog Items (PBIs).

The Product Owner is then asked to group the top ranking Bugs into PBIs for inclusion in the Sprint. See this [rule](/bugs-do-you-know-how-to-handle-bugs-on-the-product-backlog).

The Team are then advised of their resourcing for the Sprint as there may be additions, subtractions, leave or public holidays which are different to the previous Sprint. Considering their previous record and their current resources, The team decide on the number of story points that they will deliver in the forthcoming Sprint. When the team are not currently co-located this is often done by voting, and discussed until consensus is reached.

The team then size (assign Story points to) PBIs starting at the top until there are more than enough PBIs to fill the Sprint.

The process of sizing is somewhat formal. Either using cards or IM (essential if not co-located) the team vote privately on the size of the PBI. They can either:
- Use t-shirt sizes of XXS, XS, S, M, L, XL, XXL and XXXL or 
- Their equivalent number of story points for which we use the Doubling Series of 1, 2, 4, 8, 16 or 32. 
 
Once the differring votes are in, the Scrum Master asks the smallest and biggest voters to explain the reasons for their vote. Assumptions and omisions are quickly identified through discussions and the Scrum Master encourages discussion until consensus on the story points is reached. Any PBI voted at 16 or higher should be broken down into smaller stories; re-prioritized by the Product Owner and re-sized if necessary.

![Figure: A sample PBI based on the Microsoft Scrum process template for Azure DevOps](PBI.png)

Once enough stories are sized, the Product Owner is given the opportunity to re-prioritise now knowing the relative sizes. If more PBIs need then be sized then they are. The Scrum Master keeps everything going and facilitates negotiation between the team and the Product Owner until final priority is confirmed and the team commit to a number of stories and the meeting concludes.

This meeting should be timeboxed to an hour for every week in the Sprint. However, the Scrum Master must be sensitive to the meeting producing a workable result.

### Capacity Planning

It is important for Sprint capacity planning to be consistent across all teams. As such, there should be consistency in how many story points you allocate to a Sprint. It's unreasonable to think that someone will be able to work productively and consecutively for 8 hours straight on a particular task. For example, if a task is allotted a 4 for effort (8 hours), the developer will probably spend about 6 hours coding, and 2 of those 8 hours fixing bugs, communicating, or working on the admin side of things. Even if devs may try to factor these things into their estimation, a 20% buffer never hurts.

Therefore, a standard 1-week Sprint with 2 resources would have about 32 story points allocated.

**Note:** This is specifically for the first couple of Sprints in a project, until you get an average velocity that you can use for capacity planning moving forward.

### How will the work needed to deliver the Increment be achieved?

To answer the second question the team create tasks, with sub-tasks where necessary, for everything that needs to be done to implement the PBI. Every task and sub-task should be given an estimate in hours and the same value placed in the Remaining field.

No actual work on the Sprint should start until this planning is complete. It is these Remaining hours that determine the first value in the burndown chart which sets the Sprint on its way to completion. There must be no omissions or the team will start without an accurate burndown and we all know that "The team is nothing without a burndown".

The team should also ensure that the burndown chart is working and will be automatically sent to all members of the Scrum team overnight.   

The meeting concludes when The Team reports to the Scrum Master that their planning is complete and they are able to display the burndown chart.

Ideally this meeting is timeboxed to as many hours as there will be weeks in the Sprint. However, the Sprint Planning is so essential that it must continue to completion outside the meeting if necessary.  

It is not essential for the Product Owner or the Scrum Master to be present for the whole meeting but they must be available for consultation. The Scrum Master should formally close the meeting. 

Once this meeting is finished, the Scrum Master should email the Product Owner with a [forecast](/do-you-create-a-sprint-forecast-aka-the-functionality-that-will-be-developed-during-the-sprint).

::: greybox

In Scrum, there are 4 meetings in total that you need to know about:

* Sprint Planning meeting (Described on this page)
* [Scrum meeting (Daily standup)](/meeting-do-you-update-your-tasks-before-the-daily-scrum)
* [Sprint Review meeting](/do-you-know-what-happens-at-a-sprint-review-meeting)
* [Sprint Retrospective meeting](/do-you-know-what-happens-at-a-sprint-retrospective-meeting)

:::
