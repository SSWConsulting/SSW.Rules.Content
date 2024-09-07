---
seoDescription: Automated test failures can be a valuable indicator of problems in your codebase, but tolerating them or skipping them can lead to wasted investment and ignored results.
type: rule
title: Do you understand the dangers of tolerating automated test failures?
uri: dangers-of-tolerating-test-failures
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - do-you-swarm-to-fix-the-build
  - automated-ui-testing
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

- There are some "flaky" tests and they'll probably pass if we just re-run them - read this [Twitter thread from Michael Bolton](https://twitter.com/michaelbolton/status/1363873246467284998?s=20&t=MDk03REH9QoO2i3Dmtzrcg) on so-called "flaky tests"
- Only a few tests are failing (out of thousands), so it's not a big deal!
- It's always the same tests that fail, so we know everything is really OK even though the build is not "green"
- We haven't got time to fix the tests right now, we'll come back and fix them later

Tolerating test failures quickly erodes the trust in the results of the tests, to the point where the results are ignored and so they become pointless to run. This is a significant waste of your investment in building automated tests.

::: greybox
You need anything other than a "green build" to be a problem that the whole team takes seriously. This requires your automated tests to be reliable and stable, so that they only fail when they've identified a problem in the software.

**Tip:** It's better to have fewer, more reliable tests than more, unreliable ones (since the results of these unreliable tests don't tell you anything definitive about the state of the software under test).
:::

#### "Skip" the failing tests

It might be tempting to deliberately skip the failing tests to get back to a "green build" state, with the intention of fixing them later.

The first problem with this is those failing tests that you're choosing to skip might actually be tests that find significant problems in the software - and now you'll deliberately overlook these problems.

The second problem is that "later" never comes - higher priority work arises and going back to fix up these tests is unlikely to get the priority it needs. Keeping track of which tests are being skipped also adds unnecessary overhead and increases the risk of problems being introduced but going undetected.

### Better ways to handle automated test failures

> The best measure of success, is how you deal with failure.
> &nbsp; - Ronnie Radke

When an automated test fails because of a problem in the software, you should prioritise fixing the problem.

When a test fails but **not** because of a problem in the software:

- If the test is important enough to keep, fix it
- If there's no value in the test anymore, delete it

::: greybox
Remember that you've invested the time and effort into writing automated tests for a reason. Quite reasonably, you have doubts about your code and you write tests to help overcome these doubts.

This means the automated test code is important and needs to be high quality.
:::
