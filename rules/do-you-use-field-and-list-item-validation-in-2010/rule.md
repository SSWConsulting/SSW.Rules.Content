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

class CreateShoppingListHandler : SPItemEventReceiver
<br>    {
<br>        public override void ItemAdding(SPItemEventProperties properties)
<br>        {
<br>            float price = 0;
<br>            float cost = 0;

<br>            if(float.TryParse(properties.ListItem.Fields["Price"].ToString(), out price) && float.TryParse(properties.ListItem.Fields["Cost"].ToString(), out cost))
<br>            {
<br>                if(price &lt; cost)
<br>                {
<br>                    properties.ErrorMessage = "The cost must not be less than the price";
<br>                    properties.Cancel = true;
<br>                }
<br>            }            
<br>        }
<br>    }Bad example: using custom code – creating a<br>custom event receiver on the item (the item adding event or item updating<br>event)
![](ListValidation.jpg)
Good example: using no code – just using the<br>field validation on a list
 A demo of this from Andrew Connell on
http://channel9.msdn.com/learn/courses/SharePoint2010Developer/ListsAndSchemas/FieldandListItemValidation/
<!--endintro-->
