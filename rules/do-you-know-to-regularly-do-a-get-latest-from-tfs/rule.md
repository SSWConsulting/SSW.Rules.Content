---
type: rule
archivedreason: 
title: Do you know to regularly do a Get Latest from TFS?
guid: 59306ecd-ec0d-43ae-8f0c-431dd7fe2891
uri: do-you-know-to-regularly-do-a-get-latest-from-tfs
created: 2012-03-05T23:43:02.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---


It is important to regularly do a &quot;Get Latest&quot; to make sure you are using the most recent version of the code. In a team, if you go too long without doing a Get, you are more likely to encounter inconsistencies and will have to spend time merging your code.
<br><excerpt class='endintro'></excerpt><br>
<p>As part of your team standards, you should make sure all developers are doing a Get Latest on a regular basis for each project they are working on.</p>
<p>To find out when you or another developer last did a Get from TFS, you can use the Workspace Sidekick in <a href="http&#58;//www.attrice.info/cm/tfs/index.htm">Team Foundation Sidekicks</a>. If you're the TFS Master, you should do this every couple of weeks to make sure your team is regularly retrieving files from TFS.</p>
<p><img alt="Workspace Sidekick" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/SidekicksWorkspaceLastGet.png" style="margin&#58;5px;" /><br><span class="ssw-rteStyle-FigureNormal">Figure&#58; This report shows the last time each user did a Get from </span><span class="ssw-rteStyle-FigureNormal"></span><span class="ssw-rteStyle-FigureNormal">TFS</span>It is important to note that this report does *<strong>not</strong>* show you which project, file, or set of files the most recent Get retrieved.&#160; It is possible for this report to show that you've done a recent Get while most of your code is out of date.&#160; Even&#160;performing a Get on&#160;a single file will cause an update to this report.</p>


