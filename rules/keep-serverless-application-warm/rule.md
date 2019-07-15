---
type: rule
archivedreason: 
title: Do you keep your serverless application warm (to avoid cold starts)?
guid: ad45aab9-657e-4286-9799-209958ad11ed
uri: keep-serverless-application-warm
created: 2019-07-15T03:44:14.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-keep-your-serverless-application-warm-to-avoid-cold-starts
- do-you-keep-your-serverless-application-warm-(to-avoid-cold-starts)

---


A cold start happens when a cloud function is invoked for the first time or after a long time of no invocations. Basically, it takes the server (yes – there are servers!) a little bit longer to get the function ready the first time, so it’s ready to accept and process the request. If a function is invoked a second time, it will execute faster. There is a time period during which a function stays warm. If a function is invoked again during that time period – it will be executed fast.<br><br>
<br><excerpt class='endintro'></excerpt><br>
<p>A cold start happens when a cloud function is invoked for the first time or after a long time of no invocations. Basically, it takes the server (yes – there are servers!) a little bit longer to get the function ready the first time, so it’s ready to accept and process the request. If a function is invoked a second time, it will execute faster. There is a time period during which a function stays warm. If a function is invoked again during that time period – it will be executed fast.<br>​<br><br></p>


