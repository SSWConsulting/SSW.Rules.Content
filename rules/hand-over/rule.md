---
type: rule
title: Do you know how to hand over a project?
uri: hand-over
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related: []
redirects:
  - do-you-know-how-to-handover-a-project
created: 2010-03-15T06:22:03.000Z
archivedreason: null
guid: 15b06388-5103-45e4-a5ea-96c13554df77
---

Transitioning a project smoothly is crucial, whether due to changing project assignments or planned absences. A thorough handover process ensures continuity and minimizes disruption.

It's essential to start planning the handover as soon as a change is anticipated. Review each project involved and select a team member with the appropriate skills to take over. Arrange handover meetings with high priority and ensure both parties attend.

**The handover is the responsibility of the transitioning person.**

![Figure: This is not what a handover should look like](handover-project.gif)

After the handover, the transitioning team member should focus on addressing any gaps in knowledge, ideally completing this process well before their shift in focus.

<!--endintro-->

### Handover Checklist

Include this checklist in your handover email or GitHub issue to ensure a comprehensive transition:

::: email-template
|          |     |
| -------- | --- |
| From:    | {{ YOUR NAME }} |
| To:      | {{ RECIPIENT }} |
| Cc:      | {{ OTHER TEAM MEMBERS, PRODUCT OWNER,  }} |
| Subject: | Project Handover - {{ PROJECT NAME }} |

::: email-content

Hi {{ RECIPIENT }},

As per our conversation, I have handed over {{ PROJECT NAME }} to you. See the completed handover checklist below:

1. **Confirm current tasks:** {{ CURRENT TASKS }}
2. **Confirm upcoming tasks:** {{ FUTURE TASKS }}
3. **Primary contacts:** {{ CONTACTS }}
4. **Code review:** Conduct a review to ensure code quality and consistency (for developers)
5. **Project dashboard:** Familiarize yourself with the project dashboard for an overview of project status
6. **Essential information and procedures:**
   * Source control - {{ LINK TO REPO }}
      * ensure no stale branches are present. See [Do you know when to branch in git?](/do-you-know-when-to-branch-in-git)
   * Database details - {{ DATABASE DETAILS }}
   * Documentation - {{ LINK TO DOCS }}
   * Testing steps - Include user accounts and passwords for test and staging servers
   * Deployment procedures - {{ DEPLOYMENT PROCEDURES }}
   * Server access and passwords - {{ SERVER DETAILS }}
   * Failure & Recovery processes - {{ FAILURE & RECOVERY PROCESSES }}
7. **Verification:** Ensure all provided user accounts, passwords, URLs, and server details are accurate
8. **Shadowing (Optional):** Consider shadowing for further clarification and opportunities to ask questions
9. Link to handover meeting recording: {{ LINK TO RECORDING }}
   * This should also be added to the project docs

If you have any questions, please reach out ASAP.

< as per SSW Rules: [Do you know how to hand over a project?](/hand-over)>

:::
:::

For handing over individual tasks, more details are available at [Do you know how to hand over email tasks to others?](/how-to-hand-over-tasks-to-others).

::: greybox  
**Tip:** Recording the handover process via a Teams call can be beneficial for future reference.  
:::
