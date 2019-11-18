---
type: rule
title: ​DBAs - Do you run SQL Server Services under non-Administrator accounts?
uri: dbas---do-you-run-sql-server-services-under-non-administrator-accounts
created: 2019-11-18T23:40:32.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">​​​​​​​​You should always run all SQL Server services with the lowest possible privileges allowed in case the account is compromised. In SQL 2000 this was a bit of a pain as you would have to manually create a minimal account with the bare minimum required privileges. SQL Server 2005 setup makes the whole process of granting privileges a whole lot easer than in SQL 2000 - because it automatically creates groups with all the necessary ​permissions for you!​<br></p> </span>

<dl class="image"><dt><img src="/PublishingImages/SQLDatabases_RunAsAccount_GroupsCreated.png" alt="SQLDatabases_RunAsAccount_GroupsCreated.png" style="width&#58;750px;" /></dt><dd>Figure &#58;&#160;SQL 2005 now creates groups for all the SQL Server services with the bare minimum permissions for you</dd></dl>
<p>For good old SQL 2000, you must manually give the SQL Server Service accounts the following permissions&#58;</p><ul><li>Ability to log on as a service</li><li>Ability to access and change the MSSQL directory</li><li>Ability to access and change applicable .mdf, .ndf, and .ldf files</li><li>Ability to read and write to certain registry keys under&#58;</li></ul><p>
   <br>HKEY_LOCAL_MACHINE\Software\Microsoft\MSSQLServer.<br>-or- for any named instance&#58; HKEY_LOCAL_MACHINE\Software\Microsoft\Microsoft SQL Server.<br>HKEY_LOCAL_MACHINE\System\CurrentControlset\Services\MSSQLServer.<br>-or- for any named instance&#58; HKEY_LOCAL_MACHINE\System\CurrentControlset\Services\MSSQL$Instancename.<br>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Perflib.<br><br>If you are running any SQL Server Service in an user account that has administrator privileges a user that compromises the account could do anything that administrator could do - including playing around with the registry with procedures like xp_regdeletevalue. So, if you use an Administrator account, you're in effect giving away the keys to the house. Is this something you want to do?<br><br></p>


