---
type: rule
archivedreason: 
title: Do you avoid deploying source code on the production server?
guid: d8faf9ec-e8fb-4399-90fe-c01f818420f8
uri: avoid-deploying-source-code-on-the-production-server
created: 2016-11-17T13:15:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-deploying-source-code-on-the-production-server

---

When you are deploying an ASP.NET project (no matter it's a Web site or a Web application), do not copy all files of this project to the production server because source code will be deployed during this simple copy and it makes easier for others to access or tamper the source code of your site.

Instead, please use 'Publish' utility to deploy your Web site or Web application. This utility can remove the source code from the site.

<!--endintro-->

1. Web Site Project
          **Publish Web Site** dialog box is designed to precompile and deploy your Web site to a new location (whatever it is, ftp://..., http://... or drive:\path). During the deployment, source code are removed automatically. Besides, the precompilation process finds any compilation errors and identifies the errors in the configuration file.
    To access this dialog box, please open a Web site that you want to deploy and click  **Build** menu, then click  **Publish Web Site** .

![Figure: How to open Publish Web Site dialog box](PublishWebsite.jpg)  

![Figure: Publish Web Site dialog box](PublishWebsiteDialog.JPG)  
    See more about [Publishing Web Sites](https://msdn.microsoft.com/en-us/library/20yh9f1b.aspx).
2. Web Application Project 
          The  **Publish Web** dialog box enables you to build and publish a Web application project to a new location. Like  **Publish Web Site** dialog box, this utility can remove source code. However you have to select  **Only files needed to run this application** to specify it. Other benefit of this utility is that potential errors and compile-time errors in the Web.config file and in other non-code files can be found.
    To access this dialog box, open a Web application project that you want to publish and click  **Publish** ApplicationName on the  **Build** menu.

![Figure: How to open Publish Web dialog ('WebApp' is the name of this application)](PublishWebApp.jpg)  

![Figure: Publish Web dialog box](PublishWebAppDialog.JPG)  
    See more about [How to Publish Web Applications](https://msdn.microsoft.com/en-us/library/aa983453.aspx).
