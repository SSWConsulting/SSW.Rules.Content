---
type: rule
title: Do you write end-to-end tests for critical happy-paths?
uri: do-you-write-end-to-end-tests-for-critical-happy-paths
created: 2016-05-02T18:13:41.0000000Z
authors:
- id: 55
  title: Steve Leigh

---



<span class='intro'> <p>It’s not uncommon for critical workflows in projects to become flaky and brittle, and on occasion, this will not be caught until the product hits production.&#160; An example of a critical workflow is placing an order on a shopping cart, or adding a timesheet in a time tracking site.<br>&#160;<br>These are workflows that, if errors occur, the product becomes rather useless, and thus needs to be strongly tested.<br></p> </span>

The best way to test this workflow is by performing the workflow against a real environment, using a real browser – of course, in a repeatable, consistent way.<br>&#160;<br>A nice option is to use <a href="http&#58;//seleno.teststack.net/"> Seleno</a>​&#160;with an appropriate web driver for the desired browser – see the Seleno documentation.&#160; This library lets you write code to drive a user’s action in a browser, including&#160; for example logging in, searching for a product, adding it to the cart, proceeding to checkout, entering test credit card information and ensuring the success message.<div>&#160;<br>This isn’t free though. &#160;The nature of these tests mean that without proper care and maintenance, tests will fail intermittently. &#160;There are difficult-to-predict timings, DOM changes and browser compatibility issues and ongoing maintainability - so it is beneficial to limit these kinds of tests to critical happy-paths.</div><dl class="badImage"><dt><img src="/PublishingImages/test-bad.png" alt="test-bad.png" /></dt><dd>Figure&#58; Bad example - No end-to-end tests, no automatic feedback when things go catastrophically wrong </dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/test-good.png" alt="test-good.png" /></dt><dd>Figure&#58; Good example - End-to-end Seleno tests run in Continuous-Integration, giving us very rapid feedback when the deployment breaks </dd></dl>


