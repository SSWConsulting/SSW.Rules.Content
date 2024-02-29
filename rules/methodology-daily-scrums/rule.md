---
type: rule
title: Methodology - Do you do Daily Scrums (aka stand-up meetings)?
uri: methodology-daily-scrums
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
related:
  - participate-in-daily-scrum-meetings
  - use-the-status-message-in-teams
  - keep-track-of-a-parking-lot-for-topics
  - do-you-make-your-team-meetings-easy-to-find
  - the-war-room-does-your-development-room-have-an-electronic-task-board-physical-is-ok-too-for-small-co-located-teams
  - ask-for-help
  - when-to-email-chat-call-or-meet
redirects:
  - methodology-do-you-do-daily-scrums-aka-stand-up-meetings
  - methodology-do-you-do-daily-scrums-(aka-stand-up-meetings)
created: 2009-02-28T09:43:16.000Z
archivedreason: null
guid: f15f834f-70dd-4f38-8597-9e561336caf2
---
Tight project teams have a Daily 'Scrum' every day at the same time.

It was once called a 'stand-up meeting' but that discriminates people in wheelchairs.

It is best to have it standing up, so it's short and to the point. No-one wants to stand around waffling.

<!--endintro-->

Everybody knows the 3 essential questions:

1. **What did you do yesterday?** (and did you update Azure DevOps (was TFS) OR other bug tracking system)?
2. **What are you going to do today?** (and my current task on the [physical task board](/the-war-room-does-your-development-room-have-an-electronic-task-board-physical-is-ok-too-for-small-co-located-teams) has my picture on it)
3. **Do you have any roadblocks?** (aka issues/impediments)

Asking these questions of every team member means no-one can hide and everyone remains connected. Further, you can notice what was promised and what was performed. This enables the team to discover issues quickly and keep abreast of the progress.

The team's successes and failures are shared, and anyone who knows the answer to someone else's problem can help with a solution, **after** the meeting.

`youtube: https://www.youtube.com/embed/YR84qH6d7QE`
**Figure: Watch a Daily Scrum at Microsoft (short)**

`youtube: https://www.youtube.com/embed/-UUrLxNBK_g`
**Figure: Watch a Daily Scrum at Microsoft (long)**

> "Great video guys. Remember, it is ok to change Scrum, actually, it is necessary for success. Just adhere to the values of Scrum. "
> Stephen Forte (Board member ScrumAlliance.com)

**Follow these essential tips to improve your Daily Scrum meetings:**

### Tip #1: Be prepared for the meeting

Before you join the Daily Scrum, [check the group](/how-to-see-what-is-going-on-in-your-project) to see what your colleagues have been discussing and working on, and check the portal to confirm the meeting time. If you’re joining a new project or re-joining a previous one after some time away, these steps are important to keep yourself up-to-date and abreast of progress.

Then you’ll be able to say to your Scrum Master, “I’ve had a look at the Teams group. I am ready to join the daily Scrum.”

### Tip #2: Have your Scrum Master review the Sprint Progress at the end

At the end of the Scrum, the Scrum Master should [review the current burn down](/reports-do-you-schedule-the-burndown-and-stories-overview-reports-to-be-emailed-to-the-team-every-day) to check on the progress of the team.

![Figure: A burndown chart in visualstudio.com](burndowntfspreview.png)

### Tip #3: Keep a schedule of the Daily Scrum times on a wall (+ have a recurring appointment in Outlook)

::: email-template
|          |     |
| -------- | --- |
| To:      | {{ TEAM }} |
| Recurrence:      | Everyday |
| Subject: | Daily Scrum –  {{ PROJECT NAME }} |
::: email-content  

### Hi {{ TEAM NAME }}

As per our conversation, the Daily Scrum will be held each day.

* Project: XXX
* Scrum Master: XXX
* Task board: XXX

&lt;This email was sent as per [Do you do Daily Scrums?](/methodology-daily-scrums)&gt;

:::
:::
::: good
Figure: Schedule a recurring Daily Scrum meeting in Outlook using this template
:::

![Figure: Or you can use Microsoft Teams](teams-meeting-daily-scrum.jpg)

### Tip #4: Keep to the schedule. Same place, same time (and start even if people are missing)

Get started on time. Especially in the beginning, people will be late, but the meeting should be held with the remaining people. Don't worry. People learn.

If the Scrum Master is not a full-time member of the team (often they are), they should attend every now and then to check the Scrum process is being followed and the Daily Scrums are being used synchronize the team and not a general meeting.

::: greybox
**Notes:**

* The Product Owner (often the client) is not required at the stand-up meeting. If they wish to turn up, remind them that they have tape stuck over their mouth, so they don't talk
* If you are not doing an approved Sprint and doing ad-hoc work, then best if the Product Owner (aka client) attends ([see Ad Hoc work](/do-you-know-the-difference-between-ad-hoc-work-and-managed-work))

:::

### Tip #5: Do you update tasks before the Daily Scrum?

Daily Scrums are more effective when team members arrive when their tasks are already updated.

See [Do you update your tasks before the daily stand-up meeting?](/meeting-do-you-update-your-tasks-before-the-daily-scrum)

### Tip #6: Don't go into detail

Keep your answers short and concise. Do not stray from the 3 main questions. Remember to use the "Parking Lot" to record topics to discuss after the Daily Scrum.

### Tip #7: No phones + no checking email. No distractions

Technology in the Daily Scrum causes people to lose focus on the goal. The goal is for the team to synchronize by sharing what they are doing. Avoid giving people the opportunity to be distracted easily by forbidding email, SMS and mobile phones from the Daily Scrum.

### Tip #8: Use a task board (even better use an electronic one)

A task board allows people to visualize what the team is talking about.

