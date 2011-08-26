---
type: rule
archivedreason: 
title: Do you have a deployment plan?
guid: f730bb7f-e390-4f50-90e6-5d460779aedc
uri: do-you-have-a-deployment-plan
created: 2011-08-26T19:34:05.0000000Z
authors: []
related: []
redirects: []

---


Instructions are very important when maintaining a project. When someone new joins the project, you want to make sure that they can easily find the documentation to do tasks like setting up the project and deploying it. See our rule &quot;<a href="/SoftwareDevelopment/RulesToBetterDotNETProjects/Pages/DoYouMakeInstructions.aspx">Do you make instructions at the beginning and improve it gradually for web projects</a>&quot;
<br><excerpt class='endintro'></excerpt><br>
<p>That being said, the deployment plan is an important part of the Instructions.docx. It should clearly layout all the steps required to&#58;</p>
<ol>
<li>Deploy from scratch to a new server</li>
<li>Update versions</li>
<li>Rollback to a previous version</li>
<li>Update Schema or data</li>
</ol>
<p>It should also include checks to verify the deployment was successful e.g.</p>
<ol>
<li>Check zsValidate.aspx</li>
<li>Check runtime settings (e.g. Payment Gateways, Google Analytics, Connection strings)</li>
<li>Manual testing procedure (e.g. Place an order)</li>
</ol>
<p>This document should also be signed off by the project lead and verified by the client.</p>



