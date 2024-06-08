---
type: rule
archivedreason: 
title: Do you use the security options in Outlook?
guid: 4756ad65-7273-4ea4-bf6f-95f7a586da27
uri: do-you-use-the-security-options-in-outlook
created: 2009-04-03T08:20:20.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
related: []
redirects: []

---

When you distribute important information by email all you can do is put "Do Not Forward this please". Important corporate information should be protected better than this.

<!--endintro-->

![Figure: You can protect your email messages](outlookIRM.jpg)  

This solution exists in Microsoft Office and is built into Outlook. Entitled 'Information Rights Management', a file level security application built onto Windows Server. The capability enables you to prevent recipients of your emails (and attachments) from forwarding them on, copying any text, or printing the document (be aware that determined chaps could use a lower level screen shot program to get past this).

Additionally, it encrypts the file as it's sent away. As an added basis - you can secure on a group level (based on Active Directory groups). To prevent an email being forwarded simply create a new email and select the "options" tab and click on "permission" in the ribbon and select "do not forward".

![Figure: How to prevent emails being forwarded in Outlook](outlook-prevent-FW.jpg)  

**Note:** You may be interested to know that every mail item that you send gets a file saved with these credentials so you can still open the emails when you are offline. To see: go to Start - Run %USERPROFILE%\Local Settings\Application Data\Microsoft\drm.
