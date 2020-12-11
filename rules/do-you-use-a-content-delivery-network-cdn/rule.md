---
type: rule
archivedreason: 
title: Do you use a Content Delivery Network (CDN)?
guid: 8312c849-88a5-4745-82e7-739127d6e9f8
uri: do-you-use-a-content-delivery-network-cdn
created: 2019-05-16T06:32:40.0000000Z
authors:
- id: 82
  title: Barry Sanders
- id: 1
  title: Adam Cogan
- id: 80
  title: Shane Ye
related: []

---


<p>​If your site takes too long to load, there is a high chance your users will not wait for it to finish loading and abandon viewing it. It is therefore important that we use techniques to make pages load as quickly as possible. One of these techniques is to use a Content Delivery Network (CDN) to reduce the network latency for delivering pages, images, javascript and CSS libraries to users​. This results in faster page load times and a ​better experience for your users.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<strong style="color:#333333;">What is a CDN?</strong><br>CDN is short for a Content Delivery Network. It is a system of distributed servers (network) that deliver pages and other Web content to a user, based on the geographic locations of the user, the origin of the webpage and the content delivery server.<div><br><strong style="color:#333333;">Why use a CDN?</strong></div><div><strong style="color:#333333;"></strong>A website may be hosted in a particular region, but have the majority of its users coming from an entirely different region – for example, if your site is hosted in North America, GTmetrix(A free tool that analyzes your page's speed performance) might report fast speeds based on our default test location, but if a good chunk of your users come from China, their speed will not be as fast as you experience it to be.<br>Using a CDN can improve your user’s experience in terms of speed, and as we know – speed matters!​<br>Ensuring a consistent experience for all your users is important.<br>CDNs not only ensure a faster experience to your users, but they also help to prevent site crashes in the event of traffic surges – CDNs help to distribute bandwidth across multiple servers, instead of allowing one server to handle all traffic.​<br></div><div><br></div><div><strong>How to choose a CDN?</strong><br></div><div>When choosing a CDN provider, take into account where your user base is located and which CDN provider support those locations. For example, some CDN provides are not fast or reliable when accessed from China (behind the Great Firewall).<br></div><div><br><strong style="color:#333333;">Which CDNs work well from China?</strong></div><div><strong style="color:#333333;"></strong>1.http://www.staticfile.org/<br>2.http://www.bootcdn.cn/<br>3.http://cdn.code.baidu.com/<br>4.http://lib.sinaapp.com/<br>5.http://cdnjs.net/<br></div><div>6.https://www.cloudflare.com/network/china/(Cloudflare’s China Service​)<br></div><div>7.https://www.akamai.com(Akami)<br></div><div>8.https://cdnjs.cloudflare.com ​<br></div><div><br><strong style="color:#333333;">Which ones do not work well from China?</strong><br>1.https://maxcdn.bootstrapcdn.com<br>2.https://ajax.googleapis.com​<br>​​<br><br><img src="5-28.4.png" alt="5-28.1.png" style="margin:5px;width:881px;" /></div><div><dd class="ssw15-rteElement-FigureBad">Figure: Bad example, jquery.min.js from GoogleAPIs failed to load.<br></dd><br><img src="5-28.5.png" alt="5-28.2.png" style="margin:5px;width:834px;" /></div><div><dd class="ssw15-rteElement-FigureGood">F​igure: Good example, jquery.min.js from CDNJS isn't block and is very fast.​​<br></dd>​​<br><p>​</p></div>


