---
type: rule
title: How to use SSW style in RadHtmlControl?
uri: how-to-use-ssw-style-in-radhtmlcontrol
created: 2010-02-02T17:36:43.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> 
  <p>Do you know how to apply style to image, figure..etc? </p>
<p>Let's take the &quot;AvoidReplyToAllWhenBcc&quot; page as example. </p>
 </span>

First, the reason to cause the style issue is the style doesn’t apply to right place. Below is the html code after you adjust the figure manually (sorry, still not right ). Please look at the highlight part,&#160;<br>
<ul>
    <li>the “ms-rteCustom-ImageArea” style doesn’t apply to &lt;img&gt; tag, but wrapped by &lt;span&gt; with “ms-rteCustom-ImageArea” style;&#160;&#160; </li>
</ul>
<ul>
    <li>there is no style apply to figure; </li>
</ul>
<p><font class="ms-rteCustom-CodeArea" size="+0">&lt;span class=&quot;ms-rteCustom-YellowBorderBox&quot;&gt;We have a program called &lt;a href=&quot;<a shape="rect" href="/WebSites/RulesToBetterWebsitesLayout">http&#58;//rules.ssw.com.au/WebSites/RulesToBetterWebsitesLayout</a>&quot;&gt;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160; SSW LookOut! for Outlook&lt;/a&gt; to check for this rule.<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;br /&gt;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;br /&gt;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;<font class="ms-rteCustom-Highlight" size="+0">&lt;span class=&quot;ms-rteCustom-ImageArea&quot;&gt;<br>
</font>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;img style=&quot;border-bottom&#58; 0px solid; border-left&#58; 0px solid; border-top&#58; 0px solid;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; border-right&#58; 0px solid;&quot; border=&quot;0&quot; alt=&quot;Lookout Reply All BCC Warning&quot; src=&quot;<a shape="rect" href="/WebSites/RulesToBetterWebsitesLayout">http&#58;//rules.ssw.com.au/WebSites/RulesToBetterWebsitesLayout</a>&quot; /&gt;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;br /&gt;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;<font class="ms-rteCustom-Highlight" size="+0">&lt;/span&gt;</font>&lt;b&gt;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;br /&gt;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Figure&#58; SSW LookOut! for Outlook warns you if you accidentally 'Reply All' when<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; you have been BCC'ed&#160; &lt;/b&gt; &lt;/span&gt;</font><br>
1.&#160;&#160;Not sure how user inputs the&#160; content into this page. Anyway, here is the right way to add content via Telerik Editor. Please read below example of how I redo this part in Telerik Editor without changing the code manually<br>
<img width="551" height="160" class="ms-rteCustom-ImageArea" alt="Copy content in notepad" src="/PublishingImages/SaveContentInNotePad.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58;Copy content in the notepad</font>2.&#160;Delete the current content from Telerik for a new start;<br>
<br>
3.&#160;Copy the first sentence from notepad and paste into Telerik Editor in the page; (please avoid copying straightly from web page and pasting them here, it will copy the all tags as well. it might affect the styles which can’t apply correctly )<br>
<img width="560" height="345" alt="Start copying content over" src="/PublishingImages/CopyFromNotePad.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Start copying content over</font>4. Insert the image<br>
<img width="608" height="378" class="ms-rteCustom-ImageArea" style="width&#58;586px;height&#58;356px;" alt="Insert an image" src="/PublishingImages/InsertImage.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58;&#160;Add a link to text</font>5. Add an image<br>
<img width="582" height="344" alt="Insert an image" src="/PublishingImages/ApplyStyleInsertImage.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Inser an image</font>6.&#160;Press “enter” key to start a new row, then copy the figure from notepad to the Telerik editor area<br>
<img width="412" height="336" class="ms-rteCustom-ImageArea" alt="Add figure" src="/PublishingImages/ApplyStyleAddFigure.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Add figure</font>7.&#160;Apply image style to the image by click on the image, then choose a style from “Apply CSS Class” dropdown list<br>
<img width="526" height="269" class="ms-rteCustom-ImageArea" alt="Apply style to the image" src="/PublishingImages/ApplyStyleImageArea.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Apply style to the image<br>
</font><br>
8. Apply style to the figure<br>
<img width="512" height="225" class="ms-rteCustom-ImageArea" alt="Apply style to the image" src="/PublishingImages/ApplyStyleImageArea.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Apply style to the figure</font>9.Apply the yellow box<br>
<img width="462" height="143" class="ms-rteCustom-ImageArea" alt="Apply style to the figure" src="/PublishingImages/ApplyStyleFigure.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Apply yellow border box to the content</font>10. Check in the changes, then you will have - &quot;dada..&quot;<br>
<img width="511" height="176" class="ms-rteCustom-ImageArea" alt="Right stlye in use" src="/PublishingImages/ApplyStyleResult.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Right style in use</font></p>



