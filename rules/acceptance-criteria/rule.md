---
seoDescription: Do your PBIs include Acceptance Criteria?
type: rule
title: Do your PBIs include Acceptance Criteria?
uri: acceptance-criteria
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - do-you-know-the-how-to-be-a-good-product-owner
  - does-your-team-write-acceptance-tests-to-verify-acceptance-criteria
  - definition-of-done
  - report-bugs-and-suggestions
redirects:
  - do-your-user-stories-include-acceptance-criteria-(aka-never-assume-automatic-gold-plating)
  - do-your-user-stories-include-acceptance-criteria-aka-never-assume-automatic-gold-plating
created: 2011-05-30T08:13:44.000Z
archivedreason: null
guid: dbe9010e-da5b-4617-8ff3-0e1e5fdc7772
---

**Acceptance Criteria** (from the Product Owner) help to answer the question _"How will I know when I'm done with this Product Backlog Item (PBI)?"._ It defines the exact requirements that must be met for the PBI to be completed. It is the Product Owner's responsibility to ensure that all Acceptance Criteria has been added - otherwise they should not expect that work to be done.

<!--endintro-->

Acceptance Criteria are useful to every person who deals with a PBI. Developers know what they are required to implement and how their work will be tested. Testers have a basis for knowing what tests to create.

### What do good Acceptance Criteria look like?

Product Owners should make an effort to specify all of their requirements for a PBI in the Acceptance Criteria. For example, Product Owners should not assume things like:

* They will get a message that says ‘no records found’ or
* The grid will support features such as pagination or sorting

They must be specified in the Acceptance Criteria if required for the PBI to be considered complete.

![Figure: A PBI with Acceptance Criteria in Azure DevOps](acceptance-criteria-detail.jpg)

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
Figure: OK example of Acceptance Criteria - However the Product Owner probably hasn't included all of their requirements
:::

::: greybox

* When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid
* When I enter ‘zzz’ in the Search box and click ‘Search’ I will see **no** entries in the Grid
* If no results are returned, show a message box ‘No results found’
* If no search text is entered, the ‘Search’ button should be disabled
* Right-clicking on a column header should provide ‘Sort’ functionality
* If a large set of results is returned, display pagination with page numbers and ‘Prev’, ‘Next’ links

:::
::: good
Figure: Good example of Acceptance Criteria
:::

::: info
**Note:** For tiny PBI, you can omit Acceptance Criteria. Sometimes you just need a **screenshot** or, even better, a **video**.  
Be mindful that such small PBIs are the exception and not the rule when it comes to the need for Acceptance Criteria.
:::

### Negotiating "gold plating"

Any requirements that the Product Owner considers "nice to have" - as opposed to being mandatory for the PBI to be considered complete - should be negotiated with development as early as possible. Developers can spend significant time working to meet acceptance criteria that the Product Owner is actually willing to sacrifice in the interests of quicker delivery.

::: info
**Tip:** Work closely with the Product Owner to identify potential "gold plating" in the PBI. Suggest creating a separate PBI for the functionality that is nice to have but has lower priority. Doing so allows developers to focus on building the most important functionality for the PBI first and prevents valuable time being wasted on gold plating.
:::

### Technical Acceptance Criteria

Sometimes, the team may discuss including technical requirements in Acceptance Criteria. Typically, technical Acceptance Criteria should be avoided. However, there are some situations where it makes sense, such as when:

* The team is trying out something new
* The team has been misaligned in the past, and the future direction needs to be clear
* The approach to take is complex or confusing
* An abnormal approach is being taken to avoid a specific issue (e.g. reducing readability to improve performance for a particularly critical query)
* When the PBI is an Enabler (backlog items that extend the architectural runway of the solution under development or improve the performance of the development value stream)

If technical requirements are added, it should be a discussion between all of the developers in the team. If the Product Owner is technical, they are welcome to join the conversation, but they should not be the primary decision maker in this case.

Additionally, when adding technical requirements try to prefix with "Technical - " so their purpose is clear to everyone (e.g. "Technical - New CQRS Query made to get all employees")

### Acceptance Tests

Since Acceptance Criteria will be used to determine whether the work for the PBI is done or not, each of them needs to verified [using an Acceptance Test](/does-your-team-write-acceptance-tests-to-verify-acceptance-criteria).

It is good practice to make sure that each of the Acceptance Criteria is **testable** (e.g. Tests can be written to definitively determine whether the criteria has been met or not). This can help to reduce vagueness in the way Acceptance Criteria are defined.

::: info
**Note:** When all of the acceptance tests pass, the PBI **might** be acceptable - but deeper testing would be required to be more certain. When any of the acceptance tests fail, though, we know for sure that the PBI isn’t acceptable. It can be helpful to think of "Acceptance Tests" instead as "Rejection Tests".
:::

### What's the difference between "Acceptance Criteria" and "Definition of Done"?

Acceptance Criteria help to answer the question _"How will I know when I'm done with this PBI?"_. **The Acceptance Criteria are different for each PBI**, provided by the Product Owner and used as a way to communicate to all involved that the requirements for a particular PBI have been met.

The [Definition of Done](/definition-of-done) is a structured list of items, each one used to validate a PBI, which exists to ensure that the team agrees about the quality of work they’re producing. It is defined by the team and serves as a checklist that is used to check each PBI for completeness. **The definition of "Done" is intended to be applicable to all items in the Product Backlog**, not just a single PBI.

Examples of items in a Definition of Done that would **not** be part of Acceptance Criteria include:

* Code review completed
* Unit tests passed
* Code deployed to production

::: info
The term "Definition of Done" is defined in the Scrum Guide, while "Acceptance Criteria" is not.
:::

### Capture changes to the PBI from discussions

The Acceptance Criteria are the source of truth for what functionality needs to be implemented for the PBI to be considered complete, so it's important to capture any changes to the PBI and the Acceptance Criteria (e.g. adding or removing "nice to have" aspects of the PBI).

Any discussion that changes the PBI and/or the Acceptance Criteria should be noted in the Discussion section of the PBI for reference.

::: good
![Figure: Good example - Discussion about changes to the Description and Acceptance Criteria captured in the PBI](acceptance-criteria-discussion.png)
:::
