---
type: rule
archivedreason: 
title: Control Choice - Do you use Checked List Boxes instead of multi-select List Boxes?
guid: acf80273-edd5-462a-a629-b47f8a00a5aa
uri: control-choice-do-you-use-checked-list-boxes-instead-of-multi-select-list-boxes
created: 2012-11-27T08:53:22.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Multi-select listboxes are the bane of a graphical user interface, they have a number of behavioral quirks that make it difficult for users to get used to them:


* They require users to know that you select more than one item
* They lose all selections if you click in the wrong place.
* You can't tell if a Listbox is single-select or multi-select at first glance.


<!--endintro-->
<select size="8" style="width&#58;200px;"> 
         <option>Item 1</option> 
         <option>Item 2</option> 
         <option>Item 3</option> 
         <option>Item 4</option> 
         <option>Item 5</option> 
         <option>Item 6</option> 
         <option>Item 7</option> 
         <option>Item 8</option> 
         <option>Item 9</option> 
         <option>Item 10</option>
</select> 

Figure: Bad Example - List Boxes are impractical - try it and see **Checked Listboxes** are the ideal alternative. They're much more pleasant to use and are a good deal more intuitive - compare to the list above. Checked Listboxes tell users immediately that they have the ability choose multiple options.

* In ASP.NET, use 
       **System.Web.UI.WebControls.CheckBoxList** . If you're having problems with there being too many items in the list, use a 
       **scrolling DIV**
* In Windows Forms, use 
       **System.Windows.Forms.CheckedListBox**


| <input id="cblList_0" type="checkbox"><label>Item 1</label> |
| --- |
| <input id="cblList_1" type="checkbox"><label>Item 2</label> |
| <input id="cblList_2" type="checkbox"><label>Item 3</label> |
| <input id="cblList_3" type="checkbox"><label>Item 4</label> |
| <input id="cblList_4" type="checkbox"><label>Item 5</label> |
| <input id="cblList_5" type="checkbox"><label>Item 6</label> |
| <input id="cblList_6" type="checkbox"><label>Item 7</label> |
| <input id="cblList_7" type="checkbox"><label>Item 8</label> |
| <input id="cblList_8" type="checkbox"><label>Item 9</label> |
| <input id="cblList_9" type="checkbox"><label>Item 10</label> |

Figure: Good Example - The beauty of the CheckListBox in ASP.NET
We have a program called  [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/codeauditor/) to check for this rule.

* Other best practice is to remove the "size" attribute from the select tag - making it become a drop down list box

<select style="width&#58;200px;"> 
         <option>Item 1</option> 
         <option>Item 2</option> 
         <option>Item 3</option> 
         <option>Item 4</option> 
         <option>Item 5</option> 
         <option>Item 6</option> 
         <option>Item 7</option> 
         <option>Item 8</option> 
         <option>Item 9</option> 
         <option>Item 10</option>
</select> 
