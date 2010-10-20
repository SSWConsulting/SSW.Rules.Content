---
type: rule
title: How do you deploy SharePoint?
uri: how-do-you-deploy-sharepoint
created: 2009-03-30T00:44:00.0000000Z
authors: []

---



<span class='intro'> <p>We use <strong>SSWPackage.exe</strong></p>
<p>The long answer&#58;</p>
<p>Deploying changes between development, staging and production servers can be a very interesting exercise&#58;</p>
<ul>
<li>It is painstakingly awkward when you realize that you have forgotten a file</li>
<li>Or forgotten to take the latest version of a particular file</li>
<li>Each iteration is manual and can be error prone</li>
<li>The result is that your developers are working late into the evening and your SharePoint servers are down for a prolonged period of time – something that may be very difficult to accept in a corporate environment</li></ul>
<p>At SSW, we saw all this was unacceptable and work to improve this process.<br></p> </span>

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


