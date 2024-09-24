---
seoDescription: Ensure your code handles all possible scenarios, including edge cases, to improve robustness and reliability.
type: rule
title: Code - Do you handle all possible scenarios?
uri: handle-unhappy-paths
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
related:
 - validation-do-you-avoid-capturing-incorrect-data
redirects: []
created: 2024-07-22T00:00:00.0000000Z
archivedreason: null
guid: 676c1916-78b1-4ae4-b22b-4585274a873d
---

When developers build software, they naturally become experts in using the software. This is problematic because with this expertise, they will tend to focus on the happy path of the user. However, it is important to consider all possible scenarios that could occur. This includes edge cases, such as invalid inputs, unexpected user behavior, and system failures. By handling all possible scenarios, you can ensure that your code is robust and reliable.

<!--endintro-->

Here are some tips to help you spot where you need to handle more scenarios:

* Think of potential "unhappy paths"
  * Ask yourself "what could the user do wrong here?" (e.g. What if the user enters an invalid email address?)
  * Assume your users are doing something for the first time
* Get a [test please](/conduct-a-test-please) on all your code
* Do some [exploratory testing](/what-is-exploratory-testing)

::: bad
![Figure: Bad example - Users can enter invalid emails](bad-no-validaton.png)
:::

::: good
![Figure: Good example - Code checks the email is valid](good-validation-fields.png)
:::
