---
type: rule
title: Do you use Hyperlinks instead of JavaScript to open pages?
uri: do-you-use-hyperlinks-instead-of-javascript-to-open-pages
created: 2013-07-28T03:04:16.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> If possible you should always use hyperlinks to open new pages on your site instead of using JavaScript.<br> </span>

<p>​There are two good&#160;reasons for avoiding JavaScript-powered links&#58;</p><ol><li><span style="line-height&#58;20px;">Copying and pasting sections of the site to an email or a document&#160;will maintain the clickable links<br></span></li><li><span style="line-height&#58;20px;">There's an (ever-decreasing) chance a user won't have JavaScript enabled and won't be able to click the link</span></li></ol><div><p class="ssw15-rteElement-CodeArea">&lt;div&#160;onclick=&quot;window.open('mynewpage.html');&quot;&gt;Open&#160;a&#160;new&#160;page&lt;/div&gt;​
</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - This link can't be clicked on if you paste it into an email​ or if JavaScript is off</dd></div><div><p class="ssw15-rteElement-CodeArea">&lt;a&#160;href=&quot;mynewpage.html&quot;&gt;Open&#160;a&#160;new&#160;page&lt;/a&gt;
</p></div><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - This link can still&#160;be clicked on when pasted and when JavaScript is turned off​</dd>


