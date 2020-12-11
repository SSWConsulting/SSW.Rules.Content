---
type: rule
archivedreason: 
title: Tasks - Do you know to ensure that relevant emails are attached to tasks?
guid: d49fc7ef-dd61-4c72-addc-5ff3c4cb2d70
uri: tasks---do-you-know-to-ensure-that-relevant-emails-are-attached-to-tasks
created: 2010-04-28T14:41:54.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Often you will receive rich information from your Product Owner (Customer) about tasks. That information can be in the form of Word documents, HTML Emails and Pictures, but you generally receive them in the context of an Email. This should be done by one person called the scribe.


::: greybox

### The Scribe will:

1. take screenshots and notes
2. turn them into multiple emails
3. add them into the backlog with Team Companion (can be added directly into TFS on Web Browser)


:::


<!--endintro-->

You need to keep these so your Team can refer to it later, and so you can send a “done” when the task has been completed. This preserves the “history” of the task and allows you to keep relevant partied included in any future conversation.

Keep the original email so that you can     [<br>      reply DONE and delete the email](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=29d5ca5d-c191-475f-8db2-0086c44ca46c).

But keeping it in your email does not help other members of the team if they complete the task and need to send the “done”.

Worse yet, the description field in Team Foundation Server 2010 (TFS 2010) does not support HTML and images, nor does the default task template support an “interested parties” or CC field. You can attach this content manually, but it can be time consuming.

**More information:**

You should follow the existing     [<br>      Rules to Better Project Management](/Management/RulestoBetterSpecificationReviews)  and attach the email to your task so you can refer to and reply to it later when you close the task:

* [<br>         Do you know what Outlook add-ins you need?](http&#58;//www.ssw.com.au/ssw/standards/rules/RulesToBetterProjectManagementWithTFS.aspx#OutlookAddin)
* [<br>         Describe the work item request in an email](http&#58;//www.ssw.com.au/ssw/standards/rules/RulesToBetterProjectManagementWithTFS.aspx#WorkItemEmail)
* [<br>         Use Outlook Add-in to move the email to a TFS Work Item](http&#58;//www.ssw.com.au/ssw/standards/rules/RulesToBetterProjectManagementWithTFS.aspx#TeamCompanionWorkItem)


When replying to an email with “done” you should follow:

* [<br>         Do you update Team Companion template, so the email "subject" doesn't change?](http&#58;//www.ssw.com.au/ssw/standards/rules/RulesToBetterProjectManagementWithTFS.aspx#KeepConsistentName)
* [<br>         Do you update Team Companion template, so you can generate a proper "done" mail?](http&#58;//www.ssw.com.au/ssw/standards/rules/RulesToBetterProjectManagementWithTFS.aspx#EmailTemplate)


Following these simple rules will help your Product Owner understand you better, and allow your team to more effectively collaborate with each other.

An added bonus is that as we are keeping the email history in sync with TFS. When you “reply all” to the email all of the interested parties to the Task are also included. This notifies those that may have been blocked by your task to keep up to date with its status.
