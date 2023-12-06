---
type: rule
title: Do you understand relational database design?
uri: relational-database-design
authors:
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related:
  - database-normalization
  - erds
created: 2023-07-03T05:50:13.555Z
guid: f2383ae4-3e2c-487a-b3ab-14bc89273994
---
Imagine an e-commerce company called Northwind Traders, where thousands of products, multiple sellers, and millions of customers converge. In such a company, the importance of a well-designed database cannot be overstated. Consider the scenario where a customer places an order only to encounter delays and frustration due to data inconsistencies that wrongly indicate an out-of-stock product. To mitigate such chaos, developers rely on relational database design principles, including normalization and entity-relationship diagrams (ERDs). These concepts provide the foundation for a well-structured database with improved data integrity and reduced redundancy, ensuring smooth operations and customer satisfaction.

<!--endintro-->

## Poor database design - The problems

If a database lacks proper structure and organization, many problems can arise. These include:

* **Data Duplication** e.g. If Northwind Traders employee details, like home address, are stored separately in the HR and Payroll departments, an update in one place may not reflect in the other, leading to inconsistencies.
* **Update Anomalies** e.g. If a customer's phone number is stored in multiple places in the database, a change in contact information might not be updated everywhere, causing confusion when attempting to reach them.
* **Insertion Anomalies** e.g. If a database requires a vendor's details when adding a new product, it would be difficult to add a new product if the vendor information isn't available at the time of entry.
* **Deletion Anomalies** e.g. If a customer record is deleted from the database, it might unintentionally delete all associated order records, erasing valuable sales data.

## The Solution

Solving these problems is hard. Luckily, there are some tried and tested tools that help resolve these problems including:

* [Database Normalization](/database-normalization)
* [Entity Relationship Diagrams (ERDs)](/erds)

Database normalization and ERDs are the core tools needed to perform good relational database design. If these concepts are misapplied or are not used at all, there can be disastrous consequences with far-reaching effects. For example, once you start putting data into a table, it becomes significantly harder to fix since you now have a data migration problem. That's why getting database design right the first time is vital.
