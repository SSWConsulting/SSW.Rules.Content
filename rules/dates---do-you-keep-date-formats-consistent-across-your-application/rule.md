---
type: rule
archivedreason: 
title: Dates - Do you keep Date formats consistent across your application?
guid: 192c14d7-9ae7-45c4-8cdb-de6da1b39580
uri: dates---do-you-keep-date-formats-consistent-across-your-application
created: 2014-12-01T05:59:36.0000000Z
authors: []
related: []

---


<p>Date formats should always be kept consistent across your application, more importantly, 
                    it should be kept consistent with the operating system's regional settings otherwise 
                    this will cause significant confusion for your users.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt> 
      <img alt="OS Regional Settings" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BetterInterface_RegionalSettings.jpg" style="margin&#58;5px;" />
   </dt><dd> Figure&#58; Operating System's Regional Settings </dd></dl><dl class="badImage"><dt> 
      <img alt="Bad Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/BadExampleDP.gif" style="margin&#58;5px;width&#58;582px;" />
   </dt><dd> Figure&#58; Bad Example - Two screens with inconsistent date formats</dd></dl><dl class="goodImage"><dt> 
      <img alt="Good Example" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/GoodExampleDP.gif" style="margin&#58;5px;width&#58;582px;" />
   </dt><dd> Figure&#58; Good Example - Two screens with consistent date formats</dd></dl><p> The best way to do this in your code is to grab the culture information from the application thread and use it to automatically format your Datetime data type. Do not use hard coded datetime formatting strings unless it's absolutely necessary. </p><dl class="badCode"><dt><pre>startTimeTextBox.Text = resultResults.StartTime.ToString(&quot;dd/MM/yyyy hh&#58;mm&#58;ss&quot;);
                    </pre></dt><dd>Figure&#58; Bad Example - using hard coded formatting string</dd></dl><dl class="goodCode"><dt><pre>'VB.NET
'Initial CultureInfo settings for the application
Public initialCulture As CultureInfo
...
...
txtDateCreate.Text = CType(txtDateCreate.Tag, System.DateTime).ToString(initialCulture.DateTimeFormat)
                    </pre></dt><dd>Figure&#58; Good Example - Using culture info to format datetime</dd></dl>


