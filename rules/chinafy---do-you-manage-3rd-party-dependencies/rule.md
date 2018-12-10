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



<span class='intro'> ​Modern web sites can use 3rd party dependencies from many different souces. This can include js and css libraries from&#160;CDNs, video providers such as YouTube and other 3rd party APIs.<br> </span>

<p>​Many of these services are completely blocked inside other countries. China, in particular currently blocks all the below&#58;</p><p>Facebook</p><p>Google</p><p>YouTube</p><p>Vimeo</p><p>Twitter<br></p><p>If the runtime&#160;operation of your site depends upon&#160;these services, your website will either fail or perform poorly for users in China. Start by reviewing how many of these services are essential, what they do and whether there are China-based equivalents. The fewer external dependencies in your site, the easier it will be to Chinafy.&#160;&#160;<br></p><p>Every attempted&#160;request to a blocked service can add serious delays to your site's performance as each one can take&#160;over a minute&#160;to timeout.&#160;When loading a page, browers have a limit on the number of simultaneous connections thay will open. Google&#160;Chrome, for example,&#160;will support 6 connections to one domains and 10 connections&#160;overall. If all those connections get used attempting to connect&#160;to blocked resources, the entire page&#160;loading proess can stall for minutes!<br></p><p>To measure the impact of this, you need to be able to browse the website from inside China. From there you can open&#160;the site and collect perfomance measurements from the network tab of your browser's dev tools.<br></p><p><img src="/PublishingImages/BlockedDependencies.png" alt="BlockedDependencies.png" style="margin&#58;5px;width&#58;808px;" /><br></p><p><strong>Figure&#58; Bad example&#58; This brower in China was stalled attempting to load resources from Facebook, Google anf YouTube.</strong><br></p><p>This situation can&#160;first be improved by finding and removing unneccessary dependencies.&#160;&#160;Next, ensure that all required css and JavaScript content can be loaded - by either hosting within your site&#160;or using a CDN that is available from China.<br></p><p>Finally, you may find that there are feastures you still want to use elsewhere&#160;but&#160;need to&#160;disable for users in&#160;China. For more information read&#58; Do you detect available services?&#160;<br></p><p><br></p>


