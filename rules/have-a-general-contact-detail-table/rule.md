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


<p class="ssw15-rteElement-P">It is common to have a Contact Detail table to store your contact information such as phone numbers. Below is an example of a Contact Detail table and its related tables. This is bad because the PartyPhone table is too specific for a phone number and you have to add a new table to save an email or other contact information if this is needed in the future.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>​<img src="ContactDetailTable_bad.png" alt="ContactDetailTable_bad.png" /></dt><dd>Figure: Bad Example - A too specific Contact Detail table</dd></dl><p>We normally have a general Contact Detail table that includes all the different categories of phone numbers, whether it is shared or primary plus emails all in the same table.<br></p><dl class="goodImage"><dt><img src="ContactDetailTable_good.png" alt="ContactDetailTable_good.png" /></dt><dd>Figure: Good Example - A general Contact Detail table</dd></dl><p>We use a Contact Detail Category table to store these categories.<br></p><dl class="goodImage"><dt><img src="ContactDetailCategoryTable.png" alt="ContactDetailCategoryTable.png" />​<br></dt><dd>Figure: Good Example - Details of Contact Detail Category table<span style="color:#444444;">​</span></dd></dl>


