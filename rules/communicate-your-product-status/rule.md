---
type: rule
title: Communication - Do you know how to communicate Product Progress?
uri: communicate-your-product-status
guid: b396caf5-9bfb-4607-bc69-7dc13700b3cc
created: 2024-03-25T10:39:38.0000000Z
authors:
  - title: Nick Curran
    url: https://ssw.com.au/people/nick-curran
related:
  - send-sprint-forecast-and-sprint-review-retro-emails-to-the-client
  - summary-recording-sprint-reviews
archivedreason: null
---

As a Product Owner, you are representing the product's stakeholders on the Scrum Team. You will be a representative of the Product to other people in your business, such as your manager or director. You will often be asked the question "How is your Product going?"

<!--endintro-->

Keep stakeholders informed of progress and enthused about your project using monthly meetings.

## Monthly meeting agenda

To prepare for meetings and maximise the chances of success for your project, ensure you have answers to the following questions:

1. **Value - What features have been delivered recently?** Celebrate your successes and demonstrate how your product is adding value to stakeholders. Examples could include:

    * A new login screen with better accessibility for visually impaired users
    * Support for a new business process
    * A shortened user registration process

::: tip
**Tip:**: If you [record your Sprint meetings](/summary-recording-sprint-reviews), you can review the recordings as part of this briefing.
:::

