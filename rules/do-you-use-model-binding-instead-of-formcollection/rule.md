---
type: rule
title: Do you use Model Binding instead of FormCollection?
uri: do-you-use-model-binding-instead-of-formcollection
created: 2013-03-07T18:16:24.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>Model binding in the ASP.NET MVC framework is simple. Your action methods need data, and the incoming HTTP request carries the data you need. The catch is that the data is embedded into POST-ed form values, and possibly the URL itself. Enter the DefaultModelBinder, which can magically convert form values and route data into objects. Model binders allow your controller code to remain cleanly separated from the dirtiness of interrogating the request and its associated environment.</p> </span>

<dl class="badImage"><dt><div class="greyBox"><pre>public ActionResult Create(FormCollection values)
&#123;
    Recipe recipe = new Recipe();
    recipe.Name = values[&quot;Name&quot;];      
            
    // ...
            
    return View();
&#125;
</pre></div></dt><dd>Figure&#58; Bad Example – Manually reading form values and assigning them to properties is tedious boiler-plate code!</dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>[AcceptVerbs(HttpVerbs.Post)]
public ActionResult Create(Recipe newRecipe)
&#123;            
    // ...
    
    return View();
&#125;
</pre></div></dt><dd>Figure&#58; Good Example – Using MVC’s model binding allows you to work with an automatically-populated object instead</dd></dl>



