---
type: rule
title: Do you use MVC Unobtrusive Validation?
uri: do-you-use-mvc-unobtrusive-validation
created: 2013-12-12T05:01:16.0000000Z
authors:
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p class="ssw15-rteElement-P">Validation is an important part of any data-driven web application. Client-Side validation provides fast user feedback and a better UI experience but cannot be relied on&#160;for data integrity - so client-side validation should always be backed&#160;by&#160;additional server-side validation.</p><p class="ssw15-rteElement-P">With MVC Unobtrusive Validation, you can configure both client-side and server-side in one place.&#160;</p> </span>

<p class="ssw15-rteElement-P">Validation rules can be added to a model object via Data Annotations or using the Fluent Validation API.</p><p>Fluent Validation is <a href="http&#58;//www.nuget.org/packages/FluentValidation/">available as a Nuget package</a>. See&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=fd57ceac-c551-44dc-b7c3-e6c348919f0d">Do you use Fluent Validation? </a><br><br></p><dl class="image"><dt><img src="/PublishingImages/DataAttributes.png" alt="DataAttributes.png" /></dt><dd>Figure&#58; OK Example - Data Annotation attributes decorate model properties to make them required</dd></dl><dl class="image"><dt><img src="/PublishingImages/FluentValidation.png" alt="FluentValidation.png" style="width&#58;650px;" /></dt><dd>Figure&#58; Better Example - Fluent Validation allows validation metadata to be added to a class without modifying the&#160;original class.&#160;&#160;This provides much more flexibility for code reuse</dd></dl><p>If you create a new MVC web application in VisualStudio 2013, unobtrusive validation will be enabled by default. Otherwise, it's simple to <a href="http&#58;//www.nuget.org/packages/Microsoft.jQuery.Unobtrusive.Validation/">install from Nuget</a>.&#160;To use it simply&#58;</p><ol><li>​Bind your razor views&#160;to model objects&#160;<br></li><li>Use Html Helpers to render the form UI</li></ol>
<dl class="goodImage"> <dt><img src="/PublishingImages/view.png" alt="view.png" /></dt><dd>Figure&#58; Good Example - this razor view binds to a strongly typed model object and uses HTML helpers.</dd></dl><dl class="image"><dt><img src="/PublishingImages/Html.png" alt="Html.png" style="width&#58;650px;" /></dt><dd>Figure&#58; the HTML UI rendered for this view now has data-validation&#160;attributes that are followed by JQuery validation to provide rich client-side validation.</dd></dl><dl class="image"><dt><img src="/PublishingImages/SaveAction.png" alt="SaveAction.png" /></dt><dd>Figure&#58; On the server-side, the same validation rules will be checked when you call ModelState.IsValid</dd></dl>


