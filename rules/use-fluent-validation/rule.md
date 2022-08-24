---
type: rule
archivedreason: 
title: Do you use Fluent Validation?
guid: 376bf9f4-c174-4582-936a-518899200084
uri: use-fluent-validation
created: 2019-01-07T18:39:08.0000000Z
authors:
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- do-you-use-fluent-validation

---

Client-side validation provides a great user experience but this must always be backed up by server-side validation.

<!--endintro-->

![Figure: Client-side validation does not provide effective data security for your Web API endpoints](cartoon-client-side-validation.jpg)  

**.NET** and **.NET Core Web APIs** provide built-in support for validation using Data Annotations:

1. Decorate your model classes with validation attributes, e.g. [Required], [MaxLength(60)]
2. The MVC data binding system will automatically validate all entities sent to a controller and set ModelState.IsValid and ModelState.Values / Errors
3. As per [Do you apply the ValidateModel attribute to all controllers?](/do-you-apply-the-validatemodel-attribute-to-all-controllers)  you can create an attribute to apply this validation to all your Web API endpoints

**Fluent Validation** improves the built-in capabilities in a number of ways:

1. It is outside of your ApiController, so can be shared with other API protocols (like GraphQL or gRPC).
2. It plugs directly into the existing data binding and validation engine (as above) so you can adopt Fluent Validation without changing the client-side
3. It is also easy to apply Fluent Validation to inner layers of your application
4. You can specify multiple rulesets for a model without modifying the model itself
5. Fluent validation uses a powerful Fluent API with LINQ expressions

``` cs
using FluentValidation;

public class CustomerValidator: AbstractValidator<Customer> {
  public CustomerValidator() {
    RuleFor(x => x.Surname).NotEmpty();
    RuleFor(x => x.Forename).NotEmpty().WithMessage("Please specify a first name");
    RuleFor(x => x.Discount).NotEqual(0).When(x => x.HasDiscount);
    RuleFor(x => x.Address).Length(20, 250);
    RuleFor(x => x.Postcode).Must(BeAValidPostcode).WithMessage("Please specify a valid postcode");
  }

  private bool BeAValidPostcode(string postcode) {
    // custom postcode validating logic goes here
  }
}
```

::: good
Good example: Fluent Validation uses LINQ expressions allowing the development of powerful, type-checked rulesets without needing to modify the class under validation.  
:::

6. You can write conditional rules with the **.When** clause. This is great for complex form validation.

``` cs
RuleFor(x => x.Discount).NotEqual(0).When(x => x.HasDiscount);
```

::: good
Good Example: Conditional validation with the .When() clause allows for complex logic such as “Discount number cannot be 0 if the HasDiscount boolean is true”  
:::

7. Fluent Validation provides a great entry-point for writing your own custom, complex rules. For most modern Web APIs the response type is usually JSON. The validation errors raised by Fluent Validation serialize easily to JSON making it fairly trivial to handle these errors from whatever client-side framework you are using.

``` json
{
  "CompanyName": [
    "The CompanyName field is required."
  ]
}
```

::: good
Good Example: This is the JSON returned from Fluent Validation when a validation rule fails. This is exactly the same format as what would be returned by the built-in ModelState validation.  
:::
