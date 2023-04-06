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

![Figure: Everyone shows the version number somewhere on their app](LinkAuditor.png)  

Let's see how to show the Database version:
 
<!--endintro-->

### Modern Applications

These days frameworks handle database versioning for us, using code first migrations we can tell the application to automatically update the database when it starts up so its always at the latest version.

### Legacy Applications

For legacy applications that aren't using Frameworks such as EF, keeping track of a databases version can be done in the following way. 

Create a new table that will store the version info, this table is often called **\_zsDataVersion**.
![Figure: Example - SSW Link Auditor _zsDataVersion table](zsVersionTable.png)  

For SSW Link Auditor this can be seen in the table status section.
![Figure: Example - SSW Link Auditor Database version is 62](LinkAuditorVersion.png)  

![Figure: The Application keeps all the scripts in a folder called SQLScripts (this allows the application to upgrade itself and give the Reconciliation functionality)](ChangeScripts.jpg)
