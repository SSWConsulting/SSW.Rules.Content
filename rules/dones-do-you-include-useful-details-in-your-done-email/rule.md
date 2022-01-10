---
type: rule
archivedreason: 
title: Dones - Do you include useful details in your 'Done' email?
guid: d5b7a283-6bad-4b12-a49d-9a88e30a552b
uri: dones-do-you-include-useful-details-in-your-done-email
created: 2011-05-29T16:10:16.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
- title: Justin King
  url: https://ssw.com.au/people/justin-king
related: 
- dones-do-you-reply-done-and-delete-the-original-email
- done-do-you-go-beyond-done-and-follow-a-definition-of-done
redirects: []

---

Including images is a good idea, in addition when appropriate include code snippets,  and ideally have the code that changed highlighted in <font style="background-color:#ffff00;">yellow</font>.

::: greybox
An email with just the word "done" can often be enhanced with a screen capture or code snippet...
...it provides evidence
...it educates
:::

<!--endintro-->

### Benefits 

This has several benefits:

* Improved visibility and transparency - The client can see the work actually being done
* Reduced cost of fixing a bug - the cost of a bug goes up based of the length of time taken for the client to ask for a change. If you tell a developer to change something he did today, it is many times cheaper for him to fix, than if he got the same request 2 months later (when he has forgotten was it was about)
* The client can raise questions based on what he sees in the code
* Finally, in the very unlikely case that the code repository and backup goes corrupt, your emails are a backup!

### Examples

Let's look at some examples and tips:

::: bad  
![Figure: Bad example - the client cannot see any detail of what was done](NotifyCodeChangesBad.gif)  
:::

::: good  
![Figure: Good example - the client can see the image + the code changes highlighted in yellow](NotifyCodeChanges.gif)  
:::

### Tip 1: Include the URL 

If you are using TFS, you can also include a URL to the work item in TSWA.

### Tip 2: Include a .diff file

You can include the code as an attached text file.

::: good  
![Figure: Good example - this is a Text file with a .diff extension that includes the code change from TFS. If opened using NotePad2, the client can view the code changes with green and red color (added and deleted code).](NotePad2DiffFiles.gif)  
:::

### Tip 3: Force association between the code and the requirement 

For those developers lucky enough to be using Microsoft Team Foundation Server (TFS 2005, 2008 or 2010) you can associate your code changes with a work item. This means that future developers can work out not just \*what\* changed, but \*why\*. 
For those using TFS, enable the Checkin policy and force all developers to associate every check-in with a work item.

::: good  
![Figure: Make developers associate all check-ins to a work items](SourceControl\_AssociateWorkItems1.gif)  
:::

::: good  
![Figure: Enable the Check-in Policy (via Project | Team Project Settings | Source Control | Add)](SourceControl\_AssociateWorkItems2.gif)
:::
