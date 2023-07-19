---
type: rule
title: Do you use more meaningful names than Hungarian short form?
uri: do-you-use-more-meaningful-names-than-hungarian-short-form
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects: []
created: 2009-05-05T07:29:18.000Z
archivedreason: null
guid: 2d7b5600-f65a-4172-9656-b5a3c8a402b0
---

Hungarian notation is used in VB6. In .NET, there are over 35,000 classes, so we can't just call them with three letter short form. We would suggest the developer use the full class name as  in example below. As a result, the code will be much easier to read and follow up.   
<!--endintro-->

```vbnet
DateTime dt = new DateTime.Now();
DataSet ds = new DataSet();

// It could be confused with Date time.
DataTable dt = ds.Tables[0];
```
:::bad
Bad code - Without meaningful name
:::


```vbnet
DateTime currentDateTime = new DateTime.Now();
DataSet employmentDataSet = new DataSet();

DataTable ContactDetailsDataTable = ds.Tables[0];
```
::: good
Good code - Meaningful name
:::

More information on [.NET Object Naming Standard](https://www.ssw.com.au/ssw/Standards/DeveloperDotNet/DotNetStandard_ObjectNaming.aspx).
