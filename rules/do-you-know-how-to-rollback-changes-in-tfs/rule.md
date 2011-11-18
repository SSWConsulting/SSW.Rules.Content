---
type: rule
archivedreason: 
title: Do you know how to rollback changes in TFS?
guid: 6980541f-5084-4ef7-b997-51d90f4e6885
uri: do-you-know-how-to-rollback-changes-in-tfs
created: 2011-11-18T03:52:54.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
related: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>
<ol>There are two ways to do this&#58; <li>If you haven’t checked in any files since you started modifying them then the process is simple&#58; <ul><li>Right click your solution and <b>Undo Pending Changes</b><dl><dt><img alt="Undo Pending changes" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/rollback1.gif" width="266" height="307" /> </dt></dl></li></ul></li>
<li>If you aren’t so lucky and have made some commits along the way then the only option is to use the Rollback command. <ul><li>To use this you will need to install <a href="http&#58;//www.ssw.com.au/ssw/Redirect/TFSPowerToolsDownload.htm">Team Foundation Server Power Tools v1.2</a> <img title="You are now leaving SSW" src="http&#58;//www.ssw.com.au/ssw/images/external.gif" alt="" /></li>
<li>Find the revision before you started checking code in using the <b>History command</b><dl><dt><img alt="Revision List" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/rollback2.gif" width="595" height="178" /></dt>
<dd>Figure&#58; The last revision before Tristan made changes was 5367</dd></dl></li>
<li>Open the Command Prompt in your current working directory and type <b>“c&#58;\Program Files\Microsoft Team Foundation Server Power Tools\tfpt.exe” rollback /changeset&#58;5367</b><dl><dt><img alt="Rollback Changeset" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/rollback3.gif" width="807" height="342" /> </dt></dl></li>
<li>Click <b>Yes</b> and the rollback will proceed </li></ul></li></ol>
<p>It would be nice if there was a GUI for this tool so that I can just right click and select rollback. See <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx#RollbackGUI">Better Software Suggestion – TFS</a></p>


