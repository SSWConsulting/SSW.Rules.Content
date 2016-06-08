---
type: rule
title: Do you keep the URL next to each link on printing?
uri: do-you-keep-the-url-next-to-each-link-on-printing
created: 2016-06-08T21:04:47.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> We have a rule on&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=f19d44f5-5c5b-4cc8-905d-3f7ddb1edf58">using&#160;relevant words on&#160;links </a>. How to make sure&#160;people&#160;will know which words are links and what the links are after printing a page?<br> </span>

<p>As a good practice, you should use CSS to print the URL's next to each link&#160;when printing&#58;</p><p class="ssw15-rteElement-CodeArea">@media print &#123;<br>a[href]&#58;after &#123;<br>content&#58; &quot; (&quot; attr(href) &quot;)&quot;;<br>&#125;<br>&#125;</p>​<span style="line-height&#58;1.5em;">In specific cases, like on breadcrumbs and ​logo, you don't want these URL's, so you should overide the style&#58;</span><div><p class="ssw15-rteElement-CodeArea">@media print &#123;<br><span class="ssw15-rteStyle-Highlight">.breadcrumb </span>a[href]&#58;after &#123;<br>content&#58; <span class="ssw15-rteStyle-Highlight">none</span>;<br>&#125;<br>&#125; <br></p></div>


