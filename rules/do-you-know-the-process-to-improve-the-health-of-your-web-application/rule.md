---
seoDescription: Do you know the daily process to improve the health of your web application? Learn how to handle errors and bugs using just-in-time bug processing with Application Insights.
type: rule
archivedreason:
title: Errors – Do you know the daily process to improve the health of your web application?
guid: a06a5bdd-7f6f-4b4f-8769-cd05ae890ce7
uri: do-you-know-the-process-to-improve-the-health-of-your-web-application
created: 2014-08-19T00:51:51.0000000Z
authors:
  - title: Drew Robson
    url: https://ssw.com.au/people/drew-robson
  - title: Chris Briggs
    url: https://ssw.com.au/people/chris-briggs
related: []
redirects:
  - errors-do-you-know-the-daily-process-to-improve-the-health-of-your-web-application
  - errors-–-do-you-know-the-daily-process-to-improve-the-health-of-your-web-application
---

Application Insights can provide an overwhelming amount of errors in your web application, so use just-in-time bug processing to handle them.

<!--endintro-->

The goal is to each morning check your web application's dashboard and find zero errors. However, what happens if there are multiple errors? Don't panic, follow this process to improve your application's health.

![Figure: Every morning developers check Application Insights for errors](App-Insights-Failures.png)

Once you have found an exception you can drill down into it to discover more context around what was happening. You can find out the user's browser details, what page they tried to access, as well as the stack trace (Tip: make sure you follow the rule on [How to set up Application Insights](/how-to-set-up-application-insights) to enhance the stack trace).

![Figure: Drilling down into an exception to discover more.](App-Insights-Failures-drilldown.png)

It's easy to be overwhelmed by all these issues, so don't create a bug for each issue or even the top 5 issues. Simply create one bug for the most critical issue. Reproduce, fix and close the bug then you can move onto the next one and repeat. This is just-in-time bug processing and will move your application towards better health one step at a time.

::: bad  
![Figure: Bad example - creating all the bugs](20-08-2014-12-04-31-PM-compressor.png)  
:::

::: good  
![Figure: Good example - create the first bug (unfortunately bug has to be created manually)](20-08-2014-12-06-16-PM-compressor.png)  
:::
