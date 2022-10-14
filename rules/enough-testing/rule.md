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

Our testing might have revealed important new questions to ask. This leads us to the Rumsfeld Heuristic: “There are known unknowns, and there are unknown unknowns.” Has our testing moved known unknowns sufficiently into the known space? Has our testing revealed any important new known unknowns? And a hard-to-parse but important question: Are we satisified that we’ve moved the unknown unknowns sufficiently towards the knowns, or at least towards known unknowns?

5. The Mission Revoked Heuristic. Our client has told us, “Please stop testing now.” That might be because we’ve run out of budget, or because the project has been cancelled, or any number of other things. Whatever the reason is, we’re mandated to stop testing. (In fact, Time’s Up might sometimes be a special case of the more general Mission Revoked, if it’s the client rather than ourselves that have made the decision that time’s up.)

Is our client sufficiently aware of the value of continuing to test, or the risk of not continuing? If we disagree with the client, are we sufficiently aware of the business reasons to suspend testing?

6. The I Feel Stuck! Heuristic. For whatever reason, we stop because we perceive there’s something blocking us. We don’t have the information we need (many people claim that they can’t test without sufficient specifications, for example). There’s a blocking bug, such that we can’t get to the area of the product that we want to test; we don’t have the equipment or tools we need; we don’t have the expertise on the team to perform some kind of specialized test.

There might be any number of ways to get unstuck. Maybe we need help, or maybe we just need a pause (see below). Maybe more testing might allow us to learn what we need to know. Maybe the whole purpose of testing is to explore the product and discover the missing information. Perhaps there’s a workaround for the blocking bug; the tools and equipment might be available, but we don’t know about them, or we haven’t asked the right people in the right way; there might experts available to us, either on the testing team, among the programmers, or on the business side and we don’t realize it. There’s a difference between feeling stuck and being stuck.

7. The Pause That Refreshes Heuristic. Instead of stopping testing, we suspend it for a while. We might stop testing and take a break when we’re tired, or bored, or uninspired to test. We might pause to do some research, to do some planning, to reflect on what we’ve done so far, the better to figure out what to do next. The idea here is that we need a break of some kind, and can return to the product later with fresh eyes or fresh minds.

There’s another kind of pause, too: We might stop testing some feature because another has higher priority for the moment.

Sure, we might be tired or bored, but is it more important for us to hang in there and keep going? Might we learn what we need to learn more efficiently by interacting with the program now, rather than doing work offline? Might a crucial bit of information be revealed by just one more test? Is the other “priority” really a priority? Is it ready for testing? Have we already tested it enough for now?

8. The Flatline Heuristic. No matter what we do, we’re getting the same result. This can happen when the program has crashed or has become unresponsive in some way, but we might get flatline results when the program is especially stable, too—”looks good to me!”

Is the application really crashed, or might it be recovering? Is the lack of response in itself an important test result? Does our idea of “no matter what we do” incorporate sufficient variation or load to address potential risks?

9. The Customary Conclusion Heuristic. We stop testing when we usually stop testing. There’s a protocol in place for a certain number of test ideas, or test cases, or test cycles or variation, such that there’s a certain amount of testing work that we do, and we stop when that’s done. Agile teams (say that they) often implement this approach: “When all the acceptance tests pass, then we know we’re ready to ship.” Ewald Roodenrijs gives an example of this heuristic in his blog post titled When Does Testing Stop? He says he stops “when a certain amount of test cycles has been executed including the regression test”.

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