---
seoDescription: Dates should be formatted consistently across an application to avoid confusion for users, aligning with the operating system's regional settings.
type: rule
title: Dates - Do you keep date formatting consistent across your application?
uri: dates-do-you-keep-date-formats-consistent-across-your-application
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []
created: 2014-12-01T05:59:36.000Z
archivedreason: null
guid: 192c14d7-9ae7-45c4-8cdb-de6da1b39580
---

Date formats should always be kept consistent across your application, more importantly, it should be kept consistent with the operating system's regional settings otherwise this will cause significant confusion for your users.

<!--endintro-->

![Figure: Operating System's Regional Settings](./operatingsystem-language-setting.png)
**Figure: Operating System's Regional Settings**

::: bad  
![Figure: Bad example - Screens with inconsistent date formats](../../assets/BadExampleDP.gif)  
:::

::: good  
![Figure: Good example - Screens with consistent date formats](../../assets/GoodExampleDP.gif)  
:::

The best way to do this in your code is to grab the culture information from the application thread and use it to automatically format your Datetime data type. Do not use hard coded datetime formatting strings unless it's absolutely necessary.

```dotnet
startTimeTextBox.Text = resultResults.StartTime.ToString("dd/MM/yyyy hh:mm:ss");
```

::: bad
Figure: Bad example - Using hard coded formatting string
:::

```dotnet
'VB.NET
'Initial CultureInfo settings for the application
Public initialCulture As CultureInfo
...

...
txtDateCreate.Text = CType(txtDateCreate.Tag, System.DateTime).ToString(initialCulture.DateTimeFormat)
```

::: good
Figure: Good example - Using culture info to format datetime
:::

## Browser language settings

It is required to set web browser language to English (Australia) after modifying the computer reginal and language settings. This ensures proper formatting and compatibility, particularly when downloading web pages or accessing specific web content. 

For example, Power BI is date format agnostic and will honor the setting in your browser. If your browser language is set to US English, it may cause date formatting issues.

![Figure: Date format incorrect due to unmodified web page language settings](./PowerBI-wrong-date-format.png)
**Figure: Date format incorrect due to unmodified web page language settings**

Go to Browser Setting | Language | Select English (Australia) as the top priority language:

![Figure: Set English (Australia) as the top priority in the browser language settings](./browser-%20language-%20setting.png)
**Figure: Set English (Australia) as the top priority in the browser language settings**

For more, refer to [software langauge setting rules](https://www.ssw.com.au/rules/make-sure-all-software-uses-english/).
