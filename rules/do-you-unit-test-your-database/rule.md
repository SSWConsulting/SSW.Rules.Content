---
type: rule
archivedreason: 
title: Do you unit test your database?
guid: 75f0c6b8-84cb-472d-a27c-9debc9b147ee
uri: do-you-unit-test-your-database
created: 2020-03-12T23:28:06.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p class="ssw15-rteElement-P">We've all heard of writing unit tests for code and business logic, but what happens when that logic is inside SQL server?​​<br></p><p class="ssw15-rteElement-P">With Visual Studio, you can write database unit tests. These are useful for testing out:​<br></p><ul><li>Stored Procedures</li><li>Triggers</li><li>User-defined functions</li><li>Views​<br></li></ul><div>These tests can also be added to the same library as your unit, web and load tests.<br></div>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt>​<img src="AddNewTest.jpg" alt="AddNewTest.jpg" /></dt><dd>Figure 1 - Database Unit Test</dd></dl><dl class="image"><dt><img src="WriteUnitTest.jpg" alt="WriteUnitTest.jpg" /></dt><dd>Figure 2 - Writing the unit test against a stored proc​<br></dd></dl>


