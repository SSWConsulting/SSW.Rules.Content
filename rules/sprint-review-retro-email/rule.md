---
type: rule
title: Do you create a Sprint Review/Retro email?
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
related:
  - roadmap
  - do-you-know-what-happens-at-a-sprint-retrospective-meeting
  - groups-in-microsoft-365
  - following-microsoft-365-groups
  - rules-to-better-research-and-development
redirects:
  - do-you-create-a-sprint-review-retro-email
created: 2012-08-06T05:48:37.000Z
archivedreason: null
guid: aac90a70-58a3-4b10-97a1-fef2dc6bda39
---
After any Sprint Review and Retrospective, an email should be sent to all the stakeholders to update them on the outcome from the Sprint:

<!--endintro-->

Firstly, create a new email copying the information from the previous Sprint Review/Retro. As per [Do you know what happens at a Sprint Retrospective meeting?](/do-you-know-what-happens-at-a-sprint-retrospective-meeting), it should include the following:

::: info
It's important that an [Email Group](/groups-in-microsoft-365/#microsoft-365-groups) is setup for the project, and the Sprint Review is sent to that group, so that anyone who joins the project in future can access these reports from shared inbox as per [Do you choose which Microsoft 365 Groups you follow?](/following-microsoft-365-groups)
:::

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

* {{ ✅/❌/🚧 }} {{ GOAL }} – {{ DONE? }}
* {{ ✅/❌/🚧 }} {{ GOAL }} – {{ DONE? }}

Please see below for a more detailed breakdown of the Sprint:

|                    |                                      |
| ------------------ | ------------------------------------ |
| Summary Recording: | {{ VIDEO URL }} ({{ VIDEO LENGTH }}) |
| Sprint in Review:  | {{ SPRINT NUMBER }}                  |
| Sprint Duration:   | {{ NUMBER OF WEEKS }}                |
| Project:           | {{ PROJECT NAME }}                   |
| Project Portal:    | {{ LINK TO PROJECT PORTAL }}         |
| Test Environment:  | {{ LINK TO TEST ENVIRONMENT }}       |
| Product Owner:     | {{ PRODUCT OWNER NAME }}             |
| Attendees:         | {{ NAMES OF THE ATTENDEES }}         |

### Sprint Review

|   ID     |   Title         |   Assignee     |   State     |   Effort     |
| -------- | --------------- | -------------- | ----------- | ------------ |
|   ID     |   Title         |   Assignee     |   State     |   Effort     |
| {{ ID }} | {{ PBI TITLE }} | {{ ASSIGNEE }} | {{ STATE }} | {{ EFFORT }} |
| {{ ID }} | {{ PBI TITLE }} | {{ ASSIGNEE }} | {{ STATE }} | {{ EFFORT }} |

**Figure: Sprint Backlog from {{ LINK TO SPRINT BACKLOG }}**

1. Timesheet data - Who worked in the Sprint? *

:::img-medium
![Figure: Timesheet data for a Sprint](sprint-timesheet-data.png)
:::

2. Sprint Burndown - A quick overview of the Sprint

![Figure: Sprint Burndown](burndown.jpg)

3. Code Coverage - Hopefully tests are increasing each Sprint

{{ CODE COVERAGE }}

4. Velocity *(Optional)*

{{ VELOCITY }}

5. Burnup - How are we tracking for the big picture? *

![Figure: Release Burnup](release-burnup.jpg)

6. Build Pipeline Health & Production Deployments - How many times did we deploy to Production?

![Figure: Build Pipeline Health from DevOps](thumbnail-image.png)

![Figure: Deployments from {{ DEPLOYMENT SERVICE }}](production-deploy.png)

7. Application Health Overview Timeline - For the entire Sprint

![Figure: Application Health Overview Timeline](application-insights.jpg)

8. Product Roadmap

{{ ROADMAP LINK }}

Progress:

**{{ EPIC #1 }}**

* Currently {{ TOTAL # OF PBIS COMPLETED }}/{{ TOTAL # OF PBIS CREATED }} PBIs completed (there will be more)

  * {{ # OF PBIS COMPLETED THIS SPRINT }} Completed this Sprint
  * {{ # OF PBIS CREATED THIS SPRINT }}  Newly created this Sprint

**{{ EPIC #2 }}**

* Currently {{ TOTAL # OF PBIS COMPLETED }}/{{ TOTAL # OF PBIS CREATED }} PBIs completed (there will be more)

  * {{ # OF PBIS COMPLETED THIS SPRINT }} Completed this Sprint
  * {{ # OF PBIS CREATED THIS SPRINT }}  Newly created this Sprint

**{{ EPIC #3 }}**

* Currently {{ TOTAL # OF PBIS COMPLETED }}/{{ TOTAL # OF PBIS CREATED }} PBIs completed (there will be more)

  * {{ # OF PBIS COMPLETED THIS SPRINT }} Completed this Sprint
  * {{ # OF PBIS CREATED THIS SPRINT }}  Newly created this Sprint

9. R&D - Did we do any experimental work?

{{ INSERT DETAILS of any trial/error processes, and ensure all detail is captured as per [https://ssw.com.au/rules/do-you-record-your-failures](/do-you-record-your-failures) }}

{{ INSERT DETAILS of any problems for which no solutions existed, and ensure detail is captured as per [https://ssw.com.au/rules/do-you-record-your-research-under-the-pbi](/do-you-record-your-research-under-the-pbi) }}

### Sprint Retrospective

As part of our commitment to inspect and adapt as a team we conduct a Sprint Retrospective at the end of every Sprint. Here are the results of our Sprint Retrospective:

✅ **What went well?**

{{ INSERT LIST OF WHAT WENT WELL from Retro }}

❌ **What didn’t go so well?**

{{ INSERT LIST OF WHAT NOT WENT WELL from Retro }}

💡 **What improvements will be made for the next Sprint?**

{{ INSERT LIST OF IMPROVEMENTS to be made for the next Sprint }}

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

::: good
![Figure: Good Example - TinaCloud team Sprint Review email](tina-sprint-email.png)
:::
