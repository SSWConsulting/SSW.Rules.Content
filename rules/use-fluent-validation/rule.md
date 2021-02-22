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


<p class="ssw15-rteElement-P">​Client-side validation provides a great user experience but this must always be backed up by server-side validation. <br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="cartoon-client-side-validation.jpg" alt="cartoon-client-side-validation.jpg" /></dt><dd>Figure: Client-side validation does not provide effective data security for your Web API endpoints</dd></dl><p>
   <b>.NET </b>and<b> .NET Core Web APIs</b> provide built-in support for validation using Data Annotations:</p><ol><li>Decorate your model classes with validation attributes, e.g. [Required], [MaxLength(60)]<br></li><li>The MVC data binding<span style="color:#444444;"> system will automatically validate all entities sent to a controller and set ModelState.IsValid and ModelState.Values / Errors</span><br></li><li>As per <a href=/do-you-apply-the-validatemodel-attribute-to-all-controllers>Do You Apply the ValidateModel Attribute to All Controllers? </a> <span style="color:#444444;"> you can create an attribute to apply this validation to all your Web API endpoints</span><br></li></ol><p class="ssw15-rteElement-P">
   <b>Fluent Validation</b> improves the built-in capabilities in a number of ways:</p><ol><li>It is outside of your ApiController, so can be shared with other API protocols (like GraphQL or gRPC).<br></li><li>It plugs directly into the existing data binding and validation engine (as above) so you can adopt Fluent Validation without changing the client side<br></li><li>It is also easy to apply Fluent Validation to inner layers of your application<br></li><li>You can specify multiple rulesets for a model without modifying the model itself<br></li><li>Fluent validation uses a powerful Fluent API with LINQ expressions<br>
<p class="ssw15-rteElement-CodeArea">using FluentValidation;<br><br>public class CustomerValidator: AbstractValidator&lt;Customer&gt; {<br>  public CustomerValidator() {<br>    RuleFor(x =&gt; x.Surname).NotEmpty();<br>    RuleFor(x =&gt; x.Forename).NotEmpty().WithMessage("Please specify a first name");<br>    RuleFor(x =&gt; x.Discount).NotEqual(0).When(x =&gt; x.HasDiscount);<br>    RuleFor(x =&gt; x.Address).Length(20, 250);<br>    RuleFor(x =&gt; x.Postcode).Must(BeAValidPostcode).WithMessage("Please specify a valid postcode");<br>  }<br><br>  private bool BeAValidPostcode(string postcode) {<br>    // custom postcode validating logic goes here<br>  }<br>}<br></p><dd class="ssw15-rteElement-FigureGood">Good example: Fluent Validation uses LINQ expressions allowing the development of powerful, type-checked rulesets without needing to modify the class under validation. </dd></li><li>You can write conditional rules with the <b>.When</b> clause. This is great for complex form validation.<br>
<p class="ssw15-rteElement-CodeArea">    RuleFor(x =&gt; x.Discount).NotEqual(0).When(x =&gt; x.HasDiscount);<br><br></p><dd class="ssw15-rteElement-FigureGood">Good Example: Conditional validation with the .When() clause allows for complex logic such as “Discount number cannot be 0 if the HasDiscount boolean is true” </dd></li><li>Fluent Validation provides a great entry-point for writing your own custom, complex rules.<p>For most modern Web APIs the response type is usually JSON. The validation errors raised by Fluent Validation serialize easily to JSON making it fairly trivial to handle these errors from whatever client-side framework you are using.<br></p><p class="ssw15-rteElement-CodeArea">{<br>  "CompanyName": [<br>    "The CompanyName field is required."<br>  ]<br>}</p><dd class="ssw15-rteElement-FigureGood">Good Example: This is the JSON returned from Fluent Validation when a validation rule fails. This is exactly the same format as what would be returned by the built-in ModelState validation.</dd></li></ol>​<br>


