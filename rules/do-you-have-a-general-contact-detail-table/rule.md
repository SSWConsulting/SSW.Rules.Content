---
uri: do-you-have-a-general-contact-detail-table
title: Do you have a general Contact Detail table?
created: 2019-11-22 21:41:18
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">It is common to have a Contact Detail table to store your contact information such as phone numbers. Below is an example of a&#160;Contact Detail table and its related tables. This is bad because the PartyPhone table is too specific for a&#160;phone number and you have to add a new table to save an&#160;email or other contact information if this is needed in the future.​<br></p> </span>

<dl class="badImage"><dt>​<img src="/PublishingImages/ContactDetailTable_bad.png" alt="ContactDetailTable_bad.png" /></dt><dd>Figure&#58; Bad Example - A&#160;too specific Contact Detail table</dd></dl><p>We normally have a general Contact Detail table that includes all the different categories of phone numbers, whether it&#160;is shared or primary plus emails all in the same table.<br></p><dl class="goodImage"><dt><img src="/PublishingImages/ContactDetailTable_good.png" alt="ContactDetailTable_good.png" /></dt><dd>Figure&#58; Good Example - A&#160;general Contact Detail table</dd></dl><p>We use a Contact Detail Category table to store these categories.<br></p><dl class="goodImage"><dt><img src="/PublishingImages/ContactDetailCategoryTable.png" alt="ContactDetailCategoryTable.png" />​<br></dt><dd>Figure&#58; Good Example - Details of Contact Detail Category table<span style="color&#58;#444444;">​</span></dd></dl>


