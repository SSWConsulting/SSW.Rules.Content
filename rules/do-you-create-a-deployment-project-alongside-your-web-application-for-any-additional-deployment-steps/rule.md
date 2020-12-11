---
type: rule
archivedreason: 
title: Do you Create a “.Deployment” Project alongside your Web Application for any additional deployment steps?
guid: f1ae5bbf-023e-4848-8a93-3178e0725a30
uri: do-you-create-a-deployment-project-alongside-your-web-application-for-any-additional-deployment-steps
created: 2013-02-06T18:51:03.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---

Your source control repository should be the source of all truth. Everything, always, no-matter what should go into source control.

This includes any deployment scripts and Web Deploy parameter files if you need them.

<!--endintro-->

This includes your deployment scripts and Web Deploy parameter files.
<dl class="goodImage">&lt;dt&gt; 
      <img src="deployment-project.jpg" alt=""> 
   &lt;/dt&gt;<dd>Figure: Good Example - Create a Deployment project alongside your web project.  </dd></dl> In the image aboce, Vm-SynWeb.Deploy.Bat is a batch  file that will deploy your web site to Vm-SynWeb
 Vm-SynWeb.SetParameters.xml is a Web Deploy SetParameters file that specifies environment specific settings.
 \_Deploy.Bat is the base batch file that your environment specific deployment batch files will call. <dl class="image">&lt;dt&gt; 
      <img src="deployment-project-copy.jpg" alt=""> 
   &lt;/dt&gt;<dd>Figure: It is important that each of the batch and parameters files has it ‘Copy to Output Directory’ setting set to ‘Copy Always’</dd></dl>
