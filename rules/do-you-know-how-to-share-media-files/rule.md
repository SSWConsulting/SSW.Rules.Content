---
type: rule
archivedreason: Redundant https://my.sugarlearning.com/SSW/items/13879/design-shared-folders
title: Do you know how to share media files?
guid: c44339bd-9159-4b44-8495-a92a42ed763c
uri: do-you-know-how-to-share-media-files
created: 2014-04-03T19:35:33.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Rebecca Liu
  url: https://ssw.com.au/people/rebecca-liu
related: []
redirects: []

---

It is important to be able to easily share files between workers. It is also important that all content is backed up centrally in case an employee is unavailable.

Ideally SharePoint would be used for all content storage but occasionally it is not ideal.

<!--endintro-->


::: bad  
![Figure: Bad Example - SharePoint Explorer View requires waiting every time you save a file while it syncs back to the server](share-media-files-1.jpg)  
:::


::: bad  
![Figure: Bad Example - OneDrive (was SkyDrive) Pro enables offline access and saves locally and then syncs back to the SharePoint server asynchronously, but requires the whole document library to be brought to the local computer, even if you only need one folder in the document library](share-media-files-2.jpg)  
:::


::: greybox
 **Suggestion for OneDrive (was SkyDrive) Team #1 :** Enable OneDrive to have selective sync on folders within a document library.  
:::


::: bad  
![Figure: Bad Example - Files shared via SkyDrive are hard to back up centrally. When you share folders through OneDrive (was SkyDrive) they are only made available through the web interface](share-media-files-3.jpg)  
:::


::: greybox
 **Suggestion to OneDrive (was SkyDrive) Team #2:** When folders are shared with another OneDrive user, the shared folder should appear in the recipients OneDrive folder. This allows it to be backed up by a central user at HQ.  
:::


::: good  
![Figure: Good Example -  DropBox allows offline access. When you share a DropBox folder with another Dropbox user, the shared folder appears in the DropBox folder on their machine with a different icon to indicate sharing](share-media-files-4.jpg)  
:::

Having the folder on the remote machine allows remote backup. All folders used for SSW Work must be shared with the SSW Dropbox Account.
The SSW sys-admin is responsible for backing up the SSW Dropbox account daily.

![Figure: To allow you to use Dropbox for work, first create a folder called SSW\_[YourName] (e.g. SSW\_AdamStephensen), right click on the folder and choose Share this folder...](share-media-files-5.jpg)  

![Figure: Add the email address of the company Dropbox account and click Send Invites. Once the Administrator accepts the share, your important work files will be available in the case that you leave or get hit by a bus](share-media-files-6.jpg)  

![Figure: The Administrator account must now accept the sharing invitation, and the folder will be added to the Administrators Dropbox folder. The Admin should configure a machine to pull the files locally and back them up](share-media-files-7.jpg)
