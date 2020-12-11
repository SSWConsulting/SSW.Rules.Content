---
type: rule
archivedreason: 
title: Do you remove the need to type “/tfs” ?
guid: 3d5efb3b-12ed-4d73-be25-23b214a0a7d8
uri: do-you-remove-the-need-to-type-tfs-
created: 2015-05-05T19:49:26.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---

Many clients that complain when they type:  **tfs.northwind.com** 
...and then see ‘Server Error 403 – Forbidden: Access is denied’

It is not a nice experience that in 2015 the out-of-the-box requirement is still to type "/tfs".

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="tfs-url-1.jpg" alt="tfs-url-1.jpg" style="width:650px;">&lt;/dt&gt;<dd>Figure: Bad example - A horrible first experience... did I get the URL wrong? Is the server down?</dd></dl>
**Note:** The better out-of-the-box experience for Exchange OWA is to type https://mail.ssw.com.au/
...and it redirects to     
[https://mail.ssw.com.au/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fmail.ssw.com.au%2fowa%2f](https://mail.ssw.com.au/owa/auth/logon.aspx?replaceCurrent=1&url=https://mail.ssw.com.au/owa/).

So fix the nasty out-of-the-box experience.
<dl class="image">&lt;dt&gt;
      <img src="tfs-url-2.png" alt="tfs-url-2.png" style="margin:5px;width:650px;">
   &lt;/dt&gt;<dd>Figure: Option 1 – This is one way. Include some text to tell devs that they can remove the need for /tfs - on the Application Tier page specify port 80 and an empty Virtual Directory</dd></dl><dl class="image">&lt;dt&gt;
      <img src="tfs-url-3.png" alt="tfs-url-2.png" style="margin:5px;width:650px;">
   &lt;/dt&gt;<dd>Figure: Option 2 – This is another way. In IIS add the redirect to remove the need to type “/tfs” 
      <mark>(recommended)</mark></dd></dl>
