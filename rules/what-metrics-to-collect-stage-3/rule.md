---
type: rule
archivedreason: 
title: 'DevOps – Stage 3: Do you know what metrics to collect?'
guid: 7867c4c4-1830-4cac-b42e-4926645c898b
uri: what-metrics-to-collect-stage-3
created: 2016-03-07T18:22:18.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
- devops-stage-3-do-you-know-what-metrics-to-collect
- devops-–-stage-3-do-you-know-what-metrics-to-collect

---

Now that your team is spending less time deploying the application, you’ve got more time to improve other aspects of the application, but first you need to know what to improve.

Here are a few easy things to gather metrics on:

<!--endintro-->

### Application Logging (Exceptions)

See how many errors are being produced, aim to reduce this as the produce matures:

* [Do you use the best exception handling library?](/do-you-use-the-best-exception-handling-library)
* Application Insights
* RayGun.io
* [Visual Studio App Center](https://appcenter.ms)(for mobile)

But it's not only exceptions you should be looking at but also how your users are using the application, so you can see where you should invest your time:

* [Application Insights](/why-you-want-to-use-application-insights/)
* Google Analytics
* RayGun.io (Pulse)

### Application Metrics

Application/Server performance – track how your code is running in production, that way you can tell if you need to provision more servers or increase hardware specs to keep up with demand

![Figure: Application Insights gives you information about how things are running and whether there are detected abnormalities in the telemetry](2020-03-24_15-27-26.jpg)

![Figure: Azure can render the Application Insights data on a nice dashboard so you can get a high level view of your application](2020-03-24_15-27-45.jpg)

![Figure: App Center can let you monitor app install stats, usage and errors from phones just like an app running in Azure](2020-03-24_15-28-22.jpg)

### Process Metrics

Collecting stats about the application isn't enough, you also need to be able to measure the time spent in the processes used to develop and maintain the application. You should keep an eye on and measure:

* Sprint Velocity
* Time spent in testing
* Time spent deploying
* Time spent getting a new developer up to speed
* Time spent in Scrum ceremonies
* Time taken for a bug to be fixed and deployed to production

### Code Metrics

The last set of metrics you should be looking at revolves around the code and how maintainable it is. You can use tools like:

* Code Analysis
* [SonarQube](https://www.sonarqube.org)
