---
type: rule
title: Do you regularly review your automated tests?
uri: review-automated-tests
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - automated-test-code-first-class-citizen
created: 2022-12-01T01:09:23.840Z
guid: d823e149-327c-48dd-9049-12165573afd6
archivedreason: null
---
Reliable suites of automated tests can provide a lot of value to your development effort, giving fast feedback and alerting you to unexpected problems introduced by recent code changes.

The more automated the process of building, testing, deploying and delivering software is (and that's the direction a lot of teams are going in), the higher the responsibility of our tests is. Increasingly often, our tests are the only safety net (change detector) between code being written on a developer machine and that code ending up in a production environment. Therefore, it's probably a good idea to make sure that our tests detect the changes we want them to detect.

Automated test code ages just like any other code, though, and it's common to see teams adding more and more automated tests to their suites, without ever going back to review the existing tests to see if they're still relevant and adding value. This process of adding further tests over time often results in bloated test suites that take **longer to run** and require **more human effort** to diagnose failures.

Your automated tests require periodic attention and review — or else they're like smoke detectors, scattered throughout enormous buildings, whose batteries and states of repair are uncertain. As Jerry Weinberg said:

> Most of the time, a non-functioning smoke alarm is behaviorally indistinguishable from one that works. Sadly, the most common reminder to replace the batteries is a fire."
>
> * Jerry Weinberg

<!--endintro-->

![Figure: Keep your valuable tests and don't be afraid to throw away irrelevant tests of no value](keep-throw-away.jpg)

## Tips for reviewing tests

Your automated tests are a valuable asset but only when they are relevant and valuable. So review each of your tests regularly with the following questions in mind.

::: greybox
**Don't be afraid to delete tests!** - Aim for stability over (perceived) coverage and optimize your automated test suites for the value of the information they provide. It really is a case of quality over quantity, so regularly thinning out old, irrelevant, overly costly and flaky tests is a worthwhile exercise.
:::

### Is the test still relevant?

As the product changes over time, older tests can easily still run and pass but are checking for conditions that are no longer relevant.

It may even be the case that tests can no longer fail as the product has evolved, so there is simply no point in running them any more.

### Is the test adding value?

A test only adds value if it tells you something useful when it passes and when it fails.

### Does the test justify its cost?

The total cost of a test is significant, when you take into account:

* The time spent to design, code and maintain it
* The infrastructure costs involved in running it (potentially many thousands of times over its life)
* The effort involved in diagnosing its failures
* The effort involved in regularly reviewing it

So, the value of a test really needs to justify its cost. If a test is not mitigating enough risk or providing enough valuable information compared to its cost, then consider deleting (or at least simplifying) it.

## Don't be fooled by "green" tests

Teams can become very focused on achieving "green builds" where all of their automated tests pass during their build pipelines.

::: greybox
**Tip:** "All green" doesn't necessarily mean "all good"!

False negatives are the silent killers, the tests that show a pass but let a change slip by undetected.
:::

In his blog post on [flaky testing](https://developsense.com/blog/2021/02/flaky-testing), Michael  Bolton makes an important point about your "green" tests:

> Suppose you and your team have a suite of 100,000 automated checks that you proudly run on every build. Suppose that, of these, 100 run red. So you troubleshoot. It turns out that your product has problems indicated by 90 of the checks, but ten of the red results represent errors in the check code. No problem. You can fix those, now that you’re aware of the problems in them.

>Thanks to the scrutiny that red checks receive, you have become aware that 10% of the outcomes you're examining are falsely signalling failure when they are in reality successes. That’s only 10 "flaky" checks out of 100,000. Hurrah! But remember: there are 99,900 checks that you haven't scrutinized. And you probably haven't looked at them for a while.

>Suppose you're on a team of 10 people, responsible for 100,000 checks. To review those annually requires each person working solo to review 10,000 checks a year. That's 50 per person (or 100 per pair) every working day of the year. Does your working day include that?

>Here’s a question worth asking, then: if 10% of 100 red checks are misleadingly signalling a problem, what percentage of 99,900 green checks are misleadingly signalling “no problem”? They're running green, so no one looks at them. They’re probably OK. But even if your unreviewed green checks are ten times more reliable than the red checks that got your attention (because they’re red), that's 1%. That’s 999 misleadingly green checks.

This is where regular review can help us, as Michael notes in his blog post, [On green](https://developsense.com/blog/2015/07/on-green):

> When the check runs green, it's easy to remain relaxed. The alarm doesn’t sound; the emergency lighting doesn't come on; the dog doesn't bark. If we're insufficiently attentive and skeptical, every green check helps to confirm that everything is OK.
When we have unjustified trust in our checks, we have the opposite problem that we have with the smoke detector: we're unlikely to notice that the alarm doesn’t go off when it should.

> We can choose to hold on to the possibility that something might be wrong with our checks, and to identify the absence of red checks as meta-information; a suspicious silence, instead of a comforting one. The responsible homeowner checks the batteries on the smoke alarm."
