---
uri: backup---do-you-back-up-scripts
title: Backup - Do you back up scripts?
created: 2019-11-20 18:42:30
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>Scripts are an important component in the operation of any database. This is why you should back up all your scripts and historical schema snapshots - so you can track the scripts that have been run and those that need to be deployed to test and production databases. We typically store these in source control such as VSS or Team Foundation Server as a Visual Studio Database project. You should regularly generate full scripts of all objects changed, keeping the following points in mind&#58;<br></p><ul><li>Don't encrypt your database objects if you can avoid it - otherwise, they can't be scripted.</li></ul><p>​Use&#58;</p><ul><ul><li>​Enterprise Manager Generate Scripts Wizard OR​<br></li><li>​SQL DMO object model to script out the objects OR​<br></li></ul></ul><br> </span>




