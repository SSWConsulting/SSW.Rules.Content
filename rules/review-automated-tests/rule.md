---
type: rule
title: Do you regularly review your automated tests?
uri: review-automated-tests
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-12-01T01:09:23.840Z
guid: d823e149-327c-48dd-9049-12165573afd6
---
Reliable suites of automated tests can provide a lot of value to your development effort, giving fast feedback and alerting you to unexpected problems introduced by recent code changes.

Automated test code ages just like any other code, though, and it's common to see teams adding more and more automated tests to their suites, without ever going back to review the current tests to see if they're still relevant and adding value. This process of adding further tests over time often results in bloated test suites that take longer & longer to run and require more & more human effort to diagnose failures.

To continue getting genuine value from your automated tests, make sure they are regularly reviewed.

<!--endintro-->

![Figure: keep stuff, throw away stuff](keep-throw-away.jpg)

# Tips for reviewing tests

Your automated tests are a valuable asset but only when they are relevant and valuable. So review each of your tests with the following questions in mind.

### Is the test still relevant?

dsa
Maybe the check is archaic, checking for some condition that is no longer relevant, and we don’t need it any more.

### Is the test adding value?

Does it tell you something valuable if they fail)? 

### Does the test justify its cost?

related to value, but note total cost of a test is significant, writing it, running it potentially thousands of times, maintaining it, reviewing it, etc.

::: greybox
**Don't be afraid to delete tests** - esp. flaky/unreliable ones, prefer stability over (perceived) coverage
:::

# Don't be fooled by "green" tests!
noting that all green isn't necessary all good

:start
from https://developsense.com/blog/2015/07/on-green:
As my colleague James Bach puts it, checks are like motion detectors around the boundaries of our attention. When the check runs green, it’s easy to remain relaxed. The alarm doesn’t sound; the emergency lighting doesn’t come on; the dog doesn’t bark. If we’re insufficiently attentive and skeptical, every green check helps to confirm that everything is okay.
When we have unjustified trust in our checks, we have the opposite problem that we have with the cooking detector: we’re unlikely to notice that the alarm doesn’t go off when it should. That is, we don’t pay attention.


The good news is that being inattentive is optional. We can choose to hold on to the possibility that something might be wrong with our checks, and to identify the absence of red checks as meta-information; a suspicious silence, instead of a comforting one. The responsible homeowner checks the batteries on the smoke alarm, and the savvy explorer knows when to say “The forest is quiet tonight… maybe too quiet."
:end

Bolton https://developsense.com/blog/2021/02/flaky-testing

" Suppose you and your team have a suite of 100,000 automated checks that you proudly run on every build. Suppose that, of these, 100 run red. So you troubleshoot. It turns out that your product has problems indicated by 90 of the checks, but ten of the red results represent errors in the check code. No problem. You can fix those, now that you’re aware of the problems in them.

Thanks to the scrutiny that red checks receive, you have become aware that 10% of the outcomes you’re examining are falsely signalling failure when they are in reality successes. That’s only 10 “flaky” checks out of 100,000. Hurrah! But remember: there are 99,900 checks that you haven’t scrutinized. And you probably haven’t looked at them for a while.

Suppose you’re on a team of 10 people, responsible for 100,000 checks. To review those annually requires each person working solo to review 10,000 checks a year. That’s 50 per person (or 100 per pair) every working day of the year. Does your working day include that?

Here’s a question worth asking, then: if 10% of 100 red checks are misleadingly signalling a problem, what percentage of 99,900 green checks are misleadingly signalling “no problem”? They’re running green, so no one looks at them. They’re probably okay. But even if your unreviewed green checks are ten times more reliable than the red checks that got your attention (because they’re red), that’s 1%. That’s 999 misleadingly green checks.

Real testing requires intention and attention. It’s okay for a suite of checks to run unattended most of the time. But to be worth anything, they require periodic attention and review—or else they’re like smoke detectors, scattered throughout enormous buildings, whose batteries and states of repair are uncertain. And as Jerry Weinberg said, “most of the time, a nonfunctioning smoke alarm is behaviorally indistinguishable from one that works. Sadly, the most common reminder to replace the batteries is a fire.”"

**Add your rule to a category**

related: 1st class citizen rule