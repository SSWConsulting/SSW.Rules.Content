---
seoDescription: Improve user experience by adding a top "select all" checkbox for easy management of checkboxes in lists.
type: rule
archivedreason: 
title: Controls - Do you include a "select all" checkBox on the top?
guid: 98768e5a-930e-48db-bc05-11d6fe0d7a76
uri: controls-do-you-include-a-select-all-checkbox-on-the-top
created: 2012-11-27T08:42:03.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- controls-do-you-include-a-＂select-all＂-checkbox-on-the-top

---

Do you have checkbox (on the top) that let users select or unselect all checkboxes underneath it? If you have a list of checkboxes, you are going to frustrate users unless you provide an easy way to select all. The best way to achieve this is to have a checkbox at the top.

<!--endintro-->

::: good  
![Figure: Good Example - Hotmail does this](/HotmailSelectAll.gif)  
:::

![Figure: Google have done it a different way to provide multiple methods (All, All Read, All Unread, All Starred, and All Unstarred)](/GmailSelectAll.gif)  

::: bad  
![Figure: Bad Example - SQL Auditor - No CheckBox for users to perform a "select all"](/_Bad.jpg)  
:::

::: good  
![Figure: Good Example - SQL Auditor - CheckBox at the top of the column](/_good.jpg)  
:::

![Figure: Selecting all does this - selects all](/_All.jpg)  

![Figure: Deselecting all does this - selects none](/_None.jpg)  

![Figure: Selecting some should show the Indeterminate check state - aka customized selection](/_Customize.jpg)  

```
Private Sub CheckBoxSelectAll\_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) \_
Handles CheckBoxSelectAll.CheckedChanged
'Select checkbox in each row
For Each sDataGridViewRow As DataGridViewRow In Me.DataGridViewCustomer.Rows
sDataGridViewRow.Cells(0).Value = Me.CheckBoxSelectAll.Checked
Next
End Sub
```

Code: Code for selecting all checkboxes in a windows form
![Figure: Select all checkboxes in a web form](/_Web.jpg)  

```
&lt;script type="text/javascript"&gt;
function SeleteCheckBox()
{
for (var n=0; n &lt; document.form1.elements.length; n++)
{
if (document.form1.elements[n].type == "checkbox" && document.form1.elements[n].name == "gridview")
{
document.form1.elements[n].checked = document.getElementById("CheckBoxAll").checked;
}
}
}
&lt;/script&gt;
```

Code: Code for selecting all checkboxes in a web form
We have suggestions for Visual Studio .NET about this at [A top CheckBox to "select all" in windows forms](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSForm.aspx#SelectAllCheckWindows) and [A top CheckBox to "select all" in web forms.](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSAjax.aspx#SelectAllCheckWeb)
