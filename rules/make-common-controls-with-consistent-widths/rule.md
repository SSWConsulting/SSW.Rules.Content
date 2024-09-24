---
seoDescription: Make common controls consistent by standardizing widths to ensure a cohesive user experience.
type: rule
title: Do you make common controls with consistent widths?
uri: make-common-controls-with-consistent-widths
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T00:22:00.000Z
guid: abfaa422-644f-4b9f-afa0-9c0374e097b2
---

There are a few common controls we always use in our products. For example, DateTime and Ellipsis Button. We need a standard for the width so the controls should be more consistent.

<!--endintro-->

**Note:** Controls on base forms will be made to be 'protected' rather than 'private', especially so that inherited forms of different sizes don't mess up.

::: bad
![Figure: Bad example - Control sizes are not consistent](commoncontrolbad.gif)
:::

::: good
![Figure: Good example - Control sizes are all standard and consistent](commoncontrolgood.gif)
:::

::: bad
![Figure: Bad example - Non-standard size for Add & Delete buttons](adddeletebad.gif)
:::

::: good
![Figure: Good example - Standard size for Add & Delete buttons](adddeletegood.gif)
:::

We have a program called [SSW Code Auditor](https://ssw.com.au/ssw/CodeAuditor/Rules.aspx#CommonControl) to check for the following two rules:

**Rule - C#/VB.NET UI- Button Height and Width - for Standard Button (75 x 23 pixels)**

- **Level 2:** All buttons \< 6 characters:\*\* Check the standard size (75 X 23 pixels) for buttons with the word length less than or equal to six characters, except the following buttons.
- **Level 1:** The action buttons:\*\* Check the standard size (75 X 23 pixels) for the following action buttons:

  - Add
  - Delete
  - Edit
  - OK
  - Close
  - Cancel
  - Save
  - Browse
  - Select
  - Test<
  - Next
  - Back
  - Remove
  - Refresh (Exception to the rule as it has 7 letters)
