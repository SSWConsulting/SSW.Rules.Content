---
seoDescription: Ensure referential integrity in relationships by enabling cascading constraints to maintain data consistency and prevent orphaned records.
type: rule
archivedreason:
title: Relationships - Do you turn on referential integrity in relationships?
guid: b90d91f8-46fb-45b7-947b-c8ce43621844
uri: turn-on-referential-integrity-in-relationships
created: 2019-11-12T23:56:31.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - relationships-do-you-avoid-using-cascade-delete
  - relationships-do-you-use-update-cascade-when-creating-a-relationship
redirects:
  - relationships-do-you-turn-on-referential-integrity-in-relationships
---

Cascading referential integrity constraints allow you to define the actions SQL Server takes when a user attempts to delete or update a key to which existing foreign keys point. The REFERENCES clauses of the CREATE TABLE and ALTER TABLE statements support ON DELETE and ON UPDATE clauses:

- [ ON DELETE { CASCADE | NO ACTION } ]
- [ ON UPDATE { CASCADE | NO ACTION } ]

NO ACTION is the default if ON DELETE or ON UPDATE is not specified.

<!--endintro-->

Relationships should always have referential integrity turned on. If you turned it on after data has been added, you may have data in your database that violates your referential integrity rules.

![Figure: Recommended referential integrity constraints](ReferentialIntegrityCheck.jpg)
