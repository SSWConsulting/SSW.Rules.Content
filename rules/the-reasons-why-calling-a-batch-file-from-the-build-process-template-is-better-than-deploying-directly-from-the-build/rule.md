---
type: rule
archivedreason: 
title: Do you know the reasons why calling a Batch File from the Build Process Template is better than Deploying Directly from the Build?
guid: 8566b478-1aed-4c79-a42d-8e7aa48fb2db
uri: the-reasons-why-calling-a-batch-file-from-the-build-process-template-is-better-than-deploying-directly-from-the-build
created: 2013-02-05T19:39:39.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
- do-you-know-the-reasons-why-calling-a-batch-file-from-the-build-process-template-is-better-than-deploying-directly-from-the-build

---

Ideally, Builds are created once, and can then be deployed to any environment, at any point in time (Build Once, Deploy Many).
We do this by including deployment batch files in the solution, and specifying them to be called in the Build Process Template.

<!--endintro-->


::: bad  
![](deployment-scripts.jpg)  
:::
Figure: Good Example - Include deployment scripts in the solution, and execute them from the Build Process Template

| | Bad Example - Using Builds to Deploy | Good Example - Using Batch File |
| --- | --- | --- |
| Deployment Overview | <ol><li>A separate build is created per target environment</li><li>The MS Deploy parameters are put into the MSBuild parameters setting on the process template</li><li>The build for the shared development server is set to be a CI build so it is executed on every check-in</li></ol> | <ol><li>One batch file per target environment is created and checked into source control alongside the web project</li><li>Each batch file is accompanied by a corresponding Web Deploy Parameterisation XML file with environment specific settings</li><li>The build process template is modified to call the batch file to continuously deploy to the shared development server</li></ol> |
| --- | --- | --- |
| Deployment Process | <ol><li>The build is automatically deployed to the shared dev server</li><li>Lots of testing occurs and we decide to deploy to staging</li><li>We can just kick off the staging build</li><li>A whole lot of testing occurs and we want to deploy to production</li><li>We can kick off a production build, but this will deploy the latest source code to production</li><li>If we want to deploy the version of the software that we have deployed to staging we have to get that specific version from source control, and then do a production build of it</li></ol> | <ol><li>The build is automatically deployed to the shared dev server</li><li>Lots of testing occurs and we decide to deploy to staging</li><li>The batch file for any build can be executed and the build deployed to staging</li><li>A whole lot of testing occurs on staging and then we decide to deploy the same build to production
We just call the batch file in the folder to do the deployment. No new build is required</li></ol> |
| --- | --- | --- |
| Benefits | <ul><li>No need to create batch files or modify the process template</li></ul> | <ol><li>Builds are created once, and can then be deployed many times to any environment, at any point in time (Build Once, Deploy Many)</li><li>When deploying to production, we use exactly the same build package as was used to deploy to staging</li><li>The custom build process template only does the deployment if the build succeeds and all the unit tests pass</li><li>Anyone with access to the batch file can deploy… including the product owner!</li><li>You only need one build per project</li></ol> |
| --- | --- | --- |
| Cons | <ul><li>Without modifying the build process template, the build will deploy even if the unit tests fail</li><li>To deploy a specific build to a particular server, it is necessary to get the code from source control, and then do a build</li><li>Only developers can deploy</li><li>You need a build per environment for each project</li><li>Build Once, Deploy Once. (You can’t redeploy a build to a different environment)</li></ul> | <ul><li>You must customize the build process template to execute the specified batch file from the build folder</li><li>We have to create custom batch files</li></ul> |
| --- | --- | --- |


TODO: AdamS - Include the steps to customize the build process template.

The Web Platform Installer is great, but does not install all the Web Deploy 3.0 components required for continuous deployment.
