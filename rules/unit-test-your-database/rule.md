---
seoDescription: Test and automate database logic with Visual Studio's unit tests for SQL Server, ensuring stored procedures, triggers, functions, and views are thoroughly tested.
type: rule
title: Do you unit test your database?
uri: unit-test-your-database
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-unit-test-your-database
created: 2020-03-12T23:28:06.000Z
archivedreason: null
guid: 75f0c6b8-84cb-472d-a27c-9debc9b147ee
---

We've all heard of writing unit tests for code and business logic, but what happens when that logic is inside SQL server?

With Visual Studio, you can write database unit tests. These are useful for testing out:

- Stored Procedures
- Triggers
- User-defined functions
- Views

These tests can also be added to the same library as your unit, web and load tests.

<!--endintro-->

![Figure: Database Unit Test](AddNewTest.jpg)

![Figure: Writing the unit test against a stored proc](WriteUnitTest.jpg)

If you want to know how to setup database unit tests locally and in your build pipeline, check out this article: [Unit Test Stored Procedures and Automate Build, Deploy, Test Azure SQL Database Changes with CI/CD Pipelines](https://cuteprogramming.wordpress.com/2022/04/29/unit-test-stored-procedures-and-automate-build-deploy-test-azure-sql-database-changes-with-ci-cd-pipelines/)
