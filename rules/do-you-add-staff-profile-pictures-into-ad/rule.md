---
type: rule
archivedreason: 
title: Do you add Staff profile pictures into AD?
guid: 005bc852-6c6c-430c-bb5a-d6d8cb4dd741
uri: do-you-add-staff-profile-pictures-into-ad
created: 2013-08-06T23:42:18.0000000Z
authors:
- id: 47
  title: Stanley Sidik
related: []

---

You can upload Staff profile pictures into Active Directory. Exchange and Lync will automatically use these profile pictures.  
<!--endintro-->

Using a free third party tool AD Photo Edit tool which can be downloaded from     http://www.cjwdev.co.uk/ you can upload Staff profile pictures into AD. You need to run the application with Domain Admin rights. After you have uploaded the picture for a user it will take some time for the change to be replicated through to Exchange and Lync if you have use these solutions.
<dl class="image">&lt;dt&gt;<img alt="ExchangeAdPhoto.jpg" src="ExchangeAdPhoto.jpg" style="width:460px;">&lt;/dt&gt;<dd>Figure: Profile picture imported from AD into Exchange </dd></dl><dl class="image">&lt;dt&gt;<img src="Lync.jpg" alt="Lync.jpg" style="margin:5px;"><br>&lt;/dt&gt;&lt;dt&gt;<span style="color:#555555;font-size:0.9rem;font-weight:bold;line-height:16px;">Figure: Profile picture imported from AD into Lync</span>&lt;/dt&gt;</dl>
