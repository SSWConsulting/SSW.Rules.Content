---
type: category
title: Rules to Better SQL Server Schema Deployment
guid: e10caebe-e008-4e44-b594-b39c244d6c8d
uri: rules-to-better-sql-server-schema-deployment
index:
- do-you-know-deploying-is-so-easy
- tools-database-schema-changes
- do-you-have-an-understanding-of-schema-changes-and-their-increasing-complexity
- do-you-show-current-versions-app-and-database
- do-you-save-each-script-as-you-go
- should-you-compare-schemas
- the-application-do-you-make-the-app-do-the-work
- do-you-ignore-idempotency
- do-you-check-your-controlled-lookup-data
- do-you-deploy-controlled-lookup-data
- have-a-schema-master
- do-you-understand-a-data-type-change-data-motion-scripts
- validate-each-denormalized-field
- the-application-do-you-make-sure-that-the-database-structure-is-handled-automatically-via-3-buttons-create-upgrade-and-reconcile
- the-application-do-you-understand-the-danger-and-change-permissions-so-schema-changes-can-only-be-done-by-the-schema-master

---
Since 1990, SSW has supported the developer community by publishing all our best practices and rules for everyone to see.

If you still need help, visit [SSW Consulting Services](http&#58;//www.ssw.com.au/ssw/Consulting/Default.aspx)and book in a consultant.

The deployment of your schema is critical to your application. 
You should never get an error message reported from a user like:

"When I click the Save button on the product form it gives an error message about a missing field."
Bottom line is the customers' database schema should always be correct, should be managed automatically by the app and if it is not, it is their problem.

If you are using modern tools properly, this should never happen. 
