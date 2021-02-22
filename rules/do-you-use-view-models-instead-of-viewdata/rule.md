---
type: rule
archivedreason: 
title: Do you use View Models instead of ViewData?
guid: ad2abb14-7013-4ab0-ac89-d362914640d5
uri: do-you-use-view-models-instead-of-viewdata
created: 2013-03-07T18:23:38.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---

MVC provides a ViewData collection in which you can store miscellaneous pieces of information to pass to the View.  It’s also accessible it as a Dynamic object by using the ViewBag.  However, you should avoid using ViewData or ViewBag because it isn’t type-safe and relies on [Magic Strings](http&#58;//en.wikipedia.org/wiki/Magic_string).

<!--endintro-->


::: greybox


```
public ActionResult Index() {
  ViewData["Message"] = "Some Message";
  return View();
}
 
<h1><%: ViewData["Message"] &></h1>
```


:::
Figure: Bad Example – ViewData being used to pass information to the View isn’t type-safe

::: greybox


```
public ActionResult Index() {
  var model = new IndexViewModel();
  model.Message = "Some Message";
  return View();
}
 
<h1><%: Model.Message %></h1>
```


:::
Figure: Good Example – Using a ViewModel is a safer way to pass data
