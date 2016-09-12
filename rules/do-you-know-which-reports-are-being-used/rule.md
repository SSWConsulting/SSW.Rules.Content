---
type: rule
title: Do you know which reports are being used?
uri: do-you-know-which-reports-are-being-used
created: 2016-09-12T00:56:03.0000000Z
authors:
- id: 3
  title: Eric Phan

---



<span class='intro'> SSRS keeps track of each report that gets executed and records useful information like&#58;<br><div><ul><li><span style="line-height&#58;19.5px;">How long did the report take to generate<br></span></li><li><span style="line-height&#58;19.5px;">Who requested the report</span></li><li><span style="line-height&#58;19.5px;">When was the report generated</span></li><li><span style="line-height&#58;19.5px;">Report Parameters used</span></li></ul><div>So it's quite simply a matter of querying the ReportServer database for information in the ExecutionLog table.&#160;<br></div></div> </span>

<p class="ssw15-rteElement-CodeArea">​WITH RankedReports<br>AS<br>(SELECT ReportID,<br>&#160; &#160; &#160; &#160; TimeStart,<br>&#160; &#160; &#160; &#160; UserName,&#160;<br>&#160; &#160; &#160; &#160; RANK() OVER (PARTITION BY ReportID ORDER BY TimeStart DESC) AS iRank<br>&#160; &#160;FROM dbo.ExecutionLog t1<br>&#160; &#160; &#160; &#160; JOIN&#160;<br>&#160; &#160; &#160; &#160; dbo.Catalog t2<br>&#160; &#160; &#160; &#160; &#160; ON t1.ReportID = t2.ItemID<br>)<br>SELECT t2.Name AS ReportName,<br>&#160; &#160; &#160; &#160;MAX(t1.TimeStart) LastAccessed,<br>&#160; &#160; &#160; &#160;--t1.UserName,<br>&#160; &#160; &#160; &#160;t2.Path, &#160;&#160;<br>&#160; &#160; &#160; &#160;SUBSTRING(t2.Path, 0, CHARINDEX('/', t2.Path, 2)) ParentFolder,<br>&#160; &#160; &#160; &#160;t1.ReportID<br>&#160; FROM RankedReports t1<br>&#160; &#160; &#160; &#160;JOIN&#160;<br>&#160; &#160; &#160; &#160;dbo.Catalog t2<br>&#160; &#160; &#160; &#160; &#160;ON t1.ReportID = t2.ItemID<br>&#160;WHERE t1.iRank = 1<br>GROUP BY t2.Name, Path, ReportID<br>ORDER BY MAX(t1.TimeStart) DESC;<br></p><p class="ssw15-rteElement-P">​​​The query above gives you the last reports that were accessed (Credit to <a href="http&#58;//ericphan.net/blog/2016/9/12/ssrs-find-out-which-reports-area-being-used-handy-for-migrating-only-the-useful-reports-to-a-new-server">Eric Phan - SSRS - Find out which reports are being used (handy for migrating only the useful reports to a new server)​</a>)<br></p>


