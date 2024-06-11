---
seoDescription: Use a ListView over a GridView (was DataGrid) for read-only data display in Windows Forms applications to achieve a nicer look and improved functionality.
type: rule
archivedreason:
title: Control Choice - Do you use ListView over GridView (was DataGrid) for ReadOnly? (Windows Forms only)
guid: 6ce29e76-2f40-4d0d-8ff9-e156bcfbf5b5
uri: control-choice-do-you-use-listview-over-gridview-was-datagrid-for-readonly-windows-forms-only
created: 2012-11-27T08:50:09.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - control-choice-do-you-use-listview-over-gridview-(was-datagrid)-for-readonly-(windows-forms-only)
---

Yes a ListView looks nicer than a DataGrid, but a Datagrid is better because it has more functionality (out of the box that is). With a ListView you cannot:

- Copy and paste - although you can select a row of data in both controls, you can't copy and paste a whole row from the ListView
- Sort data - always useful when there are more than about 20 rows
- DataBind - always saves heaps of code

<!--endintro-->

So our old rule was to always use the ugly DataGrid (although we were never happy about that).

::: bad  
![Figure: Bad Example - The DataGrid is ugly](../../assets/UsingDataGridWhenNotNeeded.gif)  
:::

::: good  
![Figure: Good Example - A beautiful ListView - a nicer look over the datagrid](../../assets/SortableListView.gif)  
:::

So the listview looks nicer? If you are not convinced here is another one:

::: good  
![Figure: Good Example - The appearance of DataGrid and ListView](../../assets/DatagridVSListview.gif)  
:::

But another issue is how much code to write... For ListView you will need to write a bit of code to fill the list view...

this.listView1.Items.Clear(); // stops drawing to speed up the process, draw right at the end. this.listView1.BeginUpdate(); foreach(DataRow dr in this.dataSet11.Tables[0].Rows) { ListViewItem lvi = new ListViewItem(new string[] {dr[0].ToString(),dr[1].ToString(),dr[2].ToString()}); lvi.Tag = dr; this.listView1.Items.Add(lvi); } this.listView1.EndUpdate();
Figure: 8 lines of code to fill a ListView
But the datagrid is nicer to code... this is because it comes with data binding ability.

// bind it in the designer first. this.oleDbDataAdapter1.Fill(this.dataSet11);
Figure: One line of code to fill a DataGrid
But the SSW ListView (included in the [.NET Toolkit](http://www.ssw.com.au/ssw/NETToolkit/)) is nicer to code with as it comes with data binding ability.

// bind it in the designer first. this.oleDbDataAdapter1.Fill(this.dataSet11);
Figure: One line of code to fill the SSW ListView
So what is this SSW ListView?

It is an inherited control that how we implemented the ListView to give us what MS left out.

- DataBinding
- Sorting

So now the rules are:
Always use the SSW ListView.
Exception: Use the DataGrid when:

- When not read only - i.e. users will be editing data directly from the cells.
- You need more than 1 column with checkboxes, or the column with checkboxes can't be the first column. E.g.:
  ![Figure: One place when you choose a DataGrid over a ListView is when you have 2 checkbox fields](../../assets/DataGrid2CheckBoxes.gif)

So in summary, if you don't want users to edit the data directly from the cell, and only the first column need checkboxes, then the ListView is always the better choice.

| We have an example of this in the [SSW .NET Toolkit](http://www.ssw.com.au/ssw/NETToolkit/). |
| -------------------------------------------------------------------------------------------- |

| We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/) to check for this rule. |
| ----------------------------------------------------------------------------------------------------------- |

Note: We have a suggestion for Microsoft to improve the [copy and paste format from a gridview](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSForm.aspx#DataGridsFormattingonCopy)
