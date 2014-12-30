---
type: rule
archivedreason: 
title: Do You Know Which Packages To Add To Your New MVC Project?
guid: ff1fcbc9-abe1-44f8-bfda-1d8720cb3799
uri: do-you-know-which-packages-to-add-to-your-new-mvc-project
created: 2014-12-30T00:24:02.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---


​​When you create a new MVC project in Visual Studio it is important to include the right NuGet packages from the start. This makes the project more manageable and you become more efficient in producing your final result.
<br><excerpt class='endintro'></excerpt><br>
<p>​If you add old, obsolete or incorrect NuGet packages, the project will suffer and you might have decreased performance or scope creep as new requirements are discovered.&#160;</p><p>Avoid old technologies such as&#58;</p><span style="line-height&#58;1.6;background-color&#58;initial;"><ul><li><span style="line-height&#58;1.6;background-color&#58;initial;">​​</span><span style="line-height&#58;1.6;background-color&#58;initial;">MVC Web Forms</span><br></li><li><span style="line-height&#58;1.6;">Knockout</span><span style="line-height&#58;1.6;">JS</span><br></li></ul></span>​<span style="line-height&#58;1.6;">When you create a project you should be adding the following NuGet Packages&#58;</span><ul><li>AngularJS</li><li>SSW.DataOnion</li><li>SSW.HealthCheck</li><li>And for generic stuff <a href="https&#58;//github.com/ssw-au/SSW.Framework.Web.Mvc">https&#58;//github.com/ssw-au/SSW.Framework.Web.Mvc</a> ​​</li></ul>


