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
  - does-your-team-write-acceptance-tests-to-verify-acceptance-criteria
  - done-do-you-go-beyond-done-and-follow-a-definition-of-done
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

There are 2 parts to getting this right: the **Acceptance Criteria**, then the **Acceptance Tests**.

### What do good acceptance criteria look like?

Product Owners should make an effort to specify all of their requirements for a story in the Acceptance Criteria. For example, Product Owners should not assume things like:

* They will get a message that says ‘no records found’ or
* The grid will support features such as pagination or sorting

They must be specified in the Acceptance Criteria if required for the story to be considered complete.

![Figure: A User Story PBI with Acceptance Criteria in Azure DevOps](acceptance-criteria.jpg)

::: greybox
When I enter ‘Adam’ in the search box and click 'Search' I will see all entries starting with 'Adam' in the grid
:::
::: bad
Figure: Bad example of Acceptance Criteria - Incomplete 
:::

::: greybox
* When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid
* When I enter ‘zzz’ in the Search box and click ‘Search’ I will see **no** entries in the Grid
:::
::: ok
Figure: OK example of Acceptance Criteria - but the Product Owner probably hasn't included all of their requirements
:::

::: greybox
* When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid
* When I enter ‘zzz’ in the Search box and click ‘Search’ I will see **no** entries in the Grid\
* If no results are returned, show a message box ‘No results found’
* If no search text is entered, the ‘Search’ button should be disabled
* Right-clicking on a column header should provide ‘Sort’ functionality
* If a large set of results is returned, display pagination with page numbers and ‘Prev’, ‘Next’ links
:::
::: good
Figure: Good example of Acceptance Criteria
:::

::: info
**Note:** For tiny User Stories, you can omit Acceptance Criteria. Sometimes you just need a **screenshot** or, even better, a **video**. Be mindful that such small User Stories are the exception and not the rule when it comes to the need for Acceptance Criteria. 
:::

gold plating/optional stuff:

**I think we should only include criteria that we’ve agreed and committed to deliver as part of the PBI. Each AC must be definitive, so we know for certain whether we have met it or not.**

Make it clear that some ACs can be considered optional, i.e. can be completed if they are quick and easy & don't compromise the estimated effort

Adam: Gold Plating is something that a Product Owner and dev should negotiate

Andrew:
In terms of Gold Plating, while not strictly addressed in Scrum, I feel the general consensus is that a PBI should be the smallest increment of work required to create a workable/useful increment. Therefore, anything that is Gold Plating should just be a separate PBI which might be of a lower priority than the cut off for MVP or categorised as such.

### Acceptance tests

Since Acceptance Criteria will be used to determine whether the work for the story is done or not, each of them needs to verified using an acceptance test.

It is good practice to make sure that each of the Acceptance Criteria are *testable*, i.e. test(s) can be written to definitively determine whether the criteria has been met or not.

See the rule
[Do you write acceptance tests to verify Acceptance Criteria?](https://www.ssw.com.au/rules/does-your-team-write-acceptance-tests-to-verify-acceptance-criteria)

::: info
**Note:**
When all of the acceptance tests pass for the story, the story *might* be acceptable - but deeper testing would be required to be more certain. When any of the acceptance tests fail, though, we know for sure that the story isn’t acceptable. It can be helpful to think of "acceptance tests" instead as "rejection tests".
:::

### what's the difference between Acceptance Criteria and the Definition of Done?

todo
I also think there is room to identify that the DoD is scoped to all work items whereas the AC’s will be scoped to an individual item.

### Capture changes to the PBI from discussions

The Acceptance Criteria are the source of truth for what functionality needs to be implemented for the PBI to be considered complete, so it's important to capture any changes to the PBI and the Acceptance Criteria. 

Any discussion that expands upon the story and/or the Acceptance Criteria should be noted in the Discussion section of the PBI for reference.

::: good
![Figure: Good example - Discussion about changes to the story and Acceptance Criteria captured in the PBI](acceptance-criteria-discussion.png)
:::