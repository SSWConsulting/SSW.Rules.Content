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


<p>Do you have checkbox (on the top) that let users select or unselect all checkboxes underneath it? If you have a list of checkboxes, you are going to frustrate users unless you provide an easy way to select all. The best way to achieve this is to have a checkbox at the top.</p>
<br><excerpt class='endintro'></excerpt><br>
​<dl class="goodImage"><dt><img alt="Hotmail" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/HotmailSelectAll.gif" /></dt>
<dd>Figure&#58; Good Example - Hotmail does this</dd></dl>
<dl class="image"><dt><img alt="Gmail" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/GmailSelectAll.gif" /></dt>
<dd>Figure&#58; Google have done it a different way to provide multiple methods (All, All Read, All Unread, All Starred, and All Unstarred)</dd></dl>
<dl class="badImage"><dt><img alt="SQL Auditor" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SQLAuditorSelectAll_Bad.jpg" /></dt>
<dd>Figure&#58; Bad Example - SQL Auditor - No CheckBox for users to perform a &quot;select all&quot;</dd></dl>
<dl class="goodImage"><dt><img alt="SQL Auditor" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SQLAuditorSelectAll_good.jpg" /></dt>
<dd>Figure&#58; Good Example - SQL Auditor - CheckBox at the top of the column</dd></dl>
<dl class="image"><dt><a name="SelectAll_MoreDetails"></a><img alt="SQL Auditor" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SQLAuditorSelectAll_All.jpg" /></dt>
<dd>Figure&#58; Selecting all does this - selects all</dd></dl>
<dl class="image"><dt><img alt="SQL Auditor" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SQLAuditorSelectAll_None.jpg" /></dt>
<dd>Figure&#58; Deselecting all does this - selects none</dd></dl>
<dl class="image"><dt><img alt="SQL Auditor" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SQLAuditorSelectAll_Customize.jpg" /></dt>
<dd>Figure&#58; Selecting some should show the Indeterminate check state - aka customized selection</dd></dl>
<dl class="code"><dt><pre>    Private Sub CheckBoxSelectAll_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) _
        Handles CheckBoxSelectAll.CheckedChanged
        'Select checkbox in each row
        For Each sDataGridViewRow As DataGridViewRow In Me.DataGridViewCustomer.Rows
            sDataGridViewRow.Cells(0).Value = Me.CheckBoxSelectAll.Checked
        Next
    End Sub
                        </pre></dt>
<dd>Code&#58; Code for selecting all checkboxes in a windows form</dd></dl>
<dl class="image"><dt><img alt="Select all checkboxes in a web form" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SelectAllCheckBox_Web.jpg" /></dt>
<dd>Figure&#58; Select all checkboxes in a web form</dd></dl>
<dl class="code"><dt><pre>    &lt;script type=&quot;text/javascript&quot;&gt;
        function SeleteCheckBox()
        &#123;                 
            for (var n=0; n &lt; document.form1.elements.length; n++) 
            &#123;
                if (document.form1.elements[n].type == &quot;checkbox&quot; &amp;&amp; document.form1.elements[n].name == &quot;gridview&quot;)
                &#123;
                    document.form1.elements[n].checked = document.getElementById(&quot;CheckBoxAll&quot;).checked; 
                &#125;
            &#125;
        &#125;    
    &lt;/script&gt;
                        </pre></dt>
<dd>Code&#58; Code for selecting all checkboxes in a web form</dd></dl>
<div>We have suggestions for Visual Studio .NET about this at <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSForm.aspx#SelectAllCheckWindows">A top CheckBox to &quot;select all&quot; in windows forms</a> and <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSAjax.aspx#SelectAllCheckWeb">A top CheckBox to &quot;select all&quot; in web forms.</a></div>



