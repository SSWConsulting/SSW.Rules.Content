---
type: rule
archivedreason: 
title: Do you know how to find broken links?
guid: 744a4e0e-cb34-4af9-bc11-2434a5fabc01
uri: how-to-find-broken-links
created: 2016-11-28T19:04:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-how-to-find-broken-links

---


Often times, web pages are dynamic. Most link scanners are not capable of submitting form information. The trick is to allow a "door" for link scanner go through to scan a dynamic section of a site. A common technique is to hard code hidden link with a query string at the bottom of the page that allows the link scanner to follow into the simulated user input. See the following code for example: <br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="goodCode"><dt><pre>&lt;a href="KB.aspx?KBID=Q1097707"&gt;Q1097707 - How do I turn Option Strict on by default in VB.NET?&lt;/a&gt;<br></pre></dt><dd>Figure: Example source code - finding broken links<br></dd></dl><p>It will return all the knowledge base articles in a paged format. The link scanner will click the Next Page link and eventually scan through the entire knowledge base.<br></p><p>
   <a href="https://www.google.com/webmasters" target="_blank">Google webmaster tools</a> and <a href="http://www.bing.com/toolbox/webmaster/" target="_blank">Bing webmaster centre</a> are useful tools to monitor links.​<br></p><dl class="image"><dt> <img src="GoogleWebMaster.jpg" alt="In Google webmaster tools you can see all broken URLs, and even the pages who are linking to them (known as referrer, found in the 'Linked From' column)" data-pin-nopin="true" style="width:700px;" /> <br> 
   </dt><dd>Figure: In Google webmaster tools you can see all broken URLs, and even the pages who are linking to them (known as referrer, found in the 'Linked From' column)</dd></dl><dl class="image"><dt> <img src="BingWebMaster.jpg" alt="In Bing webmaster center you can find the broken URL which is linked by the above URL" data-pin-nopin="true" style="width:700px;height:577px;" /> </dt><dd>Figure: In Bing webmaster centre you can find the broken URL which is linked by the above URL<br></dd></dl><p class="ssw15-rteElement-YellowBorderBox">We have a program called <a href="https://sswlinkauditor.com/" target="_blank">SSW Link Auditor</a> to check for this rule.</p><dl class="image"><dt> <img src="link-auditor-scan.jpg" alt="Link Auditor Scan Report" style="width:700px;height:405px;" /> </dt><dd>Figure: SSW Link Auditor automatically locate broken links</dd></dl> <br>


