---
type: rule
archivedreason: 
title: Dates - Do you keep date formatting consistent across your application?
guid: 192c14d7-9ae7-45c4-8cdb-de6da1b39580
uri: dates-do-you-keep-date-formats-consistent-across-your-application
created: 2014-12-01T05:59:36.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---

Date formats should always be kept consistent across your application, more importantly, it should be kept consistent with the operating system's regional settings otherwise this will cause significant confusion for your users.

<!--endintro-->

![Figure: Operating System's Regional Settings](../../assets/BetterInterface\_RegionalSettings.jpg)  

::: bad  
![Figure: Bad Example - Two screens with inconsistent date formats](../../assets/BadExampleDP.gif)  
:::

::: good  
![Figure: Good Example - Two screens with consistent date formats](../../assets/GoodExampleDP.gif)  
:::

The best way to do this in your code is to grab the culture information from the application thread and use it to automatically format your Datetime data type. Do not use hard coded datetime formatting strings unless it's absolutely necessary.

```
startTimeTextBox.Text = resultResults.StartTime.ToString("dd/MM/yyyy hh:mm:ss");
```
::: bad
Figure: Bad Example - using hard coded formatting string
:::

```
'VB.NET
'Initial CultureInfo settings for the application
Public initialCulture As CultureInfo
...
...
txtDateCreate.Text = CType(txtDateCreate.Tag, System.DateTime).ToString(initialCulture.DateTimeFormat)
```
::: good
Figure: Good Example - Using culture info to format datetime
:::
