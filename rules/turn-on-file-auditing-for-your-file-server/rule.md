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

Windows Server has a built-in solution for auditing who accessed your files in a file share or non-shared files in your file system, but it is turned off by default.

<!--endintro-->

"Advanced Audit Policy Configuration" is a Group Policy setting in Windows that enables several audit options for your files, e.g.:

1. Object Access - Audit who opened, closed or modified files and folders in your system
2. Logon/Logoff - Audit who's logged on and off the server

To get to this setting, you need to:

1. Open your domain's or server's Group Policy (or Local Group Policy)
2. Computer Configuration | Windows Settings | Security Settings | Advanced Audit Policy Configuration
3. Choose the setting that applies to you e.g. Object Access
4. Edit the subcategory | Check "Success" and "Failure" as best practices



::: good  
![Figure: Good Example - Auditing Successes and Failures in your file shares](auditing-success-and-fail.png)  
:::

After that, your server will start logging audit events in the Event Viewer. To filter relevant events, do the following:

1. Open Window's Event Viewer | Windows Logs | Security
2. Click "Filter Current Log..." | IDs 4663, 4660, 5145:
    1. 4663 (An attempt was made to access an object) - Event ID when a user accesses a file system file
    2. 4660 (An object was deleted) - Event ID when a user deletes a file system file
    3. 5145 (A network share object was checked to see whether the client can be granted desired access.) - Event ID when a network user accesses a file share file
3. The relevant logs will start popping up:


::: good  
![Figure: Good example - Filtered logs with file access information](filtered-logs.png)  
:::

4. Click on each entry for a detailed explanation on which file was opened, which IP address was used and which user initiated the action


This kind of audit tool is an important part of any SysAdmin or Security Engineer to better see what is going on in your Windows environment.
