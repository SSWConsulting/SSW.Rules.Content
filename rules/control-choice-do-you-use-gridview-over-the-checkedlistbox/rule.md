---
seoDescription: Control choice dilemma - weighing pros and cons of using GridView over CheckedListBox in Windows Forms development.
type: rule
archivedreason:
title: Control Choice - Do you use GridView over the CheckedListBox?
guid: 4fe1955e-ea0f-47cb-a9c8-26219cb608ba
uri: control-choice-do-you-use-gridview-over-the-checkedlistbox
created: 2012-11-27T08:43:24.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

In Web we have:

* Grids E.g. <http://demos.kendoui.com/web/grid/selection.html>

In Windows Forms we have a CheckedListBox. With a CheckedListBox you cannot:

* Sort data - always useful when there are more than about 20 rows
* Contain much information - can only show one field
* DataBind - always costs heaps of code

<!--endintro-->

::: bad  
![Figure: Bad Example - The CheckedListBox is limited](/UsingCheckedListBox.gif)  
:::

::: good  
![Figure: Good Example - The DataGrid can show much more information (and if you use a 3rd Party eg. Telerik, then it can be pretty too)](/UsingDataGrid.gif)  
:::

In Windows Forms, the code of DataGrid databinding is easier than that of CheckedListBox.

ProductsService.Instance.GetAll(Me.ProductsDataSet1)
CheckedListBox1.DataSource = Me.ProductsDataSet1.Tables(0)
CheckedListBox1.ValueMember = "ProductID"
CheckedListBox1.DisplayMember = "ProductName"
For i As Integer = 0 To CheckedListBox1.Items.Count - 1
Dim checked As Boolean = CType(ProductsDataSet1.Tables(0).Rows(i)("Discontinued"), Boolean)
CheckedListBox1.SetItemChecked(i,checked)
Next
Figure: 8 lines of code to fill a CheckedListBox
ProductsService.Instance.GetAll(Me.ProductsDataSet1)
Figure: One line of code to fill a DataGrid
But the CheckedListBox is useful if only one field needs displaying.
