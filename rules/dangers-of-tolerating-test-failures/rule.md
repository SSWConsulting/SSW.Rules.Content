---
type: rule
title: Do you understand the dangers of tolerating automated test failures?
uri: dangers-of-tolerating-test-failures
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-10-27T23:26:17.217Z
guid: c078e328-cedb-4670-8f5b-f78288388032
---
A big suite of various levels of automated tests can be a great way of quickly identifying problems introduced into the codebase.

As your application changes and the number of automated tests increases over time, though, it becomes more likely that some of them will fail. It's important to handle these failures appropriately.

<!--endintro-->

![Figure: How not to handle automated test failures (Sander van der Wel from Netherlands, CC BY-SA 2.0, via Wikimedia Commons)](head-in-sand.jpg)

### Tolerating automated test failures

just a few tests
always the same ones fail, so we "know" it's really OK, etc.

Focus on "green builds", tolerating failures leads to erosion of trust in the tests to the point where they can become pointless to run
Reminder that you’re writing (test) code because you have doubts about other (product) code

### Fix or delete

If it's important enough for a test, then fix it. If there's no value in the test anymore, delete it

### "Skipping" tests

bad idea, you'll never go back

**Add your rule to a category**