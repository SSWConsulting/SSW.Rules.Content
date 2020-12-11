---
type: rule
archivedreason: 
title: Do you know the right technology?
guid: 0be6a53a-ca81-4cb6-885f-f5b38274a654
uri: do-you-know-the-right-technology
created: 2016-07-29T17:56:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan
related: []

---

Use  **.NET MVC** over  **ASP.NET Web Forms** .
<dl class="bad"><p class="ssw15-rteElement-CodeArea">&lt;asp&#58;HyperLink
    ID=&quot;HyperLink1&quot;
    runat=&quot;Server&quot;
    NavigateUrl=&quot;http&#58;//www.example.com&quot; CssClass=&quot;example&quot;
    Text=&quot;Hello World&quot;/&gt;</p><dd>Figure&#58; Bad example - Using Web Forms</dd></dl><dl class="good"><p class="ssw15-rteElement-CodeArea">&lt;a href=&quot;http&#58;//www.example.com&quot; class=&quot;example&quot; id=&quot;Example1_HyperLink1&quot;&gt;Hello World&lt;/a&gt;</p><dd>Figure&#58; Good example - Using MVC 5</dd></dl>
Read the Top 5 reasons why you should never use Web Forms again:

<!--endintro-->

1. **Testability** - MVC provides true separation of concerns, and makes it easy to test the whole application from Unit Tests to Coded UI Tests
2. **Instant Pages** - Get your admin pages up and running faster than ever with improved scaffolding. Don't get bogged down doing Create, Edit, Update, Delete
3. **Better HTML Markup Control** - Every layer of obstruction creates new problems down the track. When so much development now involves jQuery or other javascript libraries, MVC simplifies development by putting the developer back in charge of the HTML that is actually rendered
4. **Simpler Debugging** - This means that instead of complicated Webform lifecycles, your code either goes into the Route, Controller or View, so you can jump right into coding without an intimate knowledge of the page lifecycle
5. **Mobile Support** - With Adaptive Rendering, MVC allows the same User Interface to Render on Different Devices, so users can check it out on their PC, their Tablet or even their Smart Phone


Or watch the video:

`youtube: https://www.youtube.com/embed/0ugMkda9IBw?rel=0`
