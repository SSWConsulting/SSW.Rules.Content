---
type: rule
title: Do you Create a Deployment Batch file and SetParameters file for each Environment?
uri: do-you-create-a-deployment-batch-file-and-setparameters-file-for-each-environment
created: 2013-02-06T18:52:13.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>You should create a Deployment Batch file and SetParameters file for each Environment.</p> </span>

<dl class="goodImage"><dt> 
      <img src="setparameters.jpg" alt="" /> 
   </dt><dd>Figure&#58; Good Example - The batch file specifies the target Server, the ProjectName name to deploy, and the configuration file to use. You can also optionally supply additional parameters. 
      <a href="/Documents/DeployBat.txt">Download a sample _Deploy.bat file here as a .txt file</a>. </dd></dl><dl class="goodImage"><dt> 
      <img src="batfile.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example - The SetParameters file specifies MS Deploy parameterisation values.  Most important is the target “IIS Web Application Name” on the target server<br>See 
      <a target="_blank" href="http&#58;//vishaljoshi.blogspot.com.au/2010/07/web-deploy-parameterization-in-action.html">Vishal’s blog</a> for more details. </dd></dl>


