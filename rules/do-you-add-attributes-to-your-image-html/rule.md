---
type: rule
title: Do you add attributes to your image HTML?
uri: do-you-add-attributes-to-your-image-html
created: 2015-11-10T18:31:57.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>What do you do when you want images to link to your site? In the case of images, Google will look for the &quot;alt&quot; text and factor this into the search results. So when you ask someone else to link to your site with an image you should always add attributes like &quot;alt&quot; and &quot;title&quot; into the code. Here's an example.&#160;</p> </span>

<p>​<span style="line-height&#58;20.8px;">Hold the cursor over the image below and see what happens. </span></p><dl class="badImage"><dt>
      <img src="https&#58;//www.ssw.com.au/SSW/images/Raven/SSWLogo.png" data-pin-nopin="true" alt="" />
      <p class="ssw15-rteElement-CodeArea">&lt;a href=&quot;/ssw/Default.aspx&quot;&gt;<br>&#160; &#160; &#160; &lt;img src=&quot;logo.png&quot; /&gt;<br>&lt;/a&gt;</p></dt><dd>​Figure&#58; Bad example​ - No attributes to the image</dd></dl><dl class="goodImage"><dt>
      <img src="https&#58;//www.ssw.com.au/SSW/images/Raven/SSWLogo.png" data-pin-nopin="true" alt="SSW Logo" title="SSW Logo" />
      <p class="ssw15-rteElement-CodeArea">&lt;a href=&quot;/ssw/Default.aspx&quot;&gt;<br>&#160; &#160; &#160;&#160;&lt;img src=&quot;logo.png&quot; 
         <span class="ssw15-rteStyle-Highlight">alt=&quot;SSW Logo&quot;</span><span class="ssw15-rteStyle-Highlight">&#160;title=&quot;SSW Logo&quot;</span> /&gt;<br>&lt;/a&gt;</p></dt>
   <dd>​Figure&#58; Good example -&#160;Search engines will index this text. Scroll over</dd></dl>


