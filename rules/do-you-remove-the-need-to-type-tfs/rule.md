---
type: rule
archivedreason: 
title: Do you remove the need to type “/tfs” ?
guid: 3d5efb3b-12ed-4d73-be25-23b214a0a7d8
uri: do-you-remove-the-need-to-type-tfs
created: 2015-05-05T19:49:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---

Many clients that complain when they type:  **tfs.northwind.com** 
...and then see ‘Server Error 403 – Forbidden: Access is denied’

It is not a nice experience that in 2015 the out-of-the-box requirement is still to type "/tfs".

<!--endintro-->


::: bad  
![Figure: Bad example - A horrible first experience... did I get the URL wrong? Is the server down?](tfs-url-1.jpg)  
:::

**Note:** The better out-of-the-box experience for Exchange OWA is to type https://mail.ssw.com.au/
...and it redirects to     
[https://mail.ssw.com.au/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fmail.ssw.com.au%2fowa%2f](https://mail.ssw.com.au/owa/auth/logon.aspx?replaceCurrent=1&url=https://mail.ssw.com.au/owa/).

So fix the nasty out-of-the-box experience.

![Figure: Option 1 – This is one way. Include some text to tell devs that they can remove the need for /tfs - on the Application Tier page specify port 80 and an empty Virtual Directory](tfs-url-2.png)  

![Figure: Option 2 – This is another way. In IIS add the redirect to remove the need to type “/tfs”        (recommended)](tfs-url-3.png)
