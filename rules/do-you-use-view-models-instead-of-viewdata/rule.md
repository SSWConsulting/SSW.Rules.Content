---
type: rule
title: Do you use View Models instead of ViewData?
uri: do-you-use-view-models-instead-of-viewdata
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
created: 2013-03-07T18:23:38.000Z
archivedreason: null
guid: ad2abb14-7013-4ab0-ac89-d362914640d5
---

MVC provides a ViewData collection in which you can store miscellaneous pieces of information to pass to the View. It’s also accessible it as a Dynamic object by using the ViewBag.  However, you should avoid using ViewData or ViewBag because it isn’t type-safe and relies on [Magic Strings](https://en.wikipedia.org/wiki/Magic_string).

<!--endintro-->

```cs
public ActionResult Index() {
  ViewData["Message"] = "Some Message";
  return View();
}

<h1><%: ViewData["Message"] &></h1>
```
::: bad
Figure: Bad example – ViewData being used to pass information to the View isn’t type-safe
:::

```cs
public ActionResult Index() {
  var model = new IndexViewModel();
  model.Message = "Some Message";
  return View();
}

<h1><%: Model.Message %></h1>
```
::: good
Figure: Good example – Using a ViewModel is a safer way to pass data
:::

