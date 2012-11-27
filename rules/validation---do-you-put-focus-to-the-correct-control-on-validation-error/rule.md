---
type: rule
archivedreason: 
title: Validation - Do you put focus to the correct control on validation error?
guid: 43f993e2-8b11-4969-a246-a6bdd2679fb3
uri: validation---do-you-put-focus-to-the-correct-control-on-validation-error
created: 2012-11-27T09:05:50.0000000Z
authors: []
related: []

---


<div>Most fields required validation. There are three types of validations&#58;</div>
<ul><li>Required Field - the field should be filled in.</li>
<li>Formatting - the field must be in a correct format. e.g. currency or date. </li>
<li>Logical - the field needs to pass some validation tests in the business layer. </li></ul>
<br><excerpt class='endintro'></excerpt><br>
​<div>To show an error, display an error provider icon next to the field on the right. An example of this is shown in the figure below.<br></div>
<ul><li>Validation must not be done on TextChanged, this may chew the processor if it is a logical validation. It can also give unpleasant results, e.g. when entering -6.00, as soon as the '-' is entered the validation control would turn on.</li>
<li>Validation for Required fields must be done in the validating event.</li>
<li>Validation for format should be done in parse/format methods.</li>
<li>Validation for Logic should be done in Validated, since it must be entered if required, and in correct format.</li></ul>
<div>The reason for the above validation placement is that these events run in the following order&#58;</div>
<ul><li>Validating</li>
<li>Parse/Format</li>
<li>Validated</li></ul>
<dl class="goodImage"><dt><img alt="Centrix - Error Provider" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ErrorProviderIconExample.jpg" /></dt>
<dd>Figure&#58; Good Example - Error Provider Icon next to a required field</dd></dl>
<div>Do <strong>not</strong> show a message box after every error in validation. You may show a message box as an error summary when an OK or Apply is clicked. Make sure you warn the user that there is an error on the form when they attempt to save.</div>
<dl class="goodImage"><dt><img alt="Centrix - Error Provider" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ValidationBalloon.png" /></dt>
<dd>Figure&#58; Good Example - Balloon tooltips to indicate validation errors</dd></dl>



