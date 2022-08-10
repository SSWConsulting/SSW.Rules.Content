---
type: rule
title: Do you create a Sprint Review/Retro email?
uri: do-you-create-a-sprint-review-retro-email
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
  - github-sprint-templates
redirects: []
created: 2012-08-06T05:48:37.000Z
archivedreason: null
guid: aac90a70-58a3-4b10-97a1-fef2dc6bda39
---

After any Sprint Review and Retrospective, an email should be sent to all the stakeholders to update them on the outcome from the Sprint:

<!--endintro-->

Firstly, create a new email copying the information from the previous Sprint Review/Retro. As per [Do you know what happens at a Sprint Retrospective meeting?](h/do-you-know-what-happens-at-a-sprint-retrospective-meeting), it should include the following:

::: email-template
|          |     |
| -------- | --- |
| To:      | {{Product Owner}} |
| Cc:      | {{Sprint Review Attendees}}, {{Sprint Review Reporting Email}} |
| Subject: | {{Product Name}} - Sprint {{X}} Review/Retro |
::: email-content  

### Hi {{Product Owner}},

Here are the Sprint Goals and their status at a glance:

Sprint Goals (in priority order):

* Bugfixes – Done ✅
* WDM Integration – Done ✅
* SSO/Roles APIs – In Progress 🕑
* Download Documents APIs  – Not Done ❌

Please see below for a more detailed breakdown of the Sprint:

| Sprint in Review: | {{Sprint Number}}            |
| ----------------- | -------------------------------- |
| Sprint Duration:  | {{Number of weeks}}          |
| Project:          | {{Project Name}}             |
| Project Portal:   | {{Link to project Portal}}   |
| Test Environment: | {{Link to test environment}} |
| Product Owner:    | {{Product Owner Name}}       |

Attendees: *(Optional as they may be in the to and CC)*

### Sprint Review

| **ID** | **Title**                           | **State** | **Effort** |
| ------ | ----------------------------------- | --------- | ---------- |
| 24124  | UI Improvements                     | Done      | 4          |
| 24112  | Integrate Business Logic to MVC app | Done      | 8          |
| 24097  | Styling                             | Committed | 16         |

**Figure: Sprint Backlog from {{Link to Sprint Backlog in Azure DevOps}}** 

1. Sprint Burndown (a quick overview of the Sprint)

![Figure: Sprint Burndown](burndown.JPG)

2. Code Coverage (hopefully tests are increasing each Sprint)
   XXX
3. Velocity *(Optional)*
   XXX
4. Burnup (for the release - the whole project, how are we tracking for the big picture?)

![Figure: Release Burnup](ReleaseBurnup.jpg)

5. Production Deployments (How many times did we deploy to Production?)

![Figure: Deployments from Octopus Deploy](production-deploy.png)

6. Application Health Overview Timeline (For the entire Sprint)

![Application Health Overview Timeline.png](ApplicationInsights.jpg)

### R&D

**Did we do any experimental work?**

{{Insert details of any trial/error processes, and ensure all detail is captured as per [https://ssw.com.au/rules/do-you-record-your-failures](https://www.ssw.com.au/rules/do-you-record-your-failures);}}

{{Insert details of any problems for which no solutions existed, and ensure detail is captured as per <https://ssw.com.au/rules/do-you-record-your-research-under-the-pbi>;}}

### Sprint Retrospective

As part of our commitment to inspect and adapt as a team we conduct a Sprint Retrospective at the end of every Sprint. Here are the results of our Sprint Retrospective:

**What went well?** 
{{Insert list of what went well from Retro}}

**What didn’t go so well?** 
{{Insert list of what did not went well from Retro}}

**What improvements will be made for the next Sprint?** 
{{Insert list of what improvements will be made for the next Sprint}}

**Definition of Ready** *(Optional)*

{{Insert the Definition of Ready. (Normally saying that the PBIs are sized with Acceptance Criteria added)}} 

**Definition of Done** *(Optional)*

{{Insert Definition of Done. (Normally saying that it compiles, meets the acceptance criteria, and a test please has been sent if relevant)}} 

&lt;This is as per the rule: [https://rules.ssw.com.au/do-you-create-a-sprint-review-retro-email](/do-you-create-a-sprint-review-retro-email) /&gt;

:::
:::  

::: good
**Figure: Good example - Template for Sprint Review/Retro email**
:::
