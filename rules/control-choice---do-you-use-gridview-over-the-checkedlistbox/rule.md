---
type: rule
archivedreason: 
title: Control Choice - Do you use GridView over the CheckedListBox?
guid: 4fe1955e-ea0f-47cb-a9c8-26219cb608ba
uri: control-choice---do-you-use-gridview-over-the-checkedlistbox
created: 2012-11-27T08:43:24.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<div>In Web we have:<br></div>
<ul><li>Grids E.g. <a href="http://demos.kendoui.com/web/grid/selection.html">http://demos.kendoui.com/web/grid/selection.html</a> <img title="You are now leaving SSW" src="../../assets/external.gif" alt="" /></li></ul>
<div>In Windows Forms we have a CheckedListBox. With a CheckedListBox you cannot:</div>
<ul><li>Sort data - always useful when there are more than about 20 rows</li>
<li>Contain much information - can only show one field</li>
<li>DataBind - always costs heaps of code</li></ul>
<br><excerpt class='endintro'></excerpt><br>
​​
<dl class="badImage"><dt> <img alt="CheckedListBox" src="../../assets/UsingCheckedListBox.gif" /> </dt><dd>Figure: Bad Example - The CheckedListBox is limited</dd></dl><dl class="goodImage"><dt> <img alt="DataGrid" src="../../assets/UsingDataGrid.gif" width="601" height="506" /> </dt><dd>Figure: Good Example - The DataGrid can show much more information (and if you use a 3rd Party eg. Telerik, then it can be pretty too)</dd></dl><div>In Windows Forms, the code of DataGrid databinding is easier than that of CheckedListBox.</div><dl class="badCode"><dt><p>ProductsService.Instance.GetAll(Me.ProductsDataSet1)<br>CheckedListBox1.DataSource = Me.ProductsDataSet1.Tables(0)<br>CheckedListBox1.ValueMember = "ProductID"<br>CheckedListBox1.DisplayMember = "ProductName"<br>For i As Integer = 0 To CheckedListBox1.Items.Count - 1<br>Dim checked As Boolean = CType(ProductsDataSet1.Tables(0).Rows(i)("Discontinued"), Boolean)<br>CheckedListBox1.SetItemChecked(i,checked)<br>Next ​<br></p></dt><dd>Figure: 8 lines of code to fill a CheckedListBox</dd></dl><dl class="goodCode"><dt><p>ProductsService.Instance.GetAll(Me.ProductsDataSet1)</p></dt><dd>Figure: One line of code to fill a DataGrid</dd></dl><div>But the CheckedListBox is useful if only one field needs displaying.</div>


