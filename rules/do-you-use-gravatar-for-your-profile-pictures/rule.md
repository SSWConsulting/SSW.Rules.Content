---
type: rule
archivedreason: 
title: Do you use Gravatar for your profile pictures?
guid: b790dbfc-fe37-4a4a-992e-c9294620a06b
uri: do-you-use-gravatar-for-your-profile-pictures
created: 2015-03-16T10:17:40.0000000Z
authors: []
related: []

---


<p>​To keep profile management simple and make it easier for users to have a consistent experience across applications, you should use <a href="https&#58;//en.gravatar.com/">Gravatar</a> for showing profile images in your application. </p><p><em>Your Gravatar is an image that follows you from site to site appearing beside your name when you do things like comment or post on a blog.</em></p><p>It is simple to set up and if you are developing an MVC application, there are even several Nuget packages to make your life easier. The <a href="https&#58;//www.nuget.org/packages/GravatarHelper/">GravatarHelper</a> is recommended.</p><p class="ssw15-rteElement-P">Usage&#58;&#160;<br></p><p class="ssw15-rteElement-CodeArea">@Html.GravatarImage(&quot;MyEmailAddress@example.com&quot;, 80, new &#123; Title = &quot;My Gravatar&quot;, Alt = &quot;Gravatar&quot; &#125;)</p><p>Also, check out the <a href="https&#58;//en.gravatar.com/site/implement/images/">Gravatar API documentation</a> for all the options available. </p><p>The below short video shows how to get up and running with Gravatar in your ASP.NET MVC&#160;application.&#160;</p><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"><iframe width="560" height="315" src="https&#58;//www.youtube.com/embed/rjFjVD9jPIk" frameborder="0"></iframe>&#160;</div><p><br></p>
<br><excerpt class='endintro'></excerpt><br>



