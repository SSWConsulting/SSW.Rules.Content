---
type: rule
archivedreason: 
title: Do you know how to generate maintenance pages?
guid: f7a5e85c-adea-4045-8343-e9826e7cb52b
uri: how-to-generate-maintenance-pages
created: 2016-11-17T15:40:38.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-how-to-generate-maintenance-pages

---

In every application you focus on is the important business problems e.g. Invoices with multiple deliveries. Plus you have lots of lookup tables e.g. CustomerCategory. It is smart to work on the important business problems and have the lookup tables done automatically using a code generator.

The code generators to generate maintenance pages automatically, come from MS and from 3rd parties. The current choices are:

<!--endintro-->

1. We recommend [NetTiers (a template for Code Smith) in our 'The Best 3rd Party .NET Tools'](https&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/netTools.aspx#NetTiers). It is an open source template and the output code is of good quality. There are many amazing features:
    * Creates a full website project, already pre-configured and ready to begin coding against your data immediately.
    * Creates a full set of administration web controls, that serves as a basic yet fully functional web administration console for database.
    * Creates a full set of typed DataSource controls for your entire API with design time support, they are similar to the ObjectDataSource, only these are full featured and are actually developer friendly.
    * Creates a full webservice API for your domain, perfect for a .net winforms or smart client application and is simple to configure.
2. [AspDB](https&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/netTools.aspx#AspDB) is an alternative choice. You can click via a code generator (Designer) to produce a complete and acceptable Web DB application in several minutes.
3. [BLinQ](https&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/netTools.aspx#BLinQ)<strike>&#160;is a tool to generate websites that use LinQ to show and edit data.
</strike>DEAD - now replaced by ASP.NET Dynamic Data.
4. ASP.NET Dynamic Data provides the Web application scaffolding that enables you to build rich data-driven Web applications. This scaffolding is a mechanism that enhances the functionality of the existing ASP.NET framework by adding the ability to dynamically display pages based on the data model of the underlying database, without having to create pages manually. 

 **WARNING: ASP.NET Dynamic Data is in Beta and not installed on SEAL and SEALUS.**  
ASP.NET Dynamic Data has been released in VS.NET 2008 SP1.
