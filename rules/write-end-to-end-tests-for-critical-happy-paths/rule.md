---
type: rule
archivedreason: 
title: Do you write end-to-end tests for critical happy-paths?
guid: ef140a92-97ef-4071-b5b2-2bd777ee5109
uri: write-end-to-end-tests-for-critical-happy-paths
created: 2016-05-02T18:13:41.0000000Z
authors:
- title: Steve Leigh
  url: https://ssw.com.au/people/steve-leigh
related: []
redirects:
- do-you-write-end-to-end-tests-for-critical-happy-paths

---

It’s not uncommon for critical workflows in projects to become flaky and brittle, and on occasion, this will not be caught until the product hits production.  An example of a critical workflow is placing an order on a shopping cart, or adding a timesheet in a time tracking site.
 
These are workflows that, if errors occur, the product becomes rather useless, and thus needs to be strongly tested.

<!--endintro-->
 The best way to test this workflow is by performing the workflow against a real environment, using a real browser – of course, in a repeatable, consistent way.
 
A nice option is to use [Seleno](http://seleno.teststack.net/) with an appropriate web driver for the desired browser – see the Seleno documentation.  This library lets you write code to drive a user’s action in a browser, including  for example logging in, searching for a product, adding it to the cart, proceeding to checkout, entering test credit card information and ensuring the success message.
 
This isn’t free though.  The nature of these tests mean that without proper care and maintenance, tests will fail intermittently.  There are difficult-to-predict timings, DOM changes and browser compatibility issues and ongoing maintainability - so it is beneficial to limit these kinds of tests to critical happy-paths.


::: bad  
![Figure: Bad example - No end-to-end tests, no automatic feedback when things go catastrophically wrong](test-bad.png)  
:::


::: good  
![Figure: Good example - End-to-end Seleno tests run in Continuous-Integration, giving us very rapid feedback when the deployment breaks](test-good.png)  
:::
