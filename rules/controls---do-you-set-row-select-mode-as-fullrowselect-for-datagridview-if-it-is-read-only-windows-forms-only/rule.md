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

If you use the DataGridView control which is read only, you had better set row select mode as "FullRowSelect". If the data cannot be modified we can let users select the whole row instead of one column.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img alt="without FullRowSelect" src="../../assets/NoneFullRowSelect.gif">&lt;/dt&gt;
<dd>Figure: Bad Example - Row select mode is not "FullRowSelect".</dd></dl><dl class="goodImage">&lt;dt&gt;<img alt="with FullRowSelect" src="../../assets/FullRowSelect.gif">&lt;/dt&gt;
<dd>Figure: Good Example - Row select mode is "FullRowSelect".</dd></dl><dl class="image">&lt;dt&gt;<img alt="Set select mode as FullRowSelect" src="../../assets/setselectmodefull.gif">&lt;/dt&gt;
<dd>Figure: Changed row select mode to FullRowSelect.</dd></dl>
What's the next step? It's even better if you enable multiple row selection and copying, see [Do your List Views support multiple selection and copying](http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx#ListView) on [Rules to Better Windows Forms Applications](http://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx).
