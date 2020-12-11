---
type: rule
archivedreason: 
title: Do you have a general Contact Detail table?
guid: 7baaf129-21d8-49ca-b0ef-2031044d3ccf
uri: do-you-have-a-general-contact-detail-table
created: 2019-11-22T21:41:18.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

It is common to have a Contact Detail table to store your contact information such as phone numbers. Below is an example of a Contact Detail table and its related tables. This is bad because the PartyPhone table is too specific for a phone number and you have to add a new table to save an email or other contact information if this is needed in the future.

<!--endintro-->
<dl class="badImage">&lt;dt&gt;<img src="ContactDetailTable_bad.png" alt="ContactDetailTable_bad.png">&lt;/dt&gt;<dd>Figure: Bad Example - A too specific Contact Detail table</dd></dl>
We normally have a general Contact Detail table that includes all the different categories of phone numbers, whether it is shared or primary plus emails all in the same table.
<dl class="goodImage">&lt;dt&gt;<img src="ContactDetailTable_good.png" alt="ContactDetailTable_good.png">&lt;/dt&gt;<dd>Figure: Good Example - A general Contact Detail table</dd></dl>
We use a Contact Detail Category table to store these categories.
<dl class="goodImage">&lt;dt&gt;<img src="ContactDetailCategoryTable.png" alt="ContactDetailCategoryTable.png"><br>&lt;/dt&gt;<dd>Figure: Good Example - Details of Contact Detail Category table<span style="color:#444444;"></span></dd></dl>
