---
type: rule
archivedreason: 
title: Do you know what to do about ASP.NET Core default dependency injection?
guid: a841c2c6-15bb-4f13-83a7-f8c201b0e937
uri: do-you-know-what-to-do-about-aspnet-core-default-dependency-injection
created: 2016-02-05T00:28:15.0000000Z
authors:
- id: 40
  title: Igor Goldobin
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen
related: []

---

We already know what the [best IOC container is](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0aa194e1-2de9-4ed1-b430-444109d65a50), but how does ASP.NET core's default dependency injection compare?

ASP.NET Core includes default dependency injection for new Web Apps in the Startup.cs file. This is adequate for simple projects, but not designed to compete with the features of alternatives containers (like AutoFac's convention based registration).

"The default services container provided by ASP.NET Core provides a minimal feature set and is not intended to replace other containers."

- Steve Smith, ([ASP.NET Dependency Injection](http://docs.asp.net/en/latest/fundamentals/dependency-injection.html))

<!--endintro-->

You can quickly flag this error and any more by using the [SSW Code Auditor](https://www.ssw.com.au/ssw/CodeAuditor/).

Here is an example of rewiring the default code to AutoFac with the [SSW's Music Store](https://github.com/SSWConsulting/enterprise-musicstore-ui-angular2)  app:
<dl class="ssw15-rteElement-ImageArea" style="background-color:#ffffff;"><img src="SSW-DependencyInjection-Example-Default-Bad.png" alt="SSW-DependencyInjection-Example-Default-Bad.png" style="margin:5px;"><br><br>::: bad<br>Figure: Bad Example - The default dependency injection for ASP.NET Core<br><br>:::<br><br></dl><dl class="ssw15-rteElement-ImageArea" style="background-color:#ffffff;"><img src="SSW-DependencyInjection-Example-Default-Good.png" alt="SSW-DependencyInjection-Example-Default-Good.png" style="margin:5px;width:614px;height:499px;"></dl>

::: good
Figure: Good Example - The bad example rewired to utilize AutoFac. Red boxes outline the modified code


:::


### Further Reading:

* [Do you use a dependency injection centric architecture?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0a5029a1-dd4f-46d7-9f22-8ab328e7c102)
* [Do you generate the VS dependency graph?](/Pages/DoYouGenerateTheVSDependencyGraph.aspx)
* [Do you know the best dependency injection container? (aka Do not waste days evaluating IOC containers)](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0aa194e1-2de9-4ed1-b430-444109d65a50)
