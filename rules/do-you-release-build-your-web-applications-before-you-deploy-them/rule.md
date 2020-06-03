---
type: rule
title: Do you release build your web applications before you deploy them?
uri: do-you-release-build-your-web-applications-before-you-deploy-them
created: 2016-11-16T18:34:36.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'>  Additionally to the reasons found on rule&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=2e8cdcb8-70e6-4fbe-b255-4d81b8b74125">Do you always deploy Release builds to production</a>, there are more reasons doing this with ASP.NET<br><ol><ul><li>ASP.NET conducts a batch compilation on &quot;release builds&quot;, which means it tries to compile all files in the current folder into one DLL</li><li>No resource caching is performed on debug build assemblies, which means that each request/response for a resource is not cached</li></ul></ol>According to&#160;<a href="https&#58;//blogs.msdn.microsoft.com/" target="_blank">MSDN web developer tips</a>, you can choose one of the following to release build your web application<br><ol><ul><li>In web.config file, set &lt;compilation debug=&quot;false&quot;/&gt;</li><li>Disable the &lt;compilation debug=&quot;true&quot;/&gt; switch for all ASP.NET applications on the server by setting the following in Machine.config​<br></li></ul></ol> </span>

<p class="ssw15-rteElement-CodeArea">​&lt;system.web&gt; &lt;deployment retail=&quot;true&quot;/&gt; &lt;/system.web&gt; <br></p><dd class="ssw15-rteElement-FigureGood">
​​​The setting in machine.config will also turn off trace output in a page and detailed error messages remotely<br></dd><div>​Machine.config file is typically located at %SystemRoot%\Microsoft.NET\Framework\%VersionNumber%\CONFIG.​​<br></div>


