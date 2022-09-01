---
type: rule
title: Do your User Stories include Acceptance Criteria?
uri: acceptance-criteria
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related:
  - do-you-know-the-how-to-be-a-good-product-owner
  - report-bugs-and-suggestions
redirects:
  - do-your-user-stories-include-acceptance-criteria-(aka-never-assume-automatic-gold-plating)
  - do-your-user-stories-include-acceptance-criteria-aka-never-assume-automatic-gold-plating
created: 2011-05-30T08:13:44.000Z
archivedreason: null
guid: dbe9010e-da5b-4617-8ff3-0e1e5fdc7772
---
While User Stories are a great way to capture requirements, it can be difficult to work out when the implementation of a story is complete.

**Acceptance Criteria** (from the Product Owner) help to answer the question *"How will I know when I'm done with this story?".* They 
define the exact requirements that must be met for the story to be completed.

<!--endintro-->

Acceptance criteria are useful to every person who deals with a user story. Developers know what they are required to implement and how their work will be tested. Testers have a basis for knowing what tests to create.

There are 2 parts to getting this right: The **Acceptance Criteria**, then the **Acceptance Tests**.

###  What do good acceptance criteria look like?

Product Owners should make an effort to specify all of their requirements for a story in the Acceptance Criteria. For example, Product Owners should not assume things like:

* They will get a message that says ‘no records found’ or
* The grid will support features such as pagination or sorting

They must be specified in the Acceptance Criteria if required for the story to be considered complete.



**I think we should only include criteria that we’ve agreed and committed to deliver as part of the PBI. Each AC must be definitive, so we know for certain whether we have met it or not.



![Figure: A User Story with Acceptance Criteria](acceptance-criteria.jpg)

::: greybox
When I enter ‘Adam’ in the search box and click 'Search' I will see all entries starting with 'Adam' in the grid
:::
::: bad
Figure: Bad example of Acceptance Criteria - Incomplete 
:::

::: greybox
**Positive Test** -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid\
**Negative Test** - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see \*no\* entries in the Grid
:::
::: ok
Figure: OK example of Acceptance Criteria
:::

::: greybox
**Positive Test** - When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid\
**Negative Test** - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see **no** entries in the Grid\
**Gold Plating** - If no results are retuned show a message box ‘No results found’\
**Gold Plating** – Validation: If no search text is entered, the ‘Search’ button should be disabled\
**Gold Plating** – Right-clicking on a column header should provide ‘Sort’ functionality\
**Gold Plating** – If a large set of results is returned, display pagination with page numbers and ‘Prev’, ‘Next’ links
:::
::: good
Figure: Good example of Acceptance Criteria – Including Gold Plating 
:::

::: info
**Note:** For tiny User Stories, you can omit Acceptance Criteria. Sometimes you just need a **screenshot** or, even better, a **video**. Be mindful that such small User Stories are the exception and not the rule when it comes to the necessity for Acceptance Criteria. 
:::

gold plating/optional stuff:

In terms of Gold Plating, while not strictly addressed in Scrum, I feel the general consensus is that a PBI should be the smallest increment of work required to create a workable/useful increment. Therefore, anything that is Gold Plating should just be a separate PBI which might be of a lower priority than the cut off for MVP or categorised as such.

### Acceptance tests

todo
 Each AC also has to be testable, i.e. we can conceive of tests that would enable us to determine whether it has been met or not.** 
rejection criteria idea

### The difference between Acceptance Criteria and the Definition of Done?

todo
I also think there is room to identify that the DoD is scoped to all work items whereas the AC’s will be scoped to an individual item.


### Add references to discussion

As stated above the Acceptance Criteria is the source of truth for what should be done in the PBI, and any discussion that expands upon it should reference it, and be referenced in it.

::: good
![Figure: Good example - Discussion and references of what involves the Acceptance Criteria](acceptance-criteria-discussion.png)
:::