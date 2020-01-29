---
type: rule
archivedreason: 
title: Do you avoid using magic string when referencing property/variable names
guid: 9a58915a-96bb-4b3d-9a1f-9492610d6ffe
uri: avoid-using-magic-string-when-referencing-property-variable-names
created: 2020-01-29T05:00:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Liam Elliott
  url: https://ssw.com.au/people/liam-elliott
related: []
redirects:
- do-you-avoid-using-magic-string-when-referencing-property-variable-names

---


​Hard coded strings when referencing property and variable names can be problematic as your codebase evolves, and can make your code brittle.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​​(if customer.Address.ZipCode == null) throw new ArgumentNullException(&quot;ZipCode&quot;);<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58;&#160;​​​Bad Example -&#160;Hardcoding a reference to a property<br></dd><p class="ssw15-rteElement-CodeArea">​​(if customer.Address.ZipCode == null) throw new ArgumentNullException(nameof(customer.Address.ZipCode));<br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good Example - Using nameof() operator to avoid hardcoded strings<br></dd>


