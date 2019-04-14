---
type: rule
title: Do you know the best approach to validate your client requests?
uri: do-you-know-the-best-approach-to-validate-your-client-requests
created: 2019-04-14T22:49:00.0000000Z
authors:
- id: 81
  title: Jason Taylor

---



<span class='intro'> <p class="ssw15-rteElement-P">​When building Web APIs, it is important to validate each request to ensure that it meets all expected pre-conditions. The system should process valid requests but return an error for any invalid requests. In the case of ASP.NET Controllers, such validation could be implemented as follows&#58;​<br></p> </span>

<dl class="badImage"><dt>
      <img src="/PublishingImages/validate-client-requests-bad.png" alt="validate-client-requests-bad.png" />
   </dt><dd>Figure&#58; Bad Example - Managing Request Validation within the Controller</dd></dl><p>In the above example, model state validation is used to ensure the request is validated before it is sent using MediatR. I am sure you are wondering - why is this a bad example? Because in the case of creating products, we want to validate every request to create a product, not just those that come through the Web API. For example, if we're creating products using a console application that invokes the command directly, we need to ensure that those requests are valid too. So clearly the responsibility for validating requests does not belong within the Web API, but rather in a deeper layer, ideally just before the request is actioned.</p><p>One approach to solving this problem is to move validation to the Application layer, validate immediately before the request is executed. In the case of the above example, this could be implemented as follows&#58;</p><dl class="image"><dt>
      <img src="/PublishingImages/validate-client-requests-ok.png" alt="validate-client-requests-ok.png" />
   </dt><dd>Figure&#58; OK Example - Validation Handled Manually within Request Handler Ensuring All Requests are Validated</dd></dl><p>The above implementation solves the problem. Whether the request originates from the Web API or a console app it will be validated before further processing occurs. However, the above code is boilerplate and will need to be repeated for each and every request that requires validation. And of course, it will only work if the developer remembers to include the validation check in the first place!<br>&#160;<br>Fortunately, if you are following our recommendations and combining CQRS with MediatR you can solve this problem by incorporating the following behaviour into your MediatR pipeline&#58;</p><dl class="goodImage"><dt>
      <img src="/PublishingImages/validate-client-requests-good.png" alt="validate-client-requests-good.png" />
   </dt><dd>Figure&#58; Good Example - Automatically Validate All Requests By Using a MediatR Pipeline Behaviour</dd></dl><p>This 
   <strong>RequestValidationBehavior</strong> class will automatically validate all incoming requests and throw a 
   <strong>ValidationException</strong> should the request be invalid. This is the best and easiest approach since existing requests, and new requests added later, will be automatically validated. This is possible through the power of MediatR pipeline behaviours. The documentation for MediatR includes a section on Behaviours; 
   <a href="https&#58;//github.com/jbogard/MediatR/wiki/Behaviors">https&#58;//github.com/jbogard/MediatR/wiki/Behaviors</a>. Review this documentation to understand how you can enhance your request handlers with behaviours and how to register pipeline behaviours.​<br></p><p>The only step that remains is handle any validation exceptions. Within the console app, a try catch block will suffice. The action taken within the catch block will of course depend on requirements. Within the Web API, use an 
   <strong>ExceptionFilterAttribute</strong> to catch these exceptions and convert them into a 
   <strong>BadRequest </strong>result as follows&#58;<br></p><dl class="goodImage"><dt>
      <img src="/PublishingImages/validate-client-requests-good-2.png" alt="validate-client-requests-good-2.png" />
   </dt><dd>Figure&#58; Good Example – Use an ExceptionFilterAttribute to Catch and Handle Exceptions within the Web API</dd></dl>​


