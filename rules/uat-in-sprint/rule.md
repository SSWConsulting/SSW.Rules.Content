---
type: rule
title: Do you include UAT in each Sprint?
seoDescription: Embrace UAT in Scrum by incorporating your testing processes into the Sprint.
uri: uat-in-sprint
authors:
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
related:
  - acceptance-criteria
  - do-you-know-which-environments-you-need-to-provision-when-starting-a-new-project
  - do-you-have-separate-development-testing-and-production-environments
redirects:
  - no-uat-phase-in-scrum
created: 2025-10-02T22:40:45.273Z
guid: 091b9044-5067-4bfc-aa15-0fcd150eb94b
---

User Acceptance Testing (UAT) is common in software release cycles, but it can often be treated as a secondary backlog of work that's managed independently of the development Sprint. This separation adds friction, creates delays, and **costs more money** for every feature. UAT is incredibly valuable, so make sure you're doing it right.

<!-- endintro -->

`youtube: https://youtu.be/FnHAlRde0fk?t=67`
**Video: YDS: When Does UAT Happen in Scrum? (6 min)**

## What is UAT?

Developers build a feature, and before shipping that feature to the wider audience, you want to make sure it's doing exactly what you expect. This is the foundation of UAT. Depending on the size and scope of the project, UAT may be done by a single Product Owner, or a team of users (ideally real users, but sometimes stakeholders). 

Regardless, the concept remains the same. Once the development work has been signed off by the relevant testing authority, the work is approved for production and is ready to be shipped.

## ❌ UAT done wrong

In many projects, QA or testing will be treated as an entirely separate phase to development. The Scrum team will work on a PBI, merge their code, and set the PBI's status to "Ready for testing". These PBIs will then be managed separately as a "UAT backlog", where it may be days or weeks until that PBI is picked up by the QA team and actioned.

A PBI marked as "Ready for testing" means it cannot be marked as "Done" until testing is complete. This creates long-lived PBIs that constantly prevent teams from meeting their Sprint Goal, as they are never able to mark all PBIs as "Done" by the end of the Sprint.

Additionally, there may be bugs found by testers, meaning those PBIs are thrown back onto the development backlog and have to be re-prioritized and scheduled for future Sprints (or, worse, disrupt the current Sprint). Not to mention that, after all this time, the developers themselves may have already context-switched to different problems and will have to reacquaint themselves with the feature once again.

![Figure: Bad example - Walls between development and testing](dev-uat.png)

As you can imagine, this disconnect between development and acceptance testing can result in a significant drop in delivery speed, and dramatically increase the business cost for many work items.

## ✅ UAT done right

A Scrum team should be comprised of people who have all the skills needed to deliver a piece of work to production, **within a single Sprint.**

If your [Definition of Done](https://www.ssw.com.au/rules/definition-of-done/) requires a feature to pass UAT before shipping, then your Development team needs to include people who can make that happen.

From the Scrum guide:

> It is important to remember that a Developer is not necessarily a software developer. They can focus on any type of product work whether software or not and any aspect of helping to design, build, test or ship the product.
>
> [Scrum.org | What is a Developer in Scrum?](https://www.scrum.org/resources/what-is-a-scrum-developer)

![Figure: Good example - Cross-functional teams deliver features faster](cooperative-devs.png)

### Does that mean I should ditch my UAT environment?

This is a good question, and generally, the answer is "No". Environments are a separate concern, and having a UAT environment is often the best location for your testers to perform UAT testing. The important distinction here is that your deployment pipelines should be delivering code changes to whatever environment the testers need for UAT **within the same Sprint** that the feature is being developed.

### My testers are swamped - there's too much to test in a single Sprint

This can happen for a variety of reasons, and is often a symptom of a more fundamental issue. The most common culprits are:

#### Acceptance Criteria

One of the most common causes of an ever-growing backlog is ill-defined [Acceptance Criteria](/acceptance-criteria/).

**🛠️ Fix:** In a high-performing Scrum team, every PBI has well-defined AC that allow the programmers to assume the lion's share of testing - whether through building automated tests, or exploratory testing during development.

#### "Programmer to Tester" ratio

If you have a poor dev to test ratio, your testing team will be stretched too thin. If you manage your QA department separately to your development teams, this is often the result. Your testers will be trying to service multiple dev teams, with competing priorities, and thus will start to silo themselves and thereby start managing their own separate testing backlog.

**🛠️ Fix:** Embrace the **cross-functional** nature of a Scrum team, and include dedicated testers in each team.
