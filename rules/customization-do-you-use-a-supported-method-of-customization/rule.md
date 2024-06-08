---
type: rule
archivedreason: 
title: Customization - Do you use a supported method of customization?
guid: 3cd68a40-7efb-4383-8cf2-418c7dde7686
uri: customization-do-you-use-a-supported-method-of-customization
created: 2012-12-10T18:24:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

The Microsoft CRM customization tools make it no longer necessary for you to hack           ie. write triggers, stored procedures and .aspx pages. In fact if you were to do           any of these your CRM is unsupported. Changes will not be preserved in any upgrades           or fixes and Microsoft will not attend to any of your support calls until you revert           your CRM back to a supported state.

<!--endintro-->

The common ways to customize are:

1. Use the designer to add Entities and Forms (aka Tables and Forms)
2. Write SQL Reporting Services Reports
3. Write workflows with the CRM designer
4. Write workflows with VS.NET and .NET 3.0 WF (new since CRM 4.0)
5. Write callouts with VS.NET (the extension points made available)


The diagram below briefly outlines what are possible supported methods of customization.

![Figure: Microsoft CRM Customization Architecture](CRM\_Customization\_Architecture.JPG)  

Refer to P19 of the CRM Customization Manual Course 8525A for a more in depth discussion.

PS: For CRM 3.0 you can't find everything on the web - you will need the CRM Customization Manual Course 8525A - you have to buy it from Microsoft :-(
