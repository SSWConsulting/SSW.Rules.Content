---
type: rule
archivedreason: 
title: Do you use Model Binding instead of FormCollection?
guid: b3c65af5-03dd-4ff0-b816-95178d6d4eff
uri: do-you-use-model-binding-instead-of-formcollection
created: 2013-03-07T18:16:24.0000000Z
authors:
- id: 23
  title: Damian Brady
related: []

---

Model binding in the ASP.NET MVC framework is simple. Your action methods need data, and the incoming HTTP request carries the data you need. The catch is that the data is embedded into POST-ed form values, and possibly the URL itself. Enter the DefaultModelBinder, which can magically convert form values and route data into objects. Model binders allow your controller code to remain cleanly separated from the dirtiness of interrogating the request and its associated environment.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<br><br>::: greybox<br><pre>public ActionResult Create(FormCollection values)
&#123;
    Recipe recipe = new Recipe();
    recipe.Name = values[&quot;Name&quot;];      
            
    // ...
            
    return View();
&#125;
</pre><br>:::<br><br>&lt;/dt&gt;<dd>Figure&#58; Bad Example – Manually reading form values and assigning them to properties is tedious boiler-plate code!</dd></dl><dl class="goodImage">&lt;dt&gt;<br><br>::: greybox<br><pre>[AcceptVerbs(HttpVerbs.Post)]
public ActionResult Create(Recipe newRecipe)
&#123;            
    // ...
    
    return View();
&#125;
</pre><br>:::<br><br>&lt;/dt&gt;<dd>Figure&#58; Good Example – Using MVC’s model binding allows you to work with an automatically-populated object instead</dd></dl>
