---
type: rule
archivedreason: 
title: Do you use field and list item validation (in 2010)
guid: 3d380832-e28b-46a4-bcb2-4d0b92fb866d
uri: do-you-use-field-and-list-item-validation-in-2010
created: 2009-12-10T02:23:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-field-and-list-item-validation-(in-2010)

---


  <span class="ms-rteCustom-CodeArea">    class CreateShoppingListHandler : SPItemEventReceiver<br>
    {<br>
        public override void ItemAdding(SPItemEventProperties properties)<br>
        {<br>
            float price = 0;<br>
            float cost = 0;<br>
            <br>
            if(float.TryParse(properties.ListItem.Fields["Price"].ToString(), out price) && float.TryParse(properties.ListItem.Fields["Cost"].ToString(), out cost))<br>
            {<br>
                if(price &lt; cost)<br>
                {<br>
                    properties.ErrorMessage = "The cost must not be less than the price";<br>
                    properties.Cancel = true;<br>
                }<br>
            }            <br>
        }<br>
    }</span>
<span lang="EN-AU">
</span>
<span class="ms-rteCustom-FigureBad">
<span lang="EN-AU">Bad example: using custom code – creating a
custom event receiver on the item (the item adding event or item updating
event)</span>
<span lang="EN-AU">
</span>
</span>
<span lang="EN-AU">
<br>
<img src="ListValidation.jpg" alt="" /><br>
</span>
<span class="ms-rteCustom-FigureGood">
<span lang="EN-AU">Good example: using no code – just using the
field validation on a list</span>
</span>
<br>
<style>
</style>
A demo of this from Andrew Connell on<span lang="EN-AU"><br>
<a href="http://channel9.msdn.com/learn/courses/SharePoint2010Developer/ListsAndSchemas/FieldandListItemValidation/">http://channel9.msdn.com/learn/courses/SharePoint2010Developer/ListsAndSchemas/FieldandListItemValidation/</a>
</span>

<br><excerpt class='endintro'></excerpt><br>



