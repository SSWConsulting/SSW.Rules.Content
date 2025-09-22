---
type: rule
title: Do you create a Sprint Review/Retro email?
seoDescription: Learn how to create a structured Sprint Review/Retro email
  template with best practices for clear communication and effective team
  collaboration in Agile processes.
uri: sprint-review-retro-email
authors:
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
  - title: Drew Robson
    url: https://ssw.com.au/people/drew-robson
  - title: Chris Briggs
    url: https://ssw.com.au/people/chris-briggs
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
  - title: Seth Daily
    url: https://ssw.com.au/people/seth-daily
  - title: Josh Berman
    url: https://ssw.com.au/people/josh-berman
related:
  - roadmap
  - what-happens-at-retro-meetings
  - what-happens-at-a-sprint-planning-meeting
  - sprint-forecast
  - groups-in-microsoft-365
  - following-microsoft-365-groups
  - rules-to-better-research-and-development
redirects:
  - do-you-create-a-sprint-review-retro-email
created: 2012-08-06T05:48:37.000Z
archivedreason: null
guid: aac90a70-58a3-4b10-97a1-fef2dc6bda39
---

After any Sprint Review and Retrospective, an email should be sent to all the stakeholders to update them on the outcome from the Sprint.

<!--endintro-->

Learn more on [Do you know what happens at a Sprint Retrospective meeting?](/what-happens-at-retro-meetings)

Firstly, create a new email copying the information from the previous Sprint Review/Retro.

::: email-template

|          |     |
| -------- | --- |
| To:      | {{ PRODUCT OWNER }} |
| Cc:      | {{ SPRINT REVIEW ATTENDEES }}, {{ PROJECT GROUP EMAIL }}, {{ SPRINT REVIEW REPORTING EMAIL }} |
| Subject: | {{ PRODUCT NAME }} - Sprint {{ X }} Review + Retro |
::: email-content

### Hi {{ PRODUCT OWNER }}

Here are the Sprint Goals and their status at a glance:

Sprint Goals (in priority order):

* {{ ✅/❌ }} {{ DONE? }} - {{ GOAL }}
* {{ ✅/❌ }} {{ DONE? }} - {{ GOAL }}

Please see below for a more detailed breakdown of the Sprint:

|                    |                                      |
| ------------------ | ------------------------------------ |
| Sprint in Review:  | {{ SPRINT NUMBER }}                  |
| Summary Recording: | {{ YOUTUBE PLAYLIST URL }}           |
| Sprint Duration:   | {{ NUMBER OF WEEKS }}                |
| Project:           | {{ PROJECT NAME }}                   |
| Project Portal:    | {{ LINK TO PROJECT PORTAL }}         |
| Test Environment:  | {{ LINK TO TEST ENVIRONMENT }}       |
| Product Owner:     | {{ PRODUCT OWNER NAME }}             |
| Attendees:         | {{ NAMES OF THE ATTENDEES }}         |
✅ I have added the relevant stakeholders as per [Do you know what happens at a Sprint Review meeting?](/what-happens-at-a-sprint-review-meeting)

### Sprint Review

1. Timesheet data - Who worked in the Sprint?

![Figure: Timesheet data for a Sprint](sprint-timesheet-data.png)

2. What got done?

| **ID**   | **Title**       | **Assignee**   | **State**   | **Effort**   |
| -------- | --------------- | -------------- | ----------- | ------------ |
| {{ ID }} | {{ PBI TITLE }} | {{ ASSIGNEE }} | {{ STATE }} | {{ EFFORT }} |
| {{ ID }} | {{ PBI TITLE }} | {{ ASSIGNEE }} | {{ STATE }} | {{ EFFORT }} |

**Figure: Sprint Backlog from {{ LINK TO SPRINT BACKLOG }}**

3. Sprint Burndown - A quick overview of the Sprint

![Figure: Sprint Burndown](burndown-V2.png)

4. Code Coverage - Hopefully tests are increasing each Sprint

{{ CODE COVERAGE }}

5. Velocity *(Optional)*

{{ VELOCITY }}

6. Burnup - How are we tracking for the big picture? *

![Figure: Release Burnup](release-burnup.jpg)

| Metrics – last 30 days | Count |
| --- | --- |
| New PBIs | {{ NEW PBIS }} |
| AI PBIS | {{ PBIS CREATED WITH AI }} ( {{ PERCENT OF NEW PBIS CREATED WITH AI }} %) |
| Completed PBIs | {{ PBIS COMPLETED }} |
| Net Change in PBIs | {{ +/- OVERALL PBI COUNT CHANGE }} |

