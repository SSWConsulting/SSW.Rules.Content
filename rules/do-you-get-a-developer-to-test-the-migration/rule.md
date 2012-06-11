---
type: rule
archivedreason: 
title: Do you get a developer to test the migration?
guid: 0b9c4772-0345-4b76-878d-206e328f4fff
uri: do-you-get-a-developer-to-test-the-migration
created: 2009-11-08T02:06:26.0000000Z
authors:
- id: 14
  title: Martin Hinshelwood
related: []

---


<p>Getting someone else to test the migration is the best way to make sure that you have not missed anything.</p>
<ol><li>Run <span><a href="http&#58;//www.ssw.com.au/ssw/Diagnostics/" shape="rect" target="_blank">www.ssw.com.au/ssw/Diagnostics/</a></span>, check it’s all green ticks </li>
<li>Diagnostics will pick up that you need the Visual Studio 2008 SP1 Forward Compatibility Update for Team Foundation Server 2010 installed&#160; </li>
<li>Start Visual Studio 2008 </li>
<li>Open&#160;Team Explorer </li>
<li>Add a new server http&#58;//tfs.northwind.com&#58;8080/tfs/&#160;<br><span><img alt="Add Team Foundation Serve" src="/PublishingImages/AddTeamFoundationServer.png" style="width&#58;442px;height&#58;236px;" /></span>&#160;<br><font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Remember to use the &quot;/tfs&quot; option when connecting to the new server.</font></li>
<li><span>Confirm that the following are correct</span> <ol><li><span>Source Code</span> - connect to TFS2010 server and confirm that you can get latest.</li>
<li><span>Source Code history</span> - check that the source history is intact</li>
<li><span>Work Items</span> - confirm that you can see the last work items that you created</li>
<li><span>Team Project - Create a new team project and check the SharePoint portal and reports work<br>note&#58; This will need to be done using Team Explorer 2010 as it is not supported in 2008.</span> </li></ol></li></ol>
<div><strong><span style="font-size&#58;large;">Congratulations, you’ve done a successful migration.</span></strong><br></div>
<div><br></div>
<br><excerpt class='endintro'></excerpt><br>



