---
type: rule
archivedreason: Old. Was replaced by Angular, React, and Blazor.
title: Do you use .NET MVC over ASP.NET Web Forms?
guid: 0be6a53a-ca81-4cb6-885f-f5b38274a654
uri: the-right-technology
created: 2016-07-29T17:56:03.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-know-the-right-technology

---

Use  **.NET MVC** over **ASP.NET Web Forms** .

Read the Top 5 reasons why you should **never** use Web Forms again:

<!--endintro-->

1. **Testability** - MVC provides true separation of concerns, and makes it easy to test the whole application from Unit Tests to Coded UI Tests
2. **Instant Pages** - Get your admin pages up and running faster than ever with improved scaffolding. Don't get bogged down doing Create, Edit, Update, Delete
3. **Better HTML Markup Control** - Every layer of obstruction creates new problems down the track. When so much development now involves jQuery or other javascript libraries, MVC simplifies development by putting the developer back in charge of the HTML that is actually rendered
4. **Simpler Debugging** - This means that instead of complicated Webform lifecycles, your code either goes into the Route, Controller or View, so you can jump right into coding without an intimate knowledge of the page lifecycle
5. **Mobile Support** - With Adaptive Rendering, MVC allows the same User Interface to Render on Different Devices, so users can check it out on their PC, their Tablet or even their Smart Phone

Or watch the video:

`youtube: https://www.youtube.com/embed/0ugMkda9IBw?rel=0`

**Top 5 Reasons Why .NET MVC is Great (3 min)**

``` asp
<asp:HyperLink
    ID="HyperLink1"
    runat="Server"
    NavigateUrl="http://www.example.com" CssClass="example"
    Text="Hello World"/>
```
::: bad
Figure: Bad example - Using Web Forms
:::

``` dotnet
<a href="http://www.example.com" class="example" id="Example1_HyperLink1">Hello World</a>
```
::: good
Figure: Good example - Using MVC 5
:::
