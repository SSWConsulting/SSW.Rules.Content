---
seoDescription: The best approach to validate client requests is to use a MediatR pipeline behavior that automatically validates all incoming requests and throws a ValidationException if the request is invalid.
type: rule
archivedreason:
title: Do you know the best approach to validate your client requests?
guid: af4d79b0-e678-4f82-bf92-be7c3a99532e
uri: the-best-approach-to-validate-your-client-requests
created: 2019-04-14T22:49:00.0000000Z
authors:
  - title: Jason Taylor
    url: https://ssw.com.au/people/jason-taylor
related: []
redirects:
  - do-you-know-the-best-approach-to-validate-your-client-requests
---

When building Web APIs, it is important to validate each request to ensure that it meets all expected pre-conditions. The system should process valid requests but return an error for any invalid requests. In the case of ASP.NET Controllers, such validation could be implemented as follows:

<!--endintro-->

::: bad  
![Figure: Bad Example - Managing Request Validation within the Controller](validate-client-requests-bad.png)  
:::

In the above example, model state validation is used to ensure the request is validated before it is sent using MediatR. I am sure you are wondering - why is this a bad example? Because in the case of creating products, we want to validate every request to create a product, not just those that come through the Web API. For example, if we're creating products using a console application that invokes the command directly, we need to ensure that those requests are valid too. So clearly the responsibility for validating requests does not belong within the Web API, but rather in a deeper layer, ideally just before the request is actioned.

One approach to solving this problem is to move validation to the Application layer, validate immediately before the request is executed. In the case of the above example, this could be implemented as follows:

![Figure: OK Example - Validation Handled Manually within Request Handler Ensuring All Requests are Validated](validate-client-requests-ok.png)

The above implementation solves the problem. Whether the request originates from the Web API or a console app it will be validated before further processing occurs. However, the above code is boilerplate and will need to be repeated for each and every request that requires validation. And of course, it will only work if the developer remembers to include the validation check in the first place!

Fortunately, if you are following our recommendations and combining CQRS with MediatR you can solve this problem by incorporating the following behaviour into your MediatR pipeline:

::: good  
![Figure: Good Example - Automatically Validate All Requests By Using a MediatR Pipeline Behaviour](validate-client-requests-good.png)  
:::

This **RequestValidationBehavior** class will automatically validate all incoming requests and throw a **ValidationException** should the request be invalid. This is the best and easiest approach since existing requests, and new requests added later, will be automatically validated. This is possible through the power of MediatR pipeline behaviours. The documentation for MediatR includes a section on Behaviours; https://github.com/jbogard/MediatR/wiki/Behaviors. Review this documentation to understand how you can enhance your request handlers with behaviours and how to register pipeline behaviours.

The only step that remains is handle any validation exceptions. Within the console app, a try catch block will suffice. The action taken within the catch block will of course depend on requirements. Within the Web API, use an **ExceptionFilterAttribute** to catch these exceptions and convert them into a **BadRequest** result as follows:

::: good  
![Figure: Good Example – Use an ExceptionFilterAttribute to Catch and Handle Exceptions within the Web API](validate-client-requests-good-2.png)  
:::
