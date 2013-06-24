---
type: rule
title: Customization - Do you know which version of SQL Reporting Services and Visual Studio you are using?
uri: customization---do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
created: 2012-12-10T18:37:44.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 32
  title: Mehmet Ozdemir

---



<span class='intro'> <p> History</p><p style="text-decoration&#58;line-through;">CRM 3.0 is in .NET 1.1 so it was designed to work with&#58;<span style="color&#58;#000000;"></span></p><ul style="text-decoration&#58;line-through;"><li>SQL Server 2000 (even better to use 2005)</li><li>Reporting Services 2000 (design reports in VS.NET 2003)</li><li>Callouts in VS.NET 2003</li></ul><p style="text-decoration&#58;line-through;">
   <strong>Tip #1&#58;</strong> Do try to use SQL 2005 if available - it is marginally faster.</p><p style="text-decoration&#58;line-through;">
   <strong>Tip #2&#58;</strong> Don't try working in VS.NET 2005 - there are workarounds but they become          very, very painful.</p><p style="text-decoration&#58;line-through;">
   <strong>Tip #3&#58;</strong> SQL Reporting Services and the .rdl files are not backward compatible -          there is no hope of doing them in 2005 and back porting the RDL. </p><p>CRM 2011 is designed to work with&#58;</p><ul><li>SQL Server 2012 (CRM Update Rollup 6 or greater required), SQL Server 2008 (or 2008 R2)</li><li>SQL Reporting Services 2012, SQL Reporting Services 2008 (or 2008 R2)</li><li>.NET Framework 4.0 for Plugins, .NET Framework 4.0 or 3.5 for Visualizations (Charts)</li></ul><p>Make sure you are using the correct version of Visual Studio to edit reports, either Visual Studio 2008 or Visual Studio 2010 or 
   <strong>even better use Visual Studio 2012 and SSDT-BI to edit Report files</strong>.</p><p>The benefit of using SSDT-BI is you will be able to target SQL Reporting Services 2008-2012 without having different versions of Visual Studio installed.</p><p>SSDT-BI can be downloaded from&#58; 
   <a href="http&#58;//www.microsoft.com/en-au/download/details.aspx?id=36843">http&#58;//www.microsoft.com/en-au/download/details.aspx?id=36843</a></p> </span>

<p>&#160;&#160;&#160;&#160;&#160;&#160;&#160; </p>


