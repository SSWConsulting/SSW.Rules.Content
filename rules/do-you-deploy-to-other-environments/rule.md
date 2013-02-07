---
type: rule
archivedreason: 
title: Do you Deploy to other Environments?
guid: ed2c4951-62af-4e56-8e98-67c53a5fb67d
uri: do-you-deploy-to-other-environments
created: 2013-02-06T18:56:41.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---


<p>Now that you have configured “Build Once, Deploy Many” you can open the folder for any build on the build server and deploy any build, to any environment.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>This means that if you deploy version 37, and then want to roll back to version 36 simply open the folder for 36 and re-run that batch file (assuming there has been no breaking DB schema changes).</p><p style="color&#58;red;font-weight&#58;bold;">TODO&#58; AdamS – Write a rule on non-breaking Schema changes</p><dl class="image"><dt><img src="/PublishingImages/deploy-other-environments.jpg" alt="" /></dt><dd>Figure&#58; To deploy to staging and production, open the appropriate drops folder and execute the correct batch file from the drops folder</dd></dl>



