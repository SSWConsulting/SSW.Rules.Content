---
type: category
title: Rules to Better SQL Databases - Developers
guid: c66da635-3483-4287-9d19-013152b12d0f
uri: rules-to-better-sql-databases-developers
index:
- do-not-allow-nulls-in-text-fields
- do-not-allow-nulls-in-number-fields-if-it-has-the-same-meaning-as-zero
- avoid-spaces-and-empty-lines-at-the-start-of-character-columns
- use-identities-in-sql-server
- avoid-deleting-records-by-flagging-them-as-isdeleted
- make-sure-you-have-valid-date-data-in-your-database
- datetime-fields-must-be-converted-to-universal-time
- use-temporal-tables-to-audit-data-changes
- avoid-invalid-characters-in-object-identifiers
- have-a-general-contact-detail-table
- use-a-url-instead-of-an-image-in-your-database
- only-use-unicode-datatypes-in-special-circumstances
- always-use-varchar
- have-standard-tables-and-columns
- use-bit-numeric-data-type-correctly
- use-natural-or-surrogate-primary-keys
- create-primary-key-on-your-tables
- create-clustered-index-on-your-tables
- avoid-using-indexes-on-rowguid-column
- have-a-rowversion-column
- use-fillfactor-of-90-percent-for-indexes-and-constraints
- do-you-always-have-version-tracking-tables
- use-computed-columns-rather-than-denormalized-fields
- use-triggers-for-denormalized-fields
- validate-each-denormalized-field-with-procvalidate
- avoid-using-user-schema-separation
- create-a-consistent-primary-key-column-on-your-tables
- use-separate-lookup-tables-rather-than-one-large-lookup-table
- how-to-provide-best-database-schema-document
- schema-do-you-add-zs-prefix-to-system-tables
- do-not-have-views-as-redundant-objects
- every-object-name-should-be-owned-by-dbo
- keep-your-stored-procedures-simple
- return-a-value-indicating-the-status
- standardize-the-return-values-of-stored-procedures-for-success-and-failures
- use-output-parameters-if-you-need-to-return-the-value-of-variables
- check-the-global-variable-error-after-executing-a-data-manipulation-statement
- use-scope_identity-to-get-the-most-recent-row-identity
- set-nocount-on-for-production-and-nocount-off-off-for-development-debugging-purposes
- avoid-starting-user-stored-procedures-with-system-prefix-sp_-or-dt_
- avoid-using-select-when-inserting-data
- use-transactions-for-complicated-stored-procedures
- use-error-handling-in-your-stored-procedures
- sql-stored-procedure-names-should-be-prefixed-with-the-owner
- turn-on-referential-integrity-in-relationships
- use-update-cascade-when-creating-a-relationship
- avoid-using-cascade-delete
- set-not-for-replication-when-creating-a-relationship
- have-foreign-key-constraints-on-columns-ending-with-id
- object-name-should-not-be-a-reserved-word
- object-name-should-not-contain-spaces
- do-not-use-sp_rename-to-rename-objects
- object-name-should-follow-your-company-naming-conventions
- use-a-sql-server-object-naming-standard
- use-a-sql-server-stored-procedure-naming-standard
- use-a-sql-server-indexes-naming-standard
- use-a-sql-server-relationship-naming-standard
- naming-convention-for-use-on-database-server-test-and-production
- implement-business-logic-in-middle-tier
- parameterize-all-input-to-your-database
- use-sql-views
- avoid-empty-lines-at-the-start-of-character-columns
- do-not-use-table-names-longer-than-24-characters
- submit-all-dates-to-sql-server-in-iso-format

---

Here are some of the typical things that all SQL Server DBAs and Database developers should know. These rules are above and beyond the most basic textbook recommendations of:

- Ensuring your databases are Normalized and in 3rd Normal Form 
- Making sure you have primary keys, foreign keys and simple indexes to improve performance 
- Making sure you Back up regularly 
- Basic Naming conventions (see some of our object naming conventions)
- Minimizing result set sizes and data over the wire

View [Database Coding Standard and Guideline](http://www.nyx.net/~bwunder/dbChangeControl/standard.htm).

If you still need help, visit our [SQL Server Database consulting page](https://www.ssw.com.au/ssw/Consulting/Database-Development.aspx) and book in a consultant.
