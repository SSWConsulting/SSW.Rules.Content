---
type: rule
title: Do you keep SharePoint databases in a separate SQL instance?
uri: do-you-keep-sharepoint-databases-in-a-separate-sql-instance
created: 2018-06-25T23:34:07.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 9
  title: William Yin

---



<span class='intro'> <p>Because SharePoint server will create quite a few databases, it’s easier to manage them in a separate SQL instance rather than mixing it with other system’s databases&#58;<br></p> </span>

<dl class="badImage"><dt>​​​<img src="/PublishingImages/sharepoint-database-bad.png" alt="sharepoint-database-bad.png" /></dt><dd>Bad example - mixed with other systems' database</dd></dl><dl class="goodImage"><dt>​​​<img src="/PublishingImages/sharepoint-database-good.png" alt="sharepoint-database-good.png" /></dt><dd>Good example - SharePoint related databases are in a separate SQL instance from other systems' databases​<br></dd></dl>


