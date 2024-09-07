---
seoDescription: Prevent bugs and ensure quality by following a thorough testing process before submitting a version to your client.
type: rule
archivedreason:
title: Do you know the tools you need before a "Test Please"?
guid: f99a466e-47c3-4407-817c-5031e01ec4e6
uri: do-you-know-the-tools-you-need-before-a-test-please
created: 2009-02-26T02:44:26.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-the-tools-you-need-before-a-＂test-please＂
---

Don't let your client find bugs in production that they would have found if you had asked them to do a 'Test Please' 1st
Better still... Don't let your client find bugs that your internal tester would have found.
Better still... Don't let your tester find bugs that a tool could have found?

So, prior to a version being submitted to the client, these are the 4 steps you should follow:

<!--endintro-->

1. Perform automated testing with tools:

   - SSW Link Auditor (for Web Apps)

   - SSW Code Auditor (for all Apps)

   - SSW SQL Auditor (for all Apps with databases)

   - SSW SQL Deploy's Reconcile (for all Apps with databases)

   - Visual Studio Team System Code Analysis (optional)

2. Perform automated testing via Unit Tests

   - xUnit, or

   - nUnit

3. Perform an internal "Test Please" (aka "Alpha Testing" e.g. only testing that pages or forms load, not checking the business rules)
4. Then send a "Test Please" to the client (aka "Acceptance Testing" to check the business rules)
