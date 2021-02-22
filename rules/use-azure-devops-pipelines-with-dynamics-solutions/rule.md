---
type: rule
archivedreason: 
title: Do you use Azure DevOps Pipelines with your Dynamics solutions?
guid: 3c8e8c89-81e3-4752-8a94-26ae330df83a
uri: use-azure-devops-pipelines-with-dynamics-solutions
created: 2021-02-19T18:15:27.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-use-azure-devops-pipelines-with-your-dynamics-solutions

---


<p class="ssw15-rteElement-P">​Are you still managing your Dynamics solution changes manually? Manually exporting and importing solutions across environments? Manually exporting unmanaged solutions to commit to source control. If so, read on, because there is a better way! ​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>Dynamics (and model-driven Power Apps) use solution files to store and apply changes across environments. Using the 
   <a href="https://docs.microsoft.com/en-us/power-platform/alm/devops-build-tools">Power Platform Build Tools for Azure DevOps</a> will let automate manual tasks like: </p><ul><li>Exporting unmanaged solutions and committing to source control </li><li>Generating managed solutions for use in downstream environments such as Testing and Production </li><li>Deploying solutions to downstream environments </li><li>Provisioning or de-provisioning environments </li></ul><p>Want to learn more? </p><p>Check out the guide on 
   <a href="https://github.com/microsoft/PowerApps-Samples/tree/master/build-tools">GitHub</a>. The guide demonstrates: </p><ol><li>Configuring Azure DevOps </li><li>Build the 'Capture Pipeline' (Export solution) </li><li>Build the 'Build Pipeline' (Generate Build Artifact) </li><li>Build the 'Release Pipeline' (Deploy to Production) </li></ol><dl class="image"><dt>
      <img src="sample-azure-1.png" alt="sample-azure-1.png" />
   </dt><dd>Figure: Sample Azure Pipeline to export solution and commit to source control </dd></dl><dl class="image"><dt>
<img src="sample-azure-2.png" alt="sample-azure-2.png" /></dt><dd>Figure: Sample Azure Pipeline to create a managed solution from source  </dd></dl><dl class="image"><dt>
<img src="sample-azure-3.png" alt="sample-azure-3.png" /></dt><dd>Figure: Sample Release Pipeline to deploy the managed solution to production<span style="color:#444444;">​​</span></dd></dl>


