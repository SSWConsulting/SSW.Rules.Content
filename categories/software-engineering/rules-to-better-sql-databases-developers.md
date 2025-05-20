---
_template: category
type: category
title: Rules to Better SQL Databases - Developers
guid: c66da635-3483-4287-9d19-013152b12d0f
uri: rules-to-better-sql-databases-developers
index:
- rule: rules/relational-database-design/rule.md
- rule: rules/database-normalization/rule.md
- rule: rules/erds/rule.md
- rule: rules/do-not-allow-nulls-in-text-fields/rule.md
- rule: rules/do-not-allow-nulls-in-number-fields-if-it-has-the-same-meaning-as-zero/rule.md
- rule: rules/avoid-spaces-and-empty-lines-at-the-start-of-character-columns/rule.md
- rule: rules/use-identities-in-sql-server/rule.md
- rule: rules/avoid-deleting-records-by-flagging-them-as-isdeleted/rule.md
- rule: rules/make-sure-you-have-valid-date-data-in-your-database/rule.md
- rule: rules/datetime-fields-must-be-converted-to-universal-time/rule.md
- rule: rules/use-temporal-tables-to-audit-data-changes/rule.md
- rule: rules/avoid-invalid-characters-in-object-identifiers/rule.md
- rule: rules/have-a-general-contact-detail-table/rule.md
- rule: rules/use-a-url-instead-of-an-image-in-your-database/rule.md
- rule: rules/only-use-unicode-datatypes-in-special-circumstances/rule.md
- rule: rules/always-use-varchar/rule.md
- rule: rules/have-standard-tables-and-columns/rule.md
- rule: rules/use-bit-numeric-data-type-correctly/rule.md
- rule: rules/use-natural-or-surrogate-primary-keys/rule.md
- rule: rules/create-primary-key-on-your-tables/rule.md
- rule: rules/create-clustered-index-on-your-tables/rule.md
- rule: rules/avoid-using-indexes-on-rowguid-column/rule.md
- rule: rules/have-a-rowversion-column/rule.md
- rule: rules/use-fillfactor-of-90-percent-for-indexes-and-constraints/rule.md
- rule: rules/do-you-always-have-version-tracking-tables/rule.md
- rule: rules/use-computed-columns-rather-than-denormalized-fields/rule.md
- rule: rules/use-triggers-for-denormalized-fields/rule.md
- rule: rules/validate-each-denormalized-field/rule.md
- rule: rules/avoid-using-user-schema-separation/rule.md
- rule: rules/create-a-consistent-primary-key-column-on-your-tables/rule.md
- rule: rules/use-separate-lookup-tables-rather-than-one-large-lookup-table/rule.md
- rule: rules/how-to-provide-best-database-schema-document/rule.md
- rule: rules/schema-do-you-add-zs-prefix-to-system-tables/rule.md
- rule: rules/do-not-have-views-as-redundant-objects/rule.md
- rule: rules/every-object-name-should-be-owned-by-dbo/rule.md
- rule: rules/keep-your-stored-procedures-simple/rule.md
- rule: rules/return-a-value-indicating-the-status/rule.md
- rule: rules/standardize-the-return-values-of-stored-procedures-for-success-and-failures/rule.md
- rule: rules/use-output-parameters-if-you-need-to-return-the-value-of-variables/rule.md
- rule: rules/check-the-global-variable-error-after-executing-a-data-manipulation-statement/rule.md
- rule: rules/use-scope_identity-to-get-the-most-recent-row-identity/rule.md
- rule: rules/set-nocount-on-for-production-and-nocount-off-off-for-development-debugging-purposes/rule.md
- rule: rules/avoid-starting-user-stored-procedures-with-system-prefix-sp_-or-dt_/rule.md
- rule: rules/avoid-using-select-when-inserting-data/rule.md
- rule: rules/use-transactions-for-complicated-stored-procedures/rule.md
- rule: rules/use-error-handling-in-your-stored-procedures/rule.md
- rule: rules/sql-stored-procedure-names-should-be-prefixed-with-the-owner/rule.md
- rule: rules/turn-on-referential-integrity-in-relationships/rule.md
- rule: rules/use-update-cascade-when-creating-a-relationship/rule.md
- rule: rules/avoid-using-cascade-delete/rule.md
- rule: rules/set-not-for-replication-when-creating-a-relationship/rule.md
- rule: rules/have-foreign-key-constraints-on-columns-ending-with-id/rule.md
- rule: rules/object-name-should-not-be-a-reserved-word/rule.md
- rule: rules/object-name-should-not-contain-spaces/rule.md
- rule: rules/do-not-use-sp_rename-to-rename-objects/rule.md
- rule: rules/object-name-should-follow-your-company-naming-conventions/rule.md
- rule: rules/use-a-sql-server-object-naming-standard/rule.md
- rule: rules/use-a-sql-server-stored-procedure-naming-standard/rule.md
- rule: rules/use-a-sql-server-indexes-naming-standard/rule.md
- rule: rules/use-a-sql-server-relationship-naming-standard/rule.md
- rule: rules/naming-convention-for-use-on-database-server-test-and-production/rule.md
- rule: rules/implement-business-logic-in-middle-tier/rule.md
- rule: rules/parameterize-all-input-to-your-database/rule.md
- rule: rules/use-sql-views/rule.md
- rule: rules/avoid-empty-lines-at-the-start-of-character-columns/rule.md
- rule: rules/do-not-use-table-names-longer-than-24-characters/rule.md
- rule: rules/submit-all-dates-to-sql-server-in-iso-format/rule.md
- rule: rules/query-data-tools/rule.md
---

Here are some of the typical things that all SQL Server DBAs and Database developers should know. These rules are above and beyond the most basic textbook recommendations of:

* Ensuring your databases are Normalized and in 3rd Normal Form
* Making sure you have primary keys, foreign keys and simple indexes to improve performance
* Making sure you Back up regularly
* Basic Naming conventions (see some of our object naming conventions)
* Minimizing result set sizes and data over the wire

View [Database Coding Standard and Guideline](http://www.nyx.net/~bwunder/dbChangeControl/standard.htm).

Want to develop your SQL Server Database with SSW? Check [SSW's Databases consulting page](https://www.ssw.com.au/consulting/database-development).
