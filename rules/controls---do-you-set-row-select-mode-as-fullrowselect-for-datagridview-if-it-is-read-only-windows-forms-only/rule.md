---
type: rule
archivedreason: 
title: Controls - Do you set row select mode as "FullRowSelect" for DataGridView if it is read only? (Windows Forms Only)
guid: db148de9-b2ae-4cb0-a080-d167608ba90c
uri: controls---do-you-set-row-select-mode-as-fullrowselect-for-datagridview-if-it-is-read-only-windows-forms-only
created: 2012-11-27T09:17:59.0000000Z
authors: []
related: []

---


<p>If you use the DataGridView control which is read only, you had better set row select mode as "FullRowSelect". If the data cannot be modified we can let users select the whole row instead of one column.</p>
<br><excerpt class='endintro'></excerpt><br>
​<dl class="badImage"><dt><img alt="without FullRowSelect" src="../../assets/NoneFullRowSelect.gif" /></dt>
<dd>Figure: Bad Example - Row select mode is not "FullRowSelect".</dd></dl>
<dl class="goodImage"><dt><img alt="with FullRowSelect" src="../../assets/FullRowSelect.gif" /></dt>
<dd>Figure: Good Example - Row select mode is "FullRowSelect".</dd></dl>
<dl class="image"><dt><img alt="Set select mode as FullRowSelect" src="../../assets/setselectmodefull.gif" /></dt>
<dd>Figure: Changed row select mode to FullRowSelect.</dd></dl>
<div>What's the next step? It's even better if you enable multiple row selection and copying, see <a href="http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx#ListView">Do your List Views support multiple selection and copying</a> on <a href="http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx">Rules to Better Windows Forms Applications</a>.</div>



