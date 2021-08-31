---
type: rule
title: Do you know how to create your Project Portal (for existing Azure DevOps
  Team Projects)?
uri: how-to-create-project-portal
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
created: 2021-08-31T18:17:43.194Z
guid: e5adaaeb-1a44-4022-bdfe-5fc5b186ff81
---
Unfortunately the Azure DevOps team did not have time to build the feature to create a SharePoint site, after the project is created. Next version, we hope.

<!--endintro-->

There is a goofy work around:
1. Create a new temporary project (with a SharePoint site for it)
2. Disable the site for the new project, by checking off '[x] Enable team project portal'
3. Go back to the old Azure DevOps project
4. Enable the site for the original one (pointing to that newly created site)
5. Finally, delete the temporary project you created

More info at [Configure or add a project portal
](https://docs.microsoft.com/en-us/azure/devops/project/configure-or-add-a-project-portal?view=azure-devops)

