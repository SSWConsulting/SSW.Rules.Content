---
type: rule
archivedreason: 
title: Control Choice - Do you use Checked List Boxes instead of multi-select List Boxes?
guid: acf80273-edd5-462a-a629-b47f8a00a5aa
uri: control-choice---do-you-use-checked-list-boxes-instead-of-multi-select-list-boxes
created: 2012-11-27T08:53:22.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Multi-select listboxes are the bane of a graphical user interface, they have a number of behavioral quirks that make it difficult for users to get used to them:


* They require users to know that you select more than one entry by holding down the Ctrl key
* They lose all selections if you click in the wrong place.
* You can't tell if a Listbox is single-select or multi-select at first glance.


<!--endintro-->
<dl class="badImage">&lt;dt&gt;
      <select size="8" style="width&#58;200px;"> 
         &lt;option&gt;Item 1&lt;/option&gt; 
         &lt;option&gt;Item 2&lt;/option&gt; 
         &lt;option&gt;Item 3&lt;/option&gt; 
         &lt;option&gt;Item 4&lt;/option&gt; 
         &lt;option&gt;Item 5&lt;/option&gt; 
         &lt;option&gt;Item 6&lt;/option&gt; 
         &lt;option&gt;Item 7&lt;/option&gt; 
         &lt;option&gt;Item 8&lt;/option&gt; 
         &lt;option&gt;Item 9&lt;/option&gt; 
         &lt;option&gt;Item 10&lt;/option&gt;</select> &lt;/dt&gt;<dd>Figure&#58; Bad Example - List Boxes are impractical - try it and see</dd></dl>
**Checked Listboxes** are the ideal alternative. They're much more pleasant to use and are a good deal more intuitive - compare to the list above. Checked Listboxes tell users immediately that they have the ability choose multiple options.

* In ASP.NET, use <br>       **System.Web.UI.WebControls.CheckBoxList** . If you're having problems with there being too many items in the list, use a <br>       **scrolling DIV**
* In Windows Forms, use <br>       **System.Windows.Forms.CheckedListBox**

<dl class="goodImage">&lt;dt&gt;<div style="border&#58;1px inset #aaaaaa;width&#58;200px;"><table id="cblList" border="0"><tbody><tr><td>
                     <input id="cblList_0" type="checkbox">
                     &lt;label&gt;Item 1&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_1" type="checkbox">
                     &lt;label&gt;Item 2&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_2" type="checkbox">
                     &lt;label&gt;Item 3&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_3" type="checkbox">
                     &lt;label&gt;Item 4&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_4" type="checkbox">
                     &lt;label&gt;Item 5&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_5" type="checkbox">
                     &lt;label&gt;Item 6&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_6" type="checkbox">
                     &lt;label&gt;Item 7&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_7" type="checkbox">
                     &lt;label&gt;Item 8&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_8" type="checkbox">
                     &lt;label&gt;Item 9&lt;/label&gt;</td></tr><tr><td>
                     <input id="cblList_9" type="checkbox">
                     &lt;label&gt;Item 10&lt;/label&gt;</td></tr></tbody></table></div>&lt;/dt&gt;<dd>Figure&#58; Good Example - The beauty of the CheckListBox in ASP.NET</dd></dl>
We have a program called  [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/codeauditor/) to check for this rule.
