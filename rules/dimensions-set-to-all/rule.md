---
seoDescription: Reports can be simplified and made more readable by configuring every dimension's "All Caption" to be simply "All", eliminating redundancy and making data presentation cleaner.
type: rule
archivedreason:
title: Reports - Do you configure every dimension’s "All Caption" to be "All"?
guid: d9ee5679-c600-4f14-92ed-d7ea6b692455
uri: dimensions-set-to-all
created: 2014-12-01T06:06:37.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects:
  - reports-do-you-always-make-sure-the-dimensions-all-captions-all
---

In OLAP (Online Analytical Processing) cubes, dimensions are ways to categorize data. For example, in a sales cube, you might have dimensions for Time, Products, and Geography. Each dimension can have a hierarchy, and the top level is often represented as "All," which aggregates the data across all members of that dimension.

<!--endintro-->

### Default Behavior

By default, the top level of each dimension is labeled as "All" followed by the dimension name. For example:

- "All Products" for the Products dimension
- "All Time" for the Time dimension
- "All Geography" for the Geography dimension

This default labelling can be redundant and might not add clarity to the reports generated from these OLAP cubes.

### Improve Clarity by Adjusting the 'All Caption'

Simplify and unify the representation of the top level in each dimension to improve the clarity and appearance of reports.

**Adjusted Setting:** The 'All Caption' property for each dimension is set to "All" without the dimension name.

::: greybox
Dimension Caption: "All Products"  
Dimension Caption: "All Time"  
Dimension Caption: "All Geography"  
:::
::: bad
Figure: Bad example (Before adjustment) - In this scenario, the prefix "All" followed by a space and the dimension name can make reports look cluttered and does not add meaningful information
:::

::: greybox
Dimension Caption: "All"
:::
::: good
Figure: Good example (After adjustment) - In the improved scenario, each dimension's top level simply reads "All," eliminating redundancy and making the data presentation cleaner and more straightforward
:::

### How to make the change

1. Access the properties - In your OLAP cube design tool, locate the properties for each dimension
2. Adjust the 'All Caption' - Change the 'All Caption' property from "All [Dimension Name]" to just "All"
3. Apply and test - Save your changes and generate a report to ensure that the top level of each dimension now simply reads "All", making the report more aesthetically pleasing and easier to understand

Adjusting the 'All Caption' property in your OLAP cube dimensions simplifies report headings and enhances readability. This minor change can significantly impact the professionalism and clarity of your reporting solutions.
