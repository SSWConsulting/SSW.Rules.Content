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

Many times you allow a multiple selection in a grid by using a checkbox. When you do this make it easy to see the distinction of a row that is selected and one that is not. Make it subtle by dimming the unselected text.

<!--endintro-->
<dl class="badImage">&lt;dt&gt; <img alt="Seleted rows not standard out" src="../../assets/Interface_Selected_Rows_Bad.JPG"> &lt;/dt&gt;<dd>Figure: Bad Example - Selected rows are not separate from others.</dd></dl><dl class="goodImage">&lt;dt&gt; <img alt="Seleted rows standard out" src="../../assets/Interface_Selected_Rows_Good.JPG"> &lt;/dt&gt;<dd>Figure: Good Example - Selected rows are separate from others.</dd></dl>
To make this effect in datagrid, you may need to edit the  **cellcontentclick** event handler code. 
Example:
<dl class="goodCode">&lt;dt&gt;<p>private void DatagridviewRules_CellContentClick(object sender, DataGridViewCellEventArgs e)<br> {<br> if (DatagridviewRules.Columns[e.ColumnIndex] is DataGridViewCheckBoxColumn && e.ColumnIndex == 0 &&<br>e.RowIndex != -1)<br> {<br> bool boolCheckBox = (bool)(DatagridviewRules.Rows[e.RowIndex].Cells[e.ColumnIndex].Value);<br> DatagridviewRules.Rows[e.RowIndex].DefaultCellStyle.ForeColor = boolCheckBox<br> ? SystemColors.WindowText<br> : SystemColors.ControlDark;<br> DataRowView objDataRowView = (DataRowView)DatagridviewRules.Rows[e.RowIndex].DataBoundItem;<br> JobRule.DataTableJobRulesRow objDataRow = (JobRule.DataTableJobRulesRow)(objDataRowView.Row);<br> updateRuleIsEnabled(objDataRow.RuleId, boolCheckBox);<br> updateSelectAllCheckBox();<br> updateRulesCount();<br> }<br> }<br></p> &lt;/dt&gt;<dd>Setting the ForeColor to different ones, like black and gray, can separate the selected rows from others.</dd></dl>
