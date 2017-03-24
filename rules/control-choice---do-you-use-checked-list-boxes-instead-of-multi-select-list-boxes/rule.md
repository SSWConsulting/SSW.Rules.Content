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


<div>Multi-select listboxes are the bane of a graphical user interface, they have a number of behavioral quirks that make it difficult for users to get used to them&#58;<br></div>
<ul><li>They require users to know that you select more than one entry by holding down the Ctrl key</li>
<li>They lose all selections if you click in the wrong place.</li>
<li>You can't tell if a Listbox is single-select or multi-select at first glance.</li></ul>

<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
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
         <option>Item 10</option></select> </dt><dd>Figure&#58; Bad Example - List Boxes are impractical - try it and see</dd></dl><p>
   <strong>Checked Listboxes</strong> are the ideal alternative. They're much more pleasant to use and are a good deal more intuitive - compare to the list above. Checked Listboxes tell users immediately that they have the ability choose multiple options.</p><ul><li>In ASP.NET, use 
      <strong>System.Web.UI.WebControls.CheckBoxList</strong>. If you're having problems with there being too many items in the list, use a 
      <strong>scrolling DIV</strong></li><li>In Windows Forms, use 
      <strong>System.Windows.Forms.CheckedListBox</strong></li></ul><dl class="goodImage"><dt><div style="border&#58;1px inset #aaaaaa;width&#58;200px;"><table id="cblList" border="0"><tbody><tr><td>
                     <input id="cblList_0" type="checkbox" />
                     <label>Item 1</label></td></tr><tr><td>
                     <input id="cblList_1" type="checkbox" />
                     <label>Item 2</label></td></tr><tr><td>
                     <input id="cblList_2" type="checkbox" />
                     <label>Item 3</label></td></tr><tr><td>
                     <input id="cblList_3" type="checkbox" />
                     <label>Item 4</label></td></tr><tr><td>
                     <input id="cblList_4" type="checkbox" />
                     <label>Item 5</label></td></tr><tr><td>
                     <input id="cblList_5" type="checkbox" />
                     <label>Item 6</label></td></tr><tr><td>
                     <input id="cblList_6" type="checkbox" />
                     <label>Item 7</label></td></tr><tr><td>
                     <input id="cblList_7" type="checkbox" />
                     <label>Item 8</label></td></tr><tr><td>
                     <input id="cblList_8" type="checkbox" />
                     <label>Item 9</label></td></tr><tr><td>
                     <input id="cblList_9" type="checkbox" />
                     <label>Item 10</label></td></tr></tbody></table></div></dt><dd>Figure&#58; Good Example - The beauty of the CheckListBox in ASP.NET</dd></dl><p class="ssw15-rteElement-YellowBorderBox"> We have a program called 
<a href="https&#58;//www.ssw.com.au/ssw/codeauditor/">SSW Code Auditor</a> to check for this rule.​​​<br></p>


