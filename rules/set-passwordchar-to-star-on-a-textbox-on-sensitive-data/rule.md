---
type: rule
seoDescription: Protect sensitive data in textboxes by setting PasswordChar to "*" to mask user input and enhance security in your applications.
title: Do you set PasswordChar to "*" on a TextBox on sensitive data?
uri: set-passwordchar-to-star-on-a-textbox-on-sensitive-data
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:02:00.000Z
guid: a9d95e36-e677-4498-a2b6-dbf5262e675d
---

If you want to work with sensitive data on textboxes is always good practice to set PasswordChar to "*".

<!--endintro-->

::: bad
![Figure: Bad example - The user doesn't set PasswordChar to "*"](passwordcharbad.gif)
:::

::: good
![Figure: Good example - The user set PasswordChar to "*"](passwordchargood.gif)
:::
