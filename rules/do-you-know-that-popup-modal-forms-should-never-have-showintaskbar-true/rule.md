---
type: rule
archivedreason: 
title: Do you know that popup/modal forms should never have ShowInTaskbar=True?
guid: c574b18d-c6a4-4dec-a60f-85a140d28713
uri: do-you-know-that-popup-modal-forms-should-never-have-showintaskbar-true
created: 2012-11-27T04:22:06.0000000Z
authors: []
related: []
redirects: []

---

Question: What is wrong with this Picture?

![Figure: Can you tell what is wrong with this Picture?](../../assets/ShowInTaskBar.jpg)  

<!--endintro-->

Answer: The 2 SSW SQL Auditor windows are bad, because one is just a modal form.

Note: We don't check for this in Code Auditor because making a form display as popup, is done at runtime via the ShowDialog method.


```
Dim frm as new frmCustomer frm.ShowDialog
```

 Figure: Bad Code 
If your form is designed to be used modally (and thus be called using ShowDialog) then ShowInTaskbar should be set to false in the form designer.


```
Dim frm as new frmCustomer frm.ShowInTaskBar = False frm.ShowDialog
```

 Figure: Bad Code (because this should be set in the form designer) 

```
Dim frm as new frmCustomer frm.ShowDialog
```

 Figure: Good Code (ShowInTaskbar is set in the form's InitializeComponents method instead)
