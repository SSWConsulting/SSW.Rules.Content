---
type: rule
archivedreason: 
title: Do you know why you want to use Application Insights?
guid: af36ac71-56ce-4879-bb04-0d3cb42b7beb
uri: do-you-know-why-you-want-to-use-application-insights
created: 2015-07-24T04:40:05.0000000Z
authors:
- id: 45
  title: Chris Briggs
- id: 1
  title: Adam Cogan
related:
- do-you-use-an-analytics-framework-to-help-manage-exceptions
- do-you-know-how-to-set-up-application-insights

---

Knowing the holistic health of your application is important once it has been deployed into production. Getting feedback on your Availability, errors, performance, and usage is an important part of DevOps.
We recommend using Application Insights, as getting it set up and running is quick, simple and relatively painless.

Application Insights will tell you if your application goes down or runs slowly under load. If there are any uncaught exceptions, you'll be able to drill into the code to pinpoint the problem. You can also find out what your users are doing with the application so that you can tune it to their needs in each development cycle.

<!--endintro-->
<dl class="image">&lt;dt&gt; <img src="Google-analytics.png" alt=""> &lt;/dt&gt;<dd>Figure:  When developing a public website, you wouldn't deploy without Google Analytics to track metrics about user activity. </dd></dl><dl class="image">&lt;dt&gt; <img src="2020-03-24_15-27-26.jpg" alt="2020-03-24_15-27-26.jpg" style="margin:5px;width:808px;"> <br>&lt;/dt&gt;<dd>Figure: For similar reasons, you shouldn't deploy a web application without metric tracking on performance and exceptions<br></dd></dl>
1. You need a portal for your app
2. You need to know spikes are dangerous
3. You need to monitor:
    1. Errors
    2. Performance
    3. Usage

<dl class="image">&lt;dt&gt; <img src="../../assets/r437355_2104314.jpg" alt="Figure: Spikes on an Echidna are dangerous " style="width:250px;"> &lt;/dt&gt;<dd> Figure: Spikes on an Echidna are dangerous </dd></dl><dl class="image">&lt;dt&gt; <img src="../../assets/sockeye-daily-count.jpg" alt="Spikes on a graph are dangerous" style="width:500px;"> &lt;/dt&gt;<dd> Figure: Spikes on a graph are dangerous</dd></dl>
To add Application Insights to your application, make sure you follow the rule [Do you know how to set up Application Insights?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=68f64a3a-78ec-49f6-87ed-7ee92af1c809)

Can't use Application Insights? Check out the following rule [Do you use the best exception handling library](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=8c5a1235-d169-4164-92a1-08812c26fc22) ?
