---
type: rule
title: Controls - Do you make the selected/enabled rows stand out in a datagrid?
uri: controls-do-you-make-the-selected-enabled-rows-stand-out-in-a-datagrid
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2012-11-27T09:19:10.000Z
archivedreason: null
guid: ed08f7dd-7266-4961-9042-1023def979e6
---

Many times you allow a multiple selection in a grid by using a checkbox. When you do this make it easy to see the distinction of a row that is selected and one that is not. Make it subtle by dimming the unselected text.

<!--endintro-->

::: bad  
![Figure: Bad example - Selected rows are not separate from others.](../../assets/Interface\_Selected\_Rows\_Bad.JPG)  
:::

::: good  
![Figure: Good example - Selected rows are separate from others.](../../assets/Interface\_Selected\_Rows\_Good.JPG)  
:::

To make this effect in datagrid, you may need to edit the  **cellcontentclick** event handler code. 
Example:

``` cs
private void DatagridviewRules_CellContentClick(object sender, DataGridViewCellEventArgs e) {

  if (DatagridviewRules.Columns[e.ColumnIndex] is DataGridViewCheckBoxColumn && e.ColumnIndex == 0 && e.RowIndex != -1) {

    bool boolCheckBox = (bool)(DatagridviewRules.Rows[e.RowIndex].Cells[e.ColumnIndex].Value);

    DatagridviewRules.Rows[e.RowIndex].DefaultCellStyle.ForeColor = boolCheckBox ? SystemColors.WindowText : SystemColors.ControlDark;

    DataRowView objDataRowView = (DataRowView) DatagridviewRules.Rows[e.RowIndex].DataBoundItem;

    JobRule.DataTableJobRulesRow objDataRow = (JobRule.DataTableJobRulesRow)(objDataRowView.Row);

    updateRuleIsEnabled(objDataRow.RuleId, boolCheckBox);
    updateSelectAllCheckBox();
    updateRulesCount();
  }

}
```
 
Setting the ForeColor to different ones, like black and gray, can separate the selected rows from others.
