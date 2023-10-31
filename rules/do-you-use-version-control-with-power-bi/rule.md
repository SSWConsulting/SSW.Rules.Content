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

Microsoft has addressed these issues through the introduction of:

* [Git integration in Power BI Service via Microsoft Fabric] (https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration)
  * *Requires either Fabric capacity or a Power BI Premium per User license*
  * *Currently only integrates with Git repos in Azure DevOps*
* [Power BI Desktop projects] (https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)

At a high-level you can set this up as follows. 

1. Create a workspace in Power BI Service
2. Connect it with a branch in a Git repo in Azure DevOps
  <Add image>
3. Upload an existing pbix file to the workspace
4. Commit files to repo through the Power BI Service
   * Note that the pbix file itself will not be committed, so you can delete it
    <Add image>

Committing a report to the repo in this manner saves it as a Power BI Desktop Project (PBIP). A Project contains the following artifacts.  

* A Dataset folder, which contains files and folders representing a Power BI dataset
* A Reports folder, which contains the report settings, metadata for custom visuals, etc.

You now have two options to edit the report and commit changes. 
1. You can directly edit the report in Power BI Service, and then commit to the repo via Power BI Service. This is the option that non-developers may prefer as they generally don't modify the data model, and as the version control user interface is simple. 
2. Clone a local copy of the repo on your PC by using version control tools such as VS Code, and use Power BI Desktop to edit the report. 
   * The PBIP Reports folder contains a file called definition.pbir, which is what you would open to edit the report in Power BI Desktop. This allows you to edit both the report and the dataset. 
   * You would then use VS Code to commit any changes back into the repo. Since PBIP decomposes a pbix into component files, many of which are textual, you can compare files across commits. 
   * **Note:** PBIP folders do not by default contain any underlying data. So when you open a definition.pbir file the visuals will show as empty. Once you refresh the report Power BI Desktop will download a copy of the data into a file called cache.abf which gets stored in a ".pbi" folder inside the Dataset folder.
  <Add image> 
   This file should not be saved in version control. You can create a .gitignore file to prevent Git from committing it to the repository. 
  <Add image of gitignore file>
* 

::: bad\
![Figure: Bad Example – Mixed Template and Power BI Files in Source Control](PowerBI-SourceControl-BadExample.png)\
:::