---
type: rule
title: How do you deploy SharePoint?
uri: how-do-you-deploy-sharepoint
created: 2009-03-30T00:44:00.0000000Z
authors: []

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<p>Our answer to the deployment problem is&#160;a combination of tools and processes – we call it the SSWpackage.exe</p>
<ul>
<li><strong>Multiple development virtual machine environments<br></strong></li>
<ul>
<li>Test repeated deployment to staging before you actually deploy to the production server<br></li></ul>
<li><strong>SSW SharePoint Deployment Auditor</strong> – compares development, staging and production servers to identify missing files that needs to be deployed</li>
<ul>
<li>Specify ignore lists<br></li>
<li>Spits out XML code that would be easy to add to your package xml<br></li></ul>
<li><strong>SSW Package Updater</strong> – updates the solution package based on the XML definitions<br></li>
<ul>
<li>Ensure you always have the latest version of the files from development SharePoint included in your package.<br></li></ul>
<li><strong>Microsoft Visual Studio </strong>extensions for Windows SharePoint Services<br></li>
<ul>
<li>Using the latest VSeWSS 1.3 CTP<br></li>
<li>Generates the package and batch files<br></li></ul>
<li><strong>SharePoint STSADM</strong> tool for deployment</li></ul>
<p>Into the future of SSWPackage.exe</p>
<ul>
<li>Fully continuous integration with SharePoint<br></li>
<li>More SharePoint validation functions<br></li>
<li>Improved versioning control<br></li>
<li>A great GUI to bring it all together<br></li></ul>


