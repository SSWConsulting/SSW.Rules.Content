---
type: rule
archivedreason: 
title: Do you check your Workspaces when defining a new build?
guid: a8c4e7bc-555d-4420-80a5-29b0d2924d94
uri: do-you-check-your-workspaces-when-defining-a-new-build
created: 2012-03-28T05:38:50.0000000Z
authors:
- id: 23
  title: Damian Brady
- id: 28
  title: Daragh Bannigan
related: []

---


<div style="margin:0cm 0cm 0pt;"><font face="Calibri">​When defining a build, you should always check the Workspace tab. Only the workspace relevant to your build should be included.</font></div>
<br><excerpt class='endintro'></excerpt><br>
​ <div style="margin:0cm 0cm 0pt;"><font face="Calibri">If you have a number of Team Projects open from the same TFS Project Collection, all of their workspaces will be included by default.  You should remove those workspaces that aren’t being used otherwise the build server will get the source for every workspace in this list before starting a build.</font></div>
<div style="margin:0cm 0cm 0pt;"><font face="Calibri"> <img src="bad_workspace.png" alt="" style="margin:5px;" /><br>   <img src="bad.gif" alt="" style="margin:5px;" /></font><b><font face="Calibri">Figure: Bad example – Several workspaces from other team projects are included by default</font></b></div>
<div style="margin:0cm 0cm 0pt;"><font face="Calibri"> </font></div>
<div style="margin:0cm 0cm 0pt;"><img src="good_workspace.png" alt="" style="margin:5px;" /><br><b><font face="Calibri">  <img src="good.gif" alt="" style="margin:5px;" />Figure: Good example – Only the relevant workspace has been included in this build definition</font></b></div>



