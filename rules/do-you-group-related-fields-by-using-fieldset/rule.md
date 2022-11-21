---
type: rule
archivedreason: 
title: Do you group related fields by using FieldSet?
guid: 733a5e44-94b1-4226-99c6-ba94b27d0eb4
uri: do-you-group-related-fields-by-using-fieldset
created: 2014-12-22T11:52:59.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

**FieldSet** element allows you to group thematically related controls and labels. Grouping controls makes forms more accessible and easier for users to understand the purpose of filling the forms.

See the example below using "Your Details" and "Event Details".

<!--endintro-->

::: good  
![Figure: Good example - Use FieldSet for grouping](fieldset.jpg)  
:::

Here's an example of how FieldSet works:

``` html
<fieldset>
    <legend>Your Details</legend>
    <p>
        <label for="FirstName">First Name: </label>
        <input id="FirstName" type="text" /><br />
        <label for="LastName">Last Name: </label>
        <input id="LastName" type="text" /><br />
        <label for="EmailAddress">Email Address: </label>
        <input id="EmailAddress" type="text" />
    </p>
</fieldset>
```
**Figure: Example code of FieldSet**

![Figure: How that code will look on the browser](fieldset-browser.jpg)  

Things to remember:

1. Wrap logical control groups in a &lt;fieldset&gt;.
2. The first child of a &lt;fieldset&gt; should be a &lt;legend&gt;, so the user knows what to expect in that section.
