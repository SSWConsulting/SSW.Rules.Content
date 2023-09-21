---
type: rule
title: PC - Do you organize your hard disk?
uri: pc-do-you-organize-your-hard-disk
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kiki
related: []
redirects:
  - do-you-do-organize-your-hard-disk
created: 2018-06-04T02:06:32.000Z
archivedreason: null
guid: 0b99ae80-634b-47db-9a7b-b6d3763361f3
---
Using a standard file structure for storing user data on laptops makes locating the important information fast and performing automated backup operations easy - Use this checklist.

Remember, the expectation is for all the questions to be answered with "YES" by the end of this checklist.

![](data-backup.jpg)

<!--endintro-->

### Domain-joined checklist:

**1. Is your computer domain-joined?** {{ YES/NO }}  
   **Note:** To check, go to File Explorer | This PC | Right-click | Properties | Check for "Domain" or "Workgroup". If it says "DOMAIN", you are on the domain. If it says "WORKGROUP", you are not.  
   
**2. The Backup Script - Date Last Run:** {{ DD/MM/YYYY }}  
   If your computer is domain-joined, then your backup script should already be working (E.g. Daily at 11 am)  
   Go to the logs, e.g. File Explorer |  Fileserver | UserBackups | ztBackupScripts | UserLogs.log to see the last time your backup was done 

### Non-domain-joined checklist:

**1. Do you use a cloud backup application?** {{ YES/NO }}  
   Which one? {{ CLOUD APP }}   

::: greybox
**Tip:** Some good options include OneDrive for Business and Dropbox. You should [always keep important files in the cloud](/pc-do-you-use-the-best-backup-solution) for security reasons.
:::

**2. Do you keep your files in one folder structure?** {{ YES/NO }}  
Location: {{ LOCATION }} Size: {{ USED }} GB of {{ TOTAL }} GB  Errors  {{ NUMBER OF ERRORS }}

::: greybox
**Note:** For OneDrive the default is: C:\Users\[UserName]\OneDrive

**Tip:** You can have additional accounts in the same PC! (Even multiple OneDrive accounts)

**Warning:** If you are using OneDrive, it is not possible to change the root directory folder name. Normally, the root directory folder has a space in it ("OneDrive - SSW"), so keep that in mind when trying to run script or code from the OneDrive folder.
:::

When you choose a location in OneDrive, it will always create the main root folder called "OneDrive - (YourOrganization)". Use this folder to store your files.
E.g. Create a folder with your username in the root of C: prefix the folder with Data, for example, "C:\DataKaiqueBiancatti", and choose that folder to be your main OneDrive folder. It will automatically create a new folder inside it:

::: good
![Figure: Good example - Location of Data{{ YourUserName }} with OneDrive - {{ YourOrganization }} folder in it](onedrive.png)
:::

::: good
![Figure: Good example - Backup is being done automatically](OneDrive.jpg)
:::

**3. Do you keep your desktop clean?** {{ YES/NO }}  
Number of files on Desktop (Aim is zero) {{ NUMBER OF FILES }}    

You should always aim to have a clean desktop, without temporary files or unnecessary shortcuts.
Delete anything that is not necessary from there and do not save things there by default. Having a messy desktop just makes everything confusing.

**4. Do you keep your Outlook PST/OST separated from your cloud backups?** {{ YES/NO }}   

::: greybox
**Tip:** You can check where your PST/OST is via Outlook | File | Account Settings | Data Files.

**Note:** By Default it is in C:\Users\[UserName]\AppData so it is not backed up.
:::

Outlook mailboxes tend to get huge in size pretty quickly, and your emails are already being backed up by your Exchange Server, so there is no need to back these files up. PST files (Outlook 2013 and earlier) contain all your mailbox messages and OST files (Outlook 2016 and newer) contain all your messages to be used offline.

**5. Do you have a Temp folder?** {{ YES/NO }}  
Create a temporary folder for temporary files, like "C:\temp". It makes it easier to see.

**6. (Optional) Phone - Can you see the files that are on your PC on your mobile too?** {{ YES/NO }}  
Install the OneDrive (or your other selected backup application) app on your phone and log in with the same account you used on your PC.

**7. (Optional) Phone - Do you care if you lose your photos?** {{ YES/NO }}   

  **If not, why? {{ REASON }}**

  Which phone? {{ IOS/ANDROID }}

  **Which backup application are you using? {{ BACKUP APP }}**

* If Yes and iOS, then use iCloud, OneDrive or your selected backup application on your phone to back them up automatically.
* If Yes and Android, then use Google Drive, OneDrive or your selected backup application on your phone to back them up!
* If you don't care about losing your photos, do nothing!
