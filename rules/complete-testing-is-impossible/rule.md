---
type: rule
title: Do you know that “complete testing” is impossible?
uri: complete-testing-is-impossible
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
created: 2022-10-05T03:25:30.775Z
guid: a58ba6fa-1f34-40f5-afea-95e986f7e557
---
Just "test everything" they say! Without a good understanding of testing and its limitations, it's easy for clients and customers to believe that we "test everything" - but there's a problem with this belief:

:::greybox
Complete (or 100% or exhaustive) testing is impossible.
:::

<!--endintro-->

![Figure: Don't take on impossible missions!](100-is-impossible.jpg)

## Why is it impossible?

Complete testing is impossible for several reasons:

* We can’t test *all* the inputs to the program.
* We can’t test *all* the combinations of inputs to the program.
* We can’t test *all* the paths through the program.
* We can’t test for *all* of the other potential failures, such as those caused by:

  * User interface design
    errors and other usability problems
  * Incomplete requirements analyses
  * Malfunctioning hardware
  * Humans making mistakes when using the software
  * Hardware/software compatibility issues
  * Timing issues, etc.

For non-trivial programs, complete testing is impossible because the population of possible tests is infinite. So, you can’t have complete coverage - no matter how many tests you run, only partial coverage can be achieved.

https://www.developsense.com/blog/2016/04/100-coverage-is-possible/

# On 100% unit/branch/requirement, etc. coverage:

 A peculiar breed of snake-oil sellers reassure listeners that you achieve complete testing by
using their coverage monitors. Wrong. Complete line and branch coverage is not complete
testing. It will miss significant classes of bugs.

## Approach given this reality

introduce idea that testing is essentially a sampling problem
RBT & good enough

If we can’t do complete testing, what should we do? It seems to me that at the technical level
and at the legal level, we should be thinking about “good enough testing,” done with as part of a
strategy for achieving “good enough software.”

The Good Enough Software approach is difficult because we reject the easy formulations, like “Quality is
Free” and “Test Everything.” We live in a world of tradeoffs. We see imperfection as a fact of life. Our
objective is to choose design, development, testing and deferral strategies that help us manage
imperfection in the service of developing products that, despite their flaws, are excellent tools for their
purposes. (Bach, 1997a,1997b).

But you can say you’re done when you have a testing story with all the major plot points, and you can make the case that additional tests will probably not significantly change your story. Here’s the thing: Although you never know for sure if you have reached that point of diminishing returns, you don’t need to know for sure! All that’s required, all that anyone can expect of you, is that you have a compelling story for why a thoughtful and responsible tester like you might come to the judgment that you know enough about the product under test. In some situations, that will be months of testing; in other situations, only hours.

Watch the <a href="https://vimeo.com/451827063">BBST&reg; Foundations Lecture 5  - The Impossibility of Complete Testing</a> by Dr Cem kaner on <a href="https://vimeo.com">Vimeo</a>.</p>    

Read [The Impossibility of Complete Testing](https://bbst.courses/wp-content/uploads/2022/08/Kaner_impossibility.pdf) by Dr Cem Kaner

**Add your rule to a category**