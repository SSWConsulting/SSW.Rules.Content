---
type: rule
title: Do you check if your website is running?
uri: do-you-check-if-your-website-is-running
created: 2016-08-22T17:41:00.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>If you want to know your website is working or not, you need to add a ping check to the machine also an HTTP&#160;Content Scan to the website in WhatsUp. We use WhatsUp to do real-time monitoring.</p>​<span style="line-height&#58;1.6;">Follow these steps to check your website in WhatsUp&#58;</span> </span>

<ol><li>Add your website as a new device. <dl class="image"><dt> <img src="/PublishingImages/running1.GIF" alt="running1.GIF" /> </dt><dd>Figure&#58; New device</dd></dl></li><li>Ping monitor is added automatically. <dl class="image"><dt> <img src="/PublishingImages/running2.GIF" alt="running2.GIF" /> </dt><dd>Figure&#58; Ping monitor</dd></dl></li><li>Add an&#160;HTTP&#160;Content Scan monitor. <dl class="image"><dt> <img src="/PublishingImages/running3.GIF" alt="running3.GIF" /> </dt><dd>Figure&#58; HTTP Content Scan</dd></dl></li><li>Edit the scan script. In the script, you can see 2 keywords &quot;Send&quot; and &quot;Expect&quot;.<br><span style="line-height&#58;1.6;">&quot;Send&quot; expression is an </span> HTTP<span style="line-height&#58;1.6;"> request to your website.<br></span><span style="line-height&#58;1.6;">&quot;Expect&quot; expression is a regular expression to check the key word in response from your website.<br></span><span style="line-height&#58;1.6;"> <dl class="image"><dt> <img src="/PublishingImages/running4.GIF" alt="running4.GIF" /> </dt><dd>Figure&#58; Edit scan script</dd></dl> </span></li><li>Add the monitor to your device. <dl class="image"><dt> <img src="/PublishingImages/running5.GIF" alt="running5.GIF" /> </dt><dd>Figure&#58; Add monitor</dd></dl> Once a device is down or up, a WhatsUp action will tell SQL Reporting Services to send out a notification report.&#160;<br>Our report looks like this&#58; <dl class="image"><dt> <img src="/PublishingImages/running6.GIF" alt="running6.GIF" /> </dt><dd>Figure&#58; Website doesn't work<br></dd></dl><dl class="image"><dt> <img src="/PublishingImages/running7.GIF" alt="running7.GIF" /> </dt><dd>Figure&#58; Website works</dd></dl></li></ol>


