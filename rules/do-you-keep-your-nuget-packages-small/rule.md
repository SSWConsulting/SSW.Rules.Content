---
type: rule
title: Do you keep your nuget packages small?
uri: do-you-keep-your-nuget-packages-small
created: 2015-01-31T04:51:09.0000000Z
authors: []

---



<span class='intro'> When creating NuGet packages, it is better to create few small packages instead of creating one monolithic&#160;package that combines several relatively independent features.&#160; </span>

<p>​​When you are making a decision to package your reusable code and publish it to 
   <strong>NuGet</strong> sometimes it is worths splitting your package into few smaller packages. This will improve maintainability and transparency&#160;of your package. It will also make it much easier to consume and contribute to.</p><p>Lets assume you have created a set of libraries that add extra functionality to web applications. Some libraries classes work with both 
   <strong>ASP.NET MVC</strong> and 
   <strong>ASP.NET WebForms</strong> projects, some are specific to ASP.NET MVC and some are related to security. Each library may also have external dependencies on some other NuGet packages. One way to package your libraries would be to create a single YourCompany.WebExtensions package and publish it to NuGet. Sounds like a great idea, but it has number of issues. What if someone only wants to use some MVC specific classes from your package, they would still have to add your whole package, which will add some other external dependencies that you will never use.</p><p>A better approach would be to split your libraries into 3 separate packages&#58;&#160;<span style="line-height&#58;20.7999992370605px;"><strong>YourCompany.WebExtensions</strong></span><strong>.Core</strong>,&#160;<span style="line-height&#58;20.7999992370605px;"><strong>YourCompany.WebExtensions</strong></span><span style="line-height&#58;20.7999992370605px;"><strong>​.MVC </strong>and&#160;<span style="line-height&#58;20.7999992370605px;"><strong>YourCompany.WebExtensions</strong></span><span style="line-height&#58;20.7999992370605px;"><strong>​.Security</strong>.&#160;<span style="line-height&#58;20.7999992370605px;"><strong>YourCompany.WebExtensions</strong></span><span style="line-height&#58;20.7999992370605px;"><strong>.Core</strong></span> will only contain core libraries that can be used in both ASP.NET WebForm and MVC.&#160;<span style="line-height&#58;20.7999992370605px;"><strong>YourCompany.WebExtensions</strong></span><span style="line-height&#58;20.7999992370605px;"><strong>.MVC</strong> package will contain only MVC specific code and will have a dependency on the Core package.&#160;<span style="line-height&#58;20.7999992370605px;"><strong>YourCompany.WebExtensions</strong></span><span style="line-height&#58;20.7999992370605px;"><strong>.Security</strong> will only contain classes that are related to security. This will give consumer a choice as well as better transparency to the features you are trying to offer. It will also have a better maintainabilty, as one team can work on one package while you are working on another one. Patches and enhancements can also be introduced much&#160;easier.</span></span></span></span></p><dl class="badImage"><dt> 
      <img src="/PublishingImages/package2.jpg" alt="package.jpg" style="margin&#58;5px;width&#58;650px;" />
   </dt><dd>Figure&#58; Bad Example - One big library with lots of features, where most of them are obsolete with a release of ASP.NET MVC 5</dd></dl><dl class="goodImage"><dt> 
      <img src="/PublishingImages/package.jpg" alt="package.jpg" style="margin&#58;5px;width&#58;650px;" />
   </dt><dd>Figure&#58; Good Example - Lots of smaller self contained packaged with a single purpose</dd></dl>


