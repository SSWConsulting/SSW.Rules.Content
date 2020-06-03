---
type: rule
title: Do You Apply the ValidateModel Attribute to All Controllers?
uri: do-you-apply-the-validatemodel-attribute-to-all-controllers
created: 2014-11-05T18:42:04.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> Web API does not automatically return an error to the client when validation fails. It is up to the controller action to check the model state and respond appropriately. </span>

<p>​You can also create an action filter to check the model state before the controller action is invoked.​</p><dl class="image"><p class="ssw15-rteElement-CodeArea">using System.Collections.Generic;<br> using System.Linq;<br> using System.Net;<br> using System.Net.Http;<br> using System.Web.Http.Controllers;<br> using System.Web.Http.Filters;<br> using System.Web.Http.ModelBinding;<br> 
      <br> namespace MyApi.Filters<br> &#123;<br> public class ValidateModelAttribute &#58; ActionFilterAttribute<br> &#123;<br> public override void OnActionExecuting(HttpActionContext actionContext)<br> &#123;<br> if (actionContext.ModelState.IsValid == false)<br> &#123;<br> actionContext.Response = actionContext.Request.CreateErrorResponse(<br> HttpStatusCode.BadRequest, actionContext.ModelState);<br> &#125;<br> &#125;<br> &#125;<br> &#125;​ </p><dd>Figure&#58; If model validation fails, this filter returns an HTTP response that contains the validation errors. In that case, the controller action is not invoked</dd></dl><dl class="badImage"><p class="ssw15-rteElement-CodeArea">public class ProductsController &#58; ApiController<br> &#123;<br> [ValidateModel]<br> public HttpResponseMessage Post(Product product)<br> &#123;<br> // ...<br> &#125;<br> &#125; </p><dd>Figure&#58; Bad Example - Set the filter as an attribute on individual controllers or controller actions</dd></dl><dl class="goodImage"><p class="ssw15-rteElement-CodeArea">public static class WebApiConfig<br>
    &#123;<br>
        public static void Register(HttpConfiguration config)<br>
        &#123;<br>
            config.Filters.Add(new ValidateModelAttribute());<br>
<br>
            // ...<br>
        &#125;<br>
&#125;
</p><dd>Figure&#58; Good Example - Add an instance of the filter to the ​HttpConfiguration.Filterscollection to apply this filter to all Web API controllers</dd></dl>


