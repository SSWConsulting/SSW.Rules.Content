---
type: rule
archivedreason: 
title: Do you consider SEO in your AngularJS application?
guid: a2762f52-7604-417f-8be4-dbf1abb14a62
uri: do-you-consider-seo-in-your-angularjs-application
created: 2014-10-30T23:53:12.0000000Z
authors:
- id: 44
  title: Duncan Hunter
- id: 1
  title: Adam Cogan
related: []

---


​​​​​​​​Search Engine Optimisation (SEO) with a Single Page Application (SPA) needs consideration like any other Framework to ensure it is SEO friendly. Becuase AngularJS manages your routing and URLs it is important to be aware of the differences in making an AngularJS SPA SEO friendly.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>If you ignore your SEO in an Angular SPA you may not have your pages indexed by Google and lose your ranking with SEO. If your pages are not being rendered to Googles bots when they crawl your site, Google can not see your pages and it is like they do not exist.</p><div><p class="ssw15-rteElement-GreyBox">The only way to be sure your Angular SPA will be crawled and indexed properly by Google Bots is to intercept all their requests and serve them HTML you pre-render on the server. </p><div><div>It is not enough to just use hashes in your URLs (e.g., www.example.com/index.html#mystate, where #mystate is the hash fragment) or hope Google can crawl and Angular application correctly. <span style="line-height:20.8px;">You can read more here </span><a href="https://developers.google.com/webmasters/ajax-crawling/docs/getting-started" target="_blank">Guide to AJAX crawlin g for webmasters and developers</a>.  There are several libraries to help pre-render your code available on the internet. </div> ​ 
      <div>If you do not pre-render HTML you may still get good enough SEO as Google Bots are getting better at crawling JavaScript but you can not be certain it will work. You can use <a href="https://www.google.com/webmasters/tools/googlebot-fetch" style="line-height:20.8px;">Google Fetch</a><span style="line-height:20.8px;"> to test how your web pages look to a Google bot.</span></div><dl class="image"><dt> <img src="seo_for_angular-diagram.png" alt="seo_for_angular-diagram.png" /> </dt><dd>Figure: How to configure your site to pre-render HTML for Google bots.</dd></dl><p>Besides pre-rendering HTML to get your AngularJS Single Page Application (SPA) SEO friendly you can apply the following practices:<br></p><ol><li> 
            <b>Enable html5Mode for AngularJS outing</b><br><span style="line-height:1.6;">This will remove the </span><span style="line-height:1.6;">hashtagged-URLs</span><span style="line-height:1.6;"> by default for pretty URLS</span><span style="line-height:1.6;">, using the pushState feature that</span> <span style="line-height:1.6;">newer browsers have, which still falls back to the hashbang method if pushState isn't available.</span><span style="line-height:1.6;"> To enable html5Mode in AngularJs read more <a href="http://scotch.io/quick-tips/js/angular/pretty-urls-in-angularjs-removing-the-hashtag">scotch.io</a></span></li><li> 
            <b>Creating a sitemap</b><br>Web crawlers usually discover pages from links within the site and from other sites. Sitemaps supplement this data to allow crawlers that support Sitemaps to pick up all URLs in the Sitemap and learn about those URLs using the associated metadata. Using the Sitemap protocol does not guarantee that web pages are included in search engines, but provides hints for web crawlers to do a better job of crawling your site.  <span style="line-height:1.6;">More infor</span><span style="line-height:1.6;">mation at </span> <a href="http://www.sitemaps.org/protocol.html" style="line-height:1.6;">sitemap.org</a><span style="line-height:1.6;"> </span></li><li> 
            <b>Enriching your app with meta information</b><br>This step ensures your search results are represented in a meaningful and predictable way. Dynamically changing the meta tags content in the head section of the page can also help google find and represent you in their search results.  <br><span style="line-height:1.6;">For more information</span><span style="line-height:1.6;"> and a demo see this </span> <span style="line-height:1.6;">blog: </span><a href="https://weluse.de/blog/angularjs-seo-finally-a-piece-of-cake.html" style="line-height:1.6;">weluse.de</a><br></li><li> 
            <b>You can inspect what HTML Google renders with Webmaster Tools</b>, it is also an excellent source of information.</li><li>Here’s what you need to know to ensure your website is crawled correctly by Google in general regardless of if your application is a SPA: <a href="https://tv.ssw.com/5162/introduction-seo-google-tools-craig-bailey-firebootcamp">Introduction to SEO and Google Tools – Craig Bailey [FireBootCamp]</a><br>​​</li></ol><p>
         <b>Note:</b> Since May 2014 Google announced that they're finally crawling javascript making SEO for a SPA simpler. Previously your SPA needed to distinguish between normal users and crawlers - and re-route (somehow) to the special crawler-only-endpoints if a bot is requesting the page.(source: http://googlewebmastercentral.blogspot.de/2014/05/understanding-web-pages-better.html) <br></p></div></div>


