---
type: rule
archivedreason: 
title: Schema - Do you use separate lookup tables rather than one large lookup table for your lookup data?
guid: 36e90c6d-2206-40cd-991b-9eb06fa573cf
uri: use-separate-lookup-tables-rather-than-one-large-lookup-table
created: 2019-11-07T20:11:29.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-use-separate-lookup-tables-rather-than-one-large-lookup-table-for-your-lookup-data

---

::: good
Advantage: Simplifies ORM Mapping  
:::
We prefer multiple lookup tables so they make more sense in ORM tools. If you have multiple lookups to the one table, you would need to do your mappings manually rather than using a tool. E.g. you could have either: LookupTable or OrderType


<!--endintro-->

When you are obtaining the OrderType for an order, you would have either:

* Order.OrderType.OrderTypeID





> Good as it is clear what is being retrieved from the lookup table.




* Order.LookupTable.Value





> Not great as it is not clear what the nature of the lookup table is.



::: good
Advantage: Maintains Complete Referential Integrity without the need for triggers

:::
The other advantage of having separate lookup tables rather than one large one is that referential integrity is maintained.
One issue with having one large table is that you can still enter invalid values in the Order.OrderTypeID column. E.g. if Order TypeIDs range from 1-3 and CustomerTypeIDs range from 4 to 10.

If I put OrderTypeID = 10, then I will not get referential integrity errors (even though I should) because I have entered a value which exists in the lookup table (even though it is for the wrong type).


If I want to enforce referential integrity so I can only enter the correct type for my lookup table, then I would need to resort to triggers or a (fallible) coded data tier.





::: good
Advantage: You can add new columns specific to each lookup table

:::

For example, if a Lookup table (e.g. CustomerType) has an associated value (e.g. the field MaximumDebtAmount), we don't need to add a field that is irrelevant to all the other lookup tables. We can just add it to the individual lookup table.




::: bad
Disadvantage: Multiple tables make maintenance slightly more difficult, especially when making changes directly via Management Studio

:::

It is simpler to Administer one table than multiple tables, but you can reduce this problem with a good Generic Administration Page UI.
