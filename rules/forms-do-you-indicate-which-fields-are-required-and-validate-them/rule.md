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

Always indicate which fields are required. Users get frustrated when they experience a wasted trip to the server, just because they did not get an obvious indication of what was required first time around.

<!--endintro-->

::: bad  
![Figure: Bad example - No visual indication for required fields when a user first sees the form](Required-field\_Bad-example.jpg)  
:::

A designer will know the best way to indicate required field depending on the layout. However if you are in doubt and don’t have a designer around, a red asterisk is definitely the best option.

::: good  
![Figure: Good Example - A visual indication of what fields are required (use a red asterisk if you are not a designer)](Redstar\_Good-example.jpg)  
:::

### More information on ASP.NET implementation

You should combine these visual indicators with appropriate client and server side validators to make sure that your data conforms to business requirements. Adding a RequiredFieldValidator to the above textboxes gives you data validity check with minimal coding.

``` aspnet
<asp:Textbox runat="Server" ID="email" />
```
::: bad
Figure: Bad Example - No validator used, so the user won't know the email is required
:::

``` aspnet
<asp:Textbox runat="Server" ID="email"/>
    
<asp:RequiredFieldValidator runat="Server" ControlToValidate="email" ErrorMessage="Please enter an email address"
    
ID="emailReqValidator" />
```
::: good
Figure: Good Example - an ASP.NET validator in use, to indicate the fields required
:::

**Note:** For ASP.NET Dynamic Data although validation is done differently (under the covers it is using a field template + the ASP.NET validator).
