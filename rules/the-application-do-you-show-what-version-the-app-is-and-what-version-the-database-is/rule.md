---
type: rule
title: Do you show what version the App is, and what version the Database is?
uri: do-you-show-current-versions-app-and-database
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Jack Pettit
    url: https://www.ssw.com.au/people/jack-pettit
related: []
redirects: []
created: 2009-10-05T05:26:57.000Z
archivedreason: null
guid: f72682d0-f992-4021-ba50-16f394d0d2ec
---
It is best practice to always include an applications version somewhere within  the app, but do you also include the database version, its just as important! 

**(Check with Matt W - Should we change this image to Rules version)**
![Figure: Everyone shows the version number somewhere on their app](LinkAuditor.png)  

Let's see how to show the Database version:
 
<!--endintro-->

## Modern Applications 

**(Check with Matt W)**

These days we have frameworks such as EF to handle this for us, with its migrations and its ability to track changes. For more auditing purposes, check out [EF Core 6's auditing library](https://entityframework.net/ef-auditing). 

## Legacy Applications:
For legacy applications that aren't using Frameworks such as EF, keeping track of a databases version can be done in the following way. 

Create a new table that will store the version info, this table is called **_zsDataVersion**.
![Figure: SSW Link Auditor _zsDataVersion table](zsVersionTable.png)  

For SSW Link Auditor this can be seen in the table status section, with the apps current version being 62. 
![Figure: SSW Link Auditor Database version](LinkAuditorVersion.png)  
