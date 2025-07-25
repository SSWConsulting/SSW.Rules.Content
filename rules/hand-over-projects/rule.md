---
seoDescription: Learn how to hand over a project smoothly and ensure continuity with our step-by-step guide. Know the responsibilities of the person transitioning away from the project and follow our comprehensive checklist.
type: rule
title: Do you know how to hand over a project?
uri: hand-over-projects
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related:
  - handover-best-practices
  - hand-over-responsibilities
redirects:
  - do-you-know-how-to-handover-a-project
  - hand-over
created: 2010-03-15T06:22:03.000Z
archivedreason: null
guid: 15b06388-5103-45e4-a5ea-96c13554df77
---

Transitioning a project smoothly is crucial, whether due to changing project assignments or planned absences. A [thorough handover process](/handover-best-practices) ensures continuity and minimizes disruption.

**The handover is the responsibility of the person transitioning away from the project.**

It's essential to initiate the handover planning as soon as a transition is known. Review the project with the selected team member who will take over, then schedule a handover meeting with high priority.

It's important to plan from the perspective of the person receiving the handover.

<!--endintro-->

**Tip:** If you are leaving a company, ideally your handover should be done **as soon as possible** so that the developer taking over can start working on them while you’re still available to answer any questions.

![Figure: This is not how you hand over a project](handover-project.gif)

### Handover Checklist

Send this checklist in an email before the handover meeting to guide the discussion:

::: email-template

| | |
| -------- | --- |
| From: | {{ YOUR NAME }} |
| To: | {{ NEW TASK OWNER }} |
| Cc: | {{ TEAM MEMBERS, PRODUCT OWNER }} |
| Subject: | 🤝 Handover Checklist - {{ PROJECT NAME }} |

::: email-content

Hi {{ NEW TASK OWNER }},

I am looking forward to our upcoming handover meeting for {{ PROJECT NAME }}. Please find below the checklist to go through:

1. [Record this meeting](/record-teams-meetings) - It could be useful later!
2. Review the roadmap/backlog - What are the current and upcoming goals?
3. Scrum - Review [Definition of Done](/definition-of-done) and [Definition of Ready](/have-a-definition-of-ready)
4. Discuss project roles
   1. Who is the Product Owner?
   2. Who is the Scrum Master?
   3. Any other important stakeholders?
5. Architecture and Code Review
   1. Look for any [Tech Debt](/technical-debt)
   2. Test coverage and quality
6. CI/CD - Overview of the pipelines and deployment process
7. Overview of monitoring, logging, and incident response procedures
8. Project access - Ensure the new team member has all necessary permissions
9. Documentation - Review and update any missing or outdated documentation
10. Optional - Shadow some project meetings and development

We will record the meeting for future reference and add it to the project documentation. Please be ready to discuss these points, and let me know if you have any questions before the meeting.

Thanks!

< as per SSW Rules: [Do you know how to hand over a project?](/hand-over)>
:::
:::

Ensure you [reply done](/reply-done-and-delete-the-email) to this email after the handover meeting, with a checked by from the recipient.

For individual task handovers, see [how to hand over email tasks to others](/how-to-hand-over-tasks-to-others).

::: greybox  
**Tip:** Recording the handover process via a Teams call can be beneficial for future reference.

Even better at the end of a long call record a quick summary so everybody knows what was agreed. And it's easier for other people to watch.
:::
