---
type: rule
title: 'DevOps – Stage 3: Do you know what metrics to collect?'
uri: devops--stage-3-do-you-know-what-metrics-to-collect
created: 2016-03-07T18:22:18.0000000Z
authors:
- id: 3
  title: Eric Phan
- id: 78
  title: Matt Wicks

---



<span class='intro'> <p class="p1">Now that your team is spending less time deploying the application, you’ve got more time to improve other aspects of the application, but first you need to know what to improve.&#160; <br></p><p class="p1">Here are a few easy things to gather metrics on&#58;</p> </span>

<p></p><h3 class="ssw15-rteElement-H3">Application Logging (Exceptions)</h3><p class="ssw15-rteElement-P">See how many errors are being produced, aim to reduce this as the produce matures</p><p></p><ul><li>
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=8c5a1235-d169-4164-92a1-08812c26fc22" style="line-height&#58;1.6;"> <span class="s3"> https&#58;//rules.ssw.com.au/do-you-use-the-best-exception-handling-library</span></a><br></li><li>
      <span style="line-height&#58;1.6;">Application Insights</span><br></li><li>
      <span style="line-height&#58;1.6;">RayGun.io&#160;</span><br></li><li><span style="line-height&#58;1.6;"><a href="https&#58;//appcenter.ms/">Visual Studio App Center​​​</a><a href="https&#58;//www.hockeyapp.net/">&#160;</a>(for mobile)</span></li></ul><p></p><p>
   <span style="line-height&#58;1.6;">But it's not only exceptions you should be looking at but also how your users are using the application, so you can&#160;see where you should invest your time</span></p><ul><li>
      <span style="line-height&#58;1.6;">Application Insights - https&#58;//rules.ssw.com.au/why-you-want-to-use-application-insights</span><br></li><li>
      <span style="line-height&#58;1.6;">Google Analytics</span><br></li><li>
      <span style="line-height&#58;1.6;">RayGun.io (Pulse)</span></li></ul><p></p><h3 class="ssw15-rteElement-H3">Application Metrics</h3><p>Application/Server performance – track how your code is running in production, that way you can tell if you need to provision more servers or increase hardware specs to keep up with demand</p><p><img src="/SiteAssets/what-metrics-to-collect-stage-3/2020-03-24_15-27-26.jpg" alt="2020-03-24_15-27-26.jpg" style="margin&#58;5px;width&#58;808px;" />&#160;</p><dd class="ssw15-rteElement-FigureNormal">​​​​Figure&#58; Application Insights gives you information about how things are running and whether there are detected abnormalities in the telemetry<br></dd><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P"><img src="/SiteAssets/what-metrics-to-collect-stage-3/2020-03-24_15-27-45.jpg" alt="2020-03-24_15-27-45.jpg" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureNormal">​Figure&#58; Azure can render the Application Insights data on a nice dashboard so you can get a high level view of your application</dd><dd class="ssw15-rteElement-FigureNormal"><br></dd><dd class="ssw15-rteElement-FigureNormal"><img src="/SiteAssets/what-metrics-to-collect-stage-3/2020-03-24_15-28-22.jpg" alt="2020-03-24_15-28-22.jpg" style="margin&#58;5px;width&#58;808px;" />​​​​​Figure&#58; App Center can let you monitor app install stats, usage and errors from phones just like an app running in Azure<br></dd><p><span style="color&#58;#cc4141;font-family&#58;&quot;segoe ui&quot;, &quot;trebuchet ms&quot;, tahoma, arial, verdana, sans-serif;font-size&#58;18px;"><br></span></p><p><span style="color&#58;#cc4141;font-family&#58;&quot;segoe ui&quot;, &quot;trebuchet ms&quot;, tahoma, arial, verdana, sans-serif;font-size&#58;18px;">Process Metrics</span><br></p><p>Collecting stats about the application isn't enough, you also need to be able to measure the time spent in the processes used to develop and maintain the application. You should keep an eye on and measure&#58;<br></p><ul><li>Sprint Velocity<br></li><li>Time spent in testing</li><li>Time spent deploying</li><li>Time spent getting a new developer up to speed</li><li>Time spent in Scrum ceremonies</li><li>Time taken for a bug to be fixed and deployed to production</li></ul><h3 class="ssw15-rteElement-H3">Code Metrics <br></h3><p>The last set of metrics you should be looking at revolves around the code and how maintainable it is. You can use tools like&#58;<br></p><ul><li>Code Analysis<br></li><li>
      <a href="https&#58;//www.sonarqube.org/" target="_blank">SonarQube</a></li></ul>


