---
type: rule
title: Do you know how to get maximum logging in Report Server?
uri: do-you-know-how-to-get-maximum-logging-in-report-server
created: 2016-09-12T00:39:48.0000000Z
authors:
- id: 3
  title: Eric Phan

---



<span class='intro'> By default SSRS will track reporting execution for the last 60 days. This might be OK in most cases, but you may want to adjust the retention days if you want better report usage statistics.<br> </span>

<p>​T​o update the value you can&#58;<br></p><ol><li><span style="line-height&#58;1.6;">​</span><span style="line-height&#58;1.6;">​​Connect to the ReportServer database in SQL Management Studio</span><br></li><li><span style="line-height&#58;1.6;">Execute the following script and update the value to the number of days you want to track</span><br></li></ol><p></p><p class="ssw15-rteElement-CodeArea"><span style="font-family&#58;&quot;courier new&quot;;">​​EXEC SetConfigurationInfo @Name=N'ExecutionLogDaysKept',@Value=N'<span style="background-color&#58;#ffff00;">365</span>'</span><br></p><p></p><p>After you have this, you can query the ExecutionLog table to find useful information about report execution like&#58;<br></p><ul><li><span style="line-height&#58;20.8px;">​Which users are actively using the reports<br></span></li><li><span style="line-height&#58;20.8px;">How long reports are executing</span></li><li><span style="line-height&#58;20.8px;">The last time a report was executed</span></li></ul><br>


