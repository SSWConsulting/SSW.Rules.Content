---
type: rule
archivedreason: 
title: Do you have a general Contact Detail table?
guid: 7baaf129-21d8-49ca-b0ef-2031044d3ccf
uri: have-a-general-contact-detail-table
created: 2019-11-22T21:41:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-a-general-contact-detail-table

---


<p class="ssw15-rteElement-P">It is common to have a Contact Detail table to store your contact information such as phone numbers. Below is an example of Contact Detail table and its related tables. This is bad because the PartyPhone table is too specific for phone number and you have to add a new table to save email or other contact information if this is needed in the future.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>​<img src="/PublishingImages/ContactDetailTable_bad.png" alt="ContactDetailTable_bad.png" /></dt><dd>Figure&#58; a too specific Contact Detail table</dd></dl><p>We normally have a general Contact Detail table that includes all the different categories of phone numbers, whether is is shared or primary plus emails all in the same table.</p><dl class="goodImage"><dt><img src="/PublishingImages/ContactDetailTable_good.png" alt="ContactDetailTable_good.png" /></dt><dd>Figure&#58; a general Contact Detail table</dd></dl><p>We use a Contact Detail Category table to store these categories.</p><dl class="goodImage"><dt><img src="/PublishingImages/ContactDetailCategoryTable.png" alt="ContactDetailCategoryTable.png" /></dt><dd>Figure&#58; details of Contact Detail Category table<span style="color&#58;#444444;">​</span></dd></dl>


