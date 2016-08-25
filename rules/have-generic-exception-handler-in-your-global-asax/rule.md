---
type: rule
archivedreason: 
title: Do you have generic exception handler in your Global.asax?
guid: c2e66516-0d81-493e-a878-3fbd2fc96607
uri: have-generic-exception-handler-in-your-global-asax
created: 2016-08-25T14:47:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-generic-exception-handler-in-your-global-asax

---


Add your code to handle generic exception of your ASP.NET application in Application_Error.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​​private static readonly ILog log = LogManager.GetLogger(typeof(MvcApplication));<br><br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; protected void Application_Error(object sender, EventArgs e)<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; Exception ex = Server.GetLastError().GetBaseException();<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; log.Fatal(&quot;Unhandled Exception&quot;, ex);<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#125;</p><dd class="ssw15-rteElement-FigureNormal">​Figure. Exception handler in Global.asax.cs​<br></dd>


