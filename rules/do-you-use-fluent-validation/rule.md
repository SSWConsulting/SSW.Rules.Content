---
type: rule
archivedreason: 
title: Do you use Fluent Validation?
guid: 376bf9f4-c174-4582-936a-518899200084
uri: do-you-use-fluent-validation
created: 2019-01-07T18:39:08.0000000Z
authors:
- id: 34
  title: Brendan Richards
related: []

---

Client-side validation provides a great user experience but this must always be backed up by server-side validation.

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="cartoon-client-side-validation.jpg" alt="cartoon-client-side-validation.jpg">&lt;/dt&gt;<dd>Figure: Client-side validation does not provide effective data security for your Web API endpoints</dd></dl>
**.NET** and **.NET Core Web APIs** provide built-in support for validation using Data Annotations:

1. Decorate your model classes with validation attributes, e.g. [Required], [MaxLength(60)]
2. The MVC data binding system will automatically validate all entities sent to a controller and set ModelState.IsValid and ModelState.Values / Errors
3. As per [Do You Apply the ValidateModel Attribute to All Controllers?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=66e27ee9-7734-4cbd-8d40-ec6ff492fe59)  you can create an attribute to apply this validation to all your Web API endpoints


**Fluent Validation** improves the built-in capabilities in a number of ways:

1. It is outside of your ApiController, so can be shared with other API protocols (like GraphQL or gRPC).
2. It plugs directly into the existing data binding and validation engine (as above) so you can adopt Fluent Validation without changing the client side
3. It is also easy to apply Fluent Validation to inner layers of your application
4. You can specify multiple rulesets for a model without modifying the model itself
5. Fluent validation uses a powerful Fluent API with LINQ expressions
    using FluentValidation;

public class CustomerValidator: AbstractValidator<customer> {<br>  public CustomerValidator() {<br>    RuleFor(x => x.Surname).NotEmpty();<br>    RuleFor(x => x.Forename).NotEmpty().WithMessage("Please specify a first name");<br>    RuleFor(x => x.Discount).NotEqual(0).When(x => x.HasDiscount);<br>    RuleFor(x => x.Address).Length(20, 250);<br>    RuleFor(x => x.Postcode).Must(BeAValidPostcode).WithMessage("Please specify a valid postcode");<br>  }<br><br>  private bool BeAValidPostcode(string postcode) {<br>    // custom postcode validating logic goes here<br>  }<br>}<br></customer>


::: good
Good example: Fluent Validation uses LINQ expressions allowing the development of powerful, type-checked rulesets without needing to modify the class under validation. 
:::
6. You can write conditional rules with the  **.When** clause. This is great for complex form validation.
    RuleFor(x => x.Discount).NotEqual(0).When(x => x.HasDiscount);


::: good
Good Example: Conditional validation with the .When() clause allows for complex logic such as “Discount number cannot be 0 if the HasDiscount boolean is true” 
:::
7. Fluent Validation provides a great entry-point for writing your own custom, complex rules.    For most modern Web APIs the response type is usually JSON. The validation errors raised by Fluent Validation serialize easily to JSON making it fairly trivial to handle these errors from whatever client-side framework you are using.
    {
  "CompanyName": [
    "The CompanyName field is required."
  ]
}


::: good
Good Example: This is the JSON returned from Fluent Validation when a validation rule fails. This is exactly the same format as what would be returned by the built-in ModelState validation.
:::
