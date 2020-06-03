---
type: rule
title: HTML - Do you use absolute paths for newsletter links and images?
uri: html---do-you-use-absolute-paths-for-newsletter-links-and-images
created: 2018-06-07T21:48:16.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> Newsletters should always use&#160;<b>absolute</b> references to all&#160;links and images within the HTML. Relative paths don't contain the server information so&#160;users see a broken link/image - the&#160;outside email application won't find the&#160;where the file is.<br> </span>

<p class="ssw15-rteElement-CodeArea">&lt;a href=&quot;/ssw/Company/ContactUs.aspx &quot;&gt;&lt;img src=&quot;/SSW/images/SSWLogo.png&quot;&gt;&lt;/a&gt;<br></p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad example - using relative paths for both link and image on a&#160;newsletter<br></dd><p class="ssw15-rteElement-CodeArea">&lt;a href=&quot;<span class="ssw15-rteStyle-Highlight">https&#58;//ssw.com.au​</span>/ssw/Company/ContactUs.aspx &quot;&gt;&lt;img src=&quot;<span class="ssw15-rteStyle-Highlight">https&#58;//ssw.com.au</span>/SSW/images/SSWLogo.png&quot;&gt;&lt;/a&gt;</p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example - using absolute paths for both&#160;link and image&#160;on a newsletter<br></dd><p>​<br></p>


