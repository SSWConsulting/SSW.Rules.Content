---
type: rule
archivedreason: 
title: Do you know the reasons why calling a Batch File from the Build Process Template is better than Deploying Directly from the Build?
guid: 8566b478-1aed-4c79-a42d-8e7aa48fb2db
uri: do-you-know-the-reasons-why-calling-a-batch-file-from-the-build-process-template-is-better-than-deploying-directly-from-the-build
created: 2013-02-05T19:39:39.0000000Z
authors:
- id: 24
  title: Adam Stephensen
related: []

---


<p>​Ideally Builds are created once, and can then be deployed to any environment, at any point in time (Build Once, Deploy Many).<br>We do this by including deployment batch files in the solution, and specifying them to be called in the Build Process Template. </p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt> 
      <img src="/Pages/The-Reasons-why-calling-a-Batch-File-from-the-Build-Process-Template-is-better-than-Deploying-Directly-from-the-Build.aspx#" alt="" /> 
   </dt><dd>Figure&#58; Bad Example - Including xcopy command in the post build process</dd></dl><dl class="goodImage"><dt> 
      <img alt="Deployment scripts" src="/PublishingImages/deployment-scripts.jpg" /> 
   </dt><dd>Figure&#58; Good Example - Include deployment scripts in the solution, and execute them from the Build Process Template</dd></dl><table cellpadding="2" border="1"><tbody><tr><th></th><th>Bad Example - Using Builds to Deploy </th><th>Good Example - Using Batch File</th></tr><tr><th>Deployment Overview</th><td><ol><li>A separate build is created per target environment</li><li>The MS Deploy parameters are put into the MSBuild parameters setting on the process template</li><li>The build for the shared development server is set to be a CI build so it is executed on every check-in</li></ol></td><td><ol><li>One batch file per target environment is created and checked into source control alongside the web project</li><li>Each batch file is accompanied by a corresponding Web Deploy Parameterisation xml file with environment specific settings</li><li>The build process template is modified to call the batch file to continuously deploy to the shared development server</li></ol></td></tr><tr><th>Deployment Process</th><td><ol><li>The build is automatically deployed to the shared dev server</li><li>Lots of testing occurs and we decide to deploy to staging</li><li>We can just kick off the staging build</li><li>A whole lot of testing occurs and we want to deploy to production</li><li>We can kick off a production build, but this will deploy the latest source code to production</li><li>If we want to deploy the version of the software that we have deployed to staging we have to get that specific version from source control, and then do a production build of it</li></ol></td><td><ol><li>The build is automatically deployed to the shared dev server</li><li>Lots of testing occurs and we decide to deploy to staging </li><li>The batch file for any build can be executed and the build deployed to staging</li><li>A whole lot of testing occurs on staging and then we decide to deploy the same build to production<br> We just call the batch file in the folder to do the deployment. No new build is required</li></ol></td></tr><tr><th>Benefits</th><td><ul><li>No need to create batch files or modify the process template</li></ul></td><td><ol><li>Builds are created once, and can then be deployed many times to any environment, at any point in time (Build Once, Deploy Many)</li><li>When deploying to production, we use exactly the same build package as was used to deploy to staging</li><li>The custom build process template only does the deployment if the build succeeds and all the unit tests pass</li><li>Anyone with access to the batch file can deploy… including the product owner!</li><li>You only need one build per project</li></ol></td></tr><tr><th>Cons</th><td><ul><li>Without modifying the build process template, the build will deploy even if the unit tests fail </li><li>To deploy a specific build to a particular server, it is necessary to get the code from source control, and then do a build</li><li>Only developers can deploy</li><li>You need a build per environment for each project</li><li>Build Once, Deploy Once. (You can’t redeploy a build to a different environment)</li></ul></td><td><ul><li>You must customize the build process template to execute the specified batch file from the build folder</li><li>We have to create custom batch files </li></ul></td></tr></tbody></table><p style="color&#58;red;font-weight&#58;bold;">TODO&#58; AdamS - Include the steps to customize the build process template.</p><p>The Web Platform Installer is great, but does not install all the Web Deploy 3.0 components required for continuous deployment.</p>


