

---
authors:
  - id: 24
    title: Adam Stephensen
---




<span class='intro'> <p>Your source control repository should be the source of all truth. Everything, always, no-matter what should go into source control.</p><p>This includes any deployment scripts and Web Deploy parameter files if you need them.</p> </span>

<p>This includes your deployment scripts and Web Deploy parameter files.</p><dl class="goodImage"><dt> 
      <img src="/TFS/Rules-to-Better-Continuous-Deployment/PublishingImages/deployment-project.jpg" alt="" /> 
   </dt><dd>Figure&#58; Good Example - Create a Deployment project alongside your web project.  </dd></dl>
In the image aboce,​ Vm-SynWeb.Deploy.Bat is a batch  file that will deploy your web site to Vm-SynWeb<br> Vm-SynWeb.SetParameters.xml is a Web Deploy SetParameters file that specifies environment specific settings.<br> _Deploy.Bat is the base batch file that your environment specific deployment batch files will call.
<dl class="image"><dt> 
      <img src="/TFS/Rules-to-Better-Continuous-Deployment/PublishingImages/deployment-project-copy.jpg" alt="" /> 
   </dt><dd>Figure&#58; It is important that each of the batch and parameters files has it ‘Copy to Output Directory’ setting set to ‘Copy Always’</dd></dl>


