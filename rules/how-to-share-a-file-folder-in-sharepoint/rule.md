---
type: rule
archivedreason: 
title: Do you know how to share a file/folder in SharePoint?
guid: d1cab76a-50d8-4039-9975-ae6796a6ec1e
uri: how-to-share-a-file-folder-in-sharepoint
created: 2015-09-23T18:17:11.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
- title: Tanya Leahy
  url: https://ssw.com.au/people/tanya-leahy
related: 
- avoid-using-share-functionality
- do-you-know-not-to-send-attachments-in-emails
- change-link-sharing-default-behaviour
redirects:
- do-you-know-how-to-share-a-file-folder-in-sharepoint

---

You often need to share links to a file or folder in SharePoint.

<!--endintro-->

You may be tempted to share a link via the Share email invite. In doing so, the sharing permissions default to 'can view', which is fine if you are sharing the file externally. If you are sharing to someone who already has access to the file, it breaks permissions on the item you're sharing and creates a unique permission set for whoever you share it with. This means that a person who already had access to a file may find that using the shared link grants them different permissions. This makes it very difficult for SharePoint admins to maintain permissions!

::: bad  
![Figure: Bad example - Sharing URL via Share email invite](sharepoint-share-email-invite.png)  

:::  

Using "Copy link" to share a file and pasting it in an email ensures that permissions already given remain the same once the file is shared.

Your SharePoint admin should set the default sharing link type to "People with existing access" for copied links. If this has been done, then all you need to do is "Copy link" and share link via email.  

You can select the folder (or file) and click on "Copy link" at the top bar to get the link:

::: good  
![Figure: Good example - Get URL from SharePoint top bar](sharepoint-cloud-copy-folder.jpg)  

:::

You can also right-click the folder/file to copy the link:

::: good  
![Figure: Good example - Get URL by right-clicking a file in SharePoint](sharepoint-right-click-link.jpg)  

:::

If your SharePoint admin has not set the default sharing link type to "People with existing access", this can be done individually each time you share a file.

::: ok  
![Figure: OK example - Set file sharing permission to "People with existing access" each time you share](sharepoint-choose-existing-access.png)

:::
