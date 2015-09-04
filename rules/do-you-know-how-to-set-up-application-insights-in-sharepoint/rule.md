---
type: rule
title: Do you know how to set up Application Insights (in SharePoint)?
uri: do-you-know-how-to-set-up-application-insights-in-sharepoint
created: 2015-09-01T00:28:34.0000000Z
authors:
- id: 9
  title: William Yin
- id: 45
  title: Chris Briggs

---



<span class='intro'> ​ The best approach of setting up&#160;Application Insights in SharePoint is a bit different than adding to nor<span></span><span></span>mal&#160;web&#160;application.<br> </span>

<p>(Note&#58; To check the normal way of setting up Application Insights via Visual Studio, please read &quot;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=68f64a3a-78ec-49f6-87ed-7ee92af1c809">How to set up Application Insights </a> &quot;) <br></p><p>With a web application you are developing you have full control of web.config and have access to it in your Visual ​Studio project, and can follow<span style="line-height&#58;20.8px;">&#160;&quot;</span><span style="line-height&#58;20.8px;"></span><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=68f64a3a-78ec-49f6-87ed-7ee92af1c809" style="line-height&#58;20.8px;">How to set up Application Insights&#160;</a><span style="line-height&#58;20.8px;">&quot; to set up Application Insights. This way&#160;Visual Studio will do all the modifications for you automatically.</span></p><p> 
   <span style="line-height&#58;20.8px;">But when you develop on SharePoint, you <strong>do not</strong> have a full copy of web.config in your Visual Studio project, the web.config will be initialized on the SharePoint server when a new SharePoint site is&#160;created.&#160;This means Visual Studio cannot&#160;be used to update the web.config for you. Although you can modify SharePoint web.config via coding, that involves lots of development and testing work against your SharePoint&#160;server.</span></p><p> 
   <span style="line-height&#58;20.8px;">The best process to implement Applications&#160;Insights in SharePoint can be split into two parts&#58;</span></p><ol><li> 
      <span style="line-height&#58;20px;">Implement App Insight JavaScript </span> <span style="line-height&#58;20px;">in </span>master<span style="line-height&#58;20px;"> page&#160;(via Visual Studio) &#160;or web pages individually via embedded​ code, there are two good articles include the detail steps</span> 
      <ul><ul><li> 
               <span style="line-height&#58;20px;"> </span> <a style="line-height&#58;20px;">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-sharepoint/ </a></li><li> 
               <span style="line-height&#58;20px;"> <a>https&#58;//azure.microsoft.com/en-us/blog/understand-your-sharepoint-usage-with-application-insights-2/ </a></span></li></ul></ul></li><li>Use Application Insights Status Monitor configuration tool&#160;to add DLLs reference and update web.config (no coding work involved), there are two articles include the detail steps<br>
      <ul><li style="list-style-position&#58;inside;"></li><li style="list-style-position&#58;inside;"><a>http&#58;//blogs.msdn.com/b/visualstudioalm/archive/2014/08/28/monitoring-your-existing-applications.aspx </a></li><li style="list-style-position&#58;inside;">
            <a href="https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-monitor-performance-live-website-now/" style="line-height&#58;20px;">https&#58;//azure.microsoft.com/en-us/documentation/articles/app-insights-monitor-performance-live-website-now/</a>​</li></ul></li></ol>


