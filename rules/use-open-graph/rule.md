---
type: rule
archivedreason: 
title: Do you use Open Graph to control how your links are shared?
guid: 50923325-6be7-4209-b29c-0c1f6e0d7421
uri: use-open-graph
created: 2018-02-16T22:32:29.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-use-open-graph-to-control-how-your-links-are-shared

---


Open Graph is a metadata tag that&#160;allows you to control what content shows up when a page is shared on social media networks.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>It should be placed on the {ltHTMLChar}head{gtHTMLChar} section of your page. The most used properties are&#58;</p><p class="ssw15-rteElement-CodeArea">{ltHTMLChar}meta property=&quot;og&#58;title&quot; content=&quot;Your Custom Title&quot; /{gtHTMLChar}<br>{ltHTMLChar}meta property=&quot;og&#58;description&quot; content=&quot;Your custom description of the page.&quot; /{gtHTMLChar}<br>{ltHTMLChar}meta property=&quot;og&#58;image&quot; content=&quot;https&#58;//www.YourCustomImage.jpg&quot;/{gtHTMLChar}​<br></p><dl class="badImage"><dt> 
      <img src="/PublishingImages/open-graph-bad.jpg" alt="open-graph-bad.jpg" />​ </dt><dd>Figure&#58; Bad example - No image and the title was &quot;guessed&quot; by LinkedIn</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/opengraph-good.jpg" alt="opengraph-good.jpg" />
   </dt><dd>Figure&#58; Good example - Image and title defined by Open Graph tags​<br></dd></dl><p> 
   <b>Note&#58;&#160;</b>For LinkedIn you might need to&#160;add the prefix as following&#58;</p><p class="ssw15-rteElement-CodeArea">&#160;{ltHTMLChar}meta<span class="ssw15-rteStyle-Highlight"> prefix=&quot;og&#58; http&#58;//ogp.me/ns#&quot;</span> property='og&#58;title' content=&quot;Microsoft Azure | SSW Consulting - Sydney, Brisbane, Melbourne&quot;/{gtHTMLChar}​<br></p><p class="ssw15-rteElement-P">More information and other properties can be found at&#160;<a href="http&#58;//ogp.me/" target="_blank">http&#58;//ogp.me​</a><br></p>


