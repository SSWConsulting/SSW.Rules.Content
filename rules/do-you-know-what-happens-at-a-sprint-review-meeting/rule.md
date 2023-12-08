---
type: rule
title: Do you know what happens at a Sprint Review meeting?
uri: do-you-know-what-happens-at-a-sprint-review-meeting
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - sprint-review-retro-email
  - do-you-make-your-team-meetings-easy-to-find
  - tick-and-flick
  - explaining-pbis
  - getting-a-busy-person-into-the-meeting
redirects: []
created: 2010-05-06T02:07:33.000Z
archivedreason: null
guid: 863b6968-c082-4413-b90d-d68e0211adc5
---

This is the meeting where the Product Owner accepts or rejects the stories in the Sprint and the Sprint itself.

<!--endintro-->

The Team, having [prepared](/meeting-do-you-know-what-to-prepare-for-each-meeting) for the meeting, presents the stories to the Product Owner.

One person, often the Scrum Master, presents a summary to the Product Owner of the stories committed at the Sprint Planning meeting and the stories being presented for acceptance.  The Team seeks to have more stories accepted than originally committed.  It is important that the Product Owner knows at the beginning whether The Team believe that they have over or underachieved the Sprint Goal.

Each story is then presented by the Team for acceptance. They aim to get the Story accepted as quickly as possible ([aka tick and flick](/tick-and-flick)) while being totally transparent, which includes declaring whether there are any known outstanding bugs (which should already be on the Product Backlog) and adherence to the Team's Definition of Done.

`youtube: https://youtu.be/L94TEsTuLz4`

**Video: Explaining a PBI to a Product Owner with Jake Bayliss (5 min)**

**Note:** If there are additional stakeholders, make sure they are also in the loop and [up to speed on the current increment](https://www.linkedin.com/posts/scrum-trainer_scrum-agile-activity-6815396232366837760-Mhnb/).

If a Story is accepted, but more work needs to be done, a new Story to cover this work is added to the Product Backlog.  Similarly, if a bug is found during the review, it is added to the Product Backlog.

If a Story is rejected and returned to the Product Backlog but the Sprint itself is accepted, then a careful decision needs to be made.  If changes have been checked-in to the Sprint's branch then it must be established that these changes have no adverse effect or they must be carefully undone before the branch is merged with the trunk.  For this reason, it is always safer to accept stories with conditions rather than reject them.

The Scrum Master keeps the meeting on track and to the Timebox by disallowing discussions not relevant to the acceptance or rejection of the story; this is often done by making a note to bring the subject up again in the [Retrospective](/do-you-know-what-happens-at-a-sprint-retrospective-meeting) Meeting.

This meeting is normally time-boxed to as many hours as there are weeks in the Sprint.

::: greybox
In Scrum, there are 4 meetings in total that you need to know about:

* [Sprint Planning Meeting](/do-you-know-what-happens-at-a-sprint-planning-meeting)
* [Scrum Meeting (Daily standup)](/meeting-do-you-update-your-tasks-before-the-daily-scrum)
* Sprint Review Meeting (Described on this page)
* [Sprint Retrospective Meeting](/do-you-know-what-happens-at-a-sprint-retrospective-meeting)

:::

#### What if you can't attend the Sprint Review

![Figure: Playing golf](Golf-holiday.png)  

If you can't attend your team's Sprint Review (e.g. you're on leave, working part-time, or in a different timezone), you should give the team a summary of where you're at, so they can inform the stakeholders on your behalf.

* Send a brief "Sprint Review" email to the team to provide them with an update on the status of your tasks. This will enable the team to pass on the information to the client.
  
::: greybox
::: email-template
|          |     |
| -------- | --- |
| To:      | {{ YOUR SCRUM MASTER }} |
| Cc:      | {{ YOUR TEAM }} |
| Subject: | {{ YOUR NAME }} - Sprint Review {{ SPRINT REVIEW NUMBER }} Summary |  
::: email-content

### Hi Team  

I won't be able to make the Sprint Review because {{ REASON }}. Here's an update on my PBIs:

* PBI {{ PBI NUMBER }} - Done - Done Video in the PBI ready to show the client.
* PBI {{ PBI NUMBER }} - Blocked - Waiting on {{ BLOCKER }}. Details in the PBI.
...

:::
:::

:::

::: info

### Not doing Scrum?

Even if your client does **not** want to do Scrum (they might have had a bad experience in the past) you should still do this step, just under a different name.
E.g. _"Hey Bob, let’s schedule a catch up on Friday. Then I'll show you what I have done this week"_.
:::
