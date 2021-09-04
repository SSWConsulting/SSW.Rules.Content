---
type: rule
archivedreason: 
title: Do you Create a Deployment Batch file and SetParameters file for each Environment?
guid: 9a47c960-e98c-40d0-bb0f-2dbc164f476f
uri: do-you-create-a-deployment-batch-file-and-setparameters-file-for-each-environment
created: 2013-02-06T18:52:13.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---

You should create a Deployment Batch file and SetParameters file for each Environment.

<!--endintro-->


::: good  
![Figure: Good Example - The batch file specifies the target Server, the ProjectName name to deploy, and the configuration file to use. You can also optionally supply additional parameters.](setparameters.jpg)  
:::

[Download a sample Deploy.bat file here as a .txt file](DeployBat.txt)


::: good  
![Figure: Good Example - The SetParameters file specifies MS Deploy parameterisation values.  Most important is the target “IIS Web Application Name” on the target serverSee        Vishal’s blog for more details.](batfile.jpg)  
:::
