---
type: rule
archivedreason: 
title: Do you group related fields by using FieldSet?
guid: 733a5e44-94b1-4226-99c6-ba94b27d0eb4
uri: do-you-group-related-fields-by-using-fieldset
created: 2014-12-22T11:52:59.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p><strong>​FieldSet</strong> element allows you to group thematically related controls
                    and labels. Grouping controls makes forms more accessible and easier for users to
                    understand the purpose of filling the forms.</p><p>See the example below using "Your Details"
                    and "Event Details".</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="goodImage"><dt> 
      <img src="fieldset.jpg" alt="" /> 
   </dt><dd>Figure: Good example - Use FieldSet for grouping</dd><dd></dd></dl><p>Here's an example of how FieldSet works:</p><dl class="code"><dt><pre><fieldset>
    <legend>Your Details</legend>
    <p>
        <label for="FirstName">First Name: </label>
        <input id="FirstName" type="text" /><br />
        <label for="LastName">Last Name: </label>
        <input id="LastName" type="text" /><br />
        <label for="EmailAddress">Email Address: </label>
        <input id="EmailAddress" type="text" />
    </p>
</fieldset></pre></dt><dd>Figure: Example code of FieldSet</dd></dl><dl class="image">​ 
   <dt> 
      <img src="fieldset-browser.jpg" alt="" /> 
   </dt><dd>Figure: How that code will look on the browser</dd><dd></dd></dl><p>​ Things to remember:</p><ol><li>Wrap logical control groups in a <fieldset>.</li><li>The first child of a <fieldset> should be a <legend>, so the user knows what to expect in that section.</li></ol>​


