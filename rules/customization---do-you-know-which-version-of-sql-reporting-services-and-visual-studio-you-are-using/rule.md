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



<span class='intro'> 
          <p>
            CRM 3.0 is in .NET 1.1 so it was designed to work with&#58;</p>
<ul>
          <li>SQL Server 2000 (even better to use 2005)</li>
          <li>Reporting Services 2000 (design reports in VS.NET 2003)</li>
          <li>Callouts in VS.NET 2003</li>
        </ul> </span>

<p><strong>Tip #1&#58;</strong> Do try to use SQL 2005 if available - it is marginally faster.</p>
<p>
          <strong>Tip #2&#58;</strong> Don't try working in VS.NET 2005 - there are workarounds but they become
          very, very painful.</p>
<p>
          <strong>Tip #3&#58;</strong> SQL Reporting Services and the .rdl files are not backward compatible -
          there is no hope of doing them in 2005 and back porting the RDL.
        </p>


