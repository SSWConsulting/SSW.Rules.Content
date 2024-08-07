---
type: rule
archivedreason:
title: Parameters - Do you have consistent parameter names?
guid: b4ee2b12-6686-4638-8b63-549e5c64b62d
uri: consistent-parameter-names
created: 2024-08-02T10:40:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

All display names referring to the same parameter should be consistent in everywhere of your reports. In addition, the parameter name and value should be in the same line if possible.

<!--endintro-->

::: bad  
![Figure: Bad example - Inconsistent parameter names](ParameterName_Bad.gif)  
:::

::: good  
![Figure: Good example - Consistent parameter names](ParameterName_Good.gif)
:::

::: greybox
**Note: If your data is not live, but based on ETL/SSIS**
Then each time log each import to a table Eg. Once a week. Then on the report parameters show this - so users know how old the data is.
:::
