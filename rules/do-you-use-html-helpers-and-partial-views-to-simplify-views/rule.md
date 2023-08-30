---
type: rule
title: Do you use Html Helpers and Partial Views to simplify Views?
uri: do-you-use-html-helpers-and-partial-views-to-simplify-views
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
created: 2013-03-07T18:47:43.000Z
archivedreason: null
guid: 13fd4eb4-925e-47c1-b779-c54b9b869385
---

Repeated sections of User Interface should be encapsulated in either Html Helpers or Partial Views to avoid repetition.

<!--endintro-->

```cs
<div class="featured">
    @if (ViewData.ContainsKey("FeaturedProduct"))
    {
        <span class="ProductName">@ViewBag.FeaturedProduct.Name</span>
        <span class="ProductPrice">@ViewBag.FeaturedProduct.Price</span>
    }
</div>
```
::: bad
Figure: Bad example – The above code could be encapsulated into a Partial View for reuse
:::

```cs
public static class DateExtensions
{
    public static MvcHtmlString GetTodayDate(this System.Web.Mvc.HtmlHelper helper)
    {
        return new MvcHtmlString(DateTime.Now.ToShortDateString());
    }
}
@Html.GetTodayDate()
```
::: good
Figure: Good example – Using an HTML Helper extension method for reusable code
:::

```cs
@Html.Partial("_FeaturedProduct")
```
::: good
Figure: Good example – Using a Partial View for reusable sections of UI
:::