![Figure: A Task Board from Azure DevOps](tfspreviewtaskboard.png)

### Tip #9: Carry a pen and paper

Use a pen and paper to jot things down.
A whiteboard is also great for "Parking Lot" topics that arise, to be discussed after the meeting.

### Tip #10: Don't let your Daily Scrum become a general meeting - use a "Parking Lot"

A "Parking Lot" is the place for any discussions that stop the Team from answering the 3 main questions. Only interested people stay for the "Parking Lot" to discuss issues after the Daily Scrum.

### Tip #11: If you have raised impediments, consider contacting the Product Owner

Often the Product Owner won’t be at the Scrum. However, call the Product Owner if you have an Impediment (aka Roadblock). Communication with the Product Owner is essential and if you haven't touched base with him in the few days, then do so. A disconnected or absent Product Owner is a sign of dysfunction.

![Figure: Call the Product Owner if you have an Impediment (aka Roadblock)](ProductOwnerTelephone.jpg)

### Tip #12: Store Daily Scrums in the Teams team so the PO can easily access it

Sometimes, the Product Owner will want to see the Daily Scrum for many teams. Adding them to every meeting would create lots of noise in their calendar. Instead, make the [Teams meetings easy to find](/do-you-make-your-team-meetings-easy-to-find) so they can locate the Daily Scrum for any project via the Teams team.

:::bad
![Figure: Bad example - Too many Daily Scrum appointments](daily-scrum-bad.png)
:::

:::good
![Figure: Good example - Make Daily Scrums easy to find via the Teams Channel Calendar](daily-scrum-good.png)
:::

### Tip #13: What to do when you're working for a PO directly

If you don't have a team, and you're doing ad hoc work for a PO directly, it's best to contact him for the Daily Scrum every day if possible, and follow up with an email. This will keep the 2 of you synchronized.

### Tip #14: How do you enter Scrum meetings into your timesheets?

Once you have completed your stand up, add “S” to your timesheet as per [Rules to Better Timesheets](/rules-to-better-timesheets).

### Tip #15: Send an email

To avoid misunderstandings or even arguments, send your Daily Scrum as an email so everyone you are working with knows what you are working on. This is also helpful for team members who were not able to to join the Daily Scrum 😊.

::: email-template
|          |     |
| -------- | --- |
| To:      | Bob Northwind |
| Cc:      | {{ ANYONE YOU'RE WORKING WITH }} |
| Subject: | {{ YOUR NAME / TEAM NAME }} - Daily Scrum |
::: email-content  

### Hi Bob

Yesterday I worked on:

* ✅ Done - XXX
* ⏳ In Progress - XXX
* ⬜ PBI - XXX
* ❌ Blocked - XXX

Today I'm working on:

* ⏳ In Progress - XXX
* ⬜ PBI - XXX
* ⬜ Email - XXX
* ❌ Blocked - XXX

:::
:::
::: good
Figure: Good example - Always include what you previously worked on and what you plan on doing today
:::

### Tip #16: Use IM

After you have sent your email, you can also make it front and center by sending them a ping on IM.
*“Check your email for my Daily Scrum”* or paste in the below (a lightweight version with only what to do).

Use Teams or Skype to bridge gaps in geography.

**Focus on the Flow**

> "Extend this rule to focus on 'flow of value', not just people. In a continuous flow mindset, the daily standup is less about the people... it's about flow. The team faces the Scrum board and goes ticket by ticket for all the items in the 'work in progress', finding out what is needed to get it to the next stage... respecting work in progress constraints."
> [Joel Semeniuk](http://joelfromcanada.com)

When using email or IM try to be as specific as possible:

::: greybox

Hi Adam,

I have XX days until my next client booking.
I have 22 emails in my inbox.
Yesterday I was on sick leave.

Today I am working on:

* Timepro PBIs
* Tidy inbox

:::
::: bad
Figure: Bad example - Lack of details. Eg. Yesterday - if it's Monday, you wouldn't say “Yesterday was Sunday"... so if you were sick, it's more useful to go back to the prior day you were working
:::

::: greybox

Adam,

I have XX days until my next client booking.
I have 22 emails in my inbox.
<mark>Last Friday</mark> I was on sick leave.

Today I am working on:

* TimePro - <mark>Adding new button to the next day</mark>
* <mark>Getting my emails on "SSW.com" to zero</mark>

:::
::: good
Figure: Good example - Clear details
:::

### Tip #17: Auto-generate your Daily Scrum with AutoScrum

AutoScrum will scan your Azure DevOps repositories and find all the PBIs that you worked on yesterday and that are In Progress today.

More details: [github.com/AwesomeBlazor/AutoScrum](https://github.com/AwesomeBlazor/AutoScrum).

- - -

### More information

**What should I do when Blocked?**

When you are blocked, you should ideally take steps to unblock yourself. However, you should know [when to ask for help](/ask-for-help/) and understand [what mode of communication is best for your task](/when-to-email-chat-call-or-meet).

The ideal people to ask for assistance are:

* A fellow Developer that is Senior or knows the tech
* Your Scrum Master who can reach out to the Product Owner when issues reach beyond developing your project

**What happens when you run out of tasks?**

The goal is to be productive for 8 hours of the day, so communicate with the rest of the developers and work with them on any other outstanding tasks. If there are no more tasks then take the next task from the top of the Sprint Backlog.

**What happens if there is a major incident?**

It is important that any major incidents are dealt with first. Start with any major incidents that occurred in the last 24 hours.

![Figure: Daily Scrums will alert everyone if there is a major problem and get all brains aligned in the right direction. There is no sense in putting a Band-Aid on a patient's scraped knee if there is a big knife in his eye!](NewStandUpImage.jpg)
