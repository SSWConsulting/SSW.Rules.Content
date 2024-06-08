---
type: rule
archivedreason: 
title: Do you know how to setup your Outlook to send but not receive?
guid: ddd15c6d-c09f-4acb-94c1-2496508f0af3
uri: do-you-know-how-to-setup-your-outlook-to-send-but-not-receive
created: 2011-04-13T06:18:47.0000000Z
authors:
- title: Matthew Hodgkins
  url: https://ssw.com.au/people/matthew-hodgkins
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

When using your presentation computer you may want to still be able to send emails but not want to download your entire Exchange mailbox to your Boot2VHD image. This is especially relevant for people with large mailboxes.   
<!--endintro-->

Here is how you do it:

1. Open Outlook and create a new Exchange account: 
      

![Figure - Tick manually configure server settings](mail1.png)  

2. Enter your server name and username, but un-tick 
       **Use Cached Exchange Mode** :  
      
![Figure - Un-tick Use Cached Exchange Mode](Mail3.png)  

3. Finish the setup and then open Outlook
4. Configure your Send / Receive Groups: 
      
![Figure - Click Send / Receive | Click Send / Receive Groups | Click Define Send / Receive Groups](Email2.png)  

5. Now we can choose the parts of our mailbox we want to synced to our PC. The following options are recommended:
    * Untick 
             **Receive Mail Items**
    * Tick 
             **Download offline address book**
    * Tick the 
             **Outbox** folder
    * Tick the 
             **Contacts** folder
    * Tick the 
             **Sent Items** folder,
    * and select 
             **Download headers only**


![Figure - Untick "Receive mail items" | Tick "Sent Items", "Contacts" and "Outbox" | Download only headers for "Sent Items"](Email.png)  

6. When back in the main Outlook window click 
       **Send / Receive** **All** **Folders** and this will sync your sent items and contacts which will now be available offline


**Suggestion to the Microsoft Outlook Team:**

* Give us a "Sync last x weeks" for each folder
* Give us a "Work in Minimal Mode" that does the above
