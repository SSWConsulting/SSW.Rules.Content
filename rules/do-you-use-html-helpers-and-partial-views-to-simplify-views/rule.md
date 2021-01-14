---
type: rule
archivedreason: 
title: Do you use Html Helpers and Partial Views to simplify Views?
guid: 13fd4eb4-925e-47c1-b779-c54b9b869385
uri: do-you-use-html-helpers-and-partial-views-to-simplify-views
created: 2013-03-07T18:47:43.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---

Repeated sections of User Interface should be encapsulated in either Html Helpers or Partial Views to avoid repetition.

<!--endintro-->

::: greybox


```
<div class="featured">
    @if (ViewData.ContainsKey("FeaturedProduct"))
    {
        <span class="ProductName">@ViewBag.FeaturedProduct.Name</span>
        <span class="ProductPrice">@ViewBag.FeaturedProduct.Price</span>
    }
</div>
```


:::
Figure: Bad Example – The above code could be encapsulated into a Partial View for reuse
::: greybox


```
public static class DateExtensions
{
    public static MvcHtmlString GetTodayDate(this System.Web.Mvc.HtmlHelper helper)
    {
        return new MvcHtmlString(DateTime.Now.ToShortDateString());
    }
}
@Html.GetTodayDate()
```


:::
Figure: Good Example – Using an HTML Helper extension method for reusable code
::: greybox


```
@Html.Partial("_FeaturedProduct")
```


:::
Figure: Good Example – Using a Partial View for reusable sections of UI
