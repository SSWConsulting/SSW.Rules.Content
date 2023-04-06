---
type: rule
archivedreason: 
title: Do you use more meaningful names than Hungarian short form?
guid: 2d7b5600-f65a-4172-9656-b5a3c8a402b0
uri: do-you-use-more-meaningful-names-than-hungarian-short-form
created: 2009-05-05T07:29:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

Hungarian notation is used in VB6. In .NET, there are over 35,000 classes, so we can't just call them with three letter short form. We would suggest the developer use the full class name as  in example below. As a result, the code will be much easier to read and follow up.   
<!--endintro-->


```
//Bad Code


                          DateTime dt = new DateTime.Now();


                          DataSet ds = new DataSet();


                          // It could be confused with Date time.


                          DataTable dt = ds.Tables[0];
```

          Bad code - Without meaningful name.             

```
//Good Code


                     DateTime currentDateTime = new DateTime.Now();


                     DataSet employmentDataSet = new DataSet();


                     DataTable ContactDetailsDataTable = ds.Tables[0];
```

          Good code - With meaningful name.   
[More information on naming convention](http&#58;//www.ssw.com.au/ssw/Standards/DeveloperDotNet/DotNetStandard_ObjectNaming.aspx).




| We have a program called [SSW Code Auditor](http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule |
| --- |
