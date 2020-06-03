---
type: rule
title: Do you keep your "DataBinder.Eval" clean?
uri: do-you-keep-your-databindereval-clean
created: 2016-09-01T18:07:57.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Remember ASP code, you had lots of inline processing. Using DataBinder.Eval encourages the same tendencies. DataBinder.Eval is OK, so is formatting a number to a currency. But not formatting based on business rules. The general rule is, any code between&#160;<b>&lt;%#</b>&#160;and&#160;<strong>DataBinder.Eval</strong>&#160;is bad and should be moved into protected method on the form.</p><p style="text-align&#58;left;">Here is a good and a bad way to binding fields in ASP.NET in a datagrid.<br><br>Putting all the field binding code AND the business rule in the</p><p style="text-align&#58;left;"> control<br></p><ul><li><b>Bad&#58; </b>Business logic is in the presentation layer (.aspx file)<br></li><li><b>Bad&#58;</b> No intellisense</li><li><b>Bad&#58;</b> Compile errors are not picked up&#160;<br></li></ul> </span>

<p>​​<br></p><p class="ssw15-rteElement-CodeArea">&lt;asp&#58;Label id=&quot;tumorSizeLabel&quot; runat=&quot;server&quot; Text='&lt;%# iif( Container.DataItem.Row.IsNull(&quot;TumorSize&quot;), &quot;N/A&quot;,DataBinder.Eval(Container, &quot;DataItem.TumorSize&quot;, &quot;0.00&quot;)) %&gt;'/&gt;</p><dd class="ssw15-rteElement-FigureBad"> Bad code​​ </dd><p class="ssw15-rteElement-P">​​Putting the code on the ItemDataBound Event.</p><ul><li>
      <b>Good&#58;</b> Business logic is in the code behind (.vb or .cs file)</li><li>
      <b>Good</b><b>&#58;</b> intellisense</li><li>
      <b>Bad&#58;</b> Code Bloat</li><li>
      <b>Bad&#58;</b> Have to use server control for all controls (viewstate bloat)</li></ul><p> 
   <strong>In server page&#58;</strong>&#160;</p><p class="ssw15-rteElement-CodeArea">​​&lt;asp&#58;Label id=&quot;tumorSizeLabel&quot; runat=&quot;server&quot; /&gt;&#160;</p><p>
   <strong>In code behind&#58;</strong></p><p class="ssw15-rteElement-CodeArea">Private Sub patientDataGrid_ItemDataBound( ByVal sender As Object, ByVal e As DataGridItemEventArgs)_<br>Handles patientDataGrid.ItemDataBound<br>If( e.Item.ItemType = ListItemType.Item Or e.Item.ItemType = ListItemType.AlternatingItem) Then<br>Dim tumorSizeLabel As Label = e.Item.FindControl(&quot;tumorSizeLabel&quot;)<br>Dim rowView As DataRowView = CType(e.Item.DataItem, DataRowView)<br>Dim row As PatientDataSet.PatientRow = CType(rowView.Row, PatientDataSet.PatientRow)<br>If row.IsTumorSizeNull() Then<br>tumorSizeLabel.Text = &quot;N/A&quot;<br>Else<br>tumorSizeLabel.Text = row.TumorSize.ToString(&quot;0.00&quot;)<br>End If<br>End If<br>End Sub</p><dd class="ssw15-rteElement-FigureGood">
Good code​​
</dd><p class="ssw15-rteElement-YellowBorderBox">​​We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.​​​<br></p>​<br>


