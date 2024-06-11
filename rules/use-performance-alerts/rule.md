---
seoDescription: DBAs can use performance alerts to proactively detect and address potential issues before they impact database performance or cause downtime.
type: rule
archivedreason:
title: DBAs - Do you use Performance Alerts?
guid: feed9331-a823-454b-9326-ab7eaf3f8e7c
uri: use-performance-alerts
created: 2019-11-22T20:37:16.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - dbas-do-you-use-performance-alerts
---

Performance alerts work well for problems that need to be discovered before they occur.

For example, one problem that you may encounter is database file growth. Since databases are set to grow to a certain percentage, you needed to configure an alert to let you know when my database would draw close to that threshold. you can configure a performance alert that fired off when it reached 80% of that threshold. Here is an example of what you can do:

<!--endintro-->

To configure an alert to trigger an application, perform the following steps:

1. Start the Microsoft Management Console (MMC) Performance snap-in (Start, Programs, Administrative Tools, Performance).
2. Expand Performance Logs and Alerts, and select Alerts.
3. Right-click in the right pane, and select New Alert Settings.
4. Enter a name for the setting that reflects what the alert will monitor, and click OK.
5. On the General tab, add the counter the alert will monitor and specify the values that will trigger the action.
6. On the Action tab, select the Run this Program checkbox.
7. Click the Browse button, and select the name of the application you want to run.
8. Click OK.

![](performanceAlert.gif)  
You have just configured an application to run in response to an alert. Unfortunately, because the program doesn't interact with the desktop, it runs in the background, visible only in Task Manager. To enable the program to run interactively, perform the following steps:

1. Start the MMC Services snap-in (Start, Programs, Administrative Tools, Services).
2. Right-click Performance Logs and Alerts, and select Properties.
3. On the Log On tab, specify the "Local System account" and select the "Allow service to interact with desktop" checkbox.
