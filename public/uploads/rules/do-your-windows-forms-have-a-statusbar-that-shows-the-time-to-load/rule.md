---
seoDescription: Windows Forms application development should include a StatusBar to display the time taken to load the form, providing valuable insights for developers and users alike.
type: rule
title: Do your Windows Forms have a StatusBar that shows the time to load?
uri: do-your-windows-forms-have-a-statusbar-that-shows-the-time-to-load
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T05:45:00.000Z
guid: 200a7e13-186d-4e30-b62c-f71512714382
---

Every form should have a StatusBar that shows the time taken to load the form.

Developers can't catch and reproduce every performance issue in the testing environment, but when users complain about performance they can send a screenshot (which would including the time to load). Users themselves also would want to monitor the performance of the application. This is one of Microsoft Internet Explorer's most appalling missing feature, the status bar only says 'Done.' when the page is loaded - 'Done: Load Time 14 seconds'.

<!--endintro-->

In the figure below, the time taken to load the form over a dialup connection is 61.1 seconds, this proves to the developer that the form is not useable over a dialup connection. In this particular case, the developer has called a 'select \* from Employees' where it was not needed, only the name, password and ID is needed for this form.

**Note:** Once the form is loaded and load time is shown, the status bar can be used to show anything useful as the form is being used.

::: good
![Figure: Good example - Another form with the StatusBar that shows the time to load - very slow on dialup.](doesntperformsowellwhenrunoveravpn2.jpg)
:::

Add a StatusBar to the form, and add a StatusBarPanel to the StatusBar, then set the properties like below.

![Figure: Add StatusBarPanel to StatusBar](statusbarpanel.gif)

```cs
private DateTime StartLoadTime = System.DateTime.Now;

private void Form1_Load(object sender, System.EventArgs e)
{
    TimeSpan elapsedLoadTime = DateTime.Now.Subtract(StartLoadTime);
    this.statusBarPanel1.Text = string.Format(
    "Load time: {0} seconds",
    Math.Round(elapsedLoadTime.TotalSeconds, 1));
}
```
