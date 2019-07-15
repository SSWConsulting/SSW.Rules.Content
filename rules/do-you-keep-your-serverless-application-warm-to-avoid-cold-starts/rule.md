---
type: rule
title: Do you keep your serverless application warm (to avoid cold starts)?
uri: do-you-keep-your-serverless-application-warm-to-avoid-cold-starts
created: 2019-07-15T03:44:14.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> A cold start happens when a cloud function is invoked for the first time or after a long time of no invocations. Basically, it takes the server (yes – there are servers!) a little bit longer to get the function ready the first time, so it’s ready to accept and process the request. If a function is invoked a second time, it will execute faster. There is a time period during which a function stays warm. If a function is invoked again during that time period – it will be executed fast.<br><br> </span>

<p>A cold start happens when a cloud function is invoked for the first time or after a long time of no invocations. Basically, it takes the server (yes – there are servers!) a little bit longer to get the function ready the first time, so it’s ready to accept and process the request. If a function is invoked a second time, it will execute faster. There is a time period during which a function stays warm. If a function is invoked again during that time period – it will be executed fast.<br>​<br><br></p>


