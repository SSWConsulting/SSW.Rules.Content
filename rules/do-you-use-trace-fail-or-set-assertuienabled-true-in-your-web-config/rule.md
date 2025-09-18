---
seoDescription: Preventing server-side dialogs and improving application reliability through configuration settings in web.config files.
type: rule
archivedreason:
title: Do you use Trace.Fail or set AssertUIEnabled="true" in your web.config?
guid: 0fa5857a-6394-471e-ac85-ba2afe055193
uri: do-you-use-trace-fail-or-set-assertuienabled-true-in-your-web-config
created: 2009-05-13T07:16:16.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects:
  - do-you-use-trace-fail-or-set-assertuienabled-＂true＂-in-your-web-config
---

Have you ever seen dialogs raised on the server-side? These dialogs would hang the thread they were on, and hang IIS until they were dismissed. In this case, you might use Trace.Fail or set AssertUIEnabled="true" in your web.config.

<!--endintro-->

See Scott's blog [Preventing Dialogs on the Server-Side in ASP.NET or Trace.Fail considered Harmful](http://www.hanselman.com/blog/PreventingDialogsOnTheServerSideInASPNETOrTraceFailConsideredHarmful.aspx)

```csharp
 public static void ExceptionFunc(string strException)
{
    System.Diagnostics.Trace.Fail(strException);
}
```

::: bad
Figure: Never use Trace.Fail &lt;configuration&gt;
:::

```csharp
   &lt;system.diagnostics&gt;
      &lt;assert AssertUIEnabled="true" logfilename="c:\log.txt" /&gt;
   &lt;/system.diagnostics&gt;
&lt;/configuration&gt;
Figure: Never set AssertUIEnabled="true" in web.config &lt;configuration&gt;
   &lt;system.diagnostics&gt;
      &lt;assert AssertUIEnabled="false" logfilename="c:\log.txt" /&gt;
   &lt;/system.diagnostics&gt;
&lt;/configuration&gt;
```

::: good
Figure: Should set AssertUIEnabled="false" in web.config
:::
