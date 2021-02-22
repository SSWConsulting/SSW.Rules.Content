---
type: rule
archivedreason: 
title: Do you keep SharePoint databases in a separate SQL instance?
guid: 8b120644-476c-4b48-9bd0-acf1e37ff4aa
uri: keep-sharepoint-databases-in-a-separate-sql-instance
created: 2018-06-25T23:34:07.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-keep-sharepoint-databases-in-a-separate-sql-instance

---

Because SharePoint server will create quite a few databases, it’s easier to manage them in a separate SQL instance rather than mixing it with other system’s databases:

<!--endintro-->


::: bad  
![Bad example - mixed with other systems' database](sharepoint-database-bad.png)  
:::


::: good  
![Good example - SharePoint related databases are in a separate SQL instance from other systems' databases](sharepoint-database-good.png)  
:::