2. **Development - How has the Roadmap progressed?** A PBI is a small chunk of work conducted to progress a larger aim. Explain how the completion of these PBIs contributed to achieving the aim of the Product Roadmap. For example:

    * Internationalization epic - Added Mandarin translations for an Angular component 
    * Subscription epic - Added payment processing

    ::: info
    **Tip**: Software such as [Azure DevOps](https://azure.microsoft.com/en-au/products/devops) and [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) can be used to graphically demonstrate progress.
    :::

    ![Figure: Progress for SugarLearning epics in Azure DevOps](product-roadmap.png)

3. **Development - What delays or blockers have been encountered while writing the software?** [Software development is painful and costly](/do-you-manage-clients-expectations/). Explain the difficulties that the project has encountered, and detail your plan to overcome those difficulties. For example:

    * The upgrade between Angular versions was delayed as the team's Frontend expert has been sick. A new expert has been brought in to complete the work
    * The new customer registration process was taking longer than expected to implement - the original prediction was 4 effort points, and is now expected to take 16. The intention is to make it simpler with fewer screens

4. **Operations - How do the product's metrics compare historically?** If you have responsibility for the operation of your product, you need to be tracking metrics such as the number of users accessing the system or how many hours they are spending on your site. Provide graphs to demonstrate trends. For example:

   * Have a graph demonstrating how the user count has changed over the course of the last 2 calendar years

    ![Figure: A graph helps demonstrate trends affecting the Product](user-metrics.png)

5. **Operations - What issues have been seen in Production?** [All errors should be logged](/do-you-log-every-error/), so you should be able to list any significant errors that stakeholders and users have experienced and the plan to prevent those errors in future. You should also be actively monitoring for performance issues. All such issues should have plans for investigation or rectification. For example:

    * The frontend has experienced an increase in exceptions when adding new users to the system. This was been tracked to a bug in how data is being serialized from the backend, and was fixed last Sprint
    * Since upgrading the database server version, a significance increase of 2 seconds in server response time has been seen. System Administrators are investigating

6. **Planning - What decisions have been made regarding the project?** As Product Owner, you will be approving changes to the behaviour of the product and many of these changes will be in development. Explain the decisions that you've made and their rationale. Try to catch misalignments in stakeholder views before your decisions are coded. For example:

    * I have modified the permissions model for the website to allow contributing users access to unpublished articles, as they often request input from each other
    * I approved the mock-ups for the website redesign, as they were cleaner and easier to understand than the current website pages

7. **Vision - Are we still happy with the Product Goal?** Circumstances and priorities change - in extreme circumstances, the Goal may need to be changed completely. Work with your stakeholders to ensure that your Product Goal fulfils their requirements. For example:

    * When building a Learning Management System, we noticed that users were heavily using the Markdown functionality. So the product was pivoted towards creating a Markdown editing system.

8. **Planning - Should the Roadmap be changed to align with the Product Goal?** Do we need to add, change or delete any Product Roadmap items to ensure that we are working towards the Product Goal while making efficient use of development resources. For example:

    * Users have had significant difficulty writing new articles, as the editing control does not make it easy to link to other articles. Therefore, work should be prioritized to improve how inter-article links are created
    * There has been a significant increase in users, so work needs to be prioritized to improve the throughput of transactions

9. **Resources - do you have everything you need to complete the updated Product Roadmap?** Ensure that you have agreements for funding, personnel or services, or everyone will be unhappy when the Roadmap is inevitably not delivered. For example:

    * To implement the article search functionality, approval is required for an increase in funding to cover the Azure Search Service instance
    * To implement the Artificial Intelligence co-writing feature, approval is required to apply for and pay for the Azure OpenAI Service

::: info
**Tip**: Record your Sprint meetings so that you have a record of the decisions and main points of the meeting. It also helps to demonstrate how the Scrum Team is working together to advance the Product.
:::

## Email Template - Recording the conversation

To aid preparation and communication of decisions, use the email template below. Note that this template uses "epics", which are collections of PBIs.

::: email-template
|     |     |
| --- | --- |
| To: | {{ STAKEHOLDERS }} |
| CC: | {{ PROJECT GROUP EMAIL }} |
| Subject: | {{ PRODUCT NAME }} - {{ DATE }} - 🤠 Roadmap Rodeo |

::: email-content

### Hi Everyone

Here is a summary of recent progress made for {{ PROJECT NAME }}.

|                        |                                           |
| ---------------------- | ----------------------------------------- |
| Sprints                | {{ START SPRINT }} - {{ CURRENT SPRINT }} |
| Dates                  | {{ START DATE }} - {{ END DATE }}         |
| Production Environment | {{ LINK TO PRODUCTION ENVIRONMENT }}      |
| Test Environment       | {{ LINK TO TEST ENVIRONMENT }}            |
| Development Dashboard  | {{ LINK TO DEVELOPMENT DASHBOARD }}       |

#### Value - Significant Delivered Features

* {{ FEATURE 1 }} - {{ BRIEF NOTE }}
* {{ FEATURE 2 }} - {{ BRIEF NOTE }}

#### Development - Roadmap Progress

{{ SCREENSHOT OF THE ROADMAP }}  
Figure: For Product Roadmap see {{ LINK TO THE ROADMAP (E.G. GITHUB PROJECTS) }}

#### Development - Delays and Blockers

* {{ EPIC 1 }}
  * {{ BLOCKAGE 1 }} - {{ PLAN TO WORK AROUND BLOCKAGE }}
* {{ EPIC 2 }}
  * {{ BLOCKAGE 2 }} - {{ PLAN TO WORK AROUND BLOCKAGE }}

#### Operations - Product Metrics

{{ GRAPH OF USER STATISTICS }}  
**Figure: Graph of user statistics**

{{ GRAPH OF AVAILABILITY }}
**Figure: Graph of availability**

#### Operations - Issues Seen in Production

* {{ OUTAGE 1 }} - {{ 1 PARAGRAPH DESCRIPTION OF FAILURE, INCLUDING TIMES THAT THE FAILURE OCCURED }}
* {{ PERFORMANCE ISSUE }} - {{ 1 PARAGRAPH DESCRIPTION OF ISSUE }}

#### Planning - Decisions

* {{ APPROVED MOCKUP 1 }} - {{ BRIEF DESCRIPTION }}
* {{ APPROVED BEHAVIOUR CHANGE 1 }} - {{ BRIEF DESCRIPTION }}

#### Vision - Product Goal Change

Changed from:

    {{ ORIGINAL GOAL }}

To:

    {{ NEW GOAL or "NO CHANGES" }}

#### Planning - Roadmap Changes

* Add {{ EPIC }}
* Deprioritize {{ EPIC }}

#### Resources - Requests

* Approved for {{ SERVICE EXPENSE }}

:::
:::

**Figure: Template for Product Status Review email**

## Good Example - Roadmap Rodeo for SugarLearning

The following is intended as a full example of a Roadmap Rodeo email.

::: email-template
|     |     |
| --- | --- |
| To: | ✉️ SugarLearningStakeholders |
| CC: | ✉️ SugarLearningDevelopers |
| Subject: | SugarLearning - 17 April 2024 - 🤠 Roadmap Rodeo |

::: email-content

### Hi Everyone

Here is a summary of recent progress made for SugarLearning.

|                        |                                           |
| ---------------------- | ----------------------------------------- |
| Sprints                | Sprint 137 - Sprint 141                   |
| Dates                  | 13 March 2024 - 17 April 2024             |
| Production Environment | https://my.sugarlearning.com              |
| Test Environment       | {{ LINK TO TEST ENVIRONMENT }}            |
| Development Dashboard  | {{ LINK TO DEVELOPMENT DASHBOARD }}       |

#### Value - Significant Delivered Features

* Angular 17 upgrade completed - frontend now using most recent Angular version

#### Development - Roadmap Progress

![Figure: For Product Roadmap see {{ LINK TO ROADMAP IN AZURE DEVOPS }}](product-roadmap.png)

#### Development - Delays and Blockers

* EF to EF Core migration
  * Test Containers - it has taken longer than expected to set up the integrated testing infrastructure.
    * This testing is required for the migration, and cannot be worked around
    * The intention is to add developers to the task

#### Operations - Product Metrics

![Figure: Graph of user statistics](sugarlearning-user-metrics.png)

![Figure: Graph of availability](sugarlearning-availability.png)

#### Operations - Issues Seen in Production

* Outage Wednesday 10 April 2024 - Site taken offline for 20 minutes due to an incorrect database connection string being set during deployment tests
* Performance - Requests to retrieve a learner's backlog are averaging 20 seconds
  * Recommendation - Upgrade Azure SQL Database Service and Compute Tier plan from "basic" to "standard"

#### Planning - Decisions

* Permissions behaviour - Contributors who create an article will retain access to the article even if that article is private and they are not assigned to it.
    * This change was triggered due to an bug where a contributor drafted an article and could not publish it.
    * Work to be conducted PBI 92491: "Amend contributor role in permissions system"

#### Vision - Product Goal Change

No Changes

#### Planning - Roadmap Changes

* Deprioritize Epic "Migrate the Chinafy branch into master" in favour of "EF to EF Core migration" to expediate development

#### Resources - Requests

* Approved for funding to upgrade Azure SQL Database Service and Compute Tier plan from "basic" to "standard"

:::
:::