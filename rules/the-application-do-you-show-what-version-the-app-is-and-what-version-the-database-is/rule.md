---
type: rule
archivedreason: 
title: The application - Do you show what version the App is, and what version the Database is?
guid: f72682d0-f992-4021-ba50-16f394d0d2ec
uri: the-application-do-you-show-what-version-the-app-is-and-what-version-the-database-is
created: 2009-10-05T05:26:57.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---



  <dl class="image">
    <dt><img width="625" height="522" alt="" style="width:576px;height:475px;" src="LinkAuditor.png" /> </dt>
    <dd>Figure: Everyone shows the version number somewhere on their app </dd>
</dl>
...but databases also need a version number.<br>
<br>
Let's see how to show the Database version:  

<br><excerpt class='endintro'></excerpt><br>

  <dl class="image">
    <dt><img alt="" src="zsVersionTable.png" /> </dt>
    <dd>Figure: The applications database should have a table storing the version info (the table is called _zsDataVersion). See an example of this in <a href="http://www.ssw.com.au/SSW/LinkAuditor/">SSW Link Auditor</a> </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="LinkAuditorVersion.png" /> </dt>
    <dd>Figure: The user can clearly see the Database version is 62 after clicking "Configure..." button in wizard "Storage Mechanism". See an example of this in <a href="http://www.ssw.com.au/SSW/LinkAuditor/">SSW Link Auditor</a> </dd>
</dl>
<dl class="image">
    <dt><img alt="" src="ChangeScripts.jpg" /> </dt>
    <dd>Figure: The Application keeps all the scripts in a folder called SQLScripts (this allows the application to upgrade itself and give the Reconciliation functionality) </dd>
</dl>



