---
type: rule
title: Do you understand why testing cannot be completely automated?
uri: why-testing-cannot-be-completely-automated
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - what-testing-really-means
created: 2022-10-06T23:22:00.911Z
guid: 88d14ac9-bbf0-4ba9-9301-66c47c6c902e
---
There is a common misconception that you can automate all the testing. 

While there can be great value in using automation in testing, human capabilities are still required for the key testing skills such as evaluation, experimentation, exploration, etc.

<!--endintro-->

![Figure: Bill Lumbergh might well ask someone to "automate all the testing" (from the movie Office Space)](automate-everything.jpg)

### Remember the difference between testing and checking

Recall the distinction between testing and checking (see [what "testing" really means](/what-testing-really-means)):

::: info
**Testing** is the process of evaluating a product by learning about it through experiencing, exploring, and experimenting. This includes questioning, study, modeling, observation, inference, etc.

**Checking** is the process of making evaluations by applying algorithmic decision rules to specific observations of a product.
:::

Looking at these definitions, **testing** is clearly a deeply human activity. Skills such as learning, exploring, questioning and inferring are not well suited to machines (even with the very best AI/ML). Humans may or may not *use* tools or other automation while exercising these skills, but that doesn’t mean that the performance of testing is itself "automated".

**Checking** is a valuable component of our overall testing effort and, by this definition, lends itself to be automated. But the binary evaluations (pass/fail) from such checks only form a small part of the testing story. 

There are many aspects of product quality that are not amenable to such black and white evaluation.

Thinking about checks, there's a lot that goes into them apart from the actual execution (by a machine or otherwise). For instance, someone...

* Decided we needed a check (risk analysis)
* Designed the check
* Implemented the check (coding)
* Decided what to observe and how to observe it, and 
* Evaluated the results from executing the check

These aspects of the check are testing activities and, importantly, they're not aspects that can be given over to a machine (i.e. be automated). There is significant testing skill required in the design, implementation and analysis of the check and its results - the execution (the automated part) is really the easy part.

> A machine producing a bit is not doing the testing; the machine, by performing checks, is accelerating and extending our capacity to perform some action that happens as part of the testing that we humans do. The machinery is invaluable, but it’s important not to be dazzled by it. Instead, pay attention to the purpose that it helps us to fulfill, and to developing the skills required to use tools wisely and effectively.
> --- Michael Bolton

### Countering suggestions to "automate all the testing"

There is often value to be gained by automating checks and leveraging automation to assist and extend humans in their testing efforts, but the real testing lies with the humans – and always will.

The next time someone suggests that you "automate all the testing", remind them this means you will need to:

::: greybox

"Automate the evaluation\
and learning\
and exploration\
and experimentation\
and modeling\
and studying of the specs\
and observation of the product\
and inference-drawing\
and questioning\
and risk assessment\
and prioritization\
and coverage analysis\
and pattern recognition\
and decision making\
and design of the test lab\
and preparation of the test lab\
and sensemaking\
and test code development\
and tool selection\
and recruiting of helpers\
and making test notes\
and preparing simulations\
and bug advocacy\
and triage\
and relationship building\
and analyzing platform dependencies\
and product configuration\
and application of oracles\
and spontaneous playful interaction with the product\
and discovery of new information\
and preparation of reports for management\
and recording of problems\
and investigation of problems\
and working out puzzling situations\
and building the test team\
and analyzing competitors\
and resolving conflicting information\
and benchmarking..."
:::
(Kudos to Michael Bolton again for the above list)

Check out Huib Schoots and Paul Holland talking about "Automation Addiction" in their Romanian Testing Conference 2022 keynote. They explain why testing can't be completely automated as well as discussing some common misconceptions and problems around automation.

`youtube: https://www.youtube.com/watch?v=c1KKOyQUSWI&t=17s`

**Video: Huib Schoots & Paul Holland - Automation Addiction (52 min)**
