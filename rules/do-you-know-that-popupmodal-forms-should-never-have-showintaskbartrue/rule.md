---
type: rule
archivedreason: 
title: Do you know that popup/modal forms should never have ShowInTaskbar=True?
guid: c574b18d-c6a4-4dec-a60f-85a140d28713
uri: do-you-know-that-popupmodal-forms-should-never-have-showintaskbartrue
created: 2012-11-27T04:22:06.0000000Z
authors: []
related: []

---

Question: What is wrong with this Picture?
<dl class="image">&lt;dt&gt;<img alt="Modal Form in Taskbar" src="../../assets/ShowInTaskBar.jpg" width="349" height="60">&lt;/dt&gt;
<dd>Figure: Can you tell what is wrong with this Picture?</dd></dl>
<!--endintro-->

Answer: The 2 SSW SQL Auditor windows are bad, because one is just a modal form.

Note: We don't check for this in Code Auditor because making a form display as popup, is done at runtime via the ShowDialog method.
<dl class="badCode">&lt;dt&gt;<pre>Dim frm as new frmCustomer frm.ShowDialog</pre>&lt;/dt&gt; <dd>Figure: Bad Code</dd></dl>
If your form is designed to be used modally (and thus be called using ShowDialog) then ShowInTaskbar should be set to false in the form designer.
<dl class="badCode">&lt;dt&gt;<pre>Dim frm as new frmCustomer frm.ShowInTaskBar = False frm.ShowDialog</pre>&lt;/dt&gt; <dd>Figure: Bad Code (because this should be set in the form designer)</dd></dl> <dl class="goodCode">&lt;dt&gt;<pre>Dim frm as new frmCustomer frm.ShowDialog</pre>&lt;/dt&gt; <dd>Figure: Good Code (ShowInTaskbar is set in the form's InitializeComponents method instead)</dd></dl>
