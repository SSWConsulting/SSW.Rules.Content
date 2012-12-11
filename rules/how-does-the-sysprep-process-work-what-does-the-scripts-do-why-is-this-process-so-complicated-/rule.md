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


<ol><span><li>SharePoint server can't be renamed after SharePoint is installed 
</li>
<li>Multiple VM's with the same name can't be powered up in the same network 
</li>
<li>So the master.vhd contains&#58; 
<ol><li>Windows 2003 server SP2 
</li>
<li>Visual Studio .NET 2005 
</li>
<li>Microsoft Office SharePoint Designer </li></ol>
</li>
<li>When sysprep is ran on the master.vhd, it generalises Windows 
2003 server (generate new machine guide, rename computer, etc), the 
scripts that run also puts &quot;administrator&quot; into the registry so that'd 
be the name of the next login prompt. A vhd that is in this state is the
 &quot;sysprep'ed&quot; vhd 
</li>
<li>When it restarts and the user logs in with administrator, it then runs the script to install 
<ol><li>SQL Server 2005 
</li>
<li>Puts MossFarm account into registry </li></ol>
</li>
<li>After restart - login with MossFarm account and run the scripts to install 
<ol><li>SharePoint 2007 sp1 </li></ol>
</li>
<li>Runs Moss\Post_Build.cmd<span style="display&#58;inline-block;"></span></li></span></ol>
<br><excerpt class='endintro'></excerpt><br>



