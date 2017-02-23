---
type: rule
archivedreason: 
title: Controls - Do you make the selected/enabled rows stand out in a datagrid?
guid: ed08f7dd-7266-4961-9042-1023def979e6
uri: controls---do-you-make-the-selectedenabled-rows-stand-out-in-a-datagrid
created: 2012-11-27T09:19:10.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>Many times you allow a multiple selection in a grid by using a checkbox. When you do this make it easy to see the distinction of a row that is selected and one that is not. Make it subtle by dimming the unselected text.<br></p>
<br><excerpt class='endintro'></excerpt><br>
​
<dl class="badImage"><dt> <img alt="Seleted rows not standard out" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/Interface_Selected_Rows_Bad.JPG" /> </dt><dd>Figure&#58; Bad Example - Selected rows are not separate from others.</dd></dl><dl class="goodImage"><dt> <img alt="Seleted rows standard out" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/Interface_Selected_Rows_Good.JPG" /> </dt><dd>Figure&#58; Good Example - Selected rows are separate from others.</dd></dl><div>To make this effect in datagrid, you may need to edit the <strong>cellcontentclick</strong> event handler code. <br>Example&#58;</div><dl class="goodCode"><dt><p>private void DatagridviewRules_CellContentClick(object sender, DataGridViewCellEventArgs e)<br> &#123;<br> if (DatagridviewRules.Columns[e.ColumnIndex] is DataGridViewCheckBoxColumn &amp;&amp; e.ColumnIndex == 0 &amp;&amp;<br>e.RowIndex != -1)<br> &#123;<br> bool boolCheckBox = (bool)(DatagridviewRules.Rows[e.RowIndex].Cells[e.ColumnIndex].Value);<br> DatagridviewRules.Rows[e.RowIndex].DefaultCellStyle.ForeColor = boolCheckBox<br> ? SystemColors.WindowText<br> &#58; SystemColors.ControlDark;<br> DataRowView objDataRowView = (DataRowView)DatagridviewRules.Rows[e.RowIndex].DataBoundItem;<br> JobRule.DataTableJobRulesRow objDataRow = (JobRule.DataTableJobRulesRow)(objDataRowView.Row);<br> updateRuleIsEnabled(objDataRow.RuleId, boolCheckBox);<br> updateSelectAllCheckBox();<br> updateRulesCount();<br> &#125;<br> &#125;<br></p> </dt><dd>Setting the ForeColor to different ones, like black and gray, can separate the selected rows from others.</dd></dl>


