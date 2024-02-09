---
type: rule
archivedreason: null
title: Do you escalate key updates and deliverables?
guid: fab0fe6c-e21b-427d-851f-116c7c116108
uri: escalate-key-updates
created: 2023-06-20T23:53:39.0000000Z
authors:
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related:
 - when-you-use-mentions-in-a-pbi
redirects:
 - escalate-done-videos
---

Key updates on projects may include Done Videos, critical text additions, or specification documents. Typically, links to these deliverables would be added to the PBI that they relate to and the relevant people would be mentioned.

<!--endintro-->

::: bad  
![Figure: Bad Example - Automated notifications from project management tools can be easily missed or overlooked amidst other notifications](critical-update-bad-example.jpg)
:::

::: good  
![Figure: Good example - For visibility and to ensure all stakeholders are in the loop, you should also send an email to the relevant people](critical-update-good-example.jpg)  
:::

Not every PBI will require an email, but if it is a key update or deliverable, it should be escalated. The developers would make this judgement call, although this could also be added upfront by the Product Owner in the Acceptance Criteria for the PBI. Here are the 3 scenarios:

1. **Standard PBI** - needed but the outcome is not very interesting: Do the PBI, just following the DoD
2. **Interesting to someone** - [@ mention them](/when-you-use-mentions-in-a-pbi)
3. **Really important** - Make sure it’s top of mind, email it

For example, you can send an email similar to this to share a new Done Video to the relevant stakeholders. If you working on a big system or internal projects, include the feature area or project name in the subject for additional context.

::: email-template  
| | |
| -------- | --- |
| To: | {{ PRODUCT OWNER }}; {{ OTHER STAKEHOLDERS }} |
| Subject: | 🎥 {{ PROJECT NAME }} - Done Video for {{ PBI TITLE }} |  
::: email-content

### Hi Team

I just made a Done Video for this PBI {{ LINK TO PBI }}.

{{ LINK TO VIDEO }}

If you have any feedback, please post it on the PBI.

<This email was sent as per [https://www.ssw.com.au/rules/escalate-key-updates](/escalate-key-updates)>

:::  
:::

This email is especially important for stakeholders that don't use, want to use, or have access to the project management tools. If they do have access, remember to also @mention them in the PBI update as per [Do you know when you use @ mentions in a PBI?
](/when-you-use-mentions-in-a-pbi/)

Sometimes the PBI work originated from an email, in which case you should reply to the email instead of starting a new email. This will allow stakeholders to have additional context.

::: info
**Note:** You should be able to easily tell if a PBI was created from email, see [Do you turn an email into a PBI before starting work?](/turn-emails-into-pbis/)
:::
