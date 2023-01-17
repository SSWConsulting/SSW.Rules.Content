---
type: rule
title: Do you know when you've done "enough" testing?
uri: enough-testing
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - risk-based-testing
created: 2022-10-14T03:38:04.007Z
guid: 0a3e4d17-303e-4658-a2a4-ebae8d08e784

---

We know that [complete testing is impossible](/complete-testing-is-impossible), so we need ways to help us decide when to stop testing... aka when we've done "enough" testing.

> "Genius sometimes consists of knowing when to stop."
— Charles de Gaulle

<!--endintro-->

### Risk-based testing

Since complete testing is impossible, choosing the tests to perform is essentially a sampling problem. Adopting approaches such as [risk-based testing](/risk-based-testing) is important in making good sampling decisions.

The focus should be on doing "good enough testing". You can say you're done when you have a testing story adequately covering the risks agreed with your stakeholders and you can make the case that additional tests will probably not significantly change your story. Depending on the situation, this might require months of testing, sometimes only hours.

### Stopping heuristics

There are other ways to decide when to stop testing.

::: greybox
Heuristics are quick, inexpensive ways of solving a problem or making a decision. \
Heuristics are fallible: they might work and they might not work. 
:::

Michael Bolton has provided a dozen [stopping heuristics](https://www.developsense.com/blog/2009/09/when-do-we-stop-test/):

1. The **Time’s Up!** Heuristic. This is a common situation, we stop testing simply because the time allocated for testing has run out.

2. The **Piñata** Heuristic. We stop testing when we see the first sufficiently dramatic problem (named because we stop whacking the software when the candy starts falling out).

3. The **Dead Horse** Heuristic. The program is too buggy to make further testing worthwhile. We know that there will be so much rework that any more testing will be invalidated by the changes.

4. The **Mission Accomplished** Heuristic. We stop testing when we have answered all of the questions that we set out to answer.

5. The **Mission Revoked** Heuristic. Our client has told us, "Please stop testing now." The budget might have run out or the project has been cancelled.

6. The **I Feel Stuck!** Heuristic. For whatever reason, we stop because we perceive there’s something blocking us. Maybe we don’t have the information we need or there's a blocking bug, such that we can’t get to the area of the product that we want to test, for example.

7. The **Pause That Refreshes** Heuristic. Instead of stopping testing, we suspend it for a while, e.g. because we're tired or distracted, or need to do more research. 
8. The **Flatline** Heuristic. No matter what we do, we’re getting the same result, e.g. the software has crashed or has become unresponsive in some way.

9. The **Customary Conclusion** Heuristic. We stop testing when we usually stop testing. There’s a protocol in place for a certain number of test ideas, or test cases, or test cycles or variation, such that there’s a certain amount of testing work that we do and we stop when that’s done. 

10. The **No More Interesting Questions** Heuristic. At this point, we’ve decided that no questions have answers sufficiently valuable to justify the cost of continuing to test, so we’re done. 

11. The **Avoidance/Indifference** Heuristic. Sometimes people don’t care about more information or the business reasons for releasing are so compelling that no problem that we can imagine would stop shipment, so no new test result would matter.

12. The **Mission Rejected** Heuristic. We stop testing when we perceive a problem for some person - in particular, an ethical issue - that prevents us from continuing work, e.g. would you continue a test if it involved providing fake test results or lying? 
