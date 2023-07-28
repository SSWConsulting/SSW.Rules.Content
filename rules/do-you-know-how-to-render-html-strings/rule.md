---
type: rule
title: Do You Know How To Render HTML Strings?
uri: do-you-know-how-to-render-html-strings
authors:
  - title: Charles Vionnet
    url: https://ssw.com.au/people/charles-vionnet
created: 2023-07-28T07:23:06.201Z
guid: 521afe97-18c3-43bc-8ada-f3782960b10f
---
To prevent cross-site scripting (XSS) attacks, HTML encoding is typically applied to restrain the browser from interpreting HTML strings as code. XSS attacks can occur when untrusted data is rendered on the browser without proper sanitization, thus potentially exposing the system to malicious scripts.

However, this approach can sometimes cause confusion when an application requires to output raw HTML content that is already HTML encoded.

<!--endintro-->

To solve this problem, the `IHtmlString` interface in .NET Core can be used to represent an HTML content that is pre-encoded and should not be encoded again.
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
You should only use IHtmlString when you are sure that the string doesn't contain any potentially harmful script tags. When dealing with user-provided content or content from an untrusted source, always ensure to sanitize or validate the HTML before rendering it.
:::



**TODO**
4. Add your rule to a category. See [How to Add and Edit Categories and Top Categories](https://github.com/SSWConsulting/SSW.Rules.Content/wiki/How-to-Add-and-Edit-Categories-and-Top-Categories).

