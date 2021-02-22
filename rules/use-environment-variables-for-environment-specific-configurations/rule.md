---
type: rule
archivedreason: 
title: Do you use Environment variables for environment-specific configurations?
guid: 0c8f342d-e4a0-4549-be76-824d609a980c
uri: use-environment-variables-for-environment-specific-configurations
created: 2020-10-27T23:29:13.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-use-environment-variables-for-environment-specific-configurations

---


<p class="ssw15-rteElement-P">If your Power Apps solution has any environment-specific configuration items, then an Environment Variable in the Solution gives you a configurable input parameter. Environment variables avoid hardcoding configuration information and having to keep track of and change configuration data when importing a solution.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​Some of the benefits of using environment variables are: ​<br></p>
<ul>
   <li>No need to manually edit configurable values in a production environment. </li><li>Configure one or more variables in one place and reference like a parameter across multiple solution components. </li><li>Enter different values while importing solutions to other environments. </li><li>Update values without a code change. </li><li>Granular level security managed by Common Data Service. </li><li>Unlimited number of variables (max solution size is 29 MB). </li><li>Service the definitions and the values independently or together. </li><li>Supported by Solution Packager and DevOps tools enable continuous integration and continuous delivery (CI/CD). </li><li>Support for localization. </li><li>Can be used to control feature flags and other application settings. </li></ul><dl class="image"><dt><img src="new-environment-variable.png" alt="new-environment-variable.png" style="width:750px;" /></dt><dd>Figure: Environment variable make configuration information easy</dd></dl><p>More information here: <a href="https://docs.microsoft.com/en-us/powerapps/maker/common-data-service/environmentvariables">https://docs.microsoft.com/en-us/powerapps/maker/common-data-service/environmentvariables</a></p>


