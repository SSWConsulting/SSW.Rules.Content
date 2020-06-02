

---
uri: do-you-have-generic-exception-handler-in-your-globalasax
title: Do you have generic exception handler in your Global.asax?
created: YYYY-08-DD 14:47:18
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> Add your code to handle generic exception of your ASP.NET application in Application_Error.<br> </span>

<p class="ssw15-rteElement-CodeArea">​​private static readonly ILog log = LogManager.GetLogger(typeof(MvcApplication));<br><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; protected void Application_Error(object sender, EventArgs e)<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Exception ex = Server.GetLastError().GetBaseException();<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; log.Fatal(&quot;Unhandled Exception&quot;, ex);<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;</p><dd class="ssw15-rteElement-FigureNormal">​Figure. Exception handler in Global.asax.cs​<br></dd>


