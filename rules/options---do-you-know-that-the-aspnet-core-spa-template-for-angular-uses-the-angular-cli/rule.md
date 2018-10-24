---
type: rule
title: Options - Do you know that the ASP.NET Core SPA Template for Angular uses the Angular CLI?
uri: options---do-you-know-that-the-aspnet-core-spa-template-for-angular-uses-the-angular-cli
created: 2018-10-24T21:43:41.0000000Z
authors:
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p class="ssw15-rteElement-InfoBox"><b>For .NET Developers only!</b></p><p>For many Angular solutions, a good practice is to keep your client-side and server-side code in separate projects.&#160;</p><ul><li>You get a clear separation of concerns</li><li>You usually expect your server-side stack to outlive your client-side technologies</li><li>You may plan to use your WebAPI with multiple user interfaces such as mobile or bots<br></li><li>Easier to deploy your angular app to a CDN<br></li></ul> </span>

<p>For some solutions, it might be simpler to integrate your client-side and server-side into a single project – and with the SPA templates for ASP.Net Core, this has never been easier.</p><ul><li>A single project might make sense for a smaller, simpler solution<br></li><li>There will be only one website to deploy to a single web server that will serve both angular and WebAPI sites<br></li><li>The project can be built with a single build process<br></li><li>This might be a good choice if you are looking to migrate an existing MVC website as you can host MVC pages and the Angular app under one site<br></li><li>This approach is easier if you want to use Windows Authentication<br></li><li>No CORS configuration required<br></li></ul><p>To create an Angular application with the SPA template new project from the command line or you can use Visual Studio. From ASP.NET Core 2.1 onwards, this template is included.&#160;&#160;</p><dl class="image"><dt><img src="/PublishingImages/create-angular-via-cmd.png" alt="create-angular-via-cmd.png" /></dt><dd>Figure&#58; Creating a project from the command line</dd></dl><dl class="image"><dt><img src="/PublishingImages/create-angular-via-vs.jpg" alt="create-angular-via-vs.jpg" /></dt><dd>Figure&#58; Creating a project using Visual Studio <br></dd></dl><p>Although Visual Studio can be used to create the project, we still recommend Visual Studio Code for working with the Angular code, as per <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=481b8d76-c2aa-4452-954a-26bb11628ba0">Do you know the best IDE for Angular? </a> <br>
   </p><h3 class="ssw15-rteElement-H3">
    ​​​The ASP.NET Core SPA Template for Angular Includes&#58;&#160;</h3><dl class="image"><dt><img src="/PublishingImages/simple-example-webapi.jpg" alt="simple-example-webapi.jpg" /></dt><dd>Figure&#58; A simple example WebAPI</dd></dl><dl class="image"><dt><img src="/PublishingImages/angular-ui-with-bootstrap.jpg" alt="angular-ui-with-bootstrap.jpg" /></dt><dd>Figure&#58; An Angular UI with Twitter Bootstrap styling</dd></dl><dl class="image"><dt><img src="/PublishingImages/angular-server-side-config.png" alt="angular-server-side-config.png" /></dt><dd>Figure&#58; Server-side configuration in Startup.cs allowing the Angular UI to be hosted from under the single ASP.NET Core website</dd></dl><p>This Angular app uses the Angular CLI and is fully compatible with any other Angular CLI app. If you want to create a new app from scratch, simply delete the contents of the <strong>ClientApp</strong> folder and run <strong>ng new.</strong>&#160;</p><p>So you get the benefits of easy client-server integration without having to compromise any Angular client-side features or Angular CLI tooling.<br></p>


