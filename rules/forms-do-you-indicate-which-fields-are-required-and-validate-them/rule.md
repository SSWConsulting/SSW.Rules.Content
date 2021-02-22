---
type: rule
archivedreason: 
title: Forms - Do you indicate which fields are required and validate them?
guid: 85f4b24e-a56b-4601-acdc-aa24e56ec395
uri: forms-do-you-indicate-which-fields-are-required-and-validate-them
created: 2014-12-04T19:32:54.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


<p>Always indicate which fields are required. Users get frustrated when they experience a wasted trip to the server, just because they did not get an obvious indication of what was required first time around.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><img src="Required-field_Bad-example.jpg" alt="Bad example of Web Sites Required Fields" /></dt><dd>Figure: Bad example - No visual indication for required fields when a user first sees the form</dd></dl><p>A designer will know the best way to indicate required field depending on the layout. However if you are in doubt and don’t have a designer around, a red asterisk is definitely the best option.</p><dl class="goodImage"><dt><img src="Redstar_Good-example.jpg" alt="Use a simple asterisk character" /></dt><dd>Figure: Good Example - A visual indication of what fields are required (use a red asterisk if you are not a designer)</dd></dl><h4>More Information</h4><p>You should combine these visual indicators with appropriate client and server side validators to make sure that your data conforms to business requirements. Adding a RequiredFieldValidator to the above textboxes gives you data validity check with minimal coding.</p><dl class="badImage"><dt><p class="ssw15-rteElement-CodeArea">&lt;asp:Textbox runat="Server" ID="email" /&gt;</p></dt><dd>Figure: Bad Example - No validator used, so the user won't know the email is required</dd></dl><dl class="goodImage"><dt><p class="ssw15-rteElement-CodeArea">&lt;asp:Textbox runat="Server" ID="email"/&gt;
    <br>&lt;asp:RequiredFieldValidator runat="Server" ControlToValidate="email" ErrorMessage="Please enter an email address"
    <br>ID="emailReqValidator" /&gt;</p></dt><dd>Figure: Good Example - an ASP.NET validator in use, to indicate the fields required</dd></dl><div class="greyBox"><p><strong>Note: </strong>For ASP.NET Dynamic Data although validation is done differently (under the covers it is using a field template + the ASP.NET validator).​</p></div>


