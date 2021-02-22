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


Open Graph is a metadata tag that allows you to control what content shows up when a page is shared on social media networks.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>It should be placed on the &lt;head&gt; section of your page. The most used properties are:</p><p class="ssw15-rteElement-CodeArea">&lt;meta property="og:title" content="Your Custom Title" /&gt;<br>&lt;meta property="og:description" content="Your custom description of the page." /&gt;<br>&lt;meta property="og:image" content="https://www.YourCustomImage.jpg"/&gt; <br></p><dl class="badImage"><dt> <img src="open-graph-bad.jpg" alt="open-graph-bad.jpg" /> </dt><dd>Figure: Bad example - Shared link has no image and the title was "guessed" by LinkedIn</dd></dl><dl class="goodImage"><dt> <img src="opengraph-good.jpg" alt="opengraph-good.jpg" /> </dt><dd>Figure: Good example - Shared link has a nice image and title, both defined via​ Open Graph tags <br></dd></dl><p> 
   <b>Note: </b>For LinkedIn you might need to add the prefix as following:</p><p class="ssw15-rteElement-CodeArea"> &lt;meta<span class="ssw15-rteStyle-Highlight"> prefix="og: http://ogp.me/ns#"</span> property='og:title' content="Microsoft Azure | SSW Consulting - Sydney, Brisbane, Melbourne"/&gt; <br></p><p class="ssw15-rteElement-P">More information and other properties can be found at <a href="http://ogp.me/" target="_blank">http://ogp.me </a><br></p>


