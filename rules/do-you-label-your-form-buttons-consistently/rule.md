---
type: rule
archivedreason: 
title: Do you label your form buttons consistently?
guid: 9963337e-8c40-491d-a1bb-43912e547d0d
uri: do-you-label-your-form-buttons-consistently
created: 2014-12-01T00:09:41.0000000Z
authors: []
related: []

---


<p><span>​The buttons that a user will typically use to close a form should be named consistently across your applications.</span></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img alt="Broker Details - Save & Close Buttons" src="../../assets/ButtonLabels_Bad.gif" style="margin:5px;" />
   </dt><dd>Figure: Bad Example - Unclear labels on the buttons</dd></dl><ul><li>
      <strong>Save</strong> button could possibly update the fields but keep the form open.</li><li>
      <strong>Close</strong> could save the fields, then close the form, when the 
      <strong> Cancel</strong> button may be more appropriate.</li></ul><p>We recommend the age-old standards of:</p><ul><li>
      <strong>OK</strong>. Close the form and save any changed data. This should be referenced by the form's AcceptButton property.</li><li>
      <strong>Cancel</strong>. Close the form without saving. This should be referenced by the form's CancelButton property.</li><li>
      <strong>Apply</strong>. Save data without closing the form.</li></ul><dl class="goodImage"><dt>
      <img alt="Outlook Contact Properties - OK, Cancel & Apply Buttons" src="../../assets/OKCancelExampleDialog.jpg" style="margin:5px;" />
   </dt><dd>Figure: Good Example - This form uses the standard button naming standards (and has the Default buttons set!)</dd></dl><p class="productBox">We have a program called 
   <a href="http://www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.</p>


