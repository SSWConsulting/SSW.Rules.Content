---
type: rule
archivedreason: 
title: Dones - Do you include useful details in your 'Done' email?
guid: d5b7a283-6bad-4b12-a49d-9a88e30a552b
uri: dones---do-you-include-useful-details-in-your-done-email
created: 2011-05-29T16:10:16.0000000Z
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


<p>​​Including images is a good idea, in addition when appropriate include code snippets,  and ideally have the code that changed highlighted in ​<font style="background-color:#ffff00;">yellow</font>. </p><p class="ssw15-rteElement-GreyBox">An email with just the word "done" can often be enhanced with a screen capture or code snippet...<br>...it provides evidence<br>...it educates<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>This has several benefits:</p><ul><li>Improved visibility and transparency - The client can see the work actually being done</li><li>Reduced cost of fixing a bug - the cost of a bug goes up based of the length of time taken for the client to ask for a change. If you tell a developer to change something he did today, it is many times cheaper for him to fix, than if he got the same request 2 months later (when he has forgotten was it was about) </li><li>The client can raise questions based on what he sees in the code</li><li>Finally, in the very unlikely case that the code repository and backup goes corrupt, your emails are a backup!</li></ul><p>Let's look at some examples and tips:</p><dl class="badImage"><dt> <img src="NotifyCodeChangesBad.gif" alt="" style="width:620px;" /> </dt><dd>Figure: Bad example - the client cannot see any detail of what was done </dd></dl><dl class="goodImage"><dt> <img src="NotifyCodeChanges.gif" border="0" alt="" style="width:592px;" /> </dt><dd>Figure: Good example - the client can see the image + the code changes highlighted in yellow </dd></dl><p> 
   <strong>Tip #1: Include the URL<br></strong>If you are using TFS, you can also include a URL to the work item in TSWA<br><br><strong>Tip #2: Include a .diff file<br></strong>You can include the code as an attached text file.  <br></p><dl class="goodImage"><dt> <img src="NotePad2DiffFiles.gif" alt="" /> </dt><dd>Figure: Good example - this is a Text file with a .diff extension that includes the code change from TFS. If opened using NotePad2, the client can view the code changes with green and red color (added and deleted code). </dd></dl><p>
   <strong>Tip 3#: Do you have force a link between the code and the requirement?</strong></p><p>For those developers lucky enough to be using Microsoft Team Foundation Server (TFS 2005, 2008 or 2010) you can associate your code changes with a work item. This means that future developers can work out not just *what* changed, but *why*. <br>For those using TFS, enable the Checkin policy and force all developers to associate every check-in with a work item.</p><dl class="image"><dt> <img alt=" " src="SourceControl_AssociateWorkItems1.gif" /> <strong> </strong></dt><dd>Figure: Make developers associate all check-ins to a work items </dd></dl> <dl class="image"> <dt> <img src="SourceControl_AssociateWorkItems2.gif" alt="" style="width:563px;" /> <strong> </strong></dt><dd>Figure: Enabling the Checkin Policy (via Project | Team Project Settings | Source Control | Add) </dd></dl> <br>


