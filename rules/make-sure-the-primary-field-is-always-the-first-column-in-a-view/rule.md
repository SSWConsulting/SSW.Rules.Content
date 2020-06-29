---
type: rule
archivedreason: 
title: Do you make sure the Primary Field is always the first column in a view?
guid: 2d7b56ea-cd7d-4b02-950b-ba4a662594ee
uri: make-sure-the-primary-field-is-always-the-first-column-in-a-view
created: 2020-06-29T21:32:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-make-sure-the-primary-field-is-always-the-first-column-in-a-view

---


When modifying existing or creating custom views in Dynamics (or Model-driven PowerApps) always pay special attention to the first column. The first column should always contain the Primary Field for the entity that the view is based on. For example, all views for Opportunities should use Topic (name), Contacts should use Full Name (fullname)&#160;as the first column.<br><br>The reason for this is the Primary Field in a view displays as a hyperlink to the underlying record. It is very convenient (and natural) to click the first item in the view, as this will then take you to the record. If any other field is used the user will either need to double click the row to navigate to the record (non-lookup) or will be taken to a completely different entities record (lookup field).<br><br>Some examples below&#58;<br><br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><img src="/PublishingImages/bad-primary-field.png" alt="bad-primary-field.png" style="width&#58;750px;" /></dt><dd>Bad Example&#58; A lookup field is the first column</dd></dl><p>In this example Account is the first column in the view, the natural tendency is the click the first column, and seeing that it's a hyperlink further confirms to the user that this is something they can click on. Clicking the first column (&quot;Northwind Traders&quot;) would navigate to the Northwind Traders Account form and not the Opportunity form for Northwind Traders.</p><dl class="badImage"><dt><img src="/PublishingImages/bad-primary-field-2.png" alt="bad-primary-field-2.png" style="width&#58;750px;" /></dt><dd>Bad Example&#58; A regular field is the first column</dd></dl><p>In this example Probability is the first column in the view, again users tend to click the first column in the view. In this example, a single click would select the entire row (with tick box selected to the left of the grid), and a double click on the first column would navigate to the Opportunity record.</p><dl class="goodImage"><dt><img src="/PublishingImages/good-primary-field.png" alt="good-primary-field.png" style="width&#58;750px;" /></dt><dd>Good Example&#58; Primary Field is the first column</dd></dl><p>In this example, the Primary Field is the first column of the view, and single-clicking the first column view navigates to the opportunity record as expected.</p><h3 class="ssw15-rteElement-H3">​Summary​<br></h3>Understanding column ordering in view is import and making sure the first column in a view is always the Primary Field will make much easier for your users.<p>​<br></p>


