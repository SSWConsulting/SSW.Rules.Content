---
type: rule
archivedreason: 
title: How does the sysprep process work, what does the scripts do? Why is this process so complicated ?
guid: cbd6b55b-c6dd-4789-be1f-cc48e197a78b
uri: how-does-the-sysprep-process-work-what-does-the-scripts-do-why-is-this-process-so-complicated-
created: 2009-02-26T02:03:41.0000000Z
authors: []
related: []

---

* SharePoint server can't be renamed after SharePoint is installed
* Multiple VM's with the same name can't be powered up in the same network
* So the master.vhd contains:
    1. Windows 2003 server SP2
    2. Visual Studio .NET 2005
    3. Microsoft Office SharePoint Designer
* When sysprep is ran on the master.vhd, it generalises Windows <br>2003 server (generate new machine guide, rename computer, etc), the <br>scripts that run also puts "administrator" into the registry so that'd <br>be the name of the next login prompt. A vhd that is in this state is the<br> "sysprep'ed" vhd
* When it restarts and the user logs in with administrator, it then runs the script to install
    1. SQL Server 2005
    2. Puts MossFarm account into registry
* After restart - login with MossFarm account and run the scripts to install
    1. SharePoint 2007 sp1
* Runs Moss\Post\_Build.cmd


<!--endintro-->
