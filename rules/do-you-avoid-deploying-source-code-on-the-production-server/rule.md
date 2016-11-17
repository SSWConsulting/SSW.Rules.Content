---
type: rule
title: Do you avoid deploying source code on the production server?
uri: do-you-avoid-deploying-source-code-on-the-production-server
created: 2016-11-17T13:15:08.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>When you are deploying an ASP.NET project (no matter it's a Web site or a Web application), do not copy all files of this project to the production server because source code will be deployed during this simple copy and it makes easier for others to access or tamper the source code of your site.</p><p>Instead, please use 'Publish' utility to deploy your Web site or Web application. This utility can remove the source code from the site.​​<br></p> </span>

<ol><li>​Web Site Project
      <p><strong>Publish Web Site</strong>&#160;dialog box is designed to precompile and deploy your Web site to a new location (whatever it is, ftp&#58;//..., http&#58;//... or drive&#58;\path). During the deployment, source code are removed automatically. Besides, the precompilation process finds any compilation errors and identifies the errors in the configuration file.</p><p>To access this dialog box, please open a Web site that you want to deploy and click&#160;<strong>Build</strong>&#160;menu, then click&#160;<strong>Publish Web Site</strong>.​
      </p><dl class="image"><dt><img src="/PublishingImages/PublishWebsite.jpg" alt="PublishWebsite.jpg" /></dt><dd>Figure&#58; How to open&#160;<strong>Publish Web Site</strong>&#160;dialog box</dd></dl><dl class="image"><dt><img src="/PublishingImages/PublishWebsiteDialog.JPG" alt="PublishWebsiteDialog.JPG" />​​ </dt><dd>Figure&#58;&#160;<strong>Publish Web Site</strong>&#160;dialog box</dd></dl><p>See more about&#160;<a href="https&#58;//msdn.microsoft.com/en-us/library/20yh9f1b.aspx" target="_blank">Publishing Web Sites</a>.</p></li><li>Web Application Project 
      <p>The&#160;<strong>Publish Web</strong>&#160;dialog box enables you to build and publish a Web application project to a new location. Like&#160;<strong>Publish Web Site</strong>&#160;dialog box, this utility can remove source code. However you have to select&#160;<strong>Only files needed to run this application</strong>&#160;to specify it. Other benefit of this utility is that potential errors and compile-time errors in the Web.config file and in other non-code files can be found.</p><p>To access this dialog box, open a Web application project that you want to publish and click&#160;<strong>Publish</strong>&#160;ApplicationName on the&#160;<strong>Build</strong>&#160;menu.​
      </p><dl class="image"><dt><img src="/PublishingImages/PublishWebApp.jpg" alt="PublishWebApp.jpg" /></dt><dd>Figure&#58; How to open&#160;<strong>Publish Web</strong>&#160;dialog ('WebApp' is the name of this application)​</dd></dl><dl class="image"><dt><img src="/PublishingImages/PublishWebAppDialog.JPG" alt="PublishWebAppDialog.JPG" /> </dt><dd>Figure&#58;&#160;<strong>Publish Web&#160;</strong>dialog box</dd></dl>​​
      <p>See more about&#160;<a href="https&#58;//msdn.microsoft.com/en-us/library/aa983453.aspx" target="_blank">How to Publish Web Applications</a>.<br></p></li></ol> ​<br>


