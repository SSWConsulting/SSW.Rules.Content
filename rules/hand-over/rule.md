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

A common source of pain, is picking up a project without a decent/complete handover. To have a successful project you must navigate over the problem of changing resources/people leaving etc.

As soon as an employee has given their resignation notice, their manager should become responsible for ensuring a successful handover takes place. Each project they are involved in should be reviewed and another employee with a matching skill set should be selected to receive the handover. Handovers should be booked in for each project with both employees in attendance, as early as possible and with high priority.

Handovers should also be done if an employee is switching project or taking leave.

![Figure: This is not how you hand over a project](handover-project.gif)

Once the handover is complete, the resigning employee should no longer work on those projects so that any gaps in knowledge can be covered ideally before their notice period expires.

Always ensure that you complete the following checklist and *always* send the email confirming the handover is complete.

Here are the 8 steps you should follow for a good handover:

<!--endintro-->

1. Confirm current tasks
2. Confirm future tasks
3. Confirm the primary contacts
4. Do a code review (only for developers)
5. Review the [project dashboard](/use-a-project-portal-for-your-team-and-client)
6. Confirm and document the location of info and procedures (hopefully, these are on a wiki or SharePoint document library). For a development project this may include:
   * Source control. Make sure there is no stale or old branches. Check out: [Do you know when to branch in git?](/do-you-know-when-to-branch-in-git)
   * Database
   * Documents
   * How to Build and Package
   * Testing Steps and users and passwords to access the test and staging servers
   * Deployment Steps
   * Servers and Passwords
   * Failure & Recovery Steps
7. Test that the users, passwords, URLs and server details provided in the handover are correct by logging in with each
8. Complete the Handover by sending an email with: As per our meeting the handover has been completed to my satisfaction
9. (Optional) Get the new dev to shadow the existing dev for some time. This gives them a chance to ask more questions

::: email-template
|          |     |
| -------- | --- |
| From:    | John |
| To:      | Peter |
| Subject: | SSW - Northwind handover |

::: email-content

Hi Peter,

Done

* **Confirm outstanding tasks**     Nothing.
* **Confirm planned tasks**     Get release 43 out.
* **Confirm location**

  * Source control: Nothing
  * Data storage: file://server/DataSSW/SSWProducts/Northwind
  * Deployment: Make a build by using WISE
  * Test: seadragon
  * Production: squirrel
  * Failure & Recovery: Do not work on the Master folder, work on local machine. If it has some issue, grab the file from master folder. Always backup master folder’s file before uploading the changes to the master folder
* **Update the Employee Responsibilities in SSW intranet: TODO**

:::
:::
::: bad
Figure Bad example - This handover is incomplete and light on details and there is no assigned action
:::

::: email-template
|          |     |
| -------- | --- |
| From:    | John |
| To:      | Peter |
| Subject: | SSW - Northwind handover |

::: email-content

Hi Peter,

As per our conversation, you will be taking over my tasks on the SSW Northwind project.

1. Review the below information as it contains vital details about the project.
2. Take over the in-progress and not started tasks that were previously assigned to me.
  - **Note:** We have already assigned you the tasks on the backlog, here: https://github.com/SSWConsulting/projects/SSWNorthwind

* **Confirm outstanding tasks:** Nothing.
* **Confirm planned tasks:** Next release is Release 43.
  The aim of this release is to improve the reporting available from the management module with chart reports
  Query = tfs\Northwind\Work Items\Team Queries\All Work Items - R43 - Management Module Reporting
      Backlog is in TFS.
  Query = tfs\Northwind\Work Items\Team Queries\All Work Items - Backlog
* **Confirm location**
       *Source control: file://tfs.ssw.com.au/tfs/Northwind*
       Data storage: file://server/DataSSW/SSWProducts/North wind
       *Deployment*
           Make a build by using WISE
           *Test db to connect to:            server: seadragon
  database: SSWNorthwind_test*
           Production db to connect to:            server: squirrel
  database: SSWNorthwind
      * **Failure & Recovery:** Do not work on the Master folder, work on a local machine. If it has some issue, grab the file from the master folder.
  Always backup master folder’s file before uploading the changes to the master folder.
  If a problem occurs, restore the backup of the master folder and restart
* **Update the Employee Responsibilities in SSW intranet:** DONE
* **Complete Handover**

:::
:::
::: good
Figure: Good example - This handover has a clear designation of responsibilities, lots of URLs and is complete
:::

If you need to hand over only a single task there are more details on [Do you know how to hand over email tasks to others?](/how-to-hand-over-tasks-to-others)

If you are handing over a process or other responsibility, it can be useful to record a Teams call of the handover, so it can be watched back later.
