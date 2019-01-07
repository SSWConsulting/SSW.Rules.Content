---
type: rule
title: Do you use Fluent Validation?
uri: do-you-use-fluent-validation
created: 2019-01-07T18:39:08.0000000Z
authors:
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p class="ssw15-rteElement-P">Client-side validation provides a great user experience but this must always be backed up by server-side validation. <br></p> </span>

<dl class="image"><dt><img src="/PublishingImages/cartoon-client-side-validation.jpg" alt="cartoon-client-side-validation.jpg" /></dt><dd>Figure&#58; Client-side validation does not provide effective data security for your Web API endpoints</dd></dl><p>
   <b>.NET </b>and<b> .NET Core Web APIs</b> provide built-in support for validation using Data Annotations&#58;</p><ol><li>Decorate your model classes with validation attributes, e.g. [Required], [MaxLength(60)]<br></li><li>The MVC data binding<span style="color&#58;#444444;"> system will automatically validate all entities sent to a controller and set ModelState.IsValid and ModelState.Values / Errors</span><br></li><li>As per&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=66e27ee9-7734-4cbd-8d40-ec6ff492fe59">Do You Apply the ValidateModel Attribute to All Controllers? </a> <span style="color&#58;#444444;">&#160;you can create an attribute to apply this validation to all your Web API endpoints</span><br></li></ol><p class="ssw15-rteElement-P">
   <b>Fluent Validation</b> improves the built-in capabilities in a number of ways&#58;</p><ol><li>It plugs directly into the existing data binding and validation engine (as above) so you can adopt Fluent Validation without changing the client side<br></li><li>It is also easy to apply Fluent Validation to inner layers of your application<br></li><li>You can specify multiple rulesets for a model without modifying the model itself<br></li><li>Fluent validation uses a powerful Fluent API with LINQ expressions<br>
<p class="ssw15-rteElement-CodeArea">using FluentValidation;<br><br>public class CustomerValidator&#58; AbstractValidator&lt;Customer&gt; &#123;<br>&#160; public CustomerValidator() &#123;<br>&#160;&#160;&#160; RuleFor(x =&gt; x.Surname).NotEmpty();<br>&#160;&#160;&#160; RuleFor(x =&gt; x.Forename).NotEmpty().WithMessage(&quot;Please specify a first name&quot;);<br>&#160;&#160;&#160; RuleFor(x =&gt; x.Discount).NotEqual(0).When(x =&gt; x.HasDiscount);<br>&#160;&#160;&#160; RuleFor(x =&gt; x.Address).Length(20, 250);<br>&#160;&#160;&#160; RuleFor(x =&gt; x.Postcode).Must(BeAValidPostcode).WithMessage(&quot;Please specify a valid postcode&quot;);<br>&#160; &#125;<br><br>&#160; private bool BeAValidPostcode(string postcode) &#123;<br>&#160;&#160;&#160; // custom postcode validating logic goes here<br>&#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">Good example&#58; Fluent Validation uses LINQ expressions allowing the development of powerful, type-checked rulesets without needing to modify the class under validation.&#160;</dd></li><li>You can write conditional rules with the <b>.When</b> clause. This is great for complex form validation.<br>
<p class="ssw15-rteElement-CodeArea">&#160;&#160;&#160; RuleFor(x =&gt; x.Discount).NotEqual(0).When(x =&gt; x.HasDiscount);<br><br></p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; Conditional validation with the .When() clause allows for complex logic such as “Discount number cannot be 0 if the HasDiscount boolean is true”&#160;</dd></li><li>Fluent Validation provides a great entry-point for writing your own custom, complex rules.<p>For most modern Web APIs the response type is usually JSON. The validation errors raised by Fluent Validation serialize easily to JSON making it fairly trivial to handle these errors from whatever client-side framework you are using.<br></p><p class="ssw15-rteElement-CodeArea">&#123;<br>&#160; &quot;CompanyName&quot;&#58; [<br>&#160;&#160;&#160; &quot;The CompanyName field is required.&quot;<br>&#160; ]<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; This is the JSON returned from Fluent Validation when a validation rule fails. This is exactly the same format as what would be returned by the built-in ModelState validation.</dd></li></ol>​<br>


