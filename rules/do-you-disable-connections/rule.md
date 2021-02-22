---
type: rule
archivedreason: 
title: Do you disable connections?
guid: 320b6c73-b779-4bae-80f9-eb84235aeb1b
uri: do-you-disable-connections
created: 2009-11-03T21:28:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---

Once you are ready to start you need to make sure that no one can access the existing TFS 2008 server while you do the migration.

1. You are ready to start
2. Send out an email notifying all users that TFS2008 will be turned off. 
Follow [Rules to better Networks](http://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterNetworks.aspx#rebootrestart)
3. Make sure no-one can check in files by either:
    1. Running [TFSQuiesce](http://support.microsoft.com/kb/950893) (recommended) 
or
    2. Turning off TFS Service
        1. Remote desktop into TFS 2008
        2. Start IIS
        3. Right click Team Foundation Server | Stop

![](StopTFSServices.png)
Figure: You need to stop anyone checking in files
4. Confirm you can no longer get latest on the Northwind team project


<!--endintro-->
