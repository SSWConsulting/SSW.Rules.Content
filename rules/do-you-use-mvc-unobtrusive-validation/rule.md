---
type: rule
title: Do you use MVC Unobtrusive Validation?
uri: do-you-use-mvc-unobtrusive-validation
created: 2013-12-12T05:01:16.0000000Z
authors:
- id: 34
  title: Brendan Richards

---



<span class='intro'> Validation is an important part of any data driven web application. Client-Side validation provides fast user feedback and a better UI experiance but cannot be relied on&#160;for data integrity - so cient-side validation should always be backup up with additional server-side validation.<br>With MVC Unobtrusive Valilidation, you can configure both client-side and server-side in one place.&#160; </span>

<p>​Validation rules can be added to a model object via Data Annotations or using the Fluent Validation API. <br>Fluent Validation is <a href="http&#58;//www.nuget.org/packages/FluentValidation/">available as a Nuget package</a>.</p><p><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/DataAttributes.png" alt="DataAttributes.png" style="margin&#58;5px;" /><br></p><dd class="ssw15-rteElement-FigureGood">OK Example&#58; Data Annotation attributes decorate model properties to make them required</dd><p><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/FluentValidation.png" alt="FluentValidation.png" style="margin&#58;5px;width&#58;650px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Better Example&#58; Fluent Validation allows validation meta data to be added to a class without modifying the&#160;original class.&#160;&#160;This provides much more flexibility for code reuse.</dd><p><br></p><p>If you create a new MVC web application in VisualStudio 2013, unobtrusive validation will be enabled by default. Otherwise it's simple to <a href="http&#58;//www.nuget.org/packages/Microsoft.jQuery.Unobtrusive.Validation/">install from Nuget​</a>.&#160;To use it simply&#58;</p><ol><li><span style="line-height&#58;1.6;">Bind your razor views&#160;to model objects&#160;</span><br></li><li><span style="line-height&#58;1.6;">Use Html Helpers to render the form UI​<br><br></span></li></ol><div><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/view.png" alt="view.png" style="margin&#58;5px;" /><br></div><dd class="ssw15-rteElement-FigureGood">Good Example&#58; this razor view binds to a stronly typed model object and uses html helpers.</dd><div><br></div><div><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/Html.png" alt="Html.png" style="margin&#58;5px;width&#58;650px;" /><br><strong>Figure&#58; the HTML UI rendered for this view now has data-validation&#160;attributes that are followed by JQuery validation to provide rich client-side validation.</strong></div><div><br></div><div><img src="/SoftwareDevelopment/RulesToBetterMVC/PublishingImages/SaveAction.png" alt="SaveAction.png" style="margin&#58;5px;" /><br></div><div><strong>Figure&#58; On the server-side, the same validation rules will be checked when you call ModelState.IsValid</strong></div><div><br></div><p><br></p>


