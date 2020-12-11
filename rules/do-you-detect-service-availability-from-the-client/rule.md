---
type: rule
archivedreason: 
title: Do you detect service availability from the client?
guid: b22a548e-76d1-4090-baae-0c58cca49cdb
uri: do-you-detect-service-availability-from-the-client
created: 2018-12-10T04:58:24.0000000Z
authors:
- id: 34
  title: Brendan Richards
- id: 1
  title: Adam Cogan
- id: 82
  title: Barry Sanders
- id: 80
  title: Shane Ye
related: []

---

Some countries (especially the People's Republic of China) strictly control access to various international web services. You can use service detection to determine whether particular services are available and fall-back gracefully or use alternative providers.

<!--endintro-->

As well as from inside China, another common place where access to third-party services may be blocked is from behind corporate firewalls.

First, read this rule:     [Do you manage your 3rd party dependencies?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=9b3eafc2-6aab-4809-9662-d81128dc3643). You should always start by carefully managing the number of 3rd party services and dependencies your application or website depends on.

There are two ways to determine service availability, these are:

### Option 1: Geolocation

You can use geolocation based on client IP to determine what services are available but this has a number of disadvantages.:

* **Unpredictability** Geolocation based on IP is never perfect
 Geo-location lookup services are not perfect. here's an example: if you use the guest internet in the Microsoft offices, the internet thinks you are outside Australia (Singapore).  
 This approach won't detect services that have been blocked by a company firewall.
* **Maintenance overhead** You need to maintain lists of locations and what services are available there - which may be subject to change (however not very often)
 The list of services allowed/blocked by the "great firewall of china" is a moving target. things get blocked and unblocked all the time with little warning. we would have to keep coming back to the site to test. So there would be an overhead maintaining lists of countries and the services they allow.
* **Extra dependency** - using IP address requires taking a dependency on an extra third-party service to perform the geo-location lookups.


For these reasons, dynamic service detection is recommended in preference to solutions based on geo-location.

### Option 2: Check Connectivity  

**Universality** - China is not the only place that blocks stuff. there are other countries to consider. Also many corporate firewalls block stuff. actively detecting access to a service from the client handles all these scenarios at runtime with no prior configuration.



SSW has created a simple Service Detection library for exactly this purpose called SSW Service Detector. This is open source and available from GitHub:[SSW Service Detector](https://github.com/SSWConsulting/SSW.ServiceDetector).

This Service Detector works by attempting to download the Favicon.ico file from the website for each service you want to use. These favicon files are small, so if a service is available, the file will download very quickly. If a service is blocked, the connection could take a long time to timeout on its own. In this situation, the service detector uses a 1.5-second timer to attempt the download and will cancel the request after this time so that these connection attempts fail quickly and don't block the entire page.
<dl class="badImage">&lt;dt&gt;
      <img src="BlockedDependencies.png" alt="" style="width:800px;">
   &lt;/dt&gt;<dd>Figure Bad Example: Attempted requests to Facebook, Google, and Youtube from China took a long time to timeout, adding significant delays to the rendering of this page<br></dd></dl><dl class="goodImage">&lt;dt&gt;
      <img src="SSW.ServiceDetector.png" alt="SSW.ServiceDetector.png" style="width:800px;">
      <br> 
   &lt;/dt&gt;<dd>Figure: Good Example - Only 4 errors on F12 in China. Using SSW.ServiceDetector, there were only short, canceled requests raised to blocked services. The site was then able to fall-back gracefully for some services and load YouKu for videos<br></dd></dl>
### Solutions

If, for example, your site displays videos, you can detect that YouTube is not available in China and embed YouKu videos instead. 
Both these options require service detection to operate properly. Remember that attempting to connect to a blocked service from China could take a long time to timeout, potentially adding significant loading times to your site.

**Solution 1: Remove the content**
<dl class="image">&lt;dt&gt;<img src="youtuberemove.png" alt="youtuberemove.png" style="width:750px;">&lt;/dt&gt;</dl>
**Solution 2: Provide an alternative to the blocked service**
<dl class="image">&lt;dt&gt;<img src="youku.png" alt="youku.png" style="width:750px;">&lt;/dt&gt;</dl>
