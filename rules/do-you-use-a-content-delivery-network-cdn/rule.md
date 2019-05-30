---
type: rule
title: Do you use a Content Delivery Network (CDN)?
uri: do-you-use-a-content-delivery-network-cdn
created: 2019-05-16T06:32:40.0000000Z
authors:
- id: 82
  title: Barry Sanders
- id: 1
  title: Adam Cogan
- id: 80
  title: Shane Ye

---



<span class='intro'> <p>​If your site takes too long to load, there is a high chance your users will not wait for it to finish&#160;loading&#160;and abandon viewing it. It is therefore important that we use techniques to make pages&#160;load as quickly as possible. One of these techniques is to use a Content Delivery Network (CDN) to reduce the&#160;network&#160;latency for delivering&#160;pages,&#160;images,&#160;javascript and CSS libraries&#160;to&#160;users​.&#160;This results in faster load times and better experience for your users.<br></p> </span>

<strong style="color&#58;#333333;">What is a CDN?</strong><br>CDN&#160;is short for a Content Delivery&#160;Network. It&#160;is a system of distributed servers (network) that deliver pages and other Web content to a user, based on the geographic locations of the user, the origin of the webpage and the content delivery server.<div><br><strong style="color&#58;#333333;">Why use a CDN?</strong></div><div><strong style="color&#58;#333333;"></strong>A website may be hosted in a particular region, but have the majority of its users coming from an entirely different region – for example, if your site is&#160;hosted in North America, GTmetrix(A&#160;free tool that analyzes your page's speed performance)&#160;might report fast speeds based on our default test location, but if a good chunk of your users come from China, their speed will not be as fast as you experience it to be.<br>Using a CDN can improve your user’s experience in terms of speed, and as we know – speed matters!​<br>Ensuring a consistent experience for all your users is important.<br>CDNs not only ensure a faster experience to your users, but they also help to prevent site crashes in the event of traffic surges – CDNs help to distribute bandwidth across multiple servers, instead of allowing one server to handle all traffic.​<br></div><div><br></div><div><strong>How to choose a CDN?</strong><br></div><div>When choosing a CDN provider, take into account where your user base is located and which CDN provider support those locations. For example, some CDN provides are not fast or reliable when accessed from China (behind the Great Firewall).<br></div><div><br><strong style="color&#58;#333333;">Which CDNs work well from China?</strong></div><div><strong style="color&#58;#333333;"></strong>1.http&#58;//www.staticfile.org/<br>2.http&#58;//www.bootcdn.cn/<br>3.http&#58;//cdn.code.baidu.com/<br>4.http&#58;//lib.sinaapp.com/<br>5.http&#58;//cdnjs.net/<br></div><div>6.https&#58;//www.cloudflare.com/network/china/(Cloudflare’s China Service​)<br></div><div>7.https&#58;//www.akamai.com(Akami)<br></div><div>8.https&#58;//cdnjs.cloudflare.com ​<br></div><div><br><strong style="color&#58;#333333;">Which ones do not work well from China?</strong><br>1.https&#58;//maxcdn.bootstrapcdn.com<br>2.https&#58;//ajax.googleapis.com​<br>​​<br><br><img src="/SiteAssets/do-you-use-cdn-for-js-files/5-28.4.png" alt="5-28.1.png" style="margin&#58;5px;width&#58;881px;" /></div><div><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example,&#160;jquery.min.js from&#160;GoogleAPIs failed to load.<br></dd><br><img src="/SiteAssets/do-you-use-cdn-for-js-files/5-28.5.png" alt="5-28.2.png" style="margin&#58;5px;width&#58;834px;" /></div><div><dd class="ssw15-rteElement-FigureGood">F​igure&#58; Good example, jquery.min.js from CDNJS isn't&#160;block and is very fast.​​<br></dd>​​<br><p>​</p></div>


