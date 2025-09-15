---
seoDescription: Avoid using MDI forms due to their limitations and outdated design, instead opting for SDI applications that provide a more intuitive and modern user experience.
type: rule
title: Do you avoid using MDI forms?
uri: do-you-avoid-using-mdi-forms
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T06:02:00.000Z
guid: 6489edd3-2c3d-4420-b9a8-bd89b57173d8
---

MDI (Multiple Document Interface) forms should be avoided in most modern data-centric applications because they:

- Are a hangover from the days of Windows 3.1 and Access 2.0
- Constrained within a smaller window
- Only show as one window on the taskbar
- Have no multiple monitor support (the killer reason)

<!--endintro-->

::: bad
![Figure: Bad example - VS.NET with tabs is cool for developers, but not for the average knowledge worker](vs.net.jpg)
:::

::: bad
![Figure: Bad example - Word 2003 in MDI mode](wordmdibad.gif)
:::

::: good
![Figure: Good example - Word 2003 with Default Settings](sdiexample.jpg)

```cs
Me.IsMdiContainer = true;

ClientForm frm = new ClientForm();
frm.MdiParent = this;
frm.Show();
```

::: bad
Figure: Bad code example - using MDI forms
:::

```cs
ClientForm frm = new ClientForm(); frm.Show();
```

::: good
Figure: Good example - not using MDI
:::

MDI forms have the advantage that the MDI parent form will have a collection **MdiChildren** which contains all of its child forms. This makes it very easy to find out which forms are already open, and to give these forms focus. Accomplishing this with an SDI application requires you to:

- A global collection of forms
- A line of code on the load and closed events of each form which adds / removes the form from the global collection

**But what about tabs?**
As developers, we love to use tabs similar Visual Studio.NET (figure below) and  browsers such as Mozilla and CrazyBrowser. Tabs are great for developers, but standard business applications (e.g Sales Order System) should be developed as SDI (Single Document Interface). This is because users are used to Outlook and other office applications, which don't use MDIs at all. If the users want to group windows, Windows XP lets you "Group Similar Taskbar Icons".
