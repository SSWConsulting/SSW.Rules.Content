---
type: rule
archivedreason: 
title: Do you avoid huge images or attachments in your email?
guid: 671b9e3f-9cf9-4492-9e2b-e0bdd9c7c470
uri: do-you-avoid-huge-images-or-attachments-in-your-email
created: 2009-03-31T03:15:46.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 2
  title: Cameron Shaw
related: []

---

When your attachment is too big, you should think twice.

<!--endintro-->

1. Avoid large attachments. So if you are sending an email that is >1MB you need to take one second to think:
    * Could a URL be better than this attachment? (see example on the right)
    * Could I send this as a UNC to an internal share?
    * Could I .zip this?
    * Could I put this picture on Flickr or Picasa?

::: greybox
Dear Mike,

Thank you for spending time with us to come to a better understanding of your business requirements. Please review the new version of the specification at [http://www.ssw.com.au/ssw/SQLAuditor/](http://www.ssw.com.au/ssw/SQLAuditor/Default.aspx)FileName.docx 

PS: The .docx was 4MB so I didn't attach a copy. 

Regards, 
Adam Cogan [www.ssw.com.au](http://www.ssw.com.au/ssw)
:::

PS: An added advantage is that the document stays alive. If the URL has been updated and a user takes a week to get around to this email, they will view the latest version.
2. If you have to attach the document, always use WinZip - it is common courtesy - I'll assume you already know that.
3. Never use Rich Text inside Outlook. As a software developer, most large messages I receive are screen captures. By all means use screen captures - pictures do tell a thousand words - but don't include unnecessarily huge images or attachments in your email. Generally the only time you will have serious size problems is if you are using Rich Text instead of HTML inside Outlook.
4. If you are sending screenshots then just send the region of the screen you need. Use a screen capture utility like [Fullshot](http://www.ssw.com.au/ssw/Standards/DeveloperGeneral/WindowsTools.aspx#Snagit) so you can use the region tool and get only the relevant part of the image you need. PS: Don't send screenshots as .bmps use .jpgs .gif or .png
5. If you are sending pictures (every year digital cameras are making our photos bigger and bigger) you may need to resize them down. You can either use Photoshop or for something quicker try Office Document Imaging. 

!["Compress Pictures" options dialog](compress-pictures.jpg)
6. SharePoint was built with sharing files in mind and is a great way to collaborate.
If you are using SharePoint to send a file you simply need to open the context menu, click "send to" and "email a link" as shown: 

![If using SharePoint 2010 you should use this context menu](sharepoint-context-menu.jpg)


**When should you break these size rules?**

Basically, you should be practical:

1. Keep history
2. Paste images into the email - not into a Word document and attach (so it stays with the customers' reply)
3. When you paste a URL, also paste the section of the web page you are referring to (allows for offline reading)


We have a program called [SSW LookOut! for Outlook](http://www.ssw.com.au/ssw/LookOut/) to check for this rule. 
![SSW LookOut](ContactorMailSize.gif)! for Outlook warns you if your mail size is large**
