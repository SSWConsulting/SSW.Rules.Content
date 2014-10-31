---
type: rule
title: Do you consider SEO in your AngularJS application?
uri: do-you-consider-seo-in-your-angularjs-application
created: 2014-10-30T23:53:12.0000000Z
authors:
- id: 44
  title: Duncan Hunter
- id: 1
  title: Adam Cogan

---



<span class='intro'> ​Search Engine Optimisation (SEO)&#160;with a Single Page Application (SPA) needs consideration like any other Framework to ensure it is&#160;SEO friendly. Becuase AngularJS manages your routing and URLs it is&#160;important to be aware of the differences in making an AngularJS SPA SEO friendly.<br> </span>

<p></p><div><span style="line-height&#58;20.7999992370605px;">​​How to get your AngularJS Single Page Application (SPA) SEO friendly&#58;<br></span></div><div><span style="line-height&#58;20.7999992370605px;"><br></span></div><ol><li><span style="line-height&#58;1.6;">Enable html5Mode for AngularJS&#160;outing<br></span><span style="line-height&#58;1.6;">This will remove the&#160;</span><span style="line-height&#58;1.6;">hashtagged-URLs</span><span style="line-height&#58;1.6;"> by default for pretty URLS</span><span style="line-height&#58;1.6;">, using the pushState feature </span><span style="line-height&#58;1.6;">newer browsers have, which still falls back to the hashbang method if pushState isn't available.</span><span style="line-height&#58;1.6;">​ To enable html5Mode in AngularJs read more <a href="http&#58;//scotch.io/quick-tips/js/angular/pretty-urls-in-angularjs-removing-the-hashtag">scotch.io​</a></span><span style="line-height&#58;1.6;">.</span></li><li><span style="line-height&#58;1.6;">Creating a sitemap<br></span><span style="line-height&#58;1.6;">More infor</span><span style="line-height&#58;1.6;">mation at </span><a href="http&#58;//www.sitemaps.org/protocol.html" style="line-height&#58;1.6;">sitemap.org</a><span style="line-height&#58;1.6;">&#160;</span></li><li><span style="line-height&#58;1.6;">&#160;Enriching your app with meta informations<br></span><span style="line-height&#58;1.6;">For&#160;more information</span><span style="line-height&#58;1.6;"> and a demo see this </span><span style="line-height&#58;1.6;">blog </span><a href="https&#58;//weluse.de/blog/angularjs-seo-finally-a-piece-of-cake.html" style="line-height&#58;1.6;">weluse.de</a><span style="line-height&#58;1.6;">.</span></li></ol><div><span style="line-height&#58;20.7999992370605px;"><br></span></div><div><span style="line-height&#58;20.7999992370605px;"><span class="ssw15-rteStyle-Caption" style="font-size&#58;12px;line-height&#58;19.2000007629395px;">Note&#58; Since</span><span class="ssw15-rteStyle-Caption" style="font-size&#58;12px;line-height&#58;19.2000007629395px;">&#160;May 2014&#160;Google announced that they're finally crawling javascript making SEO for a&#160;SPA&#160;simpler. Previouisly your&#160;SPA needed to&#160;distinguish between normal users and crawlers - and re-route (somehow) to the special crawler-only-endpoints if a bot is requesting the page​.</span><span class="ssw15-rteStyle-Caption">​</span><br></span></div>


