---
type: rule
title: Forms - Do you indicate which fields are required and validate them?
uri: forms---do-you-indicate-which-fields-are-required-and-validate-them
created: 2014-12-04T19:32:54.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Always indicate which fields are required. Users get frustrated when they experience a wasted trip to the server, just because they did not get an obvious indication of what was required first time around.</p> </span>

<dl class="badImage"><dt><img src="/PublishingImages/Required-field_Bad-example.jpg" alt="Bad example of Web Sites Required Fields" /></dt><dd>Figure&#58; Bad example - No visual indication for required fields when a user first sees the form</dd></dl><p>A designer will know the best way to indicate required field depending on the layout. However if you are in doubt and don’t have a designer around, a red asterisk is definitely the best option.</p><dl class="goodImage"><dt><img src="/PublishingImages/Redstar_Good-example.jpg" alt="Use a simple asterisk character" /></dt><dd>Figure&#58; Good Example - A visual indication of what fields are required (use a red asterisk if you are not a designer)</dd></dl><h4>More Information</h4><p>You should combine these visual indicators with appropriate client and server side validators to make sure that your data conforms to business requirements. Adding a RequiredFieldValidator to the above textboxes gives you data validity check with minimal coding.</p><dl class="badImage"><dt><p class="ssw15-rteElement-CodeArea">&lt;asp&#58;Textbox runat=&quot;Server&quot; ID=&quot;email&quot; /&gt;</p></dt><dd>Figure&#58; Bad Example - No validator used, so the user won't know the email is required</dd></dl><dl class="goodImage"><dt><p class="ssw15-rteElement-CodeArea">&lt;asp&#58;Textbox runat=&quot;Server&quot; ID=&quot;email&quot;/&gt;
    <br>&lt;asp&#58;RequiredFieldValidator runat=&quot;Server&quot; ControlToValidate=&quot;email&quot; ErrorMessage=&quot;Please enter an email address&quot;
    <br>ID=&quot;emailReqValidator&quot; /&gt;</p></dt><dd>Figure&#58; Good Example - an ASP.NET validator in use, to indicate the fields required</dd></dl><div class="greyBox"><p><strong>Note&#58; </strong>For ASP.NET Dynamic Data although validation is done differently (under the covers it is using a field template + the ASP.NET validator).​</p></div>


