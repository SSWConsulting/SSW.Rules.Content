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

![Figure: This is not how you hand over a project](handover-project.gif)

After the handover, the transitioning team member should focus on addressing any gaps in knowledge, ideally completing this process well before their shift in focus.

Ensure completion of the following checklist and confirm the handover via email.

<!--endintro-->

Here are the 8 steps for an effective handover:

1. Confirm current tasks
2. Confirm upcoming tasks
3. Identify primary contacts
4. Conduct a code review (for developers)
5. Examine the [project dashboard](/use-a-project-portal-for-your-team-and-client)
6. Document the location of essential information and procedures, ideally stored in a wiki or SharePoint document library. For development projects, this may include:
   * Source control - ensure there are no stale branches. Refer to: [Do you know when to branch in git?](/do-you-know-when-to-branch-in-git)
   * Database details
   * Documentation
   * Build and package instructions
   * Testing steps, including user accounts and passwords for test and staging servers
   * Deployment procedures
   * Server access and passwords
   * Failure & Recovery processes
7. Verify the accuracy of user accounts, passwords, URLs, and server details provided during the handover
8. Conclude the handover with an email confirmation that the process has been completed satisfactorily
9. (Optional) Allow the new project member to shadow the previous one, enabling further clarification and question opportunities

::: email-template
|          |     |
| -------- | --- |
| From:    | John |
| To:      | Peter |
| Subject: | SSW - Northwind Project Handover |

::: email-content

Hi Peter,

As per our conversation, I am transitioning to a new role, and you will be taking over the Northwind project. Below are the key details:

* **Confirm outstanding tasks:** None
* **Confirm planned tasks:** Prepare for Release 43, focusing on enhancing management module reporting.
* **Location of resources:**
  * Source control: [file://tfs.ssw.com.au/tfs/Northwind](#)
  * Data storage: [file://server/DataSSW/SSWProducts/Northwind](#)
  * Deployment: Use WISE for builds
  * Test database: `seadragon` | SSWNorthwind_test
  * Production database: `squirrel` | SSWNorthwind
  * **Failure & Recovery:** Work locally and backup the master folder before making changes. Use the master folder backup for recovery if needed.

All tasks have been assigned to you in the backlog. Please review and let me know if you have any questions.

:::
:::
::: good
Figure: Good example - Clear handover details with actionable steps and resources
:::

For handing over individual tasks, more details are available at [Do you know how to hand over email tasks to others?](/how-to-hand-over-tasks-to-others).

::: greybox  
**Tip:** Recording the handover process via a Teams call can also be beneficial for future reference.  
:::