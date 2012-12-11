

---
authors:

---




<span class='intro'> <ol><span><li>SharePoint server can't be renamed after SharePoint is installed 
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
<li>Runs Moss\Post_Build.cmd<span style="display&#58;inline-block;"></span></li></span></ol> </span>

<ol>
<li>SharePoint server can't be renamed after SharePoint is installed 
<li>Multiple VM's with the same name can't be powered up in the same network 
<li>So the master.vhd contains&#58; 
<ol>
<li>Windows 2003 server SP2 
<li>Visual Studio .NET 2005 
<li>Microsoft Office SharePoint Designer </li></ol>
<li>When sysprep is ran on the master.vhd, it generalises Windows 2003 server (generate new machine guide, rename computer, etc), the scripts that run also puts &quot;administrator&quot; into the registry so that'd be the name of the next login prompt. A vhd that is in this state is the &quot;sysprep'ed&quot; vhd 
<li>When it restarts and the user logs in with administrator, it then runs the script to install 
<ol>
<li>SQL Server 2005 
<li>Puts MossFarm account into registry </li></ol>
<li>After restart - login with MossFarm account and run the scripts to install 
<ol>
<li>SharePoint 2007 sp1 </li></ol>
<li>Runs Moss\Post_Build.cmd</li></ol>


