---
type: rule
title: Do you know the difference between Fixed Price and Time and Materials work?
seoDescription: Consulting services billed on time and materials or fixed price, with differences including warranty, scope definition, payment terms, and testing requirements.
uri: fixed-price-vs-time-and-materials
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Jean Thirion
    url: https://www.ssw.com.au/people/jean-thirion
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/ulysses-maclaren
related:
  - fixed-price-deliver-the-project-and-start-the-warranty-period
redirects:
  - do-you-know-the-difference-between-fixed-price-and-time-and-materials-work
created: 2010-07-16T04:26:47.000Z
archivedreason: null
guid: 715139ed-271a-464e-889a-b4c84fcbbef8
---

There are two fundamental ways any consultant can bill clients, with differences including warranty, scope definition, payment terms, and testing requirements.

<!--endintro-->

## Time and Materials

Time and materials is the standard mode of operation where the client is billed for the time spent by the consultant. There is no warranty on time and materials work.

## Fixed Price

Fixed price is where the client is billed a fixed amount agreed between the client and the consultant. Fixed price contracts have the following conditions:

* All specification work to be conducted on a Time and Materials basis
* All screen mock-ups and business rules must be signed by the client
* A fixed price can only be done on a release by release basis, not on an entire project (this protects everyone)
* A 20% premium is added to the release estimates - just like an insurance premium because the consultant is carrying the risk
* Variations/change requests have to have separate written approval. e.g. _"Hi John, You've asked for XXX. This is not covered in the original scope and so will be charged extra. Our estimate is YYY hours at $ZZZ + GST per hour. Please approve."_
* Development is conducted off-site (to prevent unauthorised scope-development)
* 50% of the fixed price is payable before work commences, the balance is payable at the delivery of the first external test please
* There is a 7-day warranty on [bugs](/management-is-your-client-clear-on-the-definition-of-a-bug) which commences when the first external test please is issued
* Warranty only applies to Development / Staging environments (once the work is deployed to Production, no warranty applies)
* The following release cannot commence until the prior release is signed-off

This set of conditions ensure a fair distribution of risk for both parties. It's perfectly fine to be unhappy about a feature and requesting some changes, but once approved, a piece of work shouldn't be worked on again for free.

### Analogy

The warranty process is similar to what happens at a restaurant; if you look carefully when your meal is served and realise it's not what you ordered or there's something wrong with it, it's perfectly fine to send it back. However once you've started to eat your burger, it's too late to send it back and ask it to be changed 🧑‍🍳

::: img-medium
![Figure: Testing the application in Staging is like tasting your meal](refusing-meal-restaurant.jpeg "Figure: Refusing a meal at the restaurant")
:::
