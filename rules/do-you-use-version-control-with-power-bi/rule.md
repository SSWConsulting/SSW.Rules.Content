---
type: rule
title: Do you use version control with Power BI?
uri: do-you-use-version-control-with-power-bi
authors:
  - title: Manu Gulati
    url: https://ssw.com.au/people/manu-gulati
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
  - title: Patricia Barros
    url: https://ssw.com.au/people/patricia-barros
  - title: Chris Beaver
    url: https://ssw.com.au/people/chris-beaver
related:
  - do-you-know-the-best-tool-to-migration-from-tfvc-to-git
redirects: []
created: 2017-03-29T06:06:12.000Z
archivedreason: null
guid: 80cbeca6-d33a-4ad3-8127-d3ae46fc5f00
---
### Foundational Concepts ###
Doing version control with Power BI reports used to be problematic. The primary way of doing this was to commit the pbix file into the repository using source control tools such as Visual Studio Code (VS Code). However, this has some drawbacks: 

* Data itself gets saved to source control, which is bad as it could be large 
* Unable to see what has changed
* Version control process is not user friendly for non-developers

::: bad
![Figure: Bad example - Not a good practice to commit pbix files to source control](bad-example-pbix-source-control.png)
:::

Microsoft has addressed these issues through the introduction of:

* [Git integration in Power BI Service via Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration)
  * *Requires either Fabric capacity or a Power BI Premium per User license*
  * *Currently only integrates with Git repos in Azure DevOps*
* [Power BI Desktop projects](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)

The following video from Microsoft Build 2023 provides an overview of this. 

`youtube: https://www.youtube.com/watch?v=OdkS7DF7ElY`
**Video: Empower every BI professional to do more with Microsoft Fabric | OD06 (Watch from min 5:00 to 13:00)**

At a high-level you can set up version control as follows. Click on the links to get more detailed instructions on Microsoft Learn. 

1. [Connect a workspace in Power BI Service with a branch in a Git repo in Azure DevOps](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=commit-to-git#connect-a-workspace-to-an-azure-repo)
2. [Commit changes to repo through the Power BI Service](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=commit-to-git#commit-changes-to-git)
3. [Update the workspace from Git](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started?tabs=commit-to-git#update-workspace-from-git)

Committing a report to the repo in this manner saves it as a Power BI Desktop Project (PBIP). A Project no longer contains a pbix file. It instead decomposes the report into the following artifacts.  

* [A Dataset folder](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset), which contains files and folders representing a Power BI dataset
* [A Reports folder](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report), which contains the report settings, metadata for custom visuals, etc.

::: img-medium
![Figure: PBIP artifacts](ProjectFolders.png)
:::

Whenever you see a .pbix file it should be converted to PBIP artifacts by following the instructions given in the articles above. 

### Developing Reports ###
You should no longer edit or publish reports directly in the production workspace. A better process for editing and committing reports is described below. 

#### Business Users ####

If you're a business user watch [this video](https://www.youtube.com/watch?v=XMGPDnTmYOw) to get a walkthrough of the process you would follow to edit and commit reports. 
The entire process is done on Power BI Service (web) (except the step to create a pull request). At a high-level the steps are:
1. Create a private workspace corresponding to the workspace where your report resides (1 time)
2. Connect the private workspace to repo (1 time)
3. Create new feature branch off ‘main’ (every time)
4. Setup dataset connections (1 time) (take help from SysAdmins or Power BI Admins)
5. Edit the report in Power BI Service (every time)
6. Commit report to feature branch (every time)
7. Create PR (pull request) to merge feature branch into ‘main’ on Azure DevOps (every time)
8. Next time, create new feature branch on same workspace

If you want to update the report's data model or want more sophisticated editing features, you will need to edit the report in Power BI Desktop instead. The next section explains how you can do so. 

#### Developers ####

If you're a developer watch [this video](https://www.youtube.com/watch?v=Cw3JAR1I8Ho) to get a walkthrough of the process you would follow to edit and commit reports. 
The process is done on one's PC. You will need to download Power BI Desktop. At a high-level the steps are:

1. Setup a local repository on your PC
2. Create new feature branch off ‘origin/main’
3. Open Power BI Desktop, and enable Power BI Projects - File | Option Settings | Options | Preview features | Power BI project (.pbip) save option
4. Open the [definition.pbir](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report#definitionpbir) file in the “\<Report Name\>.Reports” folder on the local repo on your PC. This will open the report in Power BI Desktop. It will allow you to edit both the report and the dataset.

   * **Note:** PBIP folders do not by default contain any underlying data. So when you open a definition.pbir file the visuals may show as empty. Once you refresh the report Power BI Desktop will download a copy of the data into a file called [cache.abf](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset#pbicacheabf) which gets stored in a ".pbi" folder inside the Dataset folder. This file should not be saved in version control. You can create a .gitignore file to prevent Git from committing it to the repository.

::: img-large
![Figure: cache.abf](PBICache.png)
:::

::: img-large
![Figure: The .gitignore file](Gitignore.png)
:::

5. Edit report in Power BI Desktop
6. Commit report to feature branch
7. Create PR to merge feature branch into ‘origin/main’ on Azure DevOps
8. If you are creating a new report in Power BI Desktop, please save the report as a **.pbip** report (and not .pbix). You can do so via File | Save as | Select .pbip as the file type.

### Deploying Reports ###
Deployments would typically be done by Power BI Admins. You as a dev generally won't do this directly unless you're responsible for a workspace yourself. 
Reports can be deployed to a production workspace by simply syncing the workspace with the 'main' branch in the Reports repository. The figure below illustrates this. 

![Figure: Example showing how to sync changes into a workspace in Power BI Service, effectively deploying reports](SyncChanges.png)
**Figure: Example showing how to sync changes into a workspace in Power BI Service, effectively deploying reports**
   
