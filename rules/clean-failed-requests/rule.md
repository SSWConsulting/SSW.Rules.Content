---
type: rule
archivedreason:
title: Do you keep Failed Requests clean?
guid: efa91cc5-943b-42f9-acc8-867ef943e4eb
uri: clean-failed-requests
created: 2023-09-22T06:44:51Z
authors:
  - title: Vlad Kireyev
    url: https://www.ssw.com.au/people/vlad-kireyev/
related:
---
Application Insights provide crucial insights into the health and performance of the application. Failed Requests allow the DevOps specialists to identify the specific errors and exceptions occurring in the application. However, keeping Failed Requests clean is crucial to troubleshoot and pinpoint the root causes of the problems efficiently. A cluttered failed requests list filled with irrelevant entries can make it difficult to identify the critical issues that require immediate attention.

<!--endintro-->

## Understand your Failed Requests

When cleaning up Failed Requests, it is important to identify the patterns between frequent offenders and categorize them into the following three categories:
1.	Irrelevant – Failed Requests that you expect but cannot do anything about.  
Examples: 404 responses to “/autodiscover.xml”, “/robots933456.txt”.

2.	Spam – Failed requests to the non-existent URLs for your application.  
Examples: 404 responses to “.php” or “wordpress” endpoints, which are not part of your application.

3.	Fixable – Failed Requests that you identify as bugs in your application.  
You can identify these requests by their URL belonging to the real endpoints or files in your application.  
Create Issues for these bugs, and if you cannot fix any of them yourself, pass them on to the people who can.  
Examples: 404 responses from missing images, 400 responses from API.

::: info
**Note:** Not everything you encounter can be matched to a pattern or fixed straight away. 
If that is the case, continue to other requests. As the logs become cleaner, it will get easier to understand the problems with the left-over requests.
:::
