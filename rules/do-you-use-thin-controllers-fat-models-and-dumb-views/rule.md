---
type: rule
title: Do you use Thin controllers, Fat models and Dumb views?
uri: do-you-use-thin-controllers-fat-models-and-dumb-views
created: 2012-07-18T17:54:57.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <h2>Thin Controllers</h2>
<p>You need to think of a controller as more of a coordinator than a controller. <br>It is responsible for calling the business layer and passing from the business layer to the view. <br>It is also responsible for process flow.</p> </span>

<span class="ms-rteCustom-CodeArea">public ActionResult Details(decimal todaysWeather)<br>&#123;<br>var todaysWeatherInFarhenheit = ((9.0 / 5.0) * todaysWeather) + 32;<br>return View(todaysWeatherInFarhenheit); &#125;<br></span><span class="ms-rteCustom-FigureBad">Figure&#58; Business logic is mixed up within the controller making it fatter than it should be</span> <span class="ms-rteCustom-CodeArea">public ActionResult Index()<br>&#123;<br>var todaysWeather = weatherDB.Today.ToList();<br>return View(todaysWeather);<br>&#125; </span><span class="ms-rteCustom-FigureGood">Figure&#58; The controller is co-ordinating between the business layer and the view</span> <span class="ms-rteCustom-CodeArea">public ActionResult Details(int? id)<br>&#123;<br>if (!id.HasValue)<br>return RedirectToAction(&quot;Index&quot;);<br><br>return View();<br>&#125; </span><span class="ms-rteCustom-FigureGood">Figure&#58; The controller is co-ordinating process flow (directing traffic)</span> <h2>Dumb Views</h2>
<p>Views shouldn't have any flow logic, application logic or business rules.<br>The only logic you should have in the view is in relation to the displaying of data.<br>The view should never go out and get information from somewhere else.</p>
<span class="ms-rteCustom-CodeArea">@&#123; var theMonth = DateTime.Now.Month; &#125;<br>&lt;p&gt;The numeric value of the current month&#58; @theMonth&lt;/p&gt;<br><br>@&#123;<br>var outsidetempinfahrenheit = ((9.0 / 5.0) * model.outsideTemp) + 32;<br>var weatherMessage = &quot;Hello, it is &quot; + outsidetempinfahrenheit + &quot; <br>degrees.&quot;;<br>&#125;<br>&lt;p&gt;Today's weather&#58; @weatherMessage&lt;/p&gt; </span><span class="ms-rteCustom-FigureBad">Figure&#58; Business logic is mixed in with the view</span> <span class="ms-rteCustom-CodeArea">@&#123; var theMonth = DateTime.Now.Month; &#125;<br>&lt;p&gt;The numeric value of the current month&#58; @theMonth&lt;/p&gt;<br><br>@&#123;<br>var weatherMessage = &quot;Hello, it is &quot; + model.outsideTemp + &quot; degrees.&quot;;<br>&#125;<br>&lt;p&gt;Today's weather&#58; @weatherMessage&lt;/p&gt;<br></span><span class="ms-rteCustom-FigureGood">Figure&#58; The logic is related to the displaying of data only</span> <h2>Fat Model</h2>
<p>So where do we put all the logic? The answer of course is in the model, hence the name fat model.</p>


