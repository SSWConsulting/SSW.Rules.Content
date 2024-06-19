---
seoDescription: Enable multiple selection and copying in your List Views to simplify user interaction and reduce errors.
type: rule
title: Do your List Views support multiple selection and copying?
uri: do-your-list-views-support-multiple-selection-and-copying
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T06:52:00.000Z
guid: 0ba5f20b-0fba-474f-a7cc-e9936a6f391b
---

List Views such as in [SSW Diagnostics](https://ssw.com.au/ssw/Diagnostics/) can present a wealth of information to the user. But too often, users are unable to copy this information to paste into a support email because the list view doesn't support copying. Instead, the user has to frustratingly retype the information with the risk of introducing errors.

<!--endintro-->

::: bad
![Figure: Bad example - List view with only single selection and no copying](listview_bad.png)
:::

::: good
![Figure: Good example - List view with multiple selection and copying](listview_good.png)
:::

Make it easier for the user by enabling the "MultiSelection" property of a ListView and providing a right click menu with a "Copy" item that copies to the clipboard.
