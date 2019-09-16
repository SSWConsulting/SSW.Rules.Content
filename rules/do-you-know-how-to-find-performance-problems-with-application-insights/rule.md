---
type: rule
archivedreason: 
title: Do you know how to find performance problems with Application Insights?
guid: 2b768e59-9f1c-4475-91df-e75b4f0ec0b8
uri: do-you-know-how-to-find-performance-problems-with-application-insights
created: 2015-10-25T13:34:58.0000000Z
authors:
- title: Chris Briggs
  url: https://ssw.com.au/people/chris-briggs
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---


<p>​​​​Once you have set up your Application Insights as per the rule 'Do you know how to set up Application Insights' and&#160;you have your daily failed requests down to zero, you can start looking for performance problems. You will discover that uncovering your performance related problems are relatively straightforward.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>The main focus of the first blade is the 'Overview timeline' chart, which gives you a birds eye view of the health of your application.</p><dl class="image"><dt><img src="/PublishingImages/performance-1.jpg" alt="performance-1.jpg" /></dt><dd>Figure&#58; There are 3 spikes to investigate (one on each graph), but which is the most important?&#160;Hint&#58; look at the scales!<br></dd></dl><p>Developers can see the following insights&#58;</p><ul><li>Number of requests to the server and how many have failed (First blue graph)</li><li>The breakdown of your page load times (Green Graph)</li><li>How the application is scaling under different load types over a given period</li><li>When your key usage peaks occur</li></ul><p>Always investigate the spikes first, notice how the two blue ones line up? That should be investigated, however,​ notice that the green peak is actually at <strong>4 hours.</strong> This is definitely the first thing we'll look at.</p><dl class="image"><dt><img src="/PublishingImages/performance%202.png" alt="performance 2.png" /></dt><dd>Figure&#58; The 'Average of Browser page load time by URL base' graph will highlight the slowest page.</dd></dl><p>As we can see that a single request took four hours in the 'Average of Browser page load time by URL base' graph, it is important to examine this request.</p><p>It would be nice to see the prior week for comparison, however, we're unable to in this section. <br><br></p><dl class="image"><dt><img src="/PublishingImages/performance-3.png" alt="performance-3.png" /></dt><dd>Figure&#58; In this case, the user agent string gives away the cause, Baidu (a Chinese search engine) got stuck and failed to index the page.</dd></dl><p>
   <strong>At this point, we'll create a PBI to investigate the problem and fix it.</strong></p><p>(Suggestion to Microsoft, please allow annotating the graph to say we've investigated the spike) <br><br></p><p>The other spike which requires investigation is in the server response times. To investigate it, click on the blue spike. This will open the Server response blade that allows you to compare the current server performance metrics to the previous weeks.&#160;</p><dl class="image"><dt><img src="/PublishingImages/performance-4.jpg" alt="performance-4.jpg" /></dt><dd>Figure&#58; In this case, the most important detail to action is the Get Healthcheck issue. Now you should be able to optimise the slowest pages​<br></dd></dl><p>In this view, we find performance related issues when the usage graph shows similarities to the previous week but the response times are higher. When this occurs, click and drag on the timeline to select the spike and then click the magnifying glass to ‘zoom in’. This will reload the ‘Average of Server response time by Operation name’ graph with only data for the selected period. <br></p><h3 class="ssw15-rteElement-H3">Looking beyond the Average&#160;Response Times<br></h3><p>High average response&#160;times are easy to find and indicate an endpoint that is usually slow - so this is a good metric to start with. But sometimes a low&#160;average value can contain many successful&#160;fast requests hiding a few much slower requests.<br></p><p>Application insights plots out the&#160;distribution of response time values&#160; allowing potential issues to be spotted.<br></p><p><img src="/SiteAssets/do-you-know-how-to-find-performance-problems-with-application-insights/distribution.png" alt="distribution.png" style="margin&#58;5px;width&#58;808px;" /><br><br></p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; this distribution graph show that under an average value of&#160;54.9ms, 99% of requests were unser 23ms but there were a few requests taking up to 32 seconds!<br></dd><p><br></p>


