---
type: rule
title: Do you use the Distributed File System for your file shares?
uri: do-you-use-the-distributed-file-system-for-your-file-shares
created: 2017-07-10T21:18:15.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> ​Occasionally, one server and its drives will not have sufficient space to store all related files in a network share. For example, you may have a &quot;SetupFiles&quot; directory that stores all Setup executables on your network e.g. \\bee\SetupFiles. There are problems with this approach.<br> </span>

<ol><li>You will run out of space - which means you will have to copy or move old (but still used) setup files around to other drives (\\bee\d$\SetupOld\ ) or other machines e.g. \\tuna\SetupFiles. This fragmentation of your setup files can cause confusion for your users.</li><li>When you retire or rename the old server, links to the old server location will not work</li></ol><p>So how do you get around this problem? The answer is in the&#160;<strong>Distributed File System (DFS)</strong>. Instead of having several server-specific file share locations, you can have a domain-wide setup location that offers a seamless experience to your users. DFS will even track a history of when and where file locations were moved.<br></p><dl class="image"><dt><img src="/PublishingImages/Network_DistributedFileSystem.gif" alt="Network_DistributedFileSystem.gif" /></dt><dd>Figure&#58; The Distributed File System consolidates many separate file shares into one convenient location for your users</dd></dl>​<br>


