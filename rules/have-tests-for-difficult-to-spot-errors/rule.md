---
type: rule
archivedreason: 
title: Do you have tests for difficult to spot errors - e.g. Arithmetic, Rounding, Regular Expressions?
guid: 8bb8ec43-680b-4610-8ffc-0cd9c559b03b
uri: have-tests-for-difficult-to-spot-errors
created: 2020-03-12T19:51:40.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-tests-for-difficult-to-spot-errors-e-g-arithmetic-rounding-regular-expressions

---

By difficult to spot errors we mean errors that do not give the user a prompt that an error has occurred. Things such as: Arithmetic, Rounding or Regular Expressions should have unit tests written for them.

<!--endintro-->

Sample Code:
![](unit test - arithmetic code.jpg)
 **Figure: Function to calculate a total for a list of items** 
For a function like this, it might be simple to spot errors when there are one or two items, but if you were to calculate the total for 50 items, then the task of spotting an error isn't so easy. That's why a unit test should be written so that you know when the function doesn't work.

**Sample Test:**

**![](unit test - arithmetic tests.jpg)
**
 **Figure: Test calculates total by checking something we know the result of. (Note: it doesn't need a failure case because it isn't a Regex.)
**
