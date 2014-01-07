---
type: rule
archivedreason: 
title: Control Choice - Do you use ListView over GridView (was DataGrid) for ReadOnly? (Windows Forms only)
guid: 6ce29e76-2f40-4d0d-8ff9-e156bcfbf5b5
uri: control-choice---do-you-use-listview-over-gridview-was-datagrid-for-readonly-windows-forms-only
created: 2012-11-27T08:50:09.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<div>Yes a ListView looks nicer than a DataGrid, but a Datagrid is better because it has more functionality (out of the box that is). With a ListView you cannot&#58;</div>
<ul><li>Copy and paste - although you can select a row of data in both controls, you can't copy and paste a whole row from the ListView</li>
<li>Sort data - always useful when there are more than about 20 rows</li>
<li>DataBind - always saves heaps of code</li></ul>
<br><excerpt class='endintro'></excerpt><br>
​<div>So our old rule was to always use the ugly DataGrid (although we were never happy about that).</div>
<dl class="badImage"><dt><img height="526" width="534" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/UsingDataGridWhenNotNeeded.gif" alt="DataGrid" /></dt>
<dd>Figure&#58; Bad Example - The DataGrid is ugly</dd></dl>
<dl class="goodImage"><dt><img height="526" width="534" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SortableListView.gif" alt="Sortable ListView" /></dt>
<dd>Figure&#58; Good Example - A beautiful ListView - a nicer look over the datagrid</dd></dl>
<div>So the listview looks nicer? If you are not convinced here is another one&#58;</div>
<dl class="goodImage"><dt><img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/DatagridVSListview.gif" alt="Datagrid and Listview" /></dt>
<dd>Figure&#58; Good Example - The appearance of DataGrid and ListView</dd></dl>
<div>But another issue is how much code to write... For ListView you will need to write a bit of code to fill the list view...</div>
<dl class="badCode"><dt><pre>    this.listView1.Items.Clear(); 
    // stops drawing to speed up the process, draw right at the end. 
    this.listView1.BeginUpdate(); 
    foreach(DataRow dr in this.dataSet11.Tables[0].Rows)
    &#123; 
       ListViewItem lvi = new ListViewItem(new string[] &#123;dr[0].ToString(),dr[1].ToString(),dr[2].ToString()&#125;);
       lvi.Tag = dr; this.listView1.Items.Add(lvi); 
    &#125; 
    this.listView1.EndUpdate();
                        </pre></dt>
<dd>Figure&#58; 8 lines of code to fill a ListView</dd></dl>
<div>But the datagrid is nicer to code... this is because it comes with data binding ability.</div>
<dl class="badCode"><dt><pre>    // bind it in the designer first. 
    this.oleDbDataAdapter1.Fill(this.dataSet11);
                        </pre></dt>
<dd>Figure&#58; One line of code to fill a DataGrid</dd></dl>
<div>But the SSW ListView (included in the <a href="http&#58;//www.ssw.com.au/ssw/NETToolkit/">.NET Toolkit</a>) is nicer to code with as it comes with data binding ability.</div>
<dl class="goodCode"><dt><pre>    // bind it in the designer first. 
    this.oleDbDataAdapter1.Fill(this.dataSet11);
                        </pre></dt>
<dd>Figure&#58; One line of code to fill the SSW ListView</dd></dl>
<div>So what is this SSW ListView?</div>
<div>It is an inherited control that how we implemented the ListView to give us what MS left out.</div>
<ul><li>DataBinding</li>
<li>Sorting</li></ul>
<div>So now the rules are&#58; <br>Always use the SSW ListView. <br>Exception&#58; Use the DataGrid when&#58; </div>
<ul><li>When not read only - i.e. users will be editing data directly from the cells.</li>
<li>You need more than 1 column with checkboxes, or the column with checkboxes can't be the first column. E.g.&#58; <dl class="image"><dt><img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/DataGrid2CheckBoxes.gif" alt="DataGrid" /></dt>
<dd>Figure&#58; One place when you choose a DataGrid over a ListView is when you have 2 checkbox fields</dd></dl></li></ul>
<div>So in summary, if you don't want users to edit the data directly from the cell, and only the first column need checkboxes, then the ListView is always the better choice.</div>
<table cellspacing="2" cellpadding="2" summary=".NET Toolkit" class="clsSSWProductTable"><tbody><tr><td>We have an example of this in the <a href="http&#58;//www.ssw.com.au/ssw/NETToolkit/">SSW .NET Toolkit</a>.</td></tr></tbody></table>
<br><table cellspacing="2" cellpadding="2" summary="Code Auditor" class="clsSSWProductTable"><tbody><tr><td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.</td></tr></tbody></table>
<br><div>Note&#58; We have a suggestion for Microsoft to improve the <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/MSForm.aspx#DataGridsFormattingonCopy">copy and paste format from a gridview</a></div>



