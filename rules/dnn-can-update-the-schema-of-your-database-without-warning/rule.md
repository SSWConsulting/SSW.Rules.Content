---
seoDescription: DNN updates database schema without warning, potentially altering data integrity.
type: rule
title: Do you know DNN can update the schema of your database without warning?
uri: dnn-can-update-the-schema-of-your-database-without-warning
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T03:05:00.000Z
archivedreason: outdated
guid: d0177cf4-52cf-4f05-876f-3ce029ef5121
---

If you point your DNN application at another database on an earlier version of DNN, it will update the database to the latest version without warning.

<!--endintro-->

Suggestion to the DNN team: Don't do this without a warning. Even better, use SSW SQL Deploy
