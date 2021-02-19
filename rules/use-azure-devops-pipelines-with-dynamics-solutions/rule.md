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


<p class="ssw15-rteElement-P">​Are you still managing your Dynamics solution changes manually? Manually exporting and importing solutions across environments? Manually exporting unmanaged solutions to commit to source control. If so, read on, because there is a better way!&#160;​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>Dynamics (and model-driven Power Apps) use solution files to store and apply changes across environments. Using the 
   <a href="https&#58;//docs.microsoft.com/en-us/power-platform/alm/devops-build-tools">Power Platform Build Tools for Azure DevOps</a> will let automate manual tasks like&#58;&#160;</p><ul><li>Exporting unmanaged solutions and committing to source control&#160;</li><li>Generating managed solutions for use in downstream environments such as Testing and Production&#160;</li><li>Deploying solutions to downstream environments&#160;</li><li>Provisioning or de-provisioning environments&#160;</li></ul><p>Want to learn more?&#160;</p><p>Check out the guide on 
   <a href="https&#58;//github.com/microsoft/PowerApps-Samples/tree/master/build-tools">GitHub</a>. The guide demonstrates&#58;&#160;</p><ol><li>Configuring Azure DevOps&#160;</li><li>Build the 'Capture Pipeline' (Export solution)&#160;</li><li>Build the 'Build Pipeline' (Generate Build Artifact)&#160;</li><li>Build the 'Release Pipeline' (Deploy to Production)&#160;</li></ol><dl class="image"><dt>
      <img src="/PublishingImages/sample-azure-1.png" alt="sample-azure-1.png" />
   </dt><dd>Figure&#58; Sample Azure Pipeline to export solution and commit to source control&#160;</dd></dl><dl class="image"><dt>
<img src="/PublishingImages/sample-azure-2.png" alt="sample-azure-2.png" /></dt><dd>Figure&#58; Sample Azure Pipeline to create a managed solution from source &#160;</dd></dl><dl class="image"><dt>
<img src="/PublishingImages/sample-azure-3.png" alt="sample-azure-3.png" /></dt><dd>Figure&#58; Sample Release Pipeline to deploy the managed solution to production<span style="color&#58;#444444;">​​</span></dd></dl>


