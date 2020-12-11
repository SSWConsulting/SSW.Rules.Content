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

You can use mail merge template, to send email to account, contact... Each mail merge template is associated to an entity, and you can only use the mail merge template that associated to the entity you're sending email to. In the following instructions, I'm sending email to the contact entity:

<!--endintro-->

1. From Dynamics CRM, click <br>       **Contacts** to view the list of contacts.
2. Search for the contact that you want to send email to.
3. Highlight the contact that you want to send email to, and click the mail merge button.
<dl class="image">&lt;dt&gt; 
         <img src="send-mail-merge-1.jpg" alt="Mail Merge Button"> 
      &lt;/dt&gt;<dd>Figure: Mail merge button</dd></dl>4. At <br>       **Select the mail merge type** , select Email.
5. At <br>       **Start with a** , select either personal mail merge template (this is your own template), or the organization template (this is the template that is used by the whole organizaion).
6. At <br>       **Merge** , check <br>       **Selected records on current page** check box.
7. Click <br>       **Ok**
<dl class="image">&lt;dt&gt; 
         <img src="send-mail-merge-2.jpg" alt="Mail Merge details"> 
      &lt;/dt&gt;<dd>Figure: Fill in the mail merge details</dd></dl>8. A Microsoft Word document is open, and the <br>       **Mail Merge Recipients** window is pop-up with the list of contacts that you're sending email to.
<dl class="image">&lt;dt&gt; 
         <img src="send-mail-merge-3.jpg" alt="Mail Merge Recipients"> 
      &lt;/dt&gt;<dd>Figure: Mail Merge Recipients</dd></dl>

::: greybox

# Attention
    If you don't see a contact in the recipient list, that means your contact either:
    * **Do Not Emails** or
    * **Do Not Bulk Emails** field set to be
    * **Do Not Allow**

:::

9. Follow the on screen instructions in Microsoft Word and edit the content of the email that you want to send.


# Attention: SSW Developers

Please remove the yellow highlight for the block of the text that need to be filled in by you and the green highlight for the CRM field while you're editing the email.

10. At the last step of the mail merge instructions in Microsoft Word, click <br>       **Electronic Mail** and fill in the subject line for your email.
<dl class="image">&lt;dt&gt;
         <img src="send-mail-merge-4.jpg" alt="Fill in subject line for email"> 
      &lt;/dt&gt;<dd>Figure: Fill in subject line for email</dd></dl>11. Click <br>       **Ok** to proceed to next step.
12. Now because we're using CRM 4 Outlook, CRM mail merge will give you an option to create the activities that associated to this email. Check <br>       **Create Microsoft Dynamic CRM Activities** radio button, and uncheck the <br>       **Include an ubsubcribe link in the email message** to create the activities.
<dl class="image">&lt;dt&gt;
         <img src="send-mail-merge-5.jpg" alt="Create activies for emails sending out using mail merge"> 
      &lt;/dt&gt;<dd>Figure: Create activies for emails sending out using mail merge</dd></dl>13. Click <br>       **OK** to send emails using your outlook.
