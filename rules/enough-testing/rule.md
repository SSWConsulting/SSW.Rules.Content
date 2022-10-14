---
type: rule
title: Do you know when you’ve done “enough” testing?
uri: enough-testing
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-10-14T03:38:04.007Z
guid: 0a3e4d17-303e-4658-a2a4-ebae8d08e784
---
We know that [complete testing is impossible](https://www.ssw.com.au/rules/complete-testing-is-impossible), so we need ways to help us decide when to stop testing, i.e. when we've done "enough" testing.

<!--endintro-->

### Risk-based testing

Since complete testing is impossible, choosing the tests to perform is essentially a sampling problem. Adopting approaches such as [risk-based testing]**(need URL here)** is important in making good sampling decisions.



The focus should be on doing "good enough testing". You can say you're done when you have a testing story adequately covering the risks agreed with your stakeholders and you can make the case that additional tests will probably not significantly change your story. Depending on the situation, this might require months of testing, sometimes only hours.

### Stopping heuristics

There are other ways to decide when to stop testing.

Heuristics are quick, inexpensive ways of solving a problem or making a decision. Heuristics are fallible that is, they might work and they might not work. Michael Bolton has provided a dozen [stopping heuristics](https://www.developsense.com/blog/2009/09/when-do-we-stop-test/):

1. The **Time’s Up!** Heuristic. This is a common situation, we stop testing simply because the time allocated for testing has run out.




2. The **Piñata** Heuristic. We stop testing when we see the first sufficiently dramatic problem (named because we stop whacking the software when the candy starts falling out).



3. The **Dead Horse** Heuristic. The program is too buggy to make further testing worthwhile. We know that there will be so much rework that any more testing will be invalidated by the changes.
4. The **Mission Accomplished** Heuristic. We stop testing when we have answered all of the questions that we set out to answer.
5. The **Mission Revoked** Heuristic. Our client has told us, "Please stop testing now." The budget might have run out or the project has been cancelled.

6. The **I Feel Stuck!** Heuristic. For whatever reason, we stop because we perceive there’s something blocking us. Maybe we don’t have the information we need or there's a blocking bug, such that we can’t get to the area of the product that we want to test, for example.

7. The **Pause That Refreshes** Heuristic. Instead of stopping testing, we suspend it for a while, e.g. because we're tired or distracted, or need to do more research. 
8. The **Flatline** Heuristic. No matter what we do, we’re getting the same result, e.g. the software has crashed or has become unresponsive in some way.




9. The **Customary Conclusion** Heuristic. We stop testing when we usually stop testing. There’s a protocol in place for a certain number of test ideas, or test cases, or test cycles or variation, such that there’s a certain amount of testing work that we do, and we stop when that’s done. Agile teams (say that they) often implement this approach: “When all the acceptance tests pass, then we know we’re ready to ship.” Ewald Roodenrijs gives an example of this heuristic in his blog post titled When Does Testing Stop? He says he stops “when a certain amount of test cycles has been executed including the regression test”.

This differs from “Time’s Up”, in that the time dimension might be more elastic than some other dimension. Since many projects seem to be dominated by the schedule, it took a while for James and me to realize that this one is in fact very common. We sometimes hear “one test per requirement” or “one positive test and one negative test per requirement” as a convention for establishing good-enough testing. (We don’t agree with it, of course, but we hear about it.)

Have we sufficiently questioned why we always stop here? Should we be doing more testing as a matter of course? Less? Is there information available—say, from the technical support department, from Sales, or from outside reviewers—that would suggest that changing our patterns might be a good idea? Have we considered all the other heuristics?

10. No more interesting questions. At this point, we’ve decided that no questions have answers sufficiently valuable to justify the cost of continuing to test, so we’re done. This heuristic tends to inform the others, in the sense that if a question or a risk is sufficiently compelling, we’ll continue to test rather than stopping.

How do we feel about our risk models? Are we in danger of running into a Black Swan—or a White Swan that we’re ignoring? Have we obtained sufficient coverage? Have we validated our oracles?

11. The Avoidance/Indifference Heuristic. Sometimes people don’t care about more information, or don’t want to know what’s going on the in the program. The application under test might be a first cut that we know will be replaced soon. Some people decide to stop testing because they’re lazy, malicious, or unmotivated. Sometimes the business reasons for releasing are so compelling that no problem that we can imagine would stop shipment, so no new test result would matter.

If we don’t care now, why were we testing in the first place? Have we lost track of our priorities? If someone has checked out, why? Sometimes businesses get less heat for not knowing about a problem than they do for knowing about a problem and not fixing it—might that be in play here?

Mission Rejected. We stop testing when we perceive a problem for some person—in particular, an ethical issue—that prevents us from continuing work on a given test, test cycle, or development project.

Would you continue a test if it involved providing fake test results? Lying? Damaging valuable equipment? Harming a human, as in the Milgram Experiment or the Stanford Prison Experiment? Maybe the victim isn’t the test subject, but the client: Would you continue a test if you believed that some cost of what you were doing—including, perhaps, your own salary—were grossly disproportionate to the value it produced? Maybe the victim is you: Would you stop testing if you believed that the client wasn’t paying you enough?

**Add risk-based testing rule as related rule: URI is risk-based-testing**

**Add rule to a category**