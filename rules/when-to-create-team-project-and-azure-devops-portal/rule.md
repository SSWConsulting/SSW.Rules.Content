---
seoDescription: When to create a team project and Azure DevOps Portal for a prospect/client? Create a TFS project and SharePoint site once a prospect/ client is ready to move forward after a Specification Review.
type: rule
title: Do you know when to create the team project and Azure DevOps Portal for a prospect/client?
uri: when-to-create-team-project-and-azure-devops-portal
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/ulysses-maclaren
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Gordon Beeming
    url: https://ssw.com.au/people/gordon-beeming
created: 2021-08-31T18:11:04.052Z
archivedreason: Azure DevOps does not support SharePoint Team Sites (since 2018) - Discontinue SharePoint integration - TFS https://learn.microsoft.com/en-us/previous-versions/azure/devops/report/sharepoint-dashboards/deprecation/discontinue-pre-tfs-2017-sharepoint-integration?view=tfs-2017. Replaced by https://ssw.com.au/rules/connect-crm-to-microsoft-teams
guid: 2a827a86-f4c9-496e-aba1-6b77ea2a1429
---

::: info
Azure DevOps does not support SharePoint Team Sites (since 2018) - Discontinue SharePoint integration - TFS <https://learn.microsoft.com/en-us/previous-versions/azure/devops/report/sharepoint-dashboards/deprecation/discontinue-pre-tfs-2017-sharepoint-integration?view=tfs-2017>.
:::

When a prospect/client is ready to move forward (typically after a Specification Review)...

<!--endintro-->

1. Create a TFS project (to track the work items and releases)
2. Create a SharePoint project site

   You can do both of these at the same time by creating a Azure DevOps project and use a SharePoint dashboard.
   ![Figure: Choose to create a new SharePoint site when creating Azure DevOps project](createnewspsite.jpeg)

**Note:** It is also possible to [create a new SharePoint site afterwards and attach it to a Azure DevOps project, via this hack](/how-to-create-Project-Portal)

3. Move all the documents you've created for this client, from the 'Prospects Site (Document Library)' into the new project site.

A few other things to do frequently do right away:

- If required, create an external user account for the Product Owner. This enables the client access to your SharePoint Extranet to see the documents, sites and reports.
- If required, let the client know they can upload additional files, or download a copy of the project for testing and deployment.
- Check permissions and access rights
- Consider synchronizing the project documents offline via Outlook or SharePoint Workspaces
- Edit the SharePoint site landing wiki-page and upload some pictures of the team
  ![Figure: Once your 'TFS Portal' is ready, add a picture of the team site, prior to letting them know about the new site](addimgtoteamsite.jpeg)
