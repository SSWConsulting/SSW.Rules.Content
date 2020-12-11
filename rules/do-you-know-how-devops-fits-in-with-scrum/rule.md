---
type: rule
archivedreason: 
title: Do you know how DevOps fits in with Scrum?
guid: 30a94709-1e33-4615-a916-fb77fdbbbf4a
uri: do-you-know-how-devops-fits-in-with-scrum
created: 2016-06-08T04:28:13.0000000Z
authors:
- id: 3
  title: Eric Phan
related: []

---

DevOps and Scrum compliment each other very well. Scrum is about inspecting and adapting with the help of the Scrum ceremonies (Standup, Review, Planning and Retro). With DevOps it's all about Building, Measuring and Improving with the help of tools and automation. <dl class="image">&lt;dt&gt;<img src="2016-06-08_14-33-24.png" alt="2016-06-08_14-33-24.png" style="width:800px;">&lt;/dt&gt;<dd>Figure: Traditional Scrum Process</dd></dl><dl class="goodImage">&lt;dt&gt;<img src="2016-06-08_14-30-33.png" alt="2016-06-08_14-30-33.png" style="width:800px;"> &lt;/dt&gt;<dd>Figure: Scrum with DevOps </dd></dl>
With DevOps, we add tools to help us automate slow process like build and deployment then add metrics to give us numbers to help quantify our processes. Then we gather the metrics and figure out what can be done to improve.

<!--endintro-->

For example with Exception Handling, you may be using a tool like [Raygun.io](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=0523c65b-2fe6-4e7b-a232-0fc3c9440447) or Elmah and have 100s of errors logged in them. So what do you do with these errors? You can:

1. Add each one to your backlog
2. Add a task to each sprint to "Get exceptions to 0"




The problem with the above is that not all exceptions are equal, and most of the time they are not more important than the planned PBIs being worked on. No developers like working a whole sprint just looking at exceptions. What should happen is:

1. Have the exceptions visible in your development process (i.e. using Slack, adding as something to check before Sprint Planning)
2. Triage the exceptions, either add them to the backlog if they are urgent and important
3. Add ignore filters to the exception logging tool to ignore errors you don't care about (e.g. 404s)
4. Prioritize the exceptions on the backlog


The goal here is to make sure you're not missing important and to reduce the noise. You want these tools to help support your efforts and make your more productive and not just be another time sink.