**Figure: Backlog stats from [the stats generator](https://backlog-sprint-tool.vercel.app/) (GitHub only)**

7. Build Pipeline Health & Production Deployments - How many times did we deploy to Production?

![Figure: Build Pipeline Health from DevOps](thumbnail-image.png)

![Figure: Deployments from {{ DEPLOYMENT SERVICE }}](production-deploy.png)

8. Application Health Overview Timeline - For the entire Sprint

![Figure: Application Health Overview Timeline](application-insights.jpg)

9. Product Roadmap

{{ ROADMAP LINK }}

Progress:

**{{ EPIC #1 }}**

* Currently {{ TOTAL # OF PBIS COMPLETED }}/{{ TOTAL # OF PBIS CREATED }} PBIs completed (there will be more)

  * {{ # OF PBIS COMPLETED THIS SPRINT }} Completed this Sprint
  * {{ # OF PBIS CREATED THIS SPRINT }}  Newly created this Sprint

*Add this for each current epic in your backlog*

10. R&D - Did we do any experimental work?

{{ INSERT DETAILS of any trial/error processes, and ensure all detail is captured as per [https://ssw.com.au/rules/do-you-record-your-failures](/do-you-record-your-failures) }}

{{ INSERT DETAILS of any problems for which no solutions existed, and ensure detail is captured as per [https://ssw.com.au/rules/do-you-record-your-research-under-the-pbi](/do-you-record-your-research-under-the-pbi) }}

11. AI use - what tools did you use?

* {{ PERSON }} - {{ TOOLS }}

#### Copilot Stats

![Figure: Copilot speaking summary was {{ DURATION }} - Image from Product Owner](meeting-length.png)

![Figure: Copilot showed the main action point was {{ MAIN ACTION POINT }} - Image from Product Owner](main-action-point.png)

### Sprint Retrospective

As part of our commitment to inspect and adapt as a team we conduct a Sprint Retrospective at the end of every Sprint. Here are the results of our Sprint Retrospective:

✅ **What went well?**

{{ INSERT LIST OF WHAT WENT WELL from Retro }}

❌ **What didn’t go so well?**

{{ INSERT LIST OF WHAT NOT WENT WELL from Retro }}

💡 **What improvements will be made for the next Sprint?**

{{ INSERT LIST OF IMPROVEMENTS to be made for the next Sprint }}

⚠️ **Do any 'For the Record' emails need to be sent?** *(Optional)*

As per <https://www.ssw.com.au/rules/for-the-record/>

{{ INSERT LIST OF 'FOR THE RECORD' EMAILS TO BE SENT }}

**Definition of Ready** *(Optional)*

{{ INSERT DEFINITION OF READY (Normally saying that the PBIs are sized with Acceptance Criteria added) }}

**Definition of Done** *(Optional)*

{{ INSERT DEFINITION OF DONE (Normally saying that it compiles, meets the acceptance criteria, and a test please has been sent if relevant) }}

&lt; This is as per the rule [https://ssw.com.au/rules/sprint-review-retro-email](/sprint-review-retro-email) /&gt;

:::
:::

::: good
Figure: Good example - Template for Sprint Review/Retro email
:::

::: info
**Note:** It's important that an [Email Group](/groups-in-microsoft-365/#microsoft-365-groups) is setup for the project, and the Sprint Review is sent to that group, so that anyone who joins the project in future can access these reports from shared inbox as per [Do you choose which Microsoft 365 Groups you follow?](/following-microsoft-365-groups)[](/following-microsoft-365-groups)
:::

::: info
**Tip:** Move all Dones to the top of your Sprint backlog to make it easier to digest the progress for the Product Owner.
:::

::: good
![Figure: Good example - TinaCloud team Sprint Review email](tina-sprint-email.png)
:::

## Recording Review and Retrospective Meetings

Creating a comprehensive summary and recording of your Sprint Meeting is a great way to communicate changes in a product to the community and stakeholders — especially for those unable to attend. See [Do you record a summary of Sprint Meetings?](/summary-recording-sprint-reviews) for details.

`youtube: https://www.youtube.com/watch?v=d1-5wziOH7o`
**Video: ✅ Good Example: Nick C in TinaCMS - Sprint 55 Review + Retro and Sprint 56 Forecast (9 min)**

`youtube: https://www.youtube.com/watch?v=eqc_fKk2ZFo`
**Video: ✅ Good Example: Josh B in Tina.io - Sprint Review 48 & Forecast 49 (13 min)**
