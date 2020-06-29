---
type: rule
title: Chinafy - Do you manage 3rd party dependencies?
uri: chinafy---do-you-manage-3rd-party-dependencies
created: 2018-12-10T03:38:44.0000000Z
authors:
- id: 34
  title: Brendan Richards
- id: 1
  title: Adam Cogan
- id: 82
  title: Barry Sanders

---



<span class='intro'> Modern websites can use 3rd party dependencies from many different sources. This can include js and CSS libraries from&#160;CDNs, video providers such as YouTube and other 3rd party APIs.<br> </span>

<p>Many of these services are completely blocked inside other countries. China,&#160;in particular, currently blocks all the below&#58;</p><ul><li>Facebook​<br></li><li>Google<br></li><li>YouTube<br></li><li>Vimeo<br></li><li>Twitter<br></li></ul><p>Although China is the most well-known country for blocking sites, other countries also block services - like Google (e.g. Iran, Syria) and YouTube (e.g. Pakistan, Syria).</p><dl class="image"><dt>
      <img src="social-media-blocked.png" alt="social-media-blocked.png" />​</dt><dd>Figure&#58; Blocked sites as per 
      <a href="https&#58;//www.freebrowsinglink.com/countries-banned-social-media/">freebrowsinglink.com/countries-banned-social-media​</a><br></dd></dl><p>If the runtime operation of your site depends upon these services, your website will either fail or perform poorly for users in China. Start by reviewing how many of these services are essential, what they do and whether there are China-based equivalents. The fewer external dependencies in your site, the easier it will be to Chinafy.</p><p>Every attempted&#160;request to a blocked service can add serious delays to your site's performance as each one can take ​over a minute&#160;to timeout.&#160;When loading a page, browsers have a limit on the number of simultaneous connections they will open. Google&#160;Chrome, for example,&#160;will support 6 connections to one domain&#160;and 10 connections&#160;overall. If all those connections get used attempting to connect&#160;to blocked resources, the entire page&#160;loading process can stall for minutes!<br></p><p>To measure the impact of this, you need to be able to browse the website from inside China. From there you can open the site and collect performance measurements from the network tab of your browser's dev tools.<br></p><dl class="badImage"><dt> 
      <img src="BlockedDependencies.png" alt="BlockedDependencies.png" style="width&#58;800px;" /> 
   </dt><dd>Figure&#58; Bad example&#58; This browser in China was stalled attempting to load resources from Facebook, Google, and YouTube.</dd></dl><p>This situation can&#160;first be improved by finding and removing unnecessary dependencies.&#160;&#160;Next, ensure that all required CSS and JavaScript content can be loaded - by either hosting within your site&#160;or using a CDN that is available from China.<br></p><p>Finally, you may find that there are features you still want to use elsewhere&#160;but&#160;need to&#160;disable for users in&#160;China. In this case, we recommend detecting the available services from the client.&#160;For more information read&#58; Do you detect available services?&#160; 
   <br></p>


