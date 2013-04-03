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


Including images is a good idea, in addition when appropriate include code snippets, &#160;and ideally have the code that changed highlighted in <font style="background-color&#58;#ffff00;">yellow</font>.&#160; 
<br><excerpt class='endintro'></excerpt><br>
<p>This has several benefits&#58; </p>
<ul><li>Improved visibility and transparency - The client can see the work actually being done </li>
<li>Reduced cost of fixing a bug - the cost of a bug goes up based&#160;of the length of time taken&#160;for the client to ask for a change. If you tell a developer&#160;to change&#160;something he did today, it is many times cheaper for him to fix, than if he got the same request 2 months later (when he has forgotten was it was about)&#160; </li>
<li>The client can raise questions based on what he sees in the code </li>
<li>Finally, in the very unlikely case that the code repository and backup goes corrupt, your emails are a backup! </li></ul>
<p>Let's look at some examples and tips&#58;<br><br><img width="650" height="468" class="ms-rteCustom-ImageArea" src="/Management/RulesToHappyClients/PublishingImages/NotifyCodeChangesBad.gif" border="0" alt="" style="border&#58;0px solid currentcolor;width&#58;620px;height&#58;438px;" /> </p>
<dl class="badImage"><span class="ms-rteCustom-FigureBad">Figure&#58; Bad example - the client cannot see any detail of what was done </span><img width="622" height="1001" class="ms-rteCustom-ImageArea" alt=" " src="/Management/RulesToHappyClients/PublishingImages/NotifyCodeChanges.gif" border="0" style="border&#58;0px solid currentcolor;width&#58;592px;height&#58;971px;" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good example - the client can see the image + the code changes highlighted in yellow </span><p><strong>Tip #1&#58; Include the URL<br></strong>If you are using TFS, you can also include a URL to the work item in TSWA<br><br><strong>Tip #2&#58; Include a .diff file<br></strong>You can include the code as an attached text file.&#160;&#160;<br></p>
<img width="800" class="ms-rteCustom-ImageArea" alt=" " src="/Management/RulesToHappyClients/PublishingImages/NotePad2DiffFiles.gif" border="0" style="border&#58;0px solid currentcolor;height&#58;338px;" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Good example - this is a Text file with a .diff extension that includes the code change from TFS. If opened using NotePad2, the client can view the code changes with green and red color (added and deleted code). </span><p><strong>Tip 3#&#58; Do you have force a link between the code and the requirement?</strong><br>For those developers lucky enough to be using Microsoft Team Foundation Server (TFS 2005, 2008 or 2010) you can associate your code changes with a work item. This means that future developers can work out not just *what* changed, but *why*. <br>For those using TFS,&#160;enable the&#160;Checkin policy&#160;and force all developers to associate every check-in with a work item. </p>
<img class="ms-rteCustom-ImageArea" alt=" " src="/Management/RulesToHappyClients/PublishingImages/SourceControl_AssociateWorkItems1.gif" border="0" style="border&#58;0px solid currentcolor;" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Make developers associate all check ins to a work items </span><img width="593" height="612" class="ms-rteCustom-ImageArea" alt=" " src="/Management/RulesToHappyClients/PublishingImages/SourceControl_AssociateWorkItems2.gif" border="0" style="border&#58;0px solid currentcolor;width&#58;563px;" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Enabling the Checkin Policy (via Project | Team Project Settings | Source Control | Add) </span></dl>


