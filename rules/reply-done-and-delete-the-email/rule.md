---
type: rule
title: Dones - Do you reply 'Done' and delete the original email?
uri: reply-done-and-delete-the-email
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Cameron Shaw
    url: https://ssw.com.au/people/cameron-shaw
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
related:
  - definition-of-done
  - dones-do-you-include-useful-details-in-your-done-email
  - when-to-send-a-done-email-in-scrum
  - close-pbis-with-context
redirects:
  - dones-do-you-reply-done-and-delete-the-original-email
created: 2009-03-23T04:03:34.000Z
archivedreason: null
guid: c2a162d0-858d-4d80-a5e7-9e5c852daa18
---
If someone asks you to perform a task by email, don't reply "OK, I will do that" or fail to reply at all. Instead, do the task and reply "<mark>Done</mark>" when the task has been completed, and then delete the email. This way the person requesting the task knows that it has been done, and doesn't waste time following you up.

<!--endintro-->

Read the "[Definition of Done](/definition-of-done)" for more information about the steps that need to be finished before replying to a done email.

::: greybox
**Only say "Done" when the work is completed.**

* [Ensure your changes are live](/dones-do-your-dones-include-a-url/#ensure-your-changes-are-live) when sending a "Done"
* If you have added the email to your backlog or to-do list, then say "<mark>Added to backlog – URL is XXX</mark>". You should still reply "Done" when you complete the task.
* For tasks that will take time to be completely done (E.g. Producing a long video), you may send a "work in progress" email. This way you avoid giving the perception that no action was in relation to the task. You should still reply "Done" when you complete the task.
:::

### Alternatives to classic "Done" emails

* If the task is already done, then reply "<mark>Already done - the reason is XXX</mark>"
* If you don't agree with the task or are unable to complete the task:
  1. [Seek clarification](/do-you-seek-clarification-via-the-telephone-first)
  1. If you still don't agree or the task is still blocked, reply "<mark>Not done - [as per our conversation](/as-per-our-conversation-emails), the reason is XXX</mark>"
* If there are multiple tasks (some "Done" and some "Not Done"), reply to each item **individually** "<mark>Done</mark>" or "<mark>Not Done</mark>"
* If the task can't be 100% completed at the time, you may reply "<mark>Partially done - the reason is XXX</mark>"
* If you have already sent a "Done", then the client asks you to undo the change, reply <mark>"Undone"</mark>

::: email-template
|          |     |
| -------- | --- |
| To:      | Jason |
| Subject: | RE: Northwind - Include one more field to the form |
::: email-content  

### Hi Jason

Not done - as per our conversation, I checked with Northwind and they're happy with the form as it is

:::
:::
::: good
Figure: Good example - "Not Done" email
:::

### Tip #1: Say "Done" first

For clarity, "Done" (or "Not done" / "Already Done" / "Partially Done") should be the first word(s) so the **reader knows the status straight away**.

### Tip #2: Provide details in your "Done"

In any reply, [include relevant information](/dones-do-you-include-useful-details-in-your-done-email), such as [URLs](/dones-do-your-dones-include-a-url), screenshots, and pieces of code/text that have been updated. This allows others to check what was done straight away.

### Tip #3: Replying "Done" to multiple tasks

It is important that you clearly reply to each of the multiple tasks.

::: email-template
|          |     |
| -------- | --- |
| To:      | Jason |
| Subject: | Northwind website - Update logo + add a photo |
::: email-content  

### Hi Jason

As per our conversation,

1. Update the logo on Northwind website the new logo
2. Take a photo of the office façade and add to the "About Us" page

Bob

:::
:::
**Figure: Original email with the client request**

::: email-template
|          |     |
| -------- | --- |
| To:      | Bob |
| Subject: | RE: Northwind website - Update logo + add a photo |
::: email-content  

### Hi Bob

I couldn't find a camera so I haven't taken the photo.

Jason
:::
:::
::: bad
Figure: Bad example – It is not clear which tasks have been done and which haven't
:::

::: email-template
|          |     |
| -------- | --- |
| To:      | Bob |
| Subject: | RE: Northwind website - Update logo + add a photo |
::: email-content  

### Hi Bob

I've replied inline in **bold**.

Jason

- - -

**From:** Bob  
**To:** Jason
**Subject:** Northwind website - Update logo + add a photo  

### Hi Jason

 &gt; 1. Update the logo on Northwind website to the new logo. **Done - See northwind&#46;com**  
 &gt; 2. Take a photo of the office façade and add to the "About Us" page. **Not Done - I couldn't find a camera**

Bob

:::
:::
::: bad
Figure: Bad example – It is clear which tasks have been done, however, [replying inline should be avoided](/email-avoid-inline) as it messes up the history
:::

::: email-template
|          |     |
| -------- | --- |
| To:      | Bob |
| Subject: | RE: Northwind website - Update logo + add a photo |
::: email-content  

### Hi Bob

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; > 1. Update the logo on Northwind website to the new logo  
Done - See <u>northwind&#46;com</u>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; > 2. Take a photo of the office façade and add to the "About Us" page  
Not Done - I couldn't find a camera.

### To myself

1. Action #2 above once I get the camera from Peter tomorrow

:::
:::
::: good
Figure: Good example – It is very clear which tasks have been done and which haven't. Quoting the original task is only necessary when some tasks are done and some are not see [Do you use indentation for readability?](/do-you-use-indentation-for-readability)
:::

::: greybox
**Extra:**

What do you do with the "Not Done" tasks?  

If there are multiple items of work in an email and you can't do them all at once, reply to each item individually ("Done" and "Not Done"). With the "Not Dones" you should add a plan to action:

a. Put [yourself in the "To:"](/dones-do-you-send-yourself-emails) if you are going to do the remaining items later.
b. Add another person if you are reassigning.
c. Give a reason if it won't be done.  
:::

#### Replying "All done"

If you have completed multiple tasks without requiring additional information, it is acceptable to respond with a simple "All done." However, be careful and use this approach **only** when the tasks are unequivocally straightforward, leaving no room for ambiguity or uncertainty.

Make sure all tasks have been done and others can see the history of the requests. An URL is especially useful in these cases.

::: email-template
|          |     |
| -------- | --- |
| To:      | Bob |
| Subject: | RE: Northwind website - Update logo + add a photo |
::: email-content  

### Hi Bob

All Done - see {{ URL }}

Jason

:::
:::
::: good
Figure: Good example – If multiple tasks are clearly 'done', then replying "All done" is a good way to simplify things
:::

### Tip #4: Replying "Done" to huge tasks

Ideally, [all PBI's should be done in less than 2 days](/create-PBIs-under-2-days). If you are given a task that is going to take more time than that, then split it by following [breaking up monster tasks](/do-you-send-tasks-one-email-at-a-time).

### Tip #5: Don't consolidate emails

If you get multiple emails or tasks, don't consolidate them. **Reply to each email individually** as you go. This way the person requesting the work hasn't [lost the email history](/do-you-keep-the-history-of-an-email) and can understand what the work is done relates to. It also means that testing and/or feedback can come in as soon as possible after the 1st completed task.

### Tip #6: Delete "Done" emails - Aim for 0 inbox

There is no point in keeping emails that just clutter your inbox. You don't need to keep the original email because after you have replied "Done", there is a copy in "Sent Items". If you must keep an email, then move to your "Saved Items" folder.

### Tip #7: When appropriate, use text instead of images

::: email-template
|          |     |
| -------- | --- |
| To:      | Bob |
| Subject: | RE: Northwind website - find orders |
::: email-content  

### Hi Bob

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    &gt;1. Find the orders<br>
Done - used the following to get it:

```sql
SELECT
ProdName = CASE WHEN Download.ProdCategoryID <> ''

THEN ProdCategory.CategoryName
ELSE Download.ProdName END,
Downloads = (SELECT Count(*) FROM ClientDiary
WHERE ClientDiary.DownloadID = Download.DownloadID 

AND ClientDiary.CategoryID = 'DOWN'
AND ClientDiary.DateCreated > '01/01/2010'
AND ClientDiary.DateCreated < '01/01/2020')
FROM
Download
LEFT JOIN ProdCategory 
ON Download.ProdCategoryID = ProdCategory.CategoryID    

ORDER By Downloads DESC
```

Jason

:::
:::

::: good
Figure: Good example - This "Done" uses text instead of an image so it is easier to search; to copy and paste; and to reply with a modification
:::

### Tip #8: Handle an email once

Follow a tip from Adam Cogan:

> During my accounting days we had large physical in-trays and you were always picking up papers,
> looking at them, deciding it’s ‘too hard to do right now’, and then picking up another piece of paper...
> I learnt that a sign of an efficient person is that they handle a piece of paper once.

Likewise, when you get an email - don't just open it, have a quick look and close it with the idea that you will go back to it later. Read it, make a decision and do the action. Delete as many emails as you can on the first go. In the same vein, when you complete all tasks in an email, delete everything in that thread.

### Tip #9: Consider alternatives in a team environment

In a development team environment, it is better to move emails to tracking systems. E.g.:

1. [Azure DevOps Work Items](/turn-emails-into-pbis)
2. [GitHub](/do-you-turn-an-email-into-a-github-issue-before-starting-work)

### Tip #10: Include a video when appropriate

See how to [record a quick and dirty "Done Video"](/record-a-quick-and-dirty-done-video).

### Tip #11: Remember to thank people - don't be too brief and icy

When replying 'Done' to a bug or issue someone reported, **remember to thank the person** for taking the time to send it. A short "Thank you for reporting this" helps to make your 'Done' warmer.
