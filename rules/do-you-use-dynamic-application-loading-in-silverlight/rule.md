---
type: rule
archivedreason: 
title: Do you use dynamic application loading in Silverlight?
guid: 8bd996ef-99a9-47a9-9d74-f7f02249df8d
uri: do-you-use-dynamic-application-loading-in-silverlight
created: 2011-05-20T02:36:18.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
related: []
redirects: []

---


In a large business application with different and distinct modules, often it will make sense to build the separate modules and load them dynamically using a combination of Inversion of Control (IoC) and Silverlight's Dynamic Assembly Loading. 

<br><excerpt class='endintro'></excerpt><br>
There are a few huge wins for a customer when you build your line of business application this way&#58; <br>
<ol>
    <li>The initial load isn't as large - you can have a quick load of a login and common UI, then as the person logs in, prepare their environment by loading additional components </li>
    <li>You can show a quick &quot;Do you know… you can do XXX&quot; while this is loading. You can also show them a quick list of what has been happening (e.g. a Dashboard). </li>
    <li>You can also implement special cases where perhaps HR and Finance both use the same area, but with different customizations. So based on who logs into the system, Silverlight can dynamically load a different assembly giving them a different behaviour. </li>
    <li>You can also build simple &quot;Plug-in&quot; like functionality, allowing simple customizations of your application based on your own published interface API. </li>
</ol>
<p>This works really well with Silverlight's Application Caching as well - and lets you build and release different component modules separately. </p>
<p>You can find out more about Silverlight's Dynamic Assembly Loading here&#58;</p>



