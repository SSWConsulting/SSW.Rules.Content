---
type: rule
title: Do you use content editor web part with care?
uri: do-you-use-content-editor-web-part-with-care
created: 2009-11-02T23:32:03.0000000Z
authors:
- id: 8
  title: John Liu

---



<span class='intro'> The Content Editor Web Part is very easy to use in any web part zone, and gives your content editors ability to add additional text and flair to a page.<br>
<img src="/PublishingImages/ContentEditorWebPart_Small.jpg" class="ms-rteCustom-ImageArea" alt="" /><span class="ms-rteCustom-FigureNormal">Figure&#58; Content Editor Web Part – available in any web part zone<br>
</span><br>
However, there is a scary hidden trap!
 </span>


  <br>
<img src="/PublishingImages/ContentEditorWebPart02_Small.jpg" class="ms-rteCustom-ImageArea" alt="" /><font class="ms-rteCustom-FigureNormal">Figure&#58; Content Editor Web Part looking mostly harmless... &#160; </font><br>
So what’s bad with the Content Editor Web Part?<br>
<ul>
    <li>The content in a content editor web part is not version controlled. </li>
    <li>If an editor accidentally overwrites a previous copy – there’s no way to go back. </li>
    <li>If an editor accidentally deletes a Content Editor Web Part – the content in it is lost. </li>
    <li>Data loss is always bad – and Content Editor Web Part gives you many different ways you can easily lose data... you need tread carefully and know the risks! </li>
</ul>
<br>
The best practice is&#58; <br>
<ol>
    <li>Do your content editing in the Content Editor Web Part, or in SharePoint Designer.</li>
    <li>Click the Source Editor button afterwards to get the&#160;raw html view. </li>
    <li>Copy and save this to a plain HTML file, and save the file in the page library (which is version controlled). </li>
    <li>In the Content Editor Web Part – link to the HTML page’s URL.<br>
    a.If the text is very tiny – may be just a big heading, you may not want to do this.<br>
    b.Using Content Link is also another way you can re-use the same text in different web pages and update them in one place – very good for big banners. </li>
</ol>
<img src="/PublishingImages/ContentEditorWebPart03_Small.jpg" class="ms-rteCustom-ImageArea" alt="" /> <font class="ms-rteCustom-FigureNormal">Figure&#58; Using Content Link to a file - safely stored in the document library. This gives us the best of both worlds </font>



