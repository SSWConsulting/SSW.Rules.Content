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


<div>Question&#58; What is wrong with this Picture?</div>
<dl class="image"><dt><img alt="Modal Form in Taskbar" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ShowInTaskBar.jpg" width="349" height="60" /></dt>
<dd>Figure&#58; Can you tell what is wrong with this Picture?</dd></dl>
<br><excerpt class='endintro'></excerpt><br>
​<div>Answer&#58; The 2 SSW SQL Auditor windows are bad, because one is just a modal form.</div>
<div>Note&#58; We don't check for this in Code Auditor because making a form display as popup, is done at runtime via the ShowDialog method.</div>
<dl class="badCode"><dt><pre>Dim frm as new frmCustomer frm.ShowDialog</pre></dt>
<dd>Figure&#58; Bad Code</dd></dl>
<div>If your form is designed to be used modally (and thus be called using ShowDialog) then ShowInTaskbar should be set to false in the form designer.</div>
<dl class="badCode"><dt><pre>Dim frm as new frmCustomer frm.ShowInTaskBar = False frm.ShowDialog</pre></dt>
<dd>Figure&#58; Bad Code (because this should be set in the form designer)</dd></dl>
<dl class="goodCode"><dt><pre>Dim frm as new frmCustomer frm.ShowDialog</pre></dt>
<dd>Figure&#58; Good Code (ShowInTaskbar is set in the form's InitializeComponents method instead)</dd></dl>



