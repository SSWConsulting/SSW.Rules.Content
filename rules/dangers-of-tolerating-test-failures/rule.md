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

As your application changes and the number of automated tests increases over time, though, it becomes more likely that some of them will fail. 

It's important to know how to handle these failures appropriately.

<!--endintro-->

![Figure: How not to handle automated test failures (Sander van der Wel from Netherlands, CC BY-SA 2.0, via Wikimedia Commons)](head-in-sand.jpg)

### Some anti-patterns in handling automated test failures

When automated tests fail due to a genuine problem in the software, this is a good thing! You should thank them and address the problem asap.

But what about test failures due to other reasons? Let's look at some common anti-patterns for dealing with such failures.

#### Tolerate the failures

Some "reasons" for tolerating test failures include:

* Only a few tests  are failing (out of thousands), so it's not a big deal!
* It's always the same tests that fail, so we "know" everything's really OK even though the build is not "green"
* We haven't got time to fix the tests right now, we'll come back and fix them later

Tolerating test failures quickly erodes the trust in the results of the tests, to the point where the results are ignored and so they become pointless to run. This is a significant waste of your investment in building automated tests.

You need anything other than a "green build" to be a problem that the whole team takes seriously. This requires your automated tests to be reliable and stable, so that they only fail when they've identified a problem in the software. 

::: greybox
**Tip:** It's better to have fewer, more reliable tests than more, unreliable ones (since the results of these unreliable tests don't tell you anything definitive about the state of the software under test).
:::

#### "Skip" the failing tests "for now"

bad idea, you'll never go back
, what if the few failing tests you're going to skip actually indicate a big problem and you're now going to deliberately overlook it?

### Better ways to handle automated test failures

Good: fix or delete
instead
Focus on "green builds", 

Reminder that you’re writing (test) code because you have doubts about other (product) code
Product problem, fix it
If it's important enough for a test, then fix it. If there's no value in the test anymore, delete it

**Look for related rules**

**Add your rule to a category**