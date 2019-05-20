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



<span class='intro'> <p>​​​In China, these&#160;changes are quite noticeable. The page load time can change from 8 seconds to 1 second.<br>​<br></p> </span>

<strong style="color&#58;#333333;">What is a CDN?</strong><br>CDN&#160;is short for the content delivery network. A content delivery network (CDN) is a system of distributed servers (network) that deliver pages and other Web content to a user, based on the geographic locations of the user, the origin of the webpage and the content delivery server.<br><strong style="color&#58;#333333;">Why use a CDN in China?</strong><br>There are firewalls in China, which causes some external resources being blocked, and some JS packages having no servers in China, so they will load very slowly.​<br><strong style="color&#58;#333333;">Which CDNs work well from China?</strong><br>1.http&#58;//www.staticfile.org/<br>2.http&#58;//www.bootcdn.cn/<br>3.http&#58;//cdn.code.baidu.com/<br>4.http&#58;//lib.sinaapp.com/<br>5.http&#58;//cdnjs.net/<br><strong style="color&#58;#333333;">Which ones do not work well from China?</strong><br>1.https&#58;//maxcdn.bootstrapcdn.com<br>2.https&#58;//ajax.googleapis.com<br><p>3.https&#58;//cdnjs.cloudflare.com ​<br></p>​<br>https&#58;//cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js<br>https&#58;//maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js<br>https&#58;//ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js<dd class="ssw15-rteElement-FigureBad">Figure&#58; bad example&#58; CloudFlare &#160; MaxCDN&#160; &#160;&#160;<br></dd><br>https&#58;//libs.cdnjs.net/popper.js/1.14.0/umd/popper.min.js<br>https&#58;//libs.cdnjs.net/twitter-bootstrap/4.1.0/js/bootstrap.min.js<br>https&#58;//libs.cdnjs.net/jquery/3.3.1/jquery.min.js<br><dd class="ssw15-rteElement-FigureGood">F​igure&#58; good example&#58; CDNJS​</dd><br><p>​</p>


