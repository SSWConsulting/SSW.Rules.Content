---
type: rule
archivedreason: 
title: Do you know how to handover a project?
guid: 15b06388-5103-45e4-a5ea-96c13554df77
uri: do-you-know-how-to-handover-a-project
created: 2010-03-15T06:22:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 13
  title: Paul Neumeyer
related: []

---

A common source of pain, is picking up a project without a decent/complete handover. To have a successful project you must navigate over the problem of changing resources/people leaving etc.

As soon as an employee has given their resignation notice, their manager should become responsible for ensuring a successful handover takes place.  Each project they were involved in should be reviewed and another employee with a matching skill set should be selected to receive the handover.  Handovers should be booked in for each project with both employees in attendance, as early as possible and with high priority.

Once the handover is complete, the resigning employee should no longer work on that project so that any gaps in knowledge can be covered ideally before their notice period expires.

Always ensure that you complete the following checklist and *always*send the email confirming the handover is complete.

Here are the 8 steps you should follow for a good handover.

<!--endintro-->

1. Confirm current tasks
2. Confirm future tasks
3. Confirm the primary contacts
4. Do a code review
5. Review the client portal
6. Confirm location of info and procedures (hopefully, these are on a wiki or SharePoint document library)
    * Source control. Make sure there is no stale or old branches. Check out: [Do you know when to branch in git?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d12d969d-0a5f-4d75-8f6b-1c33ac8f74a1)
    * Database
    * Documents
    * How to Build and Package
    * Testing Steps and users and passwords to access the test and staging servers
    * Deployment Steps
    * Servers and Passwords
    * Failure & Recovery Steps
7. Test that the users, passwords, URLs and server details provided in the handover are correct by logging in with each
8. Complete the Handover by sending an email with: As per our meeting the handover has been completed to my satisfaction



::: greybox

**From: Andy
To: Gracia
Subject: SSW - Northwind handover**

Done

* **Confirm outstanding tasks**     Nothing.
* **Confirm planned tasks**     Get release 43 out.
* **Confirm location**
    * Source control        Nothing
    * Data storage        file://server/DataSSW/SSWProducts/Northwind
    * Deployment        Make a build by using WISE
Test: seadragon
Production: squirrel
    * Failure & Recovery        Do not work on the Master folder, work on local machine. If it has some issue, grab the file from master folder.
Always backup master folder’s file before uploading the changes to the master folder
* **Update the Employee Responsibilities in SSW intranet**     **TODO**


:::

 **Figure Bad Example - This handover is incomplete and light on details** 


::: greybox

**From: Andy
To: Gracia
Subject: SSW - Northwind Handover**

Done - As per our meeting the handover has been completed to my satisfaction

* **Confirm outstanding tasks**     Nothing.
* **Confirm planned tasks**     Next release is Release 43.
The aim of this release is to improve the reporting available from the management module with chart reports
Query = tfs\Northwind\Work Items\Team Queries\All Work Items - R43 - Management Module Reporting
    Backlog is in TFS.
Query = tfs\Northwind\Work Items\Team Queries\All Work Items - Backlog
* **Confirm location**
    * Source control        file://tfs.ssw.com.au/tfs/Northwind
    * Data storage        file://server/DataSSW/SSWProducts/North wind
    * Deployment
        * Make a build by using WISE
        * Test db to connect to:            server: seadragon
database: SSWNorthwind\_test
        * Production db to connect to:            server: squirrel
database: SSWNorthwind
    * Failure & Recovery        Do not work on the Master folder, work on a local machine. If it has some issue, grab the file from the master folder.
Always backup master folder’s file before uploading the changes to the master folder.
If a problem occurs, restore the backup of the master folder and restart
* **Update the Employee Responsibilities in SSW intranet**     DONE
* **Complete Handover**


:::

 **Figure: Good Example - This handover has lots of URLs and is complete** 

If you need to handover only a single task there are more details here: [Do you know how to hand over tasks (aka Emails) to others?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=2586b50a-21b6-40b0-8004-d90d1b029bec)
