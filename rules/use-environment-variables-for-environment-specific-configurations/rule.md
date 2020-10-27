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
<p>​Some of the benefits of using environment variables are&#58;&#160;​<br></p>
<ul>
   <li>No need to manually edit configurable values in a production environment.&#160;</li><li>Configure one or more variables in one place and reference like a parameter across multiple solution components.&#160;</li><li>Enter different values while importing solutions to other environments.&#160;</li><li>Update values without a code change.&#160;</li><li>Granular level security managed by&#160;Common Data Service.&#160;</li><li>Unlimited number of variables (max solution size is 29 MB).&#160;</li><li>Service the definitions and the values independently or together.&#160;</li><li>Supported by&#160;Solution Packager&#160;and&#160;DevOps&#160;tools enable continuous integration and continuous delivery (CI/CD).&#160;</li><li>Support for localization.&#160;</li><li>Can be used to control feature flags and other application settings.&#160;</li></ul><dl class="image"><dt><img src="/PublishingImages/new-environment-variable.png" alt="new-environment-variable.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Environment variable make configuration information easy</dd></dl><p>More information here&#58; <a href="https&#58;//docs.microsoft.com/en-us/powerapps/maker/common-data-service/environmentvariables">https&#58;//docs.microsoft.com/en-us/powerapps/maker/common-data-service/environmentvariables</a></p>


