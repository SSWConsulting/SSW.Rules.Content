---
type: rule
title: Do you use Model Binding instead of FormCollection?
uri: do-you-use-model-binding-instead-of-formcollection
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
created: 2013-03-07T18:16:24.000Z
archivedreason: null
guid: b3c65af5-03dd-4ff0-b816-95178d6d4eff
---

Model binding in the ASP.NET MVC framework is simple. Your action methods need data, and the incoming HTTP request carries the data you need. The catch is that the data is embedded into POST-ed form values, and possibly the URL itself. Enter the DefaultModelBinder, which can magically convert form values and route data into objects. 

Model binders allow your controller code to remain cleanly separated from the dirtiness of interrogating the request and its associated environment.

<!--endintro-->

```cs
public ActionResult Create(FormCollection values)
{
    Recipe recipe = new Recipe();
    recipe.Name = values["Name"];      
            
    // ...
            
    return View();
}
```
::: bad
Figure: Bad example – Manually reading form values and assigning them to properties is tedious boiler-plate code!
:::

```cs
[AcceptVerbs(HttpVerbs.Post)]
public ActionResult Create(Recipe newRecipe)
{            
    // ...
    
    return View();
}
```
::: good
Figure: Good example – Using MVC’s model binding allows you to work with an automatically-populated object instead
:::

