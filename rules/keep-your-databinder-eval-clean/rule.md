---
type: rule
title: Do you keep your "DataBinder.Eval" clean?
uri: keep-your-databinder-eval-clean
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-keep-your-databinder-eval-clean
created: 2016-09-01T18:07:57.000Z
archivedreason: null
guid: 5fe6a6bd-2ff2-4db7-8a4f-cfcfa5dcd2d3
---
Remember ASP code, you had lots of inline processing. Using DataBinder.Eval encourages the same tendencies. DataBinder.Eval is OK, so is formatting a number to a currency. But not formatting based on business rules. The general rule is, any code between **&lt;%#** and **DataBinder.Eval** is bad and should be moved into protected method on the form.

Here is a good and a bad way to binding fields in ASP.NET in a datagrid.

Putting all the field binding code AND the business rule in the control:

❌ **Bad:** Business logic is in the presentation layer (.aspx file)   
❌ **Bad:** No intellisense   
❌ **Bad:** Compile errors are not picked up

<!--endintro-->

```vbnet
<asp:Label 
    id="tumorSizeLabel" 
    runat="server" 
    Text='<%# iif( Container.DataItem.Row.IsNull("TumorSize"), "N/A",DataBinder.Eval(Container, "DataItem.TumorSize", "0.00")) %>'
/>
```
::: bad
Figure: Bad code  
:::

Putting the code on the ItemDataBound Event:

✅ **Good:** Business logic is in the code behind (.vb or .cs file)  
✅ **Good:** intellisense  
❌ **Bad:** Code Bloat  
❌ **Bad:** Have to use server control for all controls (viewstate bloat)  

**In server page:**

```vbnet
<asp:Label id="tumorSizeLabel" runat="server" />
```

**In code behind:**

```vbnet
Private Sub patientDataGrid_ItemDataBound( ByVal sender As Object, ByVal e As DataGridItemEventArgs)_
Handles patientDataGrid.ItemDataBound
If( e.Item.ItemType = ListItemType.Item Or e.Item.ItemType = ListItemType.AlternatingItem) Then
Dim tumorSizeLabel As Label = e.Item.FindControl("tumorSizeLabel")
Dim rowView As DataRowView = CType(e.Item.DataItem, DataRowView)
Dim row As PatientDataSet.PatientRow = CType(rowView.Row, PatientDataSet.PatientRow)
If row.IsTumorSizeNull() Then
tumorSizeLabel.Text = "N/A"
Else
tumorSizeLabel.Text = row.TumorSize.ToString("0.00")
End If
End If
End Sub
```
::: good
Figure: Good code  
:::

We have a program called [SSW Code Auditor](https://codeauditor.com) to check for this rule.
