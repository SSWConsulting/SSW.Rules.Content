---
seoDescription: Customize your SQL Reporting Services and Visual Studio experience by knowing which version you are using to ensure compatibility with CRM 2011.
type: rule
archivedreason:
title: Customization - Do you know which version of SQL Reporting Services and Visual Studio you are using?
guid: 4c8562e5-4f70-4ee3-a38b-b283f5ba8d63
uri: customization-do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
created: 2012-12-10T18:37:44.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects: []
---

CRM 2011 is designed to work with:

- SQL Server 2012 (CRM Update Rollup 6 or greater required), SQL Server 2008 (or 2008 R2)
- SQL Reporting Services 2012, SQL Reporting Services 2008 (or 2008 R2)
- .NET Framework 4.0 for Plugins, .NET Framework 4.0 or 3.5 for Visualizations (Charts)

Make sure you are using the correct version of Visual Studio to edit reports, either Visual Studio 2008 or Visual Studio 2010 or **even better use Visual Studio 2012 and SSDT-BI to edit Report files** .

The benefit of using SSDT-BI is you will be able to target SQL Reporting Services 2008-2012 without having different versions of Visual Studio installed.

SSDT-BI can be downloaded from: [http://www.microsoft.com/en-au/download/details.aspx?id=36843](http://www.microsoft.com/en-au/download/details.aspx?id=36843&WT.mc_id=DT-MVP-33518)

<!--endintro-->

History

CRM 3.0 is in .NET 1.1 so it was designed to work with:

- SQL Server 2000 (even better to use 2005)
- Reporting Services 2000 (design reports in VS.NET 2003)
- Callouts in VS.NET 2003

**Tip #1:**  Do try to use SQL 2005 if available - it is marginally faster.

**Tip #2:**  Don't try working in VS.NET 2005 - there are workarounds but they become very, very painful.

**Tip #3:**  SQL Reporting Services and the .rdl files are not backward compatible - there is no hope of doing them in 2005 and back porting the RDL.
