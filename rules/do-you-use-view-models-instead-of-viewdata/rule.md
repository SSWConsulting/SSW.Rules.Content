---
seoDescription: Use viewModel instead of ViewData to pass data safely and efficiently in MVC applications.
type: rule
title: Do you use viewModel instead of ViewData?
uri: do-you-use-view-models-instead-of-viewdata
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Baba Kamyljanov
    url: https://ssw.com.au/people/baba-kamyljanov
related: []
redirects: []
created: 2013-03-07T18:23:38.000Z
archivedreason: null
guid: ad2abb14-7013-4ab0-ac89-d362914640d5
---

ASP.NET CORE MVC provides several ways to pass data to views:

* **Weakly typed data:** ViewData and ViewBag
* **Strongly typed data:** ViewModel

<!--endintro-->

Both ViewData and ViewBag are dynamically resolved at runtime, which can often lead to runtime errors because they aren't type-safe and rely on [Magic Strings](https://en.wikipedia.org/wiki/Magic_string).

Pass data using ViewData from Action:

```csharp
public IActionResult About()
{
    ViewData["Message"] = "Hello World!";

    ViewData["User"] = new User()
    {
        Name = "Bob Northwind",
        Age = "35"
    };

    return View();
}
```

::: bad
Figure: Bad example – ViewData is being used in Action which isn’t type-safe
:::

Show data using ViewData in View:

```razor
@{
  var user = ViewData["User"] as User;
}

<h2>ViewData["Message"]</h2>

<div>
    @user.Name<br>
    @user.Age<br>
</div>
```

::: bad
Figure: Bad example – Displaying not-safe data in View
:::

So it is better to use ViewModel to pass data to views. Because it allows to take advantage of strong type checking, and the validity of types used in a view is checked at compile time.

Pass data using ViewModel from Action:

```csharp
public IActionResult About()
{
    var viewModel = new UserViewModel()
    {
        Name = "Bob Northwind",
        Age = "35"
    };

    return View(viewModel);
}
```

::: good
Figure: Good example – ViewModel is being used in Action to pass data which is strongly-typed
:::

Show data using ViewModel in View:

```razor
@model YourNamespace.ViewModels.UserViewModel

<div>
    @Model.Name<br>
    @Model.Age<br>
</div>
```

::: good
Figure: Good example – Displaying safe data in View
:::
