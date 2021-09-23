---
type: rule
title: Domain - Do you use the Distributed File System for your file shares?
uri: use-the-distributed-file-system-for-your-file-shares
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
  - do-you-use-the-distributed-file-system-for-your-file-shares
created: 2017-07-10T21:18:15.000Z
archivedreason: null
guid: c9f9fd35-5c40-4293-87fc-ea8dfb39f480
---
Occasionally, one server and its drives will not have sufficient space to store all related files in a network share. For example, you may have a "SetupFiles" directory that stores all Setup executables on your network e.g. \bee\SetupFiles. There are problems with this approach.

<!--endintro-->

1. You will run out of space - which means you will have to copy or move old (but still used) setup files around to other drives (\bee\d$\SetupOld\ ) or other machines e.g. \tuna\SetupFiles. This fragmentation of your setup files can cause confusion for your users.
2. When you retire or rename the old server, links to the old server location will not work

So how do you get around this problem? The answer is in the **Distributed File System (DFS)**. Instead of having several server-specific file share locations, you can have a domain-wide setup location that offers a seamless experience to your users. DFS will even track a history of when and where file locations were moved.

![Figure: The Distributed File System consolidates many separate file shares into one convenient location for your users](Network\_DistributedFileSystem.gif)