---
type: rule
archivedreason: 
title: Do you turn on file auditing for your file server?
guid: f274fa44-ce17-4bde-981d-ef3329d3c8af
uri: turn-on-file-auditing-for-your-file-server
created: 2020-08-24T21:11:16.0000000Z
authors:
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
- do-you-turn-on-file-auditing-for-your-file-server

---


​Windows Server has a built-in solution for auditing who accessed your files in a file share or non-shared files in your file system, but it is turned off by default.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>&quot;Advanced Audit Policy Configuration&quot; is a Group Policy setting in Windows that enables several audit options for your files, e.g.&#58;<br> </p><ol><li>Object Access - Audit who opened, closed or modified files and folders in your system</li><li>Logon/Logoff - Audit who's logged on and off the server<br>​<br></li></ol>To get to this setting, you need to&#58;<br> 
<ol><li>Open your domain's or server's Group Policy (or Local Group Policy)</li><li>Computer Configuration | Windows Settings | Security Settings | Advanced Audit Policy Configuration</li><li>Choose the setting that applies to you e.g. Object Access</li><li>Edit the subcategory | Check &quot;Success&quot; and &quot;Failure&quot; as best practices<br></li></ol><dl class="goodImage"><dt> 
      <img src="/PublishingImages/auditing-success-and-fail.png" alt="auditing-success-and-fail.png" style="width&#58;750px;" /> 
   </dt><dd>Figure&#58; Good Example - Auditing Successes and Failures in your file shares</dd></dl><p>After that, your server will start logging audit events in the Event Viewer. To filter relevant events, do the following&#58;</p>​ 
<ol><li>Open Window's Event Viewer | Windows Logs | Security</li><li>Click &quot;Filter Current Log...&quot; | IDs 4663, 4660, 5145&#58; 
      <ol><li>4663 (An attempt was made to access an object) - Event ID when a user accesses a file system file</li><li>4660 (An object was deleted) - Event ID when a user deletes a file system file</li><li>5145 (A network share object was checked to see whether the client can be granted desired access.) - Event ID when a network user accesses a file share file</li></ol></li><li>The relevant logs will start popping up&#58;<br>
      <dl class="goodImage"><dt> 
            <img src="/PublishingImages/filtered-logs.png" alt="filtered-logs.png" /> 
         </dt><dd>Figure&#58; Good example - Filtered logs with file access information<br></dd></dl></li><li>Click on each entry for a detailed explanation on which file was opened, which IP address was used and which user initiated the action</li></ol>​
<p>This kind of audit tool is an important part of any SysAdmin or Security Engineer to better see what is going on in your Windows environment.</p>


