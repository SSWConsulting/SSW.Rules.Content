---
type: rule
archivedreason: 
title: Do you have a HealthCheck page (from /zsValidate) to make sure your website is healthy?
guid: d1d9fb82-25d3-43e8-98d7-2a4d5bee24e8
uri: have-a-healthcheck-page-to-make-sure-your-website-is-healthy
created: 2016-11-28T18:46:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
related: []
redirects:
- do-you-have-a-healthcheck-page-from-zsvalidate-to-make-sure-your-website-is-healthy
- do-you-have-a-healthcheck-page-(from-zsvalidate)-to-make-sure-your-website-is-healthy

---


<p>​Websites can be complicated, and a very small mistake can take the whole site down. But there are two different kinds of errors, coding errors and deployment errors; coding errors should be picked up by compiling and debugging, while deployment errors should be picked up by the HealthCheck page.<br></p><p>Whenever there is a deployment problem, instead of fixing it straight away, we find out what the cause of the problem is and create a HealthCheck test to prevent it from happening again. So next time, when the site is down or re-deployed to a new server, we can simply run the HealthCheck page and fix all red crosses then the site should be back online.<br></p><div>Dotnet Core has the ability to add a health check to your application and can be configured for a variety of real-time monitoring scenarios:<br><ul><li>​Health probes can be used by container orchestrators and load balancers to check an app's status. For example, a container orchestrator may respond to a failing health check by halting a rolling deployment or restarting a container. A load balancer might react to an unhealthy app by routing traffic away from the failing instance to a healthy instance.</li><li>Use of memory, disk, and other physical server resources can be monitored for healthy status.</li><li>Health checks can test an app's dependencies, such as databases and external service endpoints, to confirm availability and normal functioning.​​</li></ul>See more at <a href="https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-3.1">https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-3.1</a><br></div><div><br></div><div>If you need to add a UI to the health check system - we recommend checking out <a href="https://github.com/Xabaril/AspNetCore.Diagnostics.HealthChecks">https://github.com/Xabaril/AspNetCore.Diagnostics.HealthChecks</a>.<br><br>It includes NuGet packages that make it easy to test the health of the lots of different endpoints, and you can push the health check results to different logging platforms e.g. Application Insights, DataDog, etc<br> <br>It also includes UI (which is themable) and the UI supports automatic discovery of k8s services exposing pods that have health checks endpoints. This means you can benefit from it and avoid registering all the endpoints you want to check and let the UI discover them using the k8s API.<br> <br>Best of all they have a <a href="https://marketplace.visualstudio.com/items?itemName=luisfraile.vss-services-aspnetcorehealthcheck-extensions">Release Gate available on the DevOps market place​</a> for the release pipelines.<br></div><p></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image">​​
<dt><img src="ui-branding.png" alt="ui-branding.png" style="width:750px;" /></dt><dd>Figure: Sample Health Page<br></dd></dl><dl class="image">​​
<dt><img src="timeline.png" alt="timeline.png" /></dt><dd>​​Figure: Sample Health of an endpoint being viewed in a timeline i.e. so I can see when was a resource last healthy</dd>
<br></dl><h4>​Other products using validation status</h4><dl class="image"><dt>
      <img src="status-microsoft.jpg" alt="Microsoft summary" />
   </dt><dd>Figure: Microsoft Live status - 
      <a href="http://status.mailchimp.com/" target="_blank">www.apple.com/au/support/systemstatus/</a></dd></dl><dl class="image"><dt>
      <img src="status-google.jpg" alt="Google Apps summary" />
   </dt><dd>Figure: Google Apps status - 
      <a href="http://www.google.com/appsstatus" target="_blank">www.google.com/appsstatus</a></dd></dl><dl class="image"><dt>
      <img src="status-apple.jpg" alt="Apple summary" />
   </dt><dd>Figure: Apple status - 
      <a href="https://www.apple.com/au/support/systemstatus/" target="_blank">status.mailchimp.com</a></dd></dl><dl class="image"><dt>
      <img src="status-mailchimp.jpg" alt="Mailchimp summary" />
   </dt><dd>Figure: MailChimp status - 
      <a href="http://status.mailchimp.com/" target="_blank">status.mailchimp.com</a></dd></dl><p> See 
   <a href="https://www.ssw.com.au/SSW/Standards/Rules/RulesToBetterUnitTests.aspx#HealthCheck" class="Internal">SSW Rules - Do you have a HealthCheck page to test your website dependencies? </a> </p><dl class="image"><dt>
      <img src="check-everything.JPG" alt="check-everything.JPG" />
   </dt><dd>Figure: Check everything with care</dd></dl>
​<br>
<br>


