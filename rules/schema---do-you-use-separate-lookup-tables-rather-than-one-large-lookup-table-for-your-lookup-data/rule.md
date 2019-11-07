---
type: rule
archivedreason: 
title: Schema - Do you use separate lookup tables rather than one large lookup table for your lookup data?
guid: 36e90c6d-2206-40cd-991b-9eb06fa573cf
uri: schema---do-you-use-separate-lookup-tables-rather-than-one-large-lookup-table-for-your-lookup-data
created: 2019-11-07T20:11:29.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p class="ssw15-rteElement-P"><b>​Advantage&#58; Simplifies ORM Mapping​​​</b><br></p>We prefer multiple lookup tables so they make more sense in ORM tools. E.g. you could have either&#58;<br>
<br><excerpt class='endintro'></excerpt><br>
<p>1. OrderType<br></p><p>Or<br></p><p>2. LookupTable</p><p>But when you are obtaining the OrderType for an order, you would have</p><p>Either</p><p>Order.OrderType.OrderTypeID (Good)</p><p>Or</p><p><strong>Order.LookupTable.Value (Not great as it is not clear what the nature of the lookup table is).&#160;</strong>If you have multiple lookups to the one table, you would need to do your mappings manually rather than using a tool.<br></p><p><strong>Advantage&#58; Maintains Complete Referential Integrity without the need for triggers Advantage&#58; Maintains Complete Referential Integrity without the need for triggers</strong></p><p>The other advantage of having separate lookup tables rather than one large one is that referential integrity is maintained.</p><p>One issue with having one large table is that you can still enter invalid values in the Order.OrderTypeID column. E.g. if Order TypeIDs range from 1-3 and CustomerTypeIDs range from 4 to 10.</p><p>If I put OrderTypeID = 10, then I will not get referential integrity errors (even though I should) because I have entered a value which exists in the lookup table (even though it is for the wrong type).</p><p>If I want to enforce referential integrity so I can only enter the correct type for my lookup table, then I would need to resort to triggers or a (fallible) coded data tier.</p><p><strong>Advantage&#58; You can add new columns specific to each lookup table</strong></p><p>For example, if a Lookup table (e.g. CustomerType) has an associated value (e.g. the field MaximumDebtAmount), we don't need to add a field that is irrelevant to all the other lookup tables. We can just add it to the individual lookup table.</p><p><strong>Disadvantage&#58; Multiple tables make maintenance slightly more difficult, especially when making changes directly via Management Studio.</strong></p><p>It is simpler to Administer one table than multiple tables, but you can reduce this problem with a good Generic Administration Page UI.​<br></p>


