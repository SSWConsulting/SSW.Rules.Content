---
type: rule
archivedreason: 
title: Do you use field and list item validation (in 2010)
guid: 3d380832-e28b-46a4-bcb2-4d0b92fb866d
uri: do-you-use-field-and-list-item-validation-in-2010
created: 2009-12-10T02:23:00.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


  <span class="ms-rteCustom-CodeArea">&#160;&#160;&#160; class CreateShoppingListHandler &#58; SPItemEventReceiver<br>
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
<img src="/PublishingImages/ListValidation.jpg" alt="" /><br>
</span>
<span class="ms-rteCustom-FigureGood">
<span lang="EN-AU">Good example&#58; using no code – just using the
field validation on a list</span>
</span>
<br>
<style>
</style>
A demo of this from Andrew Connell on<span lang="EN-AU"><br>
<a href="http&#58;//channel9.msdn.com/learn/courses/SharePoint2010Developer/ListsAndSchemas/FieldandListItemValidation/">http&#58;//channel9.msdn.com/learn/courses/SharePoint2010Developer/ListsAndSchemas/FieldandListItemValidation/</a>
</span>

<br><excerpt class='endintro'></excerpt><br>



