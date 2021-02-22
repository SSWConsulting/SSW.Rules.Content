---
type: rule
archivedreason: 
title: Do you use Thin controllers, Fat models and Dumb views?
guid: 34f6ddc4-1906-4baa-b4ac-5aa37e308e9c
uri: do-you-use-thin-controllers-fat-models-and-dumb-views
created: 2012-07-18T17:54:57.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

## Thin Controllers

You need to think of a controller as more of a coordinator than a controller. 
It is responsible for calling the business layer and passing from the business layer to the view. 
It is also responsible for process flow.

<!--endintro-->
public ActionResult Details(decimal todaysWeather)
{
var todaysWeatherInFarhenheit = ((9.0 / 5.0) \* todaysWeather) + 32;
return View(todaysWeatherInFarhenheit); }
Figure: Business logic is mixed up within the controller making it fatter than it should be public ActionResult Index()
{
var todaysWeather = weatherDB.Today.ToList();
return View(todaysWeather);
} Figure: The controller is co-ordinating between the business layer and the view public ActionResult Details(int? id)
{
if (!id.HasValue)
return RedirectToAction("Index");

return View();
} Figure: The controller is co-ordinating process flow (directing traffic) 
## Dumb Views

Views shouldn't have any flow logic, application logic or business rules.
The only logic you should have in the view is in relation to the displaying of data.
The view should never go out and get information from somewhere else.
@{ var theMonth = DateTime.Now.Month; }
&lt;p&gt;The numeric value of the current month: @theMonth&lt;/p&gt;

@{
var outsidetempinfahrenheit = ((9.0 / 5.0) \* model.outsideTemp) + 32;
var weatherMessage = "Hello, it is " + outsidetempinfahrenheit + " 
degrees.";
}
&lt;p&gt;Today's weather: @weatherMessage&lt;/p&gt; Figure: Business logic is mixed in with the view @{ var theMonth = DateTime.Now.Month; }
&lt;p&gt;The numeric value of the current month: @theMonth&lt;/p&gt;

@{
var weatherMessage = "Hello, it is " + model.outsideTemp + " degrees.";
}
&lt;p&gt;Today's weather: @weatherMessage&lt;/p&gt;
Figure: The logic is related to the displaying of data only 
## Fat Model

So where do we put all the logic? The answer of course is in the model, hence the name fat model.
