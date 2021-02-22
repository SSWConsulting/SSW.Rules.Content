---
type: rule
archivedreason: 
title: Do you use dashes in your URLs?
guid: 9eec1cdc-ff5f-47cf-b4a6-0936ec4c62d4
uri: use-dashes-in-urls
created: 2015-11-09T20:51:46.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-use-dashes-in-your-urls

---


<p><span style="color:#000000;font-family:verdana, sans-serif;font-size:12px;line-height:16.8px;">​​​For maximum readability and SEO use kebab-case (dashes) in your URLs. ​</span></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-GreyBox">https://northwind.com/<b>pageonworddocumentation</b></p><dd class="ssw15-rteElement-FigureBad"> Figure: Bad example - No kebab-case in URL <br><br></dd><p class="ssw15-rteElement-GreyBox">https://northwind.com/<b>PageOnWordDocumentation</b></p><dd class="ssw15-rteElement-FigureBad"> Figure: Bad example - PascalCase (better readability and still works in small caps, but other people might share it without the MixedCase)<br><br></dd><p class="ssw15-rteElement-GreyBox">https://northwind.com/<b>page on word documentation</b><br><br>...will become<br><br> https://northwind.com/<b>page20%on20%word20%documentation</b></p><dd class="ssw15-rteElement-FigureBad"> Figure: Bad example - spaces it will show up in your URL structure as 20%, which is bad for readability and SEO<br><br></dd><p class="ssw15-rteElement-GreyBox">https://northwind.com/<b>page_on_word_documentation</b></p><dd class="ssw15-rteElement-FigureNormal"> Figure: OK​ example - underscored (snake_case) URLs have good readability but are not recommended by Google<br><br></dd><p class="ssw15-rteElement-GreyBox">https://northwind.com/<b>page-on-word-documentation</b></p><dd class="ssw15-rteElement-FigureGood">Figure: Good example - kebab-case is recommended by Google<br><br></dd><p class="ssw15-rteElement-P"> 
   <b>Note: </b>this is only for the pages and documents within a website - not for the domain. Domains are bad when they have "-" in them!<br></p><p class="ssw15-rteElement-P">Read more on <a href="https://www.seomechanic.com/seo-101-hyphens-underscores-_-urls/">SEO 101: Hyphens vs. Underscores in URLs</a><br></p><h3>More info​</h3><p>You can install the IIS <a href="http://learn.iis.net/page.aspx/460/using-the-url-rewrite-module/">URL Rewrite Module</a> for IIS7 you can make ugly URL's much more friendly.</p><dl class="image"><dt><img src="friendly-url-rule.jpg" alt="Rewrite the HTML" style="margin:5px;" /></dt><dd>Figure: Rewrite both the HTML in the page and the incoming URL's to be friendly</dd></dl><p>The caveat here is that it will only work if the URL is in the clear on the page.</p><p class="ssw15-rteElement-P"><strong>Note: </strong>This could only be done with certain links as others are postbacks as well.​​</p>


