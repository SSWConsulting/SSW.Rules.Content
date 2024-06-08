---
type: rule
archivedreason: 
title: Do you avoid relying on Javascript for crucial actions?
guid: f93855fc-baa6-4e3a-9e97-3c466d614e98
uri: do-you-avoid-relying-on-javascript-for-crucial-actions
created: 2012-07-24T18:11:08.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---

Don't assume JavaScript is always enabled.

JavaScript should be used to enhance the overall user experience and not as a dependency.

<!--endintro-->

JavaScript is very useful for improving user-interaction, along with reducing the number of requests made on the server; but it can be disabled - an estimated 2% of web users do not have JavaScript enabled

Depending on your audience you may choose to disregard this rule, but for mainstream websites it is highly recommended that you don't rely on JavaScript for crucial actions, such as  **validation** or  **business-logic** purposes. Do a server-side validation instead.


::: greybox

**Note:** This rule can be applied to any other third-party technology, such as Flash or Java. If it's not built into every web browser/device or if it can be disabled, then make sure the page is still accessible and usable without it.

:::
