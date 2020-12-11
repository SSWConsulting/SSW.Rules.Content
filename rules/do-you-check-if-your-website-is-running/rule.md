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

If you want to know your website is working or not, you need to add a ping check to the machine also an HTTP Content Scan to the website in WhatsUp. We use WhatsUp to do real-time monitoring.
Follow these steps to check your website in WhatsUp:
<!--endintro-->

1. Add your website as a new device. <dl class="image">&lt;dt&gt; <img src="running1.GIF" alt="running1.GIF"> &lt;/dt&gt;<dd>Figure: New device</dd></dl>
2. Ping monitor is added automatically. <dl class="image">&lt;dt&gt; <img src="running2.GIF" alt="running2.GIF"> &lt;/dt&gt;<dd>Figure: Ping monitor</dd></dl>
3. Add an HTTP Content Scan monitor. <dl class="image">&lt;dt&gt; <img src="running3.GIF" alt="running3.GIF"> &lt;/dt&gt;<dd>Figure: HTTP Content Scan</dd></dl>
4. Edit the scan script. In the script, you can see 2 keywords "Send" and "Expect".
"Send" expression is an  HTTP request to your website.
"Expect" expression is a regular expression to check the key word in response from your website.
 <dl class="image">&lt;dt&gt; <img src="running4.GIF" alt="running4.GIF"> &lt;/dt&gt;<dd>Figure: Edit scan script</dd></dl>
5. Add the monitor to your device. <dl class="image">&lt;dt&gt; <img src="running5.GIF" alt="running5.GIF"> &lt;/dt&gt;<dd>Figure: Add monitor</dd></dl> Once a device is down or up, a WhatsUp action will tell SQL Reporting Services to send out a notification report. 
Our report looks like this: <dl class="image">&lt;dt&gt; <img src="running6.GIF" alt="running6.GIF"> &lt;/dt&gt;<dd>Figure: Website doesn't work<br></dd></dl><dl class="image">&lt;dt&gt; <img src="running7.GIF" alt="running7.GIF"> &lt;/dt&gt;<dd>Figure: Website works</dd></dl>
