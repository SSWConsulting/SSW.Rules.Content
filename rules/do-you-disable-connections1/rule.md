---
type: rule
archivedreason: 
title: Do you disable connections?
guid: 1071b5f7-6efa-4e36-9987-39c04725a008
uri: do-you-disable-connections1
created: 2015-08-12T15:42:01.0000000Z
authors: []
related: []
redirects:
- do-you-disable-connections

---


<p>It is important that while you're upgrading, nobody can check in.  Any check-ins after you backup your database will be lost.</p><p>To make sure that nobody can change anything during the upgrade, follow these steps.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>a.               Send out an email notifying everyone TFS will be unavailable for the upgrade period<br> Follow <a href="http://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart">Rules to better Networks</a>  </p><p>b.              Make sure nobody can check in files:</p><p>c.                Open the TFS Administration Console on the server.</p><p>d.               Navigate to Application Tier / Team Project Collections.</p><p>e.              For each Team Project Collection, select it, and click "Stop Collection". Enter a useful message (this will be displayed to users trying to connect from Visual Studio) and click "Stop":</p><p><img src="stop each term.png" alt="stop each term.png" style="margin:5px;width:650px;" /><br></p><p><strong>Figure: Stop each Team Project Collection</strong></p><p> </p><p><img src="all team project.png" alt="all team project.png" style="margin:5px;width:650px;" /><br></p><p><strong>Figure: All Team Project Collections are stopped</strong></p><p>​<br></p><p>f.               In Visual Studio, confirm you can no longer connect to TFS</p><p><img src="visual studio.png" alt="visual studio.png" style="margin:5px;" /><br></p><p><strong>Figure: Visual Studio shows the message that you entered when you stopped the Team Project Collection</strong><br> <br></p>


