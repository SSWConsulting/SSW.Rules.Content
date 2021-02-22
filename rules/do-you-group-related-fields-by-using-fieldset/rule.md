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


<p><strong>​FieldSet</strong> element allows you to group thematically related controls
                    and labels. Grouping controls makes forms more accessible and easier for users to
                    understand the purpose of filling the forms.</p><p>See the example below using "Your Details"
                    and "Event Details".</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="goodImage"><dt> 
      <img src="fieldset.jpg" alt="" /> 
   </dt><dd>Figure: Good example - Use FieldSet for grouping</dd><dd></dd></dl><p>Here's an example of how FieldSet works:</p><dl class="code"><dt><pre>&lt;fieldset&gt;
    &lt;legend&gt;Your Details&lt;/legend&gt;
    &lt;p&gt;
        &lt;label for="FirstName"&gt;First Name: &lt;/label&gt;
        &lt;input id="FirstName" type="text" /&gt;&lt;br /&gt;
        &lt;label for="LastName"&gt;Last Name: &lt;/label&gt;
        &lt;input id="LastName" type="text" /&gt;&lt;br /&gt;
        &lt;label for="EmailAddress"&gt;Email Address: &lt;/label&gt;
        &lt;input id="EmailAddress" type="text" /&gt;
    &lt;/p&gt;
&lt;/fieldset&gt;</pre></dt><dd>Figure: Example code of FieldSet</dd></dl><dl class="image">​ 
   <dt> 
      <img src="fieldset-browser.jpg" alt="" /> 
   </dt><dd>Figure: How that code will look on the browser</dd><dd></dd></dl><p>​ Things to remember:</p><ol><li>Wrap logical control groups in a &lt;fieldset&gt;.</li><li>The first child of a &lt;fieldset&gt; should be a &lt;legend&gt;, so the user knows what to expect in that section.</li></ol>​


