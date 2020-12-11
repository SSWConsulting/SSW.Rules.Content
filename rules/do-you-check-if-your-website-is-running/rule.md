---
type: rule
archivedreason: 
title: Do you check if your website is running?
guid: aec5cc1b-e2f2-4f74-8080-452f7e2a0ad9
uri: do-you-check-if-your-website-is-running
created: 2016-08-22T17:41:00.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>If you want to know your website is working or not, you need to add a ping check to the machine also an HTTP Content Scan to the website in WhatsUp. We use WhatsUp to do real-time monitoring.</p>​<span style="line-height:1.6;">Follow these steps to check your website in WhatsUp:</span>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>Add your website as a new device. <dl class="image"><dt> <img src="running1.GIF" alt="running1.GIF" /> </dt><dd>Figure: New device</dd></dl></li><li>Ping monitor is added automatically. <dl class="image"><dt> <img src="running2.GIF" alt="running2.GIF" /> </dt><dd>Figure: Ping monitor</dd></dl></li><li>Add an HTTP Content Scan monitor. <dl class="image"><dt> <img src="running3.GIF" alt="running3.GIF" /> </dt><dd>Figure: HTTP Content Scan</dd></dl></li><li>Edit the scan script. In the script, you can see 2 keywords "Send" and "Expect".<br><span style="line-height:1.6;">"Send" expression is an </span> HTTP<span style="line-height:1.6;"> request to your website.<br></span><span style="line-height:1.6;">"Expect" expression is a regular expression to check the key word in response from your website.<br></span><span style="line-height:1.6;"> <dl class="image"><dt> <img src="running4.GIF" alt="running4.GIF" /> </dt><dd>Figure: Edit scan script</dd></dl> </span></li><li>Add the monitor to your device. <dl class="image"><dt> <img src="running5.GIF" alt="running5.GIF" /> </dt><dd>Figure: Add monitor</dd></dl> Once a device is down or up, a WhatsUp action will tell SQL Reporting Services to send out a notification report. <br>Our report looks like this: <dl class="image"><dt> <img src="running6.GIF" alt="running6.GIF" /> </dt><dd>Figure: Website doesn't work<br></dd></dl><dl class="image"><dt> <img src="running7.GIF" alt="running7.GIF" /> </dt><dd>Figure: Website works</dd></dl></li></ol>


