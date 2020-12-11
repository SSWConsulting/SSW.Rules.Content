---
type: rule
archivedreason: 
title: Do you know how to send email using Microsoft CRM 4 mail merge template?
guid: 83649932-3303-4280-a81d-90f2bcc83769
uri: do-you-know-how-to-send-email-using-microsoft-crm-4-mail-merge-template
created: 2013-03-13T19:30:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>You can use mail merge template, to send email to account, contact... Each mail merge template is associated to an entity, and you can only use the mail merge template that associated to the entity you're sending email to. In the following instructions, I'm sending email to the contact entity:<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>From Dynamics CRM, click 
      <b>Contacts</b> to view the list of contacts.</li><li>Search for the contact that you want to send email to.</li><li>Highlight the contact that you want to send email to, and click the mail merge button.</li><dl class="image"><dt> 
         <img src="send-mail-merge-1.jpg" alt="Mail Merge Button" /> 
      </dt><dd>Figure: Mail merge button</dd></dl><li>At 
      <b>Select the mail merge type</b>, select Email.</li><li>At 
      <b>Start with a</b>, select either personal mail merge template (this is your own template), or the organization template (this is the template that is used by the whole organizaion).</li><li>At 
      <b>Merge</b>, check 
      <b>Selected records on current page</b> check box.</li><li>Click 
      <b>Ok</b></li><dl class="image"><dt> 
         <img src="send-mail-merge-2.jpg" alt="Mail Merge details" /> 
      </dt><dd>Figure: Fill in the mail merge details</dd></dl><li>A Microsoft Word document is open, and the 
      <b>Mail Merge Recipients</b> window is pop-up with the list of contacts that you're sending email to.</li><dl class="image"><dt> 
         <img src="send-mail-merge-3.jpg" alt="Mail Merge Recipients" /> 
      </dt><dd>Figure: Mail Merge Recipients</dd></dl><div class="infoBox greyBox"><h1>Attention</h1><p>If you don't see a contact in the recipient list, that means your contact either:</p><ul><li>
            <b>Do Not Emails</b> or </li><li>
            <b>Do Not Bulk Emails</b> field set to be </li><li>
            <b>Do Not Allow</b> </li></ul></div><li>Follow the on screen instructions in Microsoft Word and edit the content of the email that you want to send.</li><div class="ssw-rteStyle-SSW-Only-Header"><h1>Attention: SSW Developers</h1><p>Please remove the yellow highlight for the block of the text that need to be filled in by you and the green highlight for the CRM field while you're editing the email.</p></div><li>At the last step of the mail merge instructions in Microsoft Word, click 
      <b>Electronic Mail</b> and fill in the subject line for your email.</li><dl class="image"><dt>
         <img src="send-mail-merge-4.jpg" alt="Fill in subject line for email" /> 
      </dt><dd>Figure: Fill in subject line for email</dd></dl><li>Click 
      <b>Ok</b> to proceed to next step.</li><li>Now because we're using CRM 4 Outlook, CRM mail merge will give you an option to create the activities that associated to this email. Check 
      <b>Create Microsoft Dynamic CRM Activities</b> radio button, and uncheck the 
      <b>Include an ubsubcribe link in the email message</b> to create the activities.</li><dl class="image"><dt>
         <img src="send-mail-merge-5.jpg" alt="Create activies for emails sending out using mail merge" /> 
      </dt><dd>Figure: Create activies for emails sending out using mail merge</dd></dl><li>Click 
      <b>OK</b> to send emails using your outlook.</li></ol>


