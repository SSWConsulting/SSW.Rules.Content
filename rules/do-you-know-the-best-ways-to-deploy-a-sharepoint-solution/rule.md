---
type: rule
archivedreason: 
title: Do you know the best ways to deploy a SharePoint solution?
guid: 285249f0-a88f-448e-b1e6-17d1e0e0cee3
uri: do-you-know-the-best-ways-to-deploy-a-sharepoint-solution
created: 2009-04-17T05:39:16.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Development for a SharePoint solution is always risky and may involve bringing down the server from time to time.  So we always customize and develop SharePoint solutions on a separate development server.  But when your development is done, do you know how to deploy your changes to the staging and eventually the production server?  
<!--endintro-->

The Bad method 
 The naïve and bad method would be to just back up the entire content database, then copy the database backup to the destination server, and restore it there.

1. Backup command: 

    stsadm –o backup –url http://servername:port -filename c:\myfile.bak
2. Restore command: 

    stsadm –o restore –url http://servername:port –filename c:\myfile.bak -overwrite


There are quite a few issues with this approach:

1. At a glance – seems simple
2. Any additional content at the destination server is wiped out – no content editing can continue while the development work is happening…
3. Backup file can be extremely large as it includes version history and a lot of extra fat, the file can easily be over a few hundred megabytes!
4. Deployment via backup and restore is not a Microsoft supported operation


The Good method 
 The better method is to build a feature or solution deployment package

1. Build a VSeWSS project for package and deployment
2. When built, this will produce a wsp file (this is a cab file) that can be deployed as features on the destination server


A few considerations for this approach:

1. Site definitions, list definitions, layouts and masterpages, static content and webparts can all be deployed this way
2. User content cannot be deployed this way. Any content will need to be exported and re-imported to move between development, staging and/or production servers.
