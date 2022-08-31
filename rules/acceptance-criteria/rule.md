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
**Stuff to consider:
It muddles acceptance criteria with the tests we might run to determine whether we have met them or not. It also confuses acceptance criteria (AC) with the Definition of Done (DoD) in places.** 

**Another significant issue with its content is around the idea of “Gold Plating”.** 

**I think we should only include criteria that we’ve agreed and committed to deliver as part of the PBI. Each AC must be definitive, so we know for certain whether we have met it or not. Each AC also has to be testable, i.e. we can conceive of tests that would enable us to determine whether it has been met or not.** 

**“Gold Plating” traditionally refers to working on a project or task past the point where the extra effort is not worth the added value. But if we’ve agreed a set of AC for a PBI, then there should be no confusion here. I see no reason to label some ACs as “Gold Plating”, while some others are not.**


**Acceptance Criteria** (from the Product Owner) define the exact requirements that must be met for the story to be completed. They answer the question *"How will I know when I'm done with this story?"*

Acceptance criteria are useful to every person who deals with a user story. Developers know what they are required to implement and how the code will be tested. Testers have a basis for knowing what tests to create.


I also think there is room to identify that the DoD is scoped to all work items whereas the AC’s will be scoped to an individual item.



It is so important because real user stories tell a team when the task is done.

<!--endintro-->

Also, Product Owners should not get heartburn because ‘obvious’ functionality was not included. All requirements should be specified in the Acceptance Criteria.

For example, Product Owners should not assume things like:

* They will get a message that says ‘no records found’ or
* The grid will support features such as pagination or sorting

They must be specified in the Acceptance Criteria if required. 

There are 2 parts to getting this right: The **Acceptance Criteria**, then the **Acceptance Tests**.





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
**Note:** For tiny User Stories, you can omit Acceptance Criteria. Sometimes you just need a **screenshot**, or even better a **video**.
:::

### Add references to discussion

As stated above the Acceptance Criteria is the source of truth for what should be done in the PBI, and any discussion that expands upon it should reference it, and be referenced in it.

::: good
![Figure: Good example - Discussion and references of what involves the Acceptance Criteria](acceptance-criteria-discussion.png)
:::