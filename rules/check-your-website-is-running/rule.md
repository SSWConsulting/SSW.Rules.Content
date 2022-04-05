---
type: rule
archivedreason: 
title: Do you check if your website is running?
guid: aec5cc1b-e2f2-4f74-8080-452f7e2a0ad9
uri: check-your-website-is-running
created: 2016-08-22T17:41:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-check-if-your-website-is-running

---

If you want to know your website is working or not, you need to add a ping check to the machine also an HTTP Content Scan to the website in WhatsUp. We use WhatsUp to do real-time monitoring.
Follow these steps to check your website in WhatsUp:
<!--endintro-->

1. Add your website as a new device. 
![Figure: New device](running1.gif)  

2. Ping monitor is added automatically. 
![Figure: Ping monitor](running2.gif)  

3. Add an HTTP Content Scan monitor. 
![Figure: HTTP Content Scan](running3.gif)  

4. Edit the scan script. In the script, you can see 2 keywords "Send" and "Expect".
"Send" expression is an  HTTP request to your website.
"Expect" expression is a regular expression to check the key word in response from your website.
 
![Figure: Edit scan script](running4.gif)  

5. Add the monitor to your device. 
![Figure: Add monitor](running5.gif)  
 Once a device is down or up, a WhatsUp action will tell SQL Reporting Services to send out a notification report. 
Our report looks like this: 
![Figure: Website doesn't work](running6.gif)  

![Figure: Website works](running7.gif)
