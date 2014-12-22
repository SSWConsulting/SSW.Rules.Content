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
                    understand the purpose of filling the forms.</p><p>See the example below using &quot;Your Details&quot;
                    and &quot;Event Details&quot;.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="goodImage"><dt> 
      <img src="/PublishingImages/fieldset.jpg" alt="" /> 
   </dt><dd>Figure&#58; Good example - Use FieldSet for grouping</dd><dd></dd></dl><p>Here's an example of how FieldSet works&#58;</p><dl class="code"><dt><pre>{ltHTMLChar}fieldset{gtHTMLChar}
    {ltHTMLChar}legend{gtHTMLChar}Your Details{ltHTMLChar}/legend{gtHTMLChar}
    {ltHTMLChar}p{gtHTMLChar}
        {ltHTMLChar}label for=&quot;FirstName&quot;{gtHTMLChar}First Name&#58; {ltHTMLChar}/label{gtHTMLChar}
        {ltHTMLChar}input id=&quot;FirstName&quot; type=&quot;text&quot; /{gtHTMLChar}{ltHTMLChar}br /{gtHTMLChar}
        {ltHTMLChar}label for=&quot;LastName&quot;{gtHTMLChar}Last Name&#58; {ltHTMLChar}/label{gtHTMLChar}
        {ltHTMLChar}input id=&quot;LastName&quot; type=&quot;text&quot; /{gtHTMLChar}{ltHTMLChar}br /{gtHTMLChar}
        {ltHTMLChar}label for=&quot;EmailAddress&quot;{gtHTMLChar}Email Address&#58; {ltHTMLChar}/label{gtHTMLChar}
        {ltHTMLChar}input id=&quot;EmailAddress&quot; type=&quot;text&quot; /{gtHTMLChar}
    {ltHTMLChar}/p{gtHTMLChar}
{ltHTMLChar}/fieldset{gtHTMLChar}</pre></dt><dd>Figure&#58; Example code of FieldSet</dd></dl><dl class="image">​ 
   <dt> 
      <img src="/PublishingImages/fieldset-browser.jpg" alt="" /> 
   </dt><dd>Figure&#58; How that code will look on the browser</dd><dd></dd></dl><p>​ Things to remember&#58;</p><ol><li>Wrap logical control groups in a {ltHTMLChar}fieldset{gtHTMLChar}.</li><li>The first child of a {ltHTMLChar}fieldset{gtHTMLChar} should be a {ltHTMLChar}legend{gtHTMLChar}, so the user knows what to expect in that section.</li></ol>​


