---
type: rule
title: Do you know the right technology?
uri: do-you-know-the-right-technology
created: 2016-07-29T17:56:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan

---



<span class='intro'> <p>Use <strong>.NET MVC</strong> over <strong>ASP.NET Web Forms</strong>.</p><dl class="bad"><p class="ssw15-rteElement-CodeArea">&lt;asp&#58;HyperLink
    ID=&quot;HyperLink1&quot;
    runat=&quot;Server&quot;
    NavigateUrl=&quot;http&#58;//www.example.com&quot; CssClass=&quot;example&quot;
    Text=&quot;Hello World&quot;/&gt;</p><dd>Figure&#58; Bad example - Using Web Forms</dd></dl><dl class="good"><p class="ssw15-rteElement-CodeArea">&lt;a href=&quot;http&#58;//www.example.com&quot; class=&quot;example&quot; id=&quot;Example1_HyperLink1&quot;&gt;Hello World&lt;/a&gt;</p><dd>Figure&#58; Good example - Using MVC 5</dd></dl><p>Read the Top 5 reasons why you should never use Web Forms again&#58;<br></p> </span>

<ol><li><strong>Testability</strong> - MVC provides true separation of concerns, and makes it easy to test the whole application from Unit Tests to Coded UI Tests</li><li><strong>Instant Pages</strong> - Get your admin pages up and running faster than ever with improved scaffolding. Don't get bogged down doing Create, Edit, Update, Delete</li><li><strong>Better HTML Markup Control</strong> - Every layer of obstruction creates new problems down the track. When so much development now involves jQuery or other javascript libraries, MVC simplifies development by putting the developer back in charge of the HTML that is actually rendered</li><li><strong>Simpler Debugging</strong> - This means that instead of complicated Webform lifecycles, your code either goes into the Route, Controller or View, so you can jump right into coding without an intimate knowledge of the page lifecycle</li><li><strong>Mobile Support</strong> - With Adaptive Rendering, MVC allows the same User Interface to Render on Different Devices, so users can check it out on their PC, their Tablet or even their Smart Phone</li></ol><p>Or watch the video&#58; ​<br></p>
                <iframe width="853" height="480" src="https&#58;//www.youtube.com/embed/0ugMkda9IBw?rel=0" frameborder="0"></iframe> <br>


