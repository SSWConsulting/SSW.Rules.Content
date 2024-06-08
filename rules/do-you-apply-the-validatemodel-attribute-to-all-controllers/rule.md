---
type: rule
title: Do You Apply the ValidateModel Attribute to All Controllers?
uri: do-you-apply-the-validatemodel-attribute-to-all-controllers
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
created: 2014-11-05T18:42:04.000Z
archivedreason: "Requested by Matt G under RE: Update [SSW] Rules to Better WebAPI"
guid: 56d03a4a-d4bb-40ee-b49e-1595a937b41f
---

Web API does not automatically return an error to the client when validation fails. It is up to the controller action to check the model state and respond appropriately. 
<!--endintro-->

You can also create an action filter to check the model state before the controller action is invoked.



```cs
using System.Collections.Generic;
 using System.Linq;
 using System.Net;
 using System.Net.Http;
 using System.Web.Http.Controllers;
 using System.Web.Http.Filters;
 using System.Web.Http.ModelBinding;
 
      
 namespace MyApi.Filters
 {
 public class ValidateModelAttribute : ActionFilterAttribute
 {
 public override void OnActionExecuting(HttpActionContext actionContext)
 {
 if (actionContext.ModelState.IsValid == false)
 {
 actionContext.Response = actionContext.Request.CreateErrorResponse(
 HttpStatusCode.BadRequest, actionContext.ModelState);
 }
 }
 }
 }
```


Figure: If model validation fails, this filter returns an HTTP response that contains the validation errors. In that case, the controller action is not invoked


```cs
public class ProductsController : ApiController
 {
 [ValidateModel]
 public HttpResponseMessage Post(Product product)
 {
 // ...
 }
 }
```


Figure: Bad Example - Set the filter as an attribute on individual controllers or controller actions


```cs
public static class WebApiConfig

    {

        public static void Register(HttpConfiguration config)

        {

            config.Filters.Add(new ValidateModelAttribute());



            // ...

        }

}
```


Figure: Good Example - Add an instance of the filter to the HttpConfiguration.Filterscollection to apply this filter to all Web API controllers
