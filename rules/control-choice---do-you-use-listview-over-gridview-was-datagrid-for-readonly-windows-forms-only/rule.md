---
type: rule
archivedreason: 
title: Control Choice - Do you use ListView over GridView (was DataGrid) for ReadOnly? (Windows Forms only)
guid: 6ce29e76-2f40-4d0d-8ff9-e156bcfbf5b5
uri: control-choice---do-you-use-listview-over-gridview-was-datagrid-for-readonly-windows-forms-only
created: 2012-11-27T08:50:09.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Yes a ListView looks nicer than a DataGrid, but a Datagrid is better because it has more functionality (out of the box that is). With a ListView you cannot:

* Copy and paste - although you can select a row of data in both controls, you can't copy and paste a whole row from the ListView
* Sort data - always useful when there are more than about 20 rows
* DataBind - always saves heaps of code


<!--endintro-->

So our old rule was to always use the ugly DataGrid (although we were never happy about that).
<dl class="badImage">&lt;dt&gt; <img height="526" width="534" src="../../assets/UsingDataGridWhenNotNeeded.gif" alt="DataGrid"> &lt;/dt&gt;<dd>Figure: Bad Example - The DataGrid is ugly</dd></dl><dl class="goodImage">&lt;dt&gt; <img height="526" width="534" src="../../assets/SortableListView.gif" alt="Sortable ListView"> &lt;/dt&gt;<dd>Figure: Good Example - A beautiful ListView - a nicer look over the datagrid</dd></dl>
So the listview looks nicer? If you are not convinced here is another one:
<dl class="goodImage">&lt;dt&gt; <img src="../../assets/DatagridVSListview.gif" alt="Datagrid and Listview" data-pin-nopin="true"> &lt;/dt&gt;<dd>Figure: Good Example - The appearance of DataGrid and ListView</dd></dl>
But another issue is how much code to write... For ListView you will need to write a bit of code to fill the list view...
<dl class="badCode">&lt;dt&gt;<p>this.listView1.Items.Clear(); // stops drawing to speed up the process, draw right at the end. this.listView1.BeginUpdate(); foreach(DataRow dr in this.dataSet11.Tables[0].Rows) { ListViewItem lvi = new ListViewItem(new string[] {dr[0].ToString(),dr[1].ToString(),dr[2].ToString()}); lvi.Tag = dr; this.listView1.Items.Add(lvi); } this.listView1.EndUpdate();</p>&lt;/dt&gt;<dd>Figure: 8 lines of code to fill a ListView</dd></dl>
But the datagrid is nicer to code... this is because it comes with data binding ability.
<dl class="badCode">&lt;dt&gt;<p>// bind it in the designer first. this.oleDbDataAdapter1.Fill(this.dataSet11);</p>&lt;/dt&gt;<dd>Figure: One line of code to fill a DataGrid</dd></dl>
But the SSW ListView (included in the [.NET Toolkit](http://www.ssw.com.au/ssw/NETToolkit/)) is nicer to code with as it comes with data binding ability.
<dl class="goodCode">&lt;dt&gt;<p>// bind it in the designer first. this.oleDbDataAdapter1.Fill(this.dataSet11); </p> &lt;/dt&gt;<dd>Figure: One line of code to fill the SSW ListView</dd></dl>
So what is this SSW ListView?

It is an inherited control that how we implemented the ListView to give us what MS left out.

* DataBinding
* Sorting


So now the rules are: 
Always use the SSW ListView. 
Exception: Use the DataGrid when:

* When not read only - i.e. users will be editing data directly from the cells.
* You need more than 1 column with checkboxes, or the column with checkboxes can't be the first column. E.g.: <dl class="image">&lt;dt&gt; <img src="../../assets/DataGrid2CheckBoxes.gif" alt="DataGrid"> &lt;/dt&gt;<dd>Figure: One place when you choose a DataGrid over a ListView is when you have 2 checkbox fields</dd></dl>


So in summary, if you don't want users to edit the data directly from the cell, and only the first column need checkboxes, then the ListView is always the better choice.


| We have an example of this in the [SSW .NET Toolkit](http://www.ssw.com.au/ssw/NETToolkit/). |
| --- |




| We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule. |
| --- |



Note: We have a suggestion for Microsoft to improve the [copy and paste format from a gridview](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSForm.aspx#DataGridsFormattingonCopy)
