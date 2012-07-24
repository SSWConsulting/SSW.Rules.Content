---
type: rule
title: Do you avoid relying on Javascript for crucial actions?
uri: do-you-avoid-relying-on-javascript-for-crucial-actions
created: 2012-07-24T18:11:08.0000000Z
authors:
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>Don't assume JavaScript is always enabled.</p>
<p>JavaScript should be used to enhance the overall user experience and not as a dependency.</p> </span>

<p>JavaScript is very useful for improving user-interaction, along with reducing the number of requests made on the server; but it can be disabled - an estimated 2% of web users do not have JavaScript enabled</p>
<p>Depending on your audience you may choose to disregard this rule, but for mainstream websites it is highly recommended that you don't rely on JavaScript for crucial actions, such as <strong>validation</strong> or <strong>business-logic </strong> purposes. Do a server-side validation instead.</p>
<div class="greyBox">
<p><strong>Note&#58; </strong>This rule can be applied to any other third-party technology, such as Flash or Java. If it's not built into every web browser/device or if it can be disabled, then make sure the page is still accessible and usable without it.</p></div>



