---
type: rule
title: Files - Do you store project documents in Teams?
uri: track-project-documents
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy
related:
  - sync-files-from-teams-to-file-explorer
  - sales-do-you-track-all-sales-related-activities-in-crm
  - integrate-dynamics-365-and-microsoft-teams
redirects:
  - the-best-place-to-store-documents-and-share-them
  - rules-to-better-microsoft-teams-the-best-place-to-store-documents-and-share-them
  - files-do-you-store-project-documents-in-teams
created: 2018-07-30T01:05:40.000Z
archivedreason: null
guid: 0ae0371f-7ff3-47af-ac51-ea78ef41a459
---
There is a myriad of options to choose from when storing and sharing documents: SharePoint, or OneDrive/Dropbox/Google Drive, or Microsoft Teams. The best choice is **Microsoft Teams** because it brings together the best of SharePoint, cloud file storage, real time collaboration and more into a single location.

<!--endintro-->

Warwick Leahy tells us why it's so important to save our files in the right place:

`youtube: https://www.youtube.com/embed/Ey_zIh0cRrU`

Want to learn more? Watch Jean Thirion's longer video on this topic:

`youtube: https://www.youtube.com/embed/Mna0QBFB6CU`

::: bad
![Figure: Bad example - You shouldn't look for files on network shares](teams - network share.png)
:::

Don't start searching from your start menu either for a program whether that be Notepad, Notepad++, OneNote or even Word. This will open the new file locally on your laptop which requires manual copying/sharing later - and it's easy to forget to do that.

::: bad
![Figure: Bad example - You shouldn't create files locally first and then copy them](teams - Not from start menu.png)
:::

Instead create your file in the Team for a start.  It is immediately backed up and shared to the entire Team.

::: good
![Figure: Good example - You can use the files tab in Teams (without leaving the app)](teams - file tab.png)
:::

The great thing about having conversations next to the file is that it is always in context. Also, future users can view the conversation when they open the file in teams.

::: good
![Figure: Good example - You can have a conversation about a file](teams - document conversation.png)
:::

Behind the scenes, storage is provided by a SharePoint site; so that is there if you want to use it. As an added bonus thanks to this; you can [take the files offline by syncing with OneDrive for Business](/sync-files-from-teams-to-file-explorer) and by default each channel gets its own folder.

::: good
![Figure: Good example - You can open the files in SharePoint](teams - open sharepoint.png)
:::

::: good
![Figure: Good example - You can sync the files in SharePoint with your current machine through OneDrive. A toast notification should popup indicating that files will be synced](teams - sync onedrive.png)
:::

::: greybox
**Note**
If you realise later that you have created a client document and uploaded it to OneDrive instead of saving it to Teams, then you should Sync Teams to your drive and copy the file locally. This will keep the file version history. Uploading the file in Teams loses that history so you may end up with an old client Team containing notes that appear to be new.
:::

### What does not get stored in Microsoft Teams?

#### For developers

* Code obviously belongs in GitHub, Azure DevOps, etc
* The [8 important documents](/do-you-review-the-documentation) should be stored in Azure DevOps (was TFS/VSTS), or instead [use Markdown with the Wiki](/do-you-make-getting-started-on-a-project-easy-for-new-developers)

#### For designers

* For large files, OneDrive is a better choice. See [the best Source Control for Designers](/do-you-know-the-best-source-control-for-designers)

### What about usernames and passwords?

Documents with usernames and passwords should not be stored in Microsoft Teams. Security is very important for everyone and every company. [Use a password manager](/password-manager) to store usernames and passwords.

**Note:** API keys, whether generic or for the individual should also be stored in a password manager.

**Note:** You can add other cloud storage providers for file storage e.g. Google Drive, Dropbox, etc. This is not recommended, as they aren't first-class citizens (i.e. if you want to share files from them, you need to go to the provider's sharing settings outside of Teams).

::: info
**Warning:** By using Teams instead of SharePoint, you are losing a number of key features:

* No full fidelity support for Metadata in Document Libraries. E.g. Can’t add extra columns into the “Files” tab
* No support for private channels. E.g. You will need a team per subset of users with different permissions
* No direct access to version history from Teams UI (still exists on SharePoint UI)
* No access to the cross-office365 Search feature. E.g. [SharePoint search is better](https://youtu.be/TiWzzdASVWE)
* No access to external content in the search feature. E.g. Can’t search ssw.com.au/rules
* No access to SharePoint designer workflows (although the new way to do it is Microsoft Flow)
:::
