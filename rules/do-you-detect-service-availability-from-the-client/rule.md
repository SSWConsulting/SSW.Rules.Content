---
type: rule
title: Do you detect service availability from the client?
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

---



<span class='intro'> Some countries (especially the People's Republic of China) strictly control access to various international web services. You can use service detection to determine whether particular services are available and fall-back gracefully or use alternative providers.​<br> </span>

<p>As well as from inside China, another common place where access to third-party services may be blocked is from behind corporate firewalls.</p><p>First, read this rule&#58; 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=9b3eafc2-6aab-4809-9662-d81128dc3643">Do you manage your 3rd party dependencies?</a>. You should always start by carefully managing the number of 3rd party services and dependencies your application or website depends on.<br></p><p>There are two ways to determine service availability, these are&#58;<br></p><h3 class="ssw15-rteElement-H3">Option 1&#58; Geolocation</h3><p>You can use geolocation based on client IP to&#160;determine&#160;what services are available but this has a number of disadvantages.&#58;</p><ul><li>
      <strong>Unpredictability</strong> Geolocation based on IP is never perfect<br> Geo-location lookup services are not perfect. here's an example&#58; if you use the guest internet in the Microsoft offices, the internet thinks you are outside Australia (Singapore).&#160;&#160;<br> This approach won't detect services that have been blocked by a company firewall.</li><li>
      <strong>Maintenance overhead</strong> You need to maintain lists of locations and what services are available there - which may be subject to change (however not very often)<br> The list of services allowed/blocked by the &quot;great firewall of china&quot; is a moving target. things get blocked and unblocked all the time with little warning. we would have to keep coming back to the site to test. So there would be an overhead maintaining lists of countries and the services they allow.</li><li>
      <strong>Extra dependency</strong> - using IP address requires taking a dependency on an extra&#160;third-party service to perform&#160;the geo-location lookups.&#160;</li></ul><p>For these reasons, dynamic service detection is recommended in preference to solutions based on geo-location.<br></p><h3 class="ssw15-rteElement-H3">​​Option 2&#58; Check Connectivity &#160;</h3><p>
   <strong>Universality</strong> - China is not the only place that blocks stuff. there are other countries&#160;to consider. Also many corporate firewalls block stuff. actively detecting access to a service from the client handles all these scenarios&#160;at runtime with no prior configuration.<br></p><p></p><p>SSW has created a simple Service Detection library for exactly this purpose&#160;called SSW Service Detector. This is open source and available from GitHub&#58;<a href="https&#58;//github.com/SSWConsulting/SSW.ServiceDetector"> SSW Service Detector</a>.</p><p>This Service Detector works by attempting to download the Favicon.ico file from the website for each service you want to&#160;use. These favicon files are small, so if a&#160;service is&#160;available, the file will download very quickly. If a service is blocked, the connection could take a long time to timeout on its own. In this situation, the service detector uses a 1.5-second timer to attempt the download and will cancel the request after this time so that these connection&#160;attempts&#160;fail quickly and don't block the entire page.<br></p><dl class="badImage"><dt> 
      <img src="/PublishingImages/BlockedDependencies.png" alt="" style="width&#58;800px;" /> 
   </dt><dd>Figure Bad Example&#58; Attempted requests to Facebook, Google, and Youtube from China&#160;took a long time to timeout, adding significant delays to the rendering of this page<br></dd></dl><dl class="goodImage"><dt> 
      <img src="/PublishingImages/SSW.ServiceDetector.png" alt="SSW.ServiceDetector.png" style="width&#58;800px;" /> 
      <br>
   </dt><dd>Figure&#58; Good Example - Only&#160;4 errors on F12 in China.&#160;Using SSW.ServiceDetector, there were only short, canceled requests raised to blocked services. The site was then able to fall-back gracefully for some services and load YouKu for videos<br></dd></dl>
<h3 class="ssw15-rteElement-H3">​Solutions</h3><p>If, for example, your site displays videos, you can detect that YouTube is not available in China and embed YouKu videos instead.&#160;<br>Both these options require service detection to operate properly. Remember that attempting to connect to a blocked service from China could take a long time to timeout, potentially adding significant loading times to your site.&#160;<br><br>Solution 1&#58; Remove the content<br><br>[​<b style="color&#58;#ff0000;"><span style="color&#58;#ff0000;">TODO&#58; JEAN</span></b><b></b>&#160;-&#160;image of the youtube removed]<br><br>Solution 2&#58; Provide an alternative to the blocked service<br><br>[<b style="color&#58;#ff0000;"><span style="color&#58;#ff0000;">TODO&#58; JEAN</span></b> -&#160;​image of the youtube changed to yuku]<br><br></p>


