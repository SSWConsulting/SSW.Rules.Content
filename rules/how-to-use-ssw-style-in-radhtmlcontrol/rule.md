---
type: rule
archivedreason: depreciated
title: How to use SSW style in RadHtmlControl?
guid: d7f9ffd2-878b-484f-8e3e-4574fb666c30
uri: how-to-use-ssw-style-in-radhtmlcontrol
created: 2010-02-02T17:36:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---



  <p>Do you know how to apply style to image, figure..etc? </p>
<p>Let's take the "AvoidReplyToAllWhenBcc" page as example. </p>

<br><excerpt class='endintro'></excerpt><br>
First, the reason to cause the style issue is the style doesn’t apply to right place. Below is the html code after you adjust the figure manually (sorry, still not right ). Please look at the highlight part, <br>
<ul>
    <li>the “ms-rteCustom-ImageArea” style doesn’t apply to &lt;img&gt; tag, but wrapped by &lt;span&gt; with “ms-rteCustom-ImageArea” style;   </li>
</ul>
<ul>
    <li>there is no style apply to figure; </li>
</ul>
<p><font class="ms-rteCustom-CodeArea" size="+0">&lt;span class="ms-rteCustom-YellowBorderBox"&gt;We have a program called &lt;a href="<a shape="rect" href="/WebSites/RulesToBetterWebsitesLayout">http://rules.ssw.com.au/WebSites/RulesToBetterWebsitesLayout</a>"&gt;<br>
        SSW LookOut! for Outlook&lt;/a&gt; to check for this rule.<br>
        &lt;br /&gt;<br>
        &lt;br /&gt;<br>
       <font class="ms-rteCustom-Highlight" size="+0">&lt;span class="ms-rteCustom-ImageArea"&gt;<br>
</font>            &lt;img style="border-bottom: 0px solid; border-left: 0px solid; border-top: 0px solid;<br>
                border-right: 0px solid;" border="0" alt="Lookout Reply All BCC Warning" src="<a shape="rect" href="/WebSites/RulesToBetterWebsitesLayout">http://rules.ssw.com.au/WebSites/RulesToBetterWebsitesLayout</a>" /&gt;<br>
            &lt;br /&gt;<br>
       <font class="ms-rteCustom-Highlight" size="+0">&lt;/span&gt;</font>&lt;b&gt;<br>
            &lt;br /&gt;<br>
            Figure: SSW LookOut! for Outlook warns you if you accidentally 'Reply All' when<br>
            you have been BCC'ed  &lt;/b&gt; &lt;/span&gt;</font><br>
1.  Not sure how user inputs the  content into this page. Anyway, here is the right way to add content via Telerik Editor. Please read below example of how I redo this part in Telerik Editor without changing the code manually<br>
<img width="551" height="160" class="ms-rteCustom-ImageArea" alt="Copy content in notepad" src="SaveContentInNotePad.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure:Copy content in the notepad</font>2. Delete the current content from Telerik for a new start;<br>
<br>
3. Copy the first sentence from notepad and paste into Telerik Editor in the page; (please avoid copying straightly from web page and pasting them here, it will copy the all tags as well. it might affect the styles which can’t apply correctly )<br>
<img width="560" height="345" alt="Start copying content over" src="CopyFromNotePad.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Start copying content over</font>4. Insert the image<br>
<img width="608" height="378" class="ms-rteCustom-ImageArea" style="width:586px;height:356px;" alt="Insert an image" src="InsertImage.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Add a link to text</font>5. Add an image<br>
<img width="582" height="344" alt="Insert an image" src="ApplyStyleInsertImage.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Inser an image</font>6. Press “enter” key to start a new row, then copy the figure from notepad to the Telerik editor area<br>
<img width="412" height="336" class="ms-rteCustom-ImageArea" alt="Add figure" src="ApplyStyleAddFigure.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Add figure</font>7. Apply image style to the image by click on the image, then choose a style from “Apply CSS Class” dropdown list<br>
<img width="526" height="269" class="ms-rteCustom-ImageArea" alt="Apply style to the image" src="ApplyStyleImageArea.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Apply style to the image<br>
</font><br>
8. Apply style to the figure<br>
<img width="512" height="225" class="ms-rteCustom-ImageArea" alt="Apply style to the image" src="ApplyStyleImageArea.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Apply style to the figure</font>9.Apply the yellow box<br>
<img width="462" height="143" class="ms-rteCustom-ImageArea" alt="Apply style to the figure" src="ApplyStyleFigure.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Apply yellow border box to the content</font>10. Check in the changes, then you will have - "dada.."<br>
<img width="511" height="176" class="ms-rteCustom-ImageArea" alt="Right stlye in use" src="ApplyStyleResult.jpg" /><br>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure: Right style in use</font></p>



