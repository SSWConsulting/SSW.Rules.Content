---
type: rule
archivedreason: 
title: Do you sync your GitHub Issues to Azure DevOps?
guid: ef4ae2ef-b45d-4403-820e-e3374019bb1c
uri: do-you-sync-your-github-issues-to-azure-devops
created: 2020-10-18T22:36:33.0000000Z
authors:
- id: 99
  title: Christian Morford-Waite
related: []

---

If you store all your code in GitHub, why not create all your issues there too?

You might be reluctant to move your backlog to GitHub from Azure DevOps as you don’t want to lose the metrics functionality. 

But you can easily sync all your GitHub Issues to Azure DevOps automatically to have the best of both worlds.


<!--endintro-->

Here's a quick guide in setting it up for your GitHub Repository and Azure DevOps.

1. Install the [Azure Boards App](https://github.com/marketplace/azure-boards) from the GitHub Marketplace
2. Create the GitHub Action secrets


> * **ADO\_PERSONAL\_ACCESS\_TOKEN** (Azure DevOps | User settings | Security | Personal access tokens)
> The [Azure Personal Access Token](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate) requires "read & write" permission for Work Items.
> * **GH\_PERSONAL\_ACCESS\_TOKEN** (GitHub | Personal settings | Developer settings | Personal access tokens)
> The [GitHub Personal Access Token](https://help.github.com/en/enterprise/2.17/user/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) requires "repo" permissions.
> * **ADO\_ORGANIZATION** (https:// **ssw** .visualstudio.com/SSW.Rules)
> The Organization name is in your Azure DevOps URL.
> * **ADO\_PROJECT** (https://ssw.visualstudio.com/ **SSW.Rules** )
> The Project name can also be found in your Azure DevOps URL.


3. Create the following GitHub Action

e.g. SSW uses this template for their projects, you may need to change the new and closed states depending on your environment.

name: Sync issue to Azure DevOps work item
on:
  issues:
    types:
      [opened, edited, deleted, closed, reopened, labeled, unlabeled, assigned]

jobs:
  alert:
    runs-on: ubuntu-latest
    steps:
      - uses: danhellem/github-actions-issue-to-work-item@master
        env:
          ado\_token: "${{ secrets.ADO\_PERSONAL\_ACCESS\_TOKEN }}"
          github\_token: "${{ secrets.GH\_PERSONAL\_ACCESS\_TOKEN }}"
          ado\_organization: "${{ secrets.ADO\_ORGANIZATION }}"
          ado\_project: "${{ secrets.ADO\_PROJECT }}"
          ado\_wit: "Product Backlog Item"
          ado\_new\_state: "New"
          ado\_close\_state: "Done"
          ado\_bypassrules: true


::: good
Figure: Good Example - GitHub Action to Sync Issues to Azure DevOps

:::

<dl class="ssw15-rteElement-ImageArea"><br><img src="GitHub-Issues-Syncing-to-AzDevOps.png" alt="" style="margin:5px;"><br><br>::: good<br>Figure: Good Example - GitHub Issues Syncing to Azure DevOps<br><br><br>:::<br><br></dl>
Pros

* Easily manage sprints and calculate burndown and cycle time
* See all your GitHub Issues and Azure DevOps PBIs in one backlog
* Automated tagging and hyperlinking between Issues and PBIs


### Cons


* The sync is only one-way GitHub Issues -> Azure DevOps Backlog
* It won’t sync existing GitHub Issues unless they are updated

 
More information about this GitHub Action can be found here https://github.com/danhellem/github-actions-issue-to-work-item
