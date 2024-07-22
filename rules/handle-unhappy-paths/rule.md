---
seoDescription: Ensure your code handles all possible scenarios, including edge cases, to improve robustness and reliability.
type: rule
title: Code - Do you handle all possible scenarios?
uri: handle-unhappy-paths
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
related: []
redirects: []
created: 2024-07-22T00:00:00.0000000Z
archivedreason: null
guid: 676c1916-78b1-4ae4-b22b-4585274a873d
---

When writing code, developers tend to focus on the happy path of the user. However, it is important to consider all possible scenarios that could occur. This includes edge cases, such as invalid inputs, unexpected user behavior, and system failures. By handling all possible scenarios, you can ensure that your code is robust and reliable.

<!--endintro-->

Here are some tips to help you spot where you need to handle more scenarios:

* Think of potential "unhappy paths" - ask yourself "what could the user do wrong here?"
  * e.g. What if the user enters an invalid email address?
* Get a [test please](/conduct-a-test-please) on all your code
* Do some [exploratory testing](/what-is-exploratory-testing)

::: bad
![Figure: Bad Example - Users can enter invalid emails](image.png)
:::

::: good
![Figure: Good Example - Code checks the email is valid](image-1.png)
:::
