---
type: rule
title: Do you remove the need to type “/tfs” ?
uri: do-you-remove-the-need-to-type-tfs-
created: 2015-05-05T19:49:26.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan

---



<span class='intro'> <p class="p1">Many clients that complain when they type&#58; <b>tfs.northwind.com </b><br>...and then see <span class="s1" style="color&#58;#ff0000;"><span style="color&#58;#ff0000;">‘Server Error 403 – Forbidden&#58; Access is denied’​</span></span></p><p class="p1">It is not a nice experience that in 2015 the out-of-the-box requirement is still to type &quot;/tfs&quot;.</p> </span>

<dl class="badImage"><dt>​<img src="tfs-url-1.jpg" alt="tfs-url-1.jpg" style="width&#58;650px;" /></dt><dd>Figure&#58; Bad example - A horrible first experience... did I get the URL wrong? Is the server down?​</dd></dl><p> 
   <strong>Note&#58; </strong>The better out-of-the-box experience for Exchange OWA is to type <a href="https&#58;//mail.ssw.com.au/" target="_blank">https&#58;//mail.ssw.com.au/</a><br>...and it redirects to 
   <br>
   <a href="https&#58;//mail.ssw.com.au/owa/auth/logon.aspx?replaceCurrent=1&amp;url=https&#58;//mail.ssw.com.au/owa/" target="_blank">https&#58;//mail.ssw.com.au/owa/auth/logon.aspx?replaceCurrent=1&amp;url=https%3a%2f%2fmail.ssw.com.au%2fowa%2f</a>.</p><p>So fix the nasty out-of-the-box experience.​<br></p><dl class="image"><dt>
      <img src="tfs-url-2.png" alt="tfs-url-2.png" style="margin&#58;5px;width&#58;650px;" />
   </dt><dd>Figure&#58; Option 1 – This is one way. Include some text to tell devs that they can remove the need for /tfs - on the Application Tier page specify port 80 and an empty Virtual Directory</dd></dl><dl class="image"><dt>
      <img src="tfs-url-3.png" alt="tfs-url-2.png" style="margin&#58;5px;width&#58;650px;" />
   </dt><dd>Figure&#58; Option 2 – This is another way. In IIS add the redirect to remove the need to type “/tfs” 
      <span class="ssw15-rteStyle-Highlight">(recommended)​​</span></dd></dl>


