---
seoDescription: Automate Dynamics solution management with Azure DevOps Pipelines, streamlining exports, deployments, and provisioning across environments.
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

Are you still managing your Dynamics solution changes manually? Manually exporting and importing solutions across environments? Manually exporting unmanaged solutions to commit to source control. If so, read on, because there is a better way!

<!--endintro-->

Dynamics (and model-driven Power Apps) use solution files to store and apply changes across environments. Using the [Power Platform Build Tools for Azure DevOps](https://docs.microsoft.com/en-us/power-platform/alm/devops-build-tools) will let automate manual tasks like:

- Exporting unmanaged solutions and committing to source control
- Generating managed solutions for use in downstream environments such as Testing and Production
- Deploying solutions to downstream environments
- Provisioning or de-provisioning environments

Want to learn more?

Check out the guide on [GitHub](https://github.com/microsoft/PowerApps-Samples/tree/master/build-tools). The guide demonstrates:

1. Configuring Azure DevOps
2. Build the 'Capture Pipeline' (Export solution)
3. Build the 'Build Pipeline' (Generate Build Artifact)
4. Build the 'Release Pipeline' (Deploy to Production)

![Figure: Sample Azure Pipeline to export solution and commit to source control](sample-azure-1.png)

![Figure: Sample Azure Pipeline to create a managed solution from source](sample-azure-2.png)

![Figure: Sample Release Pipeline to deploy the managed solution to production](sample-azure-3.png)
