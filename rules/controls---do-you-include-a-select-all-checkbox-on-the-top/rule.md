---
type: rule
archivedreason: 
title: Controls - Do you include a "select all" checkBox on the top?
guid: 98768e5a-930e-48db-bc05-11d6fe0d7a76
uri: controls---do-you-include-a-select-all-checkbox-on-the-top
created: 2012-11-27T08:42:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>​​Do you have checkbox (on the top) that let users select or unselect all checkboxes underneath it? If you have a list of checkboxes, you are going to frustrate users unless you provide an easy way to select all. The best way to achieve this is to have a checkbox at the top.<br></p>
<br><excerpt class='endintro'></excerpt><br>
​ 
<dl class="goodImage"><dt> <img alt="Hotmail" src="../../assets/HotmailSelectAll.gif" /> </dt><dd>Figure: Good Example - Hotmail does this</dd></dl><dl class="image"><dt> <img alt="Gmail" src="../../assets/GmailSelectAll.gif" /> </dt><dd>Figure: Google have done it a different way to provide multiple methods (All, All Read, All Unread, All Starred, and All Unstarred)</dd></dl><dl class="badImage"><dt> <img alt="SQL Auditor" src="../../assets/SQLAuditorSelectAll_Bad.jpg" /> </dt><dd>Figure: Bad Example - SQL Auditor - No CheckBox for users to perform a "select all"</dd></dl><dl class="goodImage"><dt> <img alt="SQL Auditor" src="../../assets/SQLAuditorSelectAll_good.jpg" /> </dt><dd>Figure: Good Example - SQL Auditor - CheckBox at the top of the column</dd></dl><dl class="image"><dt> <a name="SelectAll_MoreDetails"></a> <img alt="SQL Auditor" src="../../assets/SQLAuditorSelectAll_All.jpg" /></dt><dd>Figure: Selecting all does this - selects all</dd></dl><dl class="image"><dt> <img alt="SQL Auditor" src="../../assets/SQLAuditorSelectAll_None.jpg" /> </dt><dd>Figure: Deselecting all does this - selects none</dd></dl><dl class="image"><dt> <img alt="SQL Auditor" src="../../assets/SQLAuditorSelectAll_Customize.jpg" /> </dt><dd>Figure: Selecting some should show the Indeterminate check state - aka customized selection</dd></dl><dl class="code"><dt><p>Private Sub CheckBoxSelectAll_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) _<br>Handles CheckBoxSelectAll.CheckedChanged<br>'Select checkbox in each row<br>For Each sDataGridViewRow As DataGridViewRow In Me.DataGridViewCustomer.Rows<br>sDataGridViewRow.Cells(0).Value = Me.CheckBoxSelectAll.Checked<br>Next<br>End Sub</p></dt><dd>Code: Code for selecting all checkboxes in a windows form</dd></dl><dl class="image"><dt> <img alt="Select all checkboxes in a web form" src="../../assets/SelectAllCheckBox_Web.jpg" /> </dt><dd>Figure: Select all checkboxes in a web form</dd></dl><dl class="code"><dt><p><script type="text/javascript"><br>function SeleteCheckBox()<br>{ <br>for (var n=0; n < document.form1.elements.length; n++) <br>{<br>if (document.form1.elements[n].type == "checkbox" && document.form1.elements[n].name == "gridview")<br>{<br>document.form1.elements[n].checked = document.getElementById("CheckBoxAll").checked; <br>}<br>}<br>} <br></script>​<br></p> </dt><dd>Code: Code for selecting all checkboxes in a web form</dd></dl><div>We have suggestions for Visual Studio .NET about this at <a href="http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSForm.aspx#SelectAllCheckWindows">A top CheckBox to "select all" in windows forms</a> and <a href="http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSAjax.aspx#SelectAllCheckWeb">A top CheckBox to "select all" in web forms.</a></div>


