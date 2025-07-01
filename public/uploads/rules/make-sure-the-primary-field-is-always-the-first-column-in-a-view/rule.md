---
seoDescription: Ensure the Primary Field is always the first column in a view to provide seamless navigation and user experience in Dynamics and Model-driven PowerApps.
type: rule
title: Do you make sure the Primary Field is always the first column in a view?
uri: make-sure-the-primary-field-is-always-the-first-column-in-a-view
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
  - do-you-make-sure-the-primary-field-is-always-the-first-column-in-a-view
created: 2020-06-29T21:32:13.000Z
archivedreason: null
guid: 2d7b56ea-cd7d-4b02-950b-ba4a662594ee
---

When modifying existing or creating custom views in Dynamics (or Model-driven PowerApps) always pay special attention to the first column. The first column should always contain the **Primary Field** for the entity that the view is based on. For example, all views for **Opportunities** should use **Topic** (name), **Contacts** should use **Full Name** (fullname) as the first column.

<!--endintro-->

The reason for this is the Primary Field in a view displays as a hyperlink to the underlying record. It is very convenient and natural to click the first item in the view, as this will then take you to the record. If any other field is used the user will either need to double click the row to navigate to the record (non-lookup) or will be taken to a completely different entities record (lookup field).

Some examples below:

::: bad
![Figure: Bad example - A lookup field is the first column](bad-primary-field.png)
:::

In this example, **Account** is the first column in the view, the natural tendency is the click the first column, and seeing that it's a hyperlink further confirms to the user that this is something they can click on. Clicking the first column ("Northwind Traders") would navigate to the Northwind Traders **Account** form and not the **Opportunity** form for Northwind Traders.

::: bad
![Figure: Bad example - A regular field is the first column](bad-primary-field-2.png)
:::

In this example **Probability** is the first column in the view, again users tend to click the first column in the view. In this example, a single click would select the entire row (with tick box selected to the left of the grid), and a double click on the first column would navigate to the Opportunity record.

::: good
![Figure: Good example - Primary Field is the first column](good-primary-field.png)
:::

In this example, the **Primary Field** is the first column of the view, and single-clicking the first column view navigates to the opportunity record as expected.

Understanding column ordering in view is important and making sure the first column in a view is always the Primary Field will make it much easier for your users.
