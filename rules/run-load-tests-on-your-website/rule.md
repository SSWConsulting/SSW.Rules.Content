---
seoDescription: Ensure your website's performance and scalability under high loads with load testing, avoiding errors and downtime.
type: rule
title: Do you run load tests on your website?
uri: run-load-tests-on-your-website
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - the-best-load-testing-tools-for-web-applications
redirects:
  - do-you-run-load-tests-on-your-website
created: 2016-11-16T16:36:53.000Z
archivedreason: null
guid: f010a6f8-a386-47b6-8d9c-bd7c9b1a37a8
---

You don't want to see your company's website on the front page of the news after it fails to deal with high levels of load.

Load testing helps you to ensure that your apps can scale and stay up when peak traffic hits. Load testing is typically initiated for high-traffic seasonal events such as tax filing season, Black Friday, Christmas, summer sales, etc. but you should be regularly running load testing during development to catch any issues as early as possible.

<!--endintro-->

Once you have a website up and running, it is important to make sure that it keeps running under load. Local testing of the website will not always reveal the latent problems in the website when it is subjected to thousands of users.

Typical issues that result from failures to handle high loads are:

- 503 "Service Is Temporarily Unavailable" errors
- Very slow page load times
- Application crashes due to:
  - Insufficient resources - so application pools are recycled
  - Too many concurrent users - causing race conditions
  - Too many users trying to connect to the database - causing connection pool exhaustion

Load testing can help you to reveal these issues before you go live. Some issues might be resolved by getting a better web server, while others might require code changes and optimizations.

Load testing tools are designed to help you perform load testing, by recording metrics about the application as the load is varied and allowing you to visualize where user load impacts performance and/or causes application errors.

Visual Studio 2019 Enterprise Edition is the last version of Visual Studio with built-in [load testing functionality](https://docs.microsoft.com/en-us/visualstudio/test/walkthrough-create-and-run-a-load-test?view=vs-2022). However, it only supports Internet Explorer so **Visual Studio is not a recommended load testing option** .

:::greybox
**Note:** [Azure Load Testing](https://docs.microsoft.com/en-us/azure/load-testing/overview-what-is-azure-load-testing) is a fully managed load-testing service that enables you to generate high-scale load. It uses JMeter to generate the loads. Note that this service is currently only in Preview.
:::
