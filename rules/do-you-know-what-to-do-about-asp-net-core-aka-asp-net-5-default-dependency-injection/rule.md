---
type: rule
archivedreason: 
title: Do you know what to do about ASP.NET Core default dependency injection?
guid: a841c2c6-15bb-4f13-83a7-f8c201b0e937
uri: do-you-know-what-to-do-about-asp-net-core-aka-asp-net-5-default-dependency-injection
created: 2016-02-05T00:28:15.0000000Z
authors:
- title: Igor Goldobin
  url: https://ssw.com.au/people/igor-goldobin
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
- do-you-know-what-to-do-about-asp-net-core-(aka-asp-net-5)-default-dependency-injection
- do-you-know-what-to-do-about-asp-net-core-default-dependency-injection

---


<p>​​We already know what the <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0aa194e1-2de9-4ed1-b430-444109d65a50">best IOC containe​r is</a>, but how does ASP.NET core's default dependency injection compare​?</p><p>ASP.NET Core includes default dependency injection for new Web Apps in the Startup.cs file. This is adequate for simple projects, but not designed to compete with the features of alternatives containers (like AutoFac's convention based registration).</p><p class="ssw15-rteElement-Reference">"The default services container provided by ASP.NET Core provides a minimal feature set and is not intended to replace other containers.​​"</p><p class="ssw15-rteElement-P">- Steve Smith, (<a href="http://docs.asp.net/en/latest/fundamentals/dependency-injection.html">ASP.NET Dependency Injection</a>)<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-YellowBorderBox">You can quickly flag this error and any more by using the <a href="https://www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor​</a>.<br></p><p>Here is an example of rewiring the default code to AutoFac with the <a href="https://github.com/SSWConsulting/enterprise-musicstore-ui-angular2">SSW's Music Store​</a>  app:</p><dl class="ssw15-rteElement-ImageArea" style="background-color:#ffffff;"><img src="SSW-DependencyInjection-Example-Default-Bad.png" alt="SSW-DependencyInjection-Example-Default-Bad.png" style="margin:5px;" /><dd class="ssw15-rteElement-FigureBad">Figure: Bad Example - ​​The default dependency injection for ASP.NET Core<br></dd></dl><dl class="ssw15-rteElement-ImageArea" style="background-color:#ffffff;">​​<img src="SSW-DependencyInjection-Example-Default-Good.png" alt="SSW-DependencyInjection-Example-Default-Good.png" style="margin:5px;width:614px;height:499px;" /></dl><dd class="ssw15-rteElement-FigureGood">​​Figure: Good Example - The bad example rewired to utilize​ AutoFac. Red boxes outline the modified code<br><br></dd><h3 class="ssw15-rteElement-H3">Further Reading:​</h3><ul><li><a href=/do-you-use-a-dependency-injection-centric-architecture>Do you use a dependency injection centric architecture?</a></li><li><a href="/Pages/DoYouGenerateTheVSDependencyGraph.aspx">​Do you generate the VS dependency graph?</a>​ ​​</li><li><p class="ssw15-rteElement-P"><a href=/do-you-know-the-best-dependency-injection-container-aka-do-not-waste-days-evaluating-ioc-containers>Do you know the best dependency injection container? (aka Do not waste days evaluating IOC containers)​​</a><br></p></li></ul>


