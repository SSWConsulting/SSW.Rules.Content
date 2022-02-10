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
![Figure: Bad Example - You shouldn't look for files on network shares](https://www.ssw.com.au/rules/static/0229b18de57f44d63a8390b1ce886008/1d69c/teams%20-%20network%20share.png "Figure: Bad Example - You shouldn't look for files on network shares")
:::

Don't start searching from your start menu either for a program whether that be Notepad, Notpad++, OneNote or even Word.  This will open the new file locally on your laptop which requires manual copying/sharing later.  It's easy to forget to do.

::: bad
![Figure: Bad Example - You shouldn't create files locally first and then copy them](https://www.ssw.com.au/rules/static/89e4eda85d3e7ed9c3fe25f804179050/5c6e9/teams%20-%20Not%20from%20start%20menu.png)
:::

Instead create your file in the Team for a start.  It is immediately backed up and shared to the entire Team.

::: good
![Figure: Good Example - You can use the files tab in Teams (without leaving the app)](https://www.ssw.com.au/rules/static/b8e3908b14e5353573455fe8df248fc8/c5d70/teams%20-%20file%20tab.png)
:::

The great thing about having conversations next to the file is that it is always in context. Also, future users can view the conversation when they open the file in teams.

::: good
![Figure: Good Example - You can have a conversation about a file](https://www.ssw.com.au/rules/static/708d9cfaddc82eb7ef8de06ad39027af/c5d70/teams%20-%20document%20conversation.png)
:::

Behind the scenes, storage is provided by a SharePoint site; so that is there if you want to use it. As an added bonus thanks to this; you can [take the files offline by syncing with OneDrive for Business](/sync-files-from-teams-to-file-explorer) and by default each channel gets its own folder.

::: good
![Figure: Good Example - You can open the files in SharePoint](https://www.ssw.com.au/rules/static/b4510c000c917a3795db8f5a756a351b/c5d70/teams%20-%20open%20sharepoint.png)
:::

::: good
![Figure: Good Example - You can sync the files in SharePoint with your current machine through OneDrive. A toast notification should popup indicating that files will be synced](https://www.ssw.com.au/rules/static/6872c7a2751f0e42f37daf5f89929866/49b61/teams%20-%20sync%20onedrive.png)
:::

::: greybox
**Note** 
If you realise later that you have created a client document and not saved it to Teams but have uploaded it to Onedrive instead then to keep the file history you should Sync Teams to your drive and copy the file locally.  This will keep the file version history.  Uploading the file in Teams loses that history so you may end up with an old client Team containing notes that appear to be new.
:::

### What does not get stored in Microsoft Teams?

1. **For developers**,

A: Code obviously belongs in GitHub, Azure DevOps, etc.
B: Also the [7 important documents](/do-you-review-the-documentation) should be stored in Azure DevOps (was TFS/VSTS)... or instead [use Markdown with the Wiki](/do-you-make-getting-started-on-a-project-easy-for-new-developers)

2. **For designers** with large files, OneDrive is a better choice. See: [Do you know the best Source Control for Designers?](/do-you-know-the-best-source-control-for-designers)

### What about usernames and passwords?

Documents with user names and passwords should not be stored in Microsoft Teams. Security is very important for everyone and every company. [Use a password manager](/password-manager) to store usernames and passwords. 

**Note:** API keys, whether generic or for the individual should also be stored in a password manager.

**Note:** You can add other cloud storage providers for file storage e.g. Google Drive, Dropbox, etc.  
This is not recommended - as they aren't first-class citizens i.e. if you want to share files from them, you need to go to the provider's sharing settings outside of Teams.

**Warning:** By using Teams instead of SharePoint, you are losing a number of key features:

* No full fidelity support for Metadata in Document Libraries e.g. can’t add extra columns into the “Files” tab
* No support for private channels e.g. you will need a team per subset of users with different permissions
* No direct access to version history from Teams UI (still exists on SharePoint UI)
* No access to the cross-office365 Search feature e.g. SharePoint search is better (see video: https://youtu.be/TiWzzdASVWE)
* No access to external content in the search feature e.g. can’t search rules.ssw.com.au
* No access to SharePoint designer workflows (although the new way to do it is Microsoft Flow)
