---
type: rule
title: Planned - Do you have a planned outage process?
uri: planned-outage-process
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
  - title: Steven Andrews
    url: https://ssw.com.au/people/steven-andrews
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
  - do-you-have-a-server-reboot-restart-policy
created: 2017-06-30T19:21:55.000Z
archivedreason: null
guid: eb97dfa8-5bb8-4e19-932a-76d6f2f655fd
---
For unplanned outages, see [Unplanned - Do you have an unplanned outage process?](/unplanned-outage-process)

If your servers are down or have to go down during business hours you should notify the users at least 15 minutes beforehand so you will not get 101 people all asking you if the computer is down.

For short outages (under 15 minutes) that only affect only a few people (under 5 people), or are outside of business hours, then IM is the best method. If you use Microsoft Teams or Skype, a quick message will do.

**Note:** If they are not online on Teams or Skype, then they can't complain that they were not warned.

For extended or planned outages, or if you have a larger number of users (50+), **email** is the suggested method.

<!--endintro-->

### Email

If you send an email it is a good idea to tell the user a way to monitor the network themselves. Eg. Software solutions like SCOM or WhatsUp Gold.

Include a "[To myself](/dones-do-you-send-yourself-emails)". It gives visibility to others who are interested in what needs to be done to fix the problem and makes
it easier to remember to send the 'done' email. E.g. "done - CRM is alive again".

Example:

::: email-template\
|          |     |
| -------- | --- |
| To:      | SSWAll |
| Cc:      | YYY |
| Bcc:     | ZZZ |
| Subject: | This is the subject |\
::: email-content  

### Hi All,

Here is the summary of the outage plan: 

| **Planned/Unplanned:**      | Planned                                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Change Description:**     | Install Windows Updates and Restart Server                                                            |
| **Risk (see table below):** | LOW RISK (LOW Probability and MEDIUM Impact)                                                          |
| **Reason For Change:**      | Windows 2016 Windows Updates                                                                          |
| **Uptime over last month:** | 91.361%                                                                                               |
| **Planned Outage (mins):**  | 150                                                                                                   |
| **Planned Start Time:**     | 26 October 9:00 PM                                                                                    |
| **Planned Finish Time:**    | 26 October 11:30 PM                                                                                   |
| **Affected Services:**      | \Windows Server 2016  ,  sharepoint.ssw&#46;com.au intranet.ssw&#46;com.au  , projects.ssw&#46;com.au |

**Risk Lookup Table by Probability and Impact:** 

![Figure: Clearly showing the potential risks](risk-table.jpg)

**Note:** The following servers will be affected:

![](rule-outage-1.jpg)

and

![](rule-outage-2.jpg)

### To myself,

To show others who are interested in what needs to be done to fix the problem:

**Detailed Change Plan:** 

1. Lockout users via IIS
2. Backup server
3. Install Windows Updates 
4. Reboot server
5. Follow test plan
6. Based on result of test plan, follow backout plan if procedure failed
7. Procedure completed       

**Test Plan:** 

1. Check Event log for errors
2. Check each affected service is running
3. Call test users to start “Test Please” on the affect services 
4. Get result of user “Test Please” by email by 11:15 PM       

**Backout Plan:** 

1. Restore server from backup

**Note:** &lt;This is as per rule [What is your server reboot/restart policy?](/have-a-server-reboot-restart-policy) &gt;

:::\
::: 

Immediately before the scheduled downtime, check for logged in users, file access, and database connections.

### Users

Open 'Windows Task Manager' (Run &gt; taskmgr) and select the 'Users' tab. Check with users if they have active connections, then have them log off.

![Figure: Connected users can be viewed in Task Manager](rule-outage-3.png)

### Files

Open 'Computer Management' (Run &gt; compmgmt.msc), then 'System Tools &gt; Shared Folders'. Check 'Session' and 'Open Files' for user connections.

![Figure: Computer Management 'Open Files' View](rule-outage-4.png)

### Database

Open SQL Server Management Studio on the server. Connect to the local SQL Server. Expand 'Management' and double-click 'Activity Manager'.

![Figure: SQL Management Studio 'Active Connections' View](rule-outage-5.gif)

Once these have been checked for active users, and users have logged off, maintenance can be carried out.

**Restarts should only be performed during the following time periods**

1. Between 7am and 7:05am
2. Between 1pm and 1:05pm
3. Between 7pm and 7:05pm 

If a scheduled shutdown is required, use the PsShutdown utility from [Microsoft's Sys Internals](https://docs.microsoft.com/en-us/sysinternals/downloads/psshutdown) page.

**Always reply 'Done' when you finish the task.**