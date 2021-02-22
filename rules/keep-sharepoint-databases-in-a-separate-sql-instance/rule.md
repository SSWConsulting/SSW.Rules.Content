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


<p>Because SharePoint server will create quite a few databases, it’s easier to manage them in a separate SQL instance rather than mixing it with other system’s databases:<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>​​​<img src="sharepoint-database-bad.png" alt="sharepoint-database-bad.png" /></dt><dd>Bad example - mixed with other systems' database</dd></dl><dl class="goodImage"><dt>​​​<img src="sharepoint-database-good.png" alt="sharepoint-database-good.png" /></dt><dd>Good example - SharePoint related databases are in a separate SQL instance from other systems' databases​<br></dd></dl>


