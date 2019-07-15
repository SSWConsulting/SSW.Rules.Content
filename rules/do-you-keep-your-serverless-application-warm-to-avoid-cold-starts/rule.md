---
type: rule
title: Do you keep your serverless application warm (to avoid cold starts)?
uri: do-you-keep-your-serverless-application-warm-to-avoid-cold-starts
created: 2019-07-15T03:44:14.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> When you design your own Bot, you will very likely leverage some Bot framework/service to conduct the natural language processing part for you so that you can focus on implementing your business logic. When you build your business logic, it is common to use serverless applications such as Azure function or Google Firebase functions. As a &quot;side effect&quot; of serverless infrastructure, a&#160;cold start happens when a cloud function is invoked for the first time or after a long time of no invocations. <br><br> </span>

<p>Basically, it takes the server (yes – there are servers!) a little bit longer to get the function ready the first time, so it’s ready to accept and process the request. If a function is invoked a second time, it will execute faster. There is usually&#160;a time period during which a function stays warm. If a function is invoked again during that time period – it will be executed fast, otherwise we have to wait for the server to spin up.&#160;</p><p>Here are our recommended solutions to the problem for MS&#160;Azure and GCP respectively.&#160;<br></p><p>Microsoft Azure&#58;</p><ol><li><span style="background-color&#58;initial;color&#58;#333333;">​​​A</span><span style="background-color&#58;initial;color&#58;#333333;">dd warm up request</span></li></ol>​&#160; &#160; Use a time triggered function to keep the function app constantly warm. If you know&#160;that at a certain time of a day the Function App is likely to be cold and so you wake it up just before you expect users to send out requests.&#160;<span style="color&#58;#333333;background-color&#58;initial;">​​</span><div><span style="color&#58;#333333;background-color&#58;initial;"><br></span></div><div><span style="color&#58;#333333;background-color&#58;initial;">&#160; &#160; 2</span><span style="color&#58;#333333;background-color&#58;initial;">.&#160;</span><span style="color&#58;#333333;background-color&#58;initial;">Move to App Service Plan</span><div><div><p><span style="color&#58;#333333;">&#160; &#160; With Azure functions, you don't have to host using the serverless​ &quot;consumption&quot; plan. Instead, you can just use a regular <a href="https&#58;//azure.microsoft.com/en-au/pricing/details/app-service/plans/">Azure App Service Plan</a>, which comes with a fixed monthly​ fee per server instance. In this case, you no longer need to worry about cold starts since the compute is always available.&#160;</span></p><p>3. Upgrade to Premium Plan</p>&#160; &#160; If you want dedicated instances that are always on to eliminate cold starts as well as the ability to scale out in the same way, you can try <a href="https&#58;//docs.microsoft.com/en-us/azure/azure-functions/functions-premium-plan">Azure Functions Premium Plan (preview)</a>&#160;out.&#160;<br><p></p><p><br></p><p><br></p><p>Google Cloud Platform&#160;<br></p><p></p><ol><li>Add warm up request<br></li></ol><br><br><p></p></div><br></div></div>


