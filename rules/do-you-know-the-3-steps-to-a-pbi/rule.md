---
type: rule
archivedreason: 
title: Do you know the 3 steps to completing a PBI?
guid: 1de9df77-9b69-4242-b648-e08e5980e9a6
uri: do-you-know-the-3-steps-to-a-pbi
created: 2013-08-30T06:33:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-know-the-3-steps-to-completing-a-pbi

---

The lifecycle of a PBI can be broken down into 3 steps:

<!--endintro-->

### 1. Ready

1. Take the next PBI that was approved by the 
      [Product Owner](/rules-to-better-product-owners)
2. Is the PBI ready?
Check your PBI against your 
      [Definition of Ready](/have-a-definition-of-ready). "Ready" PBIs must have Acceptance Criteria. A good Definition of Ready also encourages a test-first mentality in requirements e.g. Use Spec Flow (Given, When, Then) and/or create Test Cases and Test Steps first.
3. Attach and copy the Product Owner's email into the Acceptance Criteria (as per [Do you attach and copy emails to the PBI?](/do-you-attach-emails-to-the-pbi)).
4. Email notification to the Product Owner - 
      [use the @ mention rule](/when-you-use-mentions-in-a-pbi)
5. Break down your PBI into tasks.
6. Don't forget to make a task for testing! (So that it is visible in the task board). Note: You can also 
      [customize the kanban board](https://www.visualstudio.com/en-us/get-started/work/work-from-the-kanban-board-vs) by adding a new column for testing, but we recommend adding a testing task to the PBI instead.

::: bad  
![Figure: Adding a new "Test" state. This is only visible in the Product Backlog and not the Sprint Backlog](KB-customize-board-columns.png)  
:::

::: good  
![Figure: Testing Task added to PBI. This is the board the team will use for 90% of the Sprint, so testing should be clearly visible here](Testing-task.png)  
:::

### 2. Code

1. From the PBI, create a new branch (so that your work is automatically tagged to the PBI)
2. On the Kanban Board, move your Task into "In Progress"
3. Checkout your new branch and start coding!
4. Code, code, code… (Red, Green, Refactor)
5. Push your changes, open a Pull Request
6. If you want feedback early, record a Done Video. E.g. Snagit


### 3. Done

Is the PBI "Done"? Check your Definition of Done, and then:

1. Open a Pull Request
2. Get another engineer in your team to do an "over the shoulder" check of the code
3. Use [Microsoft's "Test and Feedback" Chrome extension](/do-you-do-exploratory-testing) to test the app
4. Make changes based on feedback (and then get more feedback)
5. Complete the Pull Request! Merge changes to master, this automatically deploys (to either Test, Staging or Prod based on process maturity)
6. Email notification to the Product Owner – send a 
      [Done Email (reply to the original)](/dones-do-you-reply-done-and-delete-the-original-email). Big items should have a 
      [Done Video](/do-you-send-done-videos)
7. Check the Acceptance Criteria for notes about email attachments (as per 
      [Do you attach emails to the PBI?](/do-you-attach-emails-to-the-pbi)).

Congrats. Your PBI is now ready to be demonstrated during your Sprint Review! (Note: This is also the same process you follow for a Bug work item)

::: good  
![Good Figure: This image includes all the important steps in a PBI lifecycle. Print this "SSW 3 Steps to a PBI pdf" and put it on your 'War Room' wall](3StepsToAPBI.jpg)  
:::
