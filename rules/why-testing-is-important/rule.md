---
type: rule
title: Do you understand why testing is important?
uri: why-testing-is-important
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - rules-to-better-user-acceptance-tests-uat-for-bug-management
  - why-unit-tests-are-important
created: 2022-09-29T05:06:38.430Z
guid: 8b8b8eb9-0463-48bd-a686-4fd48daaa47d

---

If you ask your manager, developers, clients or other stakeholders whether they think testing is important, you're very likely to get a resounding _"yes, of course!"_. The question of **why** they believe it's important is usually more difficult for them to answer, though.

<!--endintro-->

### Reframing testing to make its importance clearer

This useful definition of testing comes from [Michael Bolton](https://developsense.com/index.html) and [James Bach](https://www.satisfice.com/):

::: greybox
Testing is the process of evaluating a product by learning about it through experiencing, exploring, and experimenting, which includes to some degree: questioning, study, modelling, observation, inference, etc.
:::

This definition highlights all of the aspects of why testing is important, with its focus on interacting with the product, engaging in learning and exploration, and running experiments to help find out if the software in front of us is the software we want for our clients. 

This type of evaluation is important and also likely to be viewed as important by the business. Rather than providing test reports about passed and failed test cases, the kinds of valuable information provided by testing viewed in this way helps to counter the common impression of testing as being a costly nuisance. 

The reality is that most stakeholders (and certainly customers) don't care about what testing we did or how we did it - but they probably care about what you learned while doing it that can be valuable in terms of deciding whether we want to proceed with giving the product to customers. 

Learning to present testing outcomes in a language that helps consumers of the information to make good decisions is a real skill. Talking about risk (be that product, project, business or societal) based on what we’ve learned during testing, for example, might be exactly what a business stakeholder is looking for in terms of value from that testing effort. 

### Why testing is important

We want to find out if there are problems that might threaten the value of the software, so that they can be fixed before it reaches the customer.

We have a desire to know if the software we've built is the software we (and, by extension, our customers) wanted

* So we need test approaches that focus on deliberately finding the important problems
* It's more than just finding the easy or obvious bugs
* The machines alone cannot provide us with this kind of knowledge (so we cannot rely on automation alone).
* We cannot rely solely on the builders of the software for testing, as they lack the critical distance from what they've built to find deep and subtle problems with it.

### Some clues that testing is *not* seen as important

How would teams/clients/organisations behave if software testing **wasn't** important to them? They would probably:

* Try to cut the cost of it or find ways to justify not doing it all (especially with expensive humans). 
* Devalue the people doing testing by compensating them differently to other team members
* Look upon testing work as a commodity that they can have performed by lowest common denominator staff (perhaps in a cheaper location). 
* Capitalize on their confirmation bias by appealing to the authority of the many articles and presentations claiming that "testing is dead". 
* Make sure that testing is seen as a separate function from the rest of development to enable their desire to remove it completely. 
* View testing as a necessary evil.

It's common to see these indications that software testing just isn't seen as important and, unfortunately, the software testing industry has traditionally done a poor job of articulating the value of testing and not being clear on what it is that good testing actually provides.
