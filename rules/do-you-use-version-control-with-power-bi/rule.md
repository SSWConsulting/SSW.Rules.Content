---
type: rule
title: Do you use version control with Power BI?
uri: do-you-use-version-control-with-power-bi
authors:
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
Doing version control with Power BI reports used to be problematic. The primary way of doing this was to commit the pbix file into the repository using source control tools such as Visual Studio Code (VS Code). However, this has some drawbacks: 

* Data itself gets saved to source control, which is bad as it could be large 
* Unable to see what has changed
* Version control process is not user friendly for non-developers

<Insert bad example>

Power BI now natively supports version control through the introduction of: 

* Git integration in Microsoft Fabric 

  * *Requires either Fabric capacity or a Power BI Premium per User license*
  * *Currently only integrates with Git repos in Azure DevOps*
* Power BI Desktop projects

At a high-level the steps to set this up are as follows. 

* Create a workspace in Power BI Service
* Connect it with a branch in a Git repo in Azure DevOps
  <Add image>
* Upload an existing pbix file to the workspace
* Commit files to repo in Power BI Service
  * Note that the pbix file itself will not be committed, so you can delete it
    <Add image>

Committing a report to the repo in this manner saves it as a Power BI Desktop Project (PBIP). A Project contains the following artifacts.  

* A Dataset folder, which contains files and folders representing a Power BI dataset
* A Reports folder
  * It contains a file called definition.pbir, which is what you would open to edit the report in Power BI Desktop
* A Project does not by default contain any underlying data. So when you open a definition.pbir file the visuals will show as empty. Once you refresh the report Power BI Desktop will download a copy of the data into a file called cache.abf which gets stored in a ".pbi" folder inside the Dataset folder.
  * This file should not be saved in version control. You can create a .gitignore file to prevent Git from committing it to the repository. 
  <Add image of gitignore file>
*
* Proposal

  * Create a Dev and main branch in SSW.PowerBI repo
  * Create a Dev and prod workspace in Power BI Service
  * Connect Dev and prod workspace with Dev and main branch in repo, respectively
  * Devs 

    * Edit reports in dev branch in local repo on their PC using Power BI Desktop
    * Commit changes to dev branch using tools such as VS Code
  * Non-devs 

    * Edit reports directly in the Dev workspace in Power BI Service
    * Commit changes to dev branch via Power BI Service
  * Create pull request on Azure DevOps to merge dev-branch with main branch

    * Pull requests can only be approved by some devs (e.g. PowerBIWhiteRobes)
  * Sync changes to the Prod workspace thereby deploying the reports to prod

<!--endintro-->

::: bad\
![Figure: Bad Example – Mixed Template and Power BI Files in Source Control](PowerBI-SourceControl-BadExample.png)\
:::