---
type: rule
archivedreason: 
title: Do you unit test your database?
guid: 75f0c6b8-84cb-472d-a27c-9debc9b147ee
uri: unit-test-your-database
created: 2020-03-12T23:28:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-unit-test-your-database

---

We've all heard of writing unit tests for code and business logic, but what happens when that logic is inside SQL server?

With Visual Studio, you can write database unit tests. These are useful for testing out:

* Stored Procedures
* Triggers
* User-defined functions
* Views


These tests can also be added to the same library as your unit, web and load tests.


<!--endintro-->

![Figure 1 - Database Unit Test](AddNewTest.jpg)  

![Figure 2 - Writing the unit test against a stored proc](WriteUnitTest.jpg)
