---
type: rule
title: Do you know how to render HTML strings?
uri: do-you-know-how-to-render-html-strings
authors:
  - title: Charles Vionnet
    url: https://ssw.com.au/people/charles-vionnet
created: 2023-07-28T07:23:06.201Z
guid: 521afe97-18c3-43bc-8ada-f3782960b10f
---
[Cross-site scripting (XSS) attacks](https://en.wikipedia.org/wiki/Cross-site_scripting) occur when untrusted data is rendered on the browser without proper sanitization, thus potentially exposing the system to malicious scripts. To prevent XSS attacks, HTML encoding is typically applied to prevent the browser from interpreting HTML strings as code.

However, this approach can cause confusion when an application needs to output content that is already HTML encoded.

<!--endintro-->

To solve this problem, the [`IHtmlString`](https://learn.microsoft.com/en-us/dotnet/api/system.web.ihtmlstring) interface in .NET Core can be used to represent HTML content that is pre-encoded and should not be encoded again.
This is to prevent double encoding, which can distort the original HTML content and cause it to display incorrectly on a web page.

```cs
string message = "Hello, <b>world</b>!";

Output: <p>Hello, &lt;b&gt;world&lt;/b&gt;!</p>
```
::: bad  
Figure: Bad example - HTML tags using a string have been HTML encoded
:::

```cs
IHtmlContent message = new HtmlString("Hello, <b>world</b>!");

Output: <p>Hello, <b>world</b>!</p>
```
::: good  
Figure: Good example - HTML tags using IHtmlContent have been treated as safe HTML and not encoded 
:::

::: info  
You should only use IHtmlString when you are sure that the string doesn't contain any potentially harmful script tags. When dealing with user-provided content or content from an untrusted source, always sanitize or validate the HTML before rendering it.
:::

