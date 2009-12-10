---
type: rule
title: Do you use field and list item validation (in 2010)
uri: do-you-use-field-and-list-item-validation-in-2010
created: 2009-12-10T02:23:00.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'>   <span class="ms-rteCustom-CodeArea">&#160;&#160;&#160; class CreateShoppingListHandler &#58; SPItemEventReceiver<br>
&#160;&#160;&#160; &#123;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160; public override void ItemAdding(SPItemEventProperties properties)<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; float price = 0;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; float cost = 0;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; if(float.TryParse(properties.ListItem.Fields[&quot;Price&quot;].ToString(), out price) &amp;&amp; float.TryParse(properties.ListItem.Fields[&quot;Cost&quot;].ToString(), out cost))<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; if(price &lt; cost)<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; properties.ErrorMessage = &quot;The cost must not be less than the price&quot;;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; properties.Cancel = true;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;<br>
&#160;&#160;&#160; &#125;</span>
<span lang="EN-AU">
</span>
<span class="ms-rteCustom-FigureBad">
<span lang="EN-AU">Bad example&#58; using custom code – creating a
custom event receiver on the item (the item adding event or item updating
event)</span>
<span lang="EN-AU">
</span>
</span>
<span lang="EN-AU">
<br>
<img width="833" height="201" src="/Standards/SoftwareDevelopment/RulesToBetterSharePoint/PublishingImages/ListValidation.jpg" /><br>
</span>
<span class="ms-rteCustom-FigureGood">
<span lang="EN-AU">Good example&#58; using no code – just using the
field validation on a list</span>
</span>
<br>
<style>
p.MsoNormal, li.MsoNormal, div.MsoNormal {
margin:0cm;
margin-bottom:.0001pt;
font-size:11.0pt;
font-family:'Calibri','sans-serif';
}

a:link, span.MsoHyperlink {
color:blue;
text-decoration:underline;
}

span.MsoHyperlinkFollowed {
color:purple;
text-decoration:underline;
}

.MsoChpDefault {
font-size:10.0pt;
}

div.Section1 {
}
</style>
A demo of this from Andrew Connell on<span lang="EN-AU"><br>
<a href="http&#58;//channel9.msdn.com/learn/courses/SharePoint2010Developer/ListsAndSchemas/FieldandListItemValidation/">http&#58;//channel9.msdn.com/learn/courses/SharePoint2010Developer/ListsAndSchemas/FieldandListItemValidation/</a>
</span>
 </span>




