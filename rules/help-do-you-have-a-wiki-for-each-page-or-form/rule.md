---
type: rule
archivedreason: 
title: Help - Do you have a wiki for each page or form?
guid: 4c7f4917-33de-4e19-b061-1c697944c71e
uri: help-do-you-have-a-wiki-for-each-page-or-form
created: 2012-11-27T02:10:18.0000000Z
authors: []
related: []
redirects: []

---

In agile development; updates, changes and bug fixes happen all the time and an issue that a user encounters today might already is fixed or have a workaround. That is why each page or form should link to a wiki page with any common problems that a user might encounter (and workarounds for them) and planned changes.

<!--endintro-->

This saves the end user from resorting to crawling the web for solutions.

 **From:** Tech Support
 **Sent:** Wednesday, 27 January 2010 4:31 PM
 **To:** Mr Northwind
 **Subject:** RE: Issue with lab management hosts

Hi Mr Northwind

There was a bug in Beta2 (fixed in upcoming RC release) wherein even if you have no lab artifacts in a host group, it did not allow you to delete host group from a Project collection in Team Foundation Admin Console UI until you delete the host groups explicitly from all the associated team projects. 

1. Run the following commands to project level association (make sure that there are no Lab environments in this Host Group).

 **TFSLabConfig.exe DeleteTeamProjectHostGroup /Collection:&lt;CollectionUrl&gt; /teamProject:\* /name:"Testing Host"**
2. Delete the host groups from Team Foundation Admin Console UI

 **There was a similar issue with the Library shares also, and has been fixed now.**


Regards
Tech Support

* * *

 **From:** Mr Northwind
 **Sent:** 27 January 2010 10:07
 **To:** Tech Support
 **Subject:** Issue with lab management hosts

I accidentally (on scvmm) created a folder called "Testing" under by All Hosts group. In TFSAC I added the AllHosts\Testing host. This led me to other problems so I tried to remove this host from TFS. Guess what? I can't remove any hosts from TFS at all! Even after I deleted it from SCVMM. The error I get is: 

TF259085: Team Foundation Server could not delete the environment location because the following All Hosts\_Testing is currently in use: TeamProjectCollectionhostGroup. Delete the resources at this location, and then try the operation again. (type SoapException)

I have no idea what this is telling me. Anyone have any ideas?

Thanks!
Mr Northwind
 Figure: Bad Example - The user encounters an issue and has to email someone about it  

::: good  
![Figure: Good Example - The 'Wiki...' link in the bottom left, takes the user to a wiki page with common issues and workarounds for this form (e.g. Creating a Project Portal)](../../assets/InterfacesWiki.png)  
:::
