---
type: rule
title: Do you know how to find broken links?
uri: do-you-know-how-to-find-broken-links
created: 2016-11-28T19:04:17.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Often times, web pages are dynamic. Most link scanners are not capable of submitting form information. The trick is to allow a &quot;door&quot; for link scanner go through to scan a dynamic section of a site. A common technique is to hard code&#160;hidden link with a query string at the bottom of the page that allows the link scanner to follow into the simulated user input. See the following code for example&#58; <br> </span>

<dl class="goodCode"><dt><pre>&lt;a href=&quot;KB.aspx?KBID=Q1097707&quot;&gt;Q1097707 - How do I turn Option Strict on by default in VB.NET?&lt;/a&gt;<br></pre></dt><dd>Figure&#58; Example source code - finding broken links<br></dd></dl><p>It will return all the knowledge base articles in a paged format. The link scanner will click the Next Page link and eventually scan through the entire knowledge base.<br></p><p>
   <a href="https&#58;//www.google.com/webmasters" target="_blank">Google webmaster tools</a>&#160;and <a href="http&#58;//www.bing.com/toolbox/webmaster/" target="_blank">Bing webmaster centre</a>&#160;are useful tools to monitor links.​<br></p><dl class="image"><dt> <img src="/PublishingImages/GoogleWebMaster.jpg" alt="In Google webmaster tools you can see all broken URLs, and even the pages who are linking to them (known as referrer, found in the 'Linked From' column)" data-pin-nopin="true" style="width&#58;700px;" /> <br> 
   </dt><dd>Figure&#58; In Google webmaster tools you can see all broken URLs, and even the pages who are linking to them (known as referrer, found in the 'Linked From' column)</dd></dl><dl class="image"><dt> <img src="/PublishingImages/BingWebMaster.jpg" alt="In Bing webmaster center you can find the broken URL which is linked by the above URL" data-pin-nopin="true" style="width&#58;700px;height&#58;577px;" /> </dt><dd>Figure&#58; In Bing webmaster centre you can find the broken URL which is linked by the above URL<br></dd></dl><p class="ssw15-rteElement-YellowBorderBox">We have a program called <a href="https&#58;//sswlinkauditor.com/" target="_blank">SSW Link Auditor</a> to check for this rule.</p><dl class="image"><dt> <img src="/PublishingImages/link-auditor-scan.jpg" alt="Link Auditor Scan Report" style="width&#58;700px;height&#58;405px;" /> </dt><dd>Figure&#58; SSW Link Auditor automatically locate broken links</dd></dl> <br>


