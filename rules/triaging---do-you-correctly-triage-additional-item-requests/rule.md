---
type: rule
archivedreason: 
title: Triaging - Do you correctly triage additional item requests?
guid: 368379e7-2a52-439c-973f-e58de293d65b
uri: triaging---do-you-correctly-triage-additional-item-requests
created: 2009-08-18T04:45:08.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 4
  title: Ulysses Maclaren
- id: 2
  title: Cameron Shaw
- id: 5
  title: Justin King
related: []

---

"Triage" is a term originally used to describe the assessment of injured persons into a priority order based on the severity and urgency of their injuries. While developers don't often deal with real life and death situations, the ability to prioritise and action issues that arise can keep the heartbeat of a project steady and strong.

<!--endintro-->

Managing additional work requests can reduce the adverse impact on estimates and deadlines.
<dl class="image" style="float:right;clear:right;">&lt;dt&gt;<img border="0" src="SuccessfulProjects_Triage.jpg" alt="" style="border:0px solid;"> &lt;/dt&gt;
<dd>Figure: Only if it's life and death does it get added "in this sprint" </dd></dl>
The first step is to analyse the priority of the additional item.



Let's look at the rules to how to prioritize:

1. **By Default, move Tasks into the Next Sprint.** 
Priority is dependent upon the severity of the request. Only if it is a 'critical bug', then it will be done "in this sprint", most tasks however go "in a later sprint". They can include new feature requests, non-critical bug fixes, modifications and undiscovered work (i.e. work you didn't initially anticipate).  

::: greybox
 **Note:** On a fixed price contract the rules change. Bugs should be fixed in the current sprint if time allows, otherwise first thing in the next sprint as they are stopping you from being paid.
:::
2. **Exception #1 - Critical Bugs go into this Sprint** 
If you have a crash-to-code bug, most of the time it will go into this sprint. If it prevents one or more users accessing the system, it will  go into this sprint. Only high-priority bugs are fixed "in this sprint".

On the other hand, a bug that was in the prior sprint and not marked as a task in this sprint, generally will be moved into the next sprint. Everything in between is grey :-(
3. **Exception #2 - A Client can Override** 
A request for a new screen with a new look-up table that doesn't prevent users from operating the system, should be allocated to "a later sprint". 
If the client really \*needs\* it done now, they must specify "must be in this sprint". This will become an 'additional item' in the current sprint. If this request from the client will have a material impact on inflexible time and budget restraints, you need to speak and inform the client. 
For example:
*"Hi Bill, this task you specified 'must be in this sprint' will take an extra 4 days. Our critical deadline will be missed. Is that OK?"*
4. **Exception #3 - A Developer can Override
** A client may request a small feature (e.g. changing the sort order of a combo-box). This work can go in this sprint as long as the task is small (less than 1/2 hour) and the sprint is under budget. 
If the work is over budget then you need to obtain approval for any 'additional item', from both the project manager and the client, before adding the request into the Release Plan. See more about how to [Obtain Approval Additional Items Exceed Estimates](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=1a59fed4-fb4b-4f47-bee8-acc65c0c4833). 
<dl class="good">&lt;dt&gt;To: Evan Lin - SSW<br>From: Alan Ha - FinaMetrica <br>Subject: Client List for Administrators<br><br>Hi Evan,<br><br>Please add a sort function (like the one in office 2007) next to the fields: Last Name, First Name, Advisers and Organization. Apply to other relevant pages which have these fields in a list <br>i.e. adviser list for administrators, client list for advisers etc. <br>Please use the text Ascending instead of "smallest to Largest" and Descending for "Largest to Smallest".<br><br>Thanks Alan<br><br>&lt;/dt&gt;
<dd> <strong>Figure: The above is a sample from a customer will by default, go into a later sprint, not the current sprint.</strong> </dd></dl><br>What tools can you use to get tasks from your inbox into a task tracking system?
5. **Use a Good 3rd party Tool to Manage Additional Requests
**     Since most feedback comes into your Outlook inbox, find a tool that converts an email into a task. The best one is [TeamCompanion for TFS](http://www.ssw.com.au/ssw/Standards/DeveloperGeneral/TFS.aspx)
