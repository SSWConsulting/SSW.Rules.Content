---
type: rule
title: Do you use dashes in your URLs?
uri: do-you-use-dashes-in-your-urls
created: 2015-11-09T20:51:46.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p><span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;16.8px;">​​​For maximum readability and SEO&#160;use kebab-case (dashes) in your URLs.&#160;​</span></p> </span>

<p class="ssw15-rteElement-GreyBox">http&#58;//northwind.com/pageonworddocumentation</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad example - No kebab-case in URL <br><br></dd><p class="ssw15-rteElement-GreyBox">http&#58;//northwind.com/PageOnWordDocumentation</p><dd class="ssw15-rteElement-FigureBad"> Fi​gure&#58; Bad example - PascalCase (better readability but&#160;still work in all small caps, so other&#160;people might share it without the MixedCase)<br><br></dd><p class="ssw15-rteElement-GreyBox">http&#58;//northwind.com/page on word documentation<br><br>...will become<br><br> http&#58;//northwind.com/page20%on20%word20%documentation</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad example - spaces it will show up in your URL structure as 20%, which is bad for readability and SEO<br><br></dd><p class="ssw15-rteElement-GreyBox">http&#58;//northwind.com/page_on_word_documentation</p><dd class="ssw15-rteElement-FigureNormal"> Figure&#58; OK​ example - underscored (snake_case)&#160;URLs&#160;have good readability but are not recommended by Google<br><br></dd><p class="ssw15-rteElement-GreyBox">http&#58;//northwind.com/page-on-word-documentation</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - kebab-case&#160;is&#160;recommended by Google<br><br></dd><p class="ssw15-rteElement-P"> 
   <b>Note&#58;&#160;</b>this is only for the pages&#160;and documents within a website -&#160;not for the domain. Domains are bad when they have &quot;-&quot; in them!<br></p><p class="ssw15-rteElement-P">Read more on&#160;<a href="https&#58;//www.seomechanic.com/seo-101-hyphens-underscores-_-urls/">SEO 101&#58; Hyphens vs. Underscores in URLs</a><br></p><h3>More info​</h3><p>You can install the IIS&#160;<a href="http&#58;//learn.iis.net/page.aspx/460/using-the-url-rewrite-module/">URL Rewrite Module</a>&#160;<img src="/Style%20Library/SSW/CoreImages/external.gif" title="You are now leaving SSW" alt="" style="margin&#58;5px;" />&#160;for IIS7 you can make ugly URL's much more friendly.</p><dl class="image"><dt><img src="/PublishingImages/friendly-url-rule.jpg" alt="Rewrite the HTML" style="margin&#58;5px;" /></dt><dd>Figure&#58; Rewrite both the HTML in the page and the incoming URL's to be friendly</dd></dl><p>The caveat here is that it will only work if the URL is in the clear on the page.</p><p class="ssw15-rteElement-P"><strong>Note&#58;&#160;</strong>This could only be done with certain links as others are postbacks as well.</p><p class="ssw15-rteElement-P">​<br></p>


