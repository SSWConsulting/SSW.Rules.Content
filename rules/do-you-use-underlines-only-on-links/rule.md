---
type: rule
archivedreason: 
title: Do you use underlines on links?
guid: b55df040-7424-48e4-b19b-14d4bcdcfbc7
uri: do-you-use-underlines-only-on-links
created: 2015-02-16T01:26:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Rebecca Liu
  url: https://ssw.com.au/people/rebecca-liu
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-use-underlines-on-links

---


<p>Users expect&#160;underlined texts to be a hyperlink. You should visually differentiate links by underlining them. Of course, this&#160;is <b>not</b> necessary on menus, obvious links,​&#160;or buttons.&#160;Never underline a text that isn't a link - Use bold or italics if you need&#160;emphasis.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img alt="Websites - Underline no hyperlink" src="http&#58;//www.ssw.com.au/SSW/Standards/Rules/Images/Websites_UnderlineNoHyperlink.gif" data-pin-nopin="true" style="width&#58;377px;" /> 
   </dt><dd>Figure&#58; Never underline the text when it isn't a link (even 
      <a target="_blank" href="https&#58;//weblogs.asp.net/scottgu/28748">Scott Guthrie agrees</a>!)<br></dd></dl><p>The default implementation of underlines in CSS is &quot;<b>text-decoration&#58;underline;</b>&quot;.<br></p><p>Another way to add look-alike underlines is by adding &quot;<b>border-bottom&#58; 1px solid #000;</b>&quot;. In this case, you can even&#160;have a dotted underline. However, it's not recommended you use this method unless you are a designer and know what you are doing. It creates extra pixels in the interface, which can potentially cause other problems in your UI, for example&#58;</p><dl class="badImage"><dt><img src="/PublishingImages/border-problem-1.gif" alt="border-problem-1.gif" style="width&#58;600px;height&#58;231px;" /></dt><dd>Figure&#58; Bad example - the different border size pushes the content down</dd></dl><dl class="badImage"><dt><img src="/PublishingImages/border-problem-2.png" alt="border-problem-2.png" style="width&#58;600px;height&#58;146px;" /></dt><dd>Figure&#58; Bad example - borders going over the text area​<br></dd></dl>


