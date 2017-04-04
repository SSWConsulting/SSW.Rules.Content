---
type: rule
title: Do you know how to find performance problems with Application Insights?
uri: do-you-know-how-to-find-performance-problems-with-application-insights
created: 2015-10-25T13:34:58.0000000Z
authors:
- id: 45
  title: Chris Briggs
- id: 78
  title: Matt Wicks
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p>​​​​Once you have set up your Application Insights as per the rule 'Do you know how to set up Application Insights.' Once you have your daily failed requests down to zero, you can start looking for performance problems. You will discover that uncovering your performance related problems are relatively straightforward.​​<br></p> </span>

<p>The main focus of the first blade is the 'Overview timeline' chart, which gives you a birds eye view of the health of your application.</p><dl class="image"><dt><img src="/PublishingImages/performance-1.jpg" alt="performance-1.jpg" /></dt><dd>Figure&#58; There are 3 spikes to investigate (one on each graph), but which is the most important?</dd></dl><p>Developers can see the following insights&#58;</p><ul><li>Number of requests to the server and how many have failed (First blue graph)</li><li>The breakdown of your page load times (Green Graph)</li><li>How the application is scaling under different load types over a given period</li><li>When your key usage peaks occur</li></ul><p>Always investigate the spikes first, notice how the two blue ones line up? That should be investigated, however,​ notice that the green peak is actually at <strong>4 hours.</strong> This is definitely the first thing we'll look at.</p><dl class="image"><dt><img src="/PublishingImages/performance%202.png" alt="performance 2.png" /></dt><dd>Figure&#58; The 'Average of Browser page load time by URL base' graph will highlight the slowest page.</dd></dl><p>As we can see that a single request took four hours in the 'Average of Browser page load time by URL base' graph, it is important to examine this request.</p><p>It would be nice to see the prior week for comparison, however, we're unable to in this section. <br><br></p><dl class="image"><dt><img src="/PublishingImages/performance-3.png" alt="performance-3.png" /></dt><dd>Figure&#58; In this case, the user agent string gives away the cause, Baidu (a Chinese search engine) got stuck and failed to index the page.</dd></dl><p>
   <strong>At this point, we'll create a PBI to investigate the problem and fix it.</strong></p><p>(Suggestion to Microsoft, please allow annotating the graph to say we've investigated the spike) <br><br></p><p>The other spike which requires investigation is in the server response times. To investigate it, click on the blue spike. This will open the Server response blade that allows you to compare the current server performance metrics to the previous weeks.&#160;</p><dl class="image"><dt><img src="/PublishingImages/performance-4.jpg" alt="performance-4.jpg" /></dt><dd>Figure&#58; In this case, the most important detail to action is the Get Healthcheck issue</dd></dl><p>In this view, we find performance related issues when the usage graph shows similarities to the previous week but the response times are higher. When this occurs, click and drag on the timeline to select the spike and then click the magnifying glass to ‘zoom in’. This will reload the ‘Average of Server response time by Operation name’ graph with only data for the selected period. <br></p>


