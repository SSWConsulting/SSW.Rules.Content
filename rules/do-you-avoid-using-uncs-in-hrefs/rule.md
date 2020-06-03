---
type: rule
title: Do you avoid using UNCs in HREFs?
uri: do-you-avoid-using-uncs-in-hrefs
created: 2016-08-26T17:56:17.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Initially, errors of this nature would be picked up in the link checking utility. However, that is not the case because the link checker will not report any problems if you run it locally - which is the normal method. The reason it won't see the problems&#160;is because the link checking utility does not check hard coded links to local servers (e.g. http&#58;//localserver/ssw/Default.aspx). Therefore, it is testing a page that will exist internally, but the page will not exist when uploaded to the web (eg.<a href="https&#58;//www.ssw.com.au/ssw/Redirect/ssw/sswhome.htm">http&#58;//www.ssw.com.au/ssw/Default.aspx</a>). <br> </span>

<dd class="ssw15-rteElement-FigureBad">​​Bad Example&#58; &lt;a href=&quot;//ant/ssw/LookOut.htm&quot;&gt;<br></dd><dd class="ssw15-rteElement-FigureGood"><strong>Good Example&#58;&#160;&lt;a href=&quot;/ssw/LookOut.htm&quot;&gt; </strong><br></dd>


