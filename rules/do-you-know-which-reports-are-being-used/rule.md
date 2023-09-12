---
type: rule
archivedreason: 
title: Do you know which reports are being used?
guid: 878ab3bb-d5d1-41ec-9ed6-800077f03576
uri: do-you-know-which-reports-are-being-used
created: 2016-09-12T00:56:03.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---

SSRS keeps track of each report that gets executed and records useful information like:


* How long did the report take to generate
* Who requested the report
* When was the report generated
* Report Parameters used


So it's quite simply a matter of querying the ReportServer database for information in the ExecutionLog table. 



<!--endintro-->



```sql
WITH RankedReports
AS
(SELECT ReportID,
        TimeStart,
        UserName, 
        RANK() OVER (PARTITION BY ReportID ORDER BY TimeStart DESC) AS iRank
   FROM dbo.ExecutionLog t1
        JOIN 
        dbo.Catalog t2
          ON t1.ReportID = t2.ItemID
)
SELECT t2.Name AS ReportName,
       MAX(t1.TimeStart) LastAccessed,
       --t1.UserName,
       t2.Path,	  
       SUBSTRING(t2.Path, 0, CHARINDEX('/', t2.Path, 2)) ParentFolder,
       t1.ReportID
  FROM RankedReports t1
       JOIN 
       dbo.Catalog t2
         ON t1.ReportID = t2.ItemID
 WHERE t1.iRank = 1
GROUP BY t2.Name, Path, ReportID
ORDER BY MAX(t1.TimeStart) DESC;
```



The query above gives you the last reports that were accessed (Credit to [Eric Phan - SSRS - Find out which reports are being used (handy for migrating only the useful reports to a new server)](http&#58;//ericphan.net/blog/2016/9/12/ssrs-find-out-which-reports-area-being-used-handy-for-migrating-only-the-useful-reports-to-a-new-server))
