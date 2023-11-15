---
type: rule
title: Data - Do you avoid deleting records by flagging them as IsDeleted (aka
  Soft Delete)?
uri: avoid-deleting-records-by-flagging-them-as-isdeleted
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - data-do-you-avoid-deleting-records-by-flagging-them-as-isdeleted-aka-soft-delete
  - data-do-you-avoid-deleting-records-by-flagging-them-as-isdeleted-(aka-soft-delete)
created: 2019-11-25T19:14:13.000Z
archivedreason: null
guid: 56fff82d-9ed7-4aee-ab22-68e4c61fe162
---
When users are deleting a lot of records as part of normal operations - they can and do make mistakes. Instead of the painful process of having to go to a backup to get these records, why not simply flag the records as IsDeleted?

<!--endintro-->

::: good
Advantages

:::

* You do not have to delete all related records e.g. Customers, Orders, Order Details. Instead, you can just flag the parent record as deleted with an "IsDeleted" bit field.
* You do not lose historical data e.g. how many products one of your previous clients purchased.
* You can actually see who deleted the record, as your standard audit columns (e.g. DateUpdated, UserUpdated are still there. The record does not just vanish.

::: bad
Disadvantages

:::

* Depending on your interface design, you may have to join to parent tables to ensure that deleted child records do not appear. Typically, the interface would be designed in such a way that you would not need be able to created new records based on the deleted items (e.g. you cannot create a new order record for a customer that is deleted). Performance of queries can potentially suffer if you have to do these joins.
* While storage space is very cheap, you are not removing records from your database. You may need to archive records if the number of deleted records becomes large.



### Best Approach for Implementing Soft Delete in Databases

Implementing a uniform soft delete pattern enhances data integrity by ensuring predictable, traceable deletions across various database components. This standardised approach streamlines database maintenance, centralising updates and reducing complexity.

#### Data Layer View with Soft Delete Filter

Create a view to select only active records from a table as opposed to directly access the actual table. This example uses the `Customers` table:

```sql
CREATE VIEW ActiveCustomers AS
SELECT *
FROM Customers
WHERE IsDeleted = 0;

```

::: greybox
Note: The ActiveCustomers view is used to access customer data and the IsDeleted clause filters out soft-deleted records, ensuring that only active records are retrieved.
:::

### Auto-generated Stored Procedure for Soft Deleting

A stored procedure can be used for soft-deleting a record by setting the `IsDeleted` column to 1 (true), this ensures a standard soft delete procedure to execute when required:

```sql
CREATE PROCEDURE SoftDeleteCustomer
    @CustomerId INT
AS
BEGIN
    UPDATE Customers
    SET IsDeleted = 1
    WHERE CustomerId = @CustomerId;
END;
```
***
Also see [Using Audit Tools](/use-temporal-tables-to-audit-data-changes) for alternatives to this approach using 3rd party auditing tools.
::: greybox

Watch William Liebenberg's SpendOps talk for more details about why soft deletes are advantageous in Azure:

* SSW TV video: 
         [Real-life SpendOps with Azure Cosmos DB](https://www.youtube.com/watch?v=qfPQR8XlwFo)
* NDC video: 
         [Azure SpendOps – The Art of Effectively Managing Azure Costs](https://www.youtube.com/watch?v=zxSlKiWOOzw)

:::