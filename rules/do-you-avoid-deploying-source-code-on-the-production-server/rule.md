---
type: rule
archivedreason: 
title: Do you avoid deploying source code on the production server?
guid: d8faf9ec-e8fb-4399-90fe-c01f818420f8
uri: do-you-avoid-deploying-source-code-on-the-production-server
created: 2016-11-17T13:15:08.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>When you are deploying an ASP.NET project (no matter it's a Web site or a Web application), do not copy all files of this project to the production server because source code will be deployed during this simple copy and it makes easier for others to access or tamper the source code of your site.</p><p>Instead, please use 'Publish' utility to deploy your Web site or Web application. This utility can remove the source code from the site.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>​Web Site Project
      <p><strong>Publish Web Site</strong> dialog box is designed to precompile and deploy your Web site to a new location (whatever it is, ftp://..., http://... or drive:\path). During the deployment, source code are removed automatically. Besides, the precompilation process finds any compilation errors and identifies the errors in the configuration file.</p><p>To access this dialog box, please open a Web site that you want to deploy and click <strong>Build</strong> menu, then click <strong>Publish Web Site</strong>.​
      </p><dl class="image"><dt><img src="PublishWebsite.jpg" alt="PublishWebsite.jpg" /></dt><dd>Figure: How to open <strong>Publish Web Site</strong> dialog box</dd></dl><dl class="image"><dt><img src="PublishWebsiteDialog.JPG" alt="PublishWebsiteDialog.JPG" />​​ </dt><dd>Figure: <strong>Publish Web Site</strong> dialog box</dd></dl><p>See more about <a href="https://msdn.microsoft.com/en-us/library/20yh9f1b.aspx" target="_blank">Publishing Web Sites</a>.</p></li><li>Web Application Project 
      <p>The <strong>Publish Web</strong> dialog box enables you to build and publish a Web application project to a new location. Like <strong>Publish Web Site</strong> dialog box, this utility can remove source code. However you have to select <strong>Only files needed to run this application</strong> to specify it. Other benefit of this utility is that potential errors and compile-time errors in the Web.config file and in other non-code files can be found.</p><p>To access this dialog box, open a Web application project that you want to publish and click <strong>Publish</strong> ApplicationName on the <strong>Build</strong> menu.​
      </p><dl class="image"><dt><img src="PublishWebApp.jpg" alt="PublishWebApp.jpg" /></dt><dd>Figure: How to open <strong>Publish Web</strong> dialog ('WebApp' is the name of this application)​</dd></dl><dl class="image"><dt><img src="PublishWebAppDialog.JPG" alt="PublishWebAppDialog.JPG" /> </dt><dd>Figure: <strong>Publish Web </strong>dialog box</dd></dl>​​
      <p>See more about <a href="https://msdn.microsoft.com/en-us/library/aa983453.aspx" target="_blank">How to Publish Web Applications</a>.<br></p></li></ol> ​<br>


