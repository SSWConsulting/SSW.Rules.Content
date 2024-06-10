---
seoDescription: Improve code readability and maintainability by replacing magic numbers with enum constants.
type: rule
archivedreason:
title: Use Enum Constants instead of Magic numbers?
guid: a1e84295-b2df-462d-9d05-7fe65e650b92
uri: use-enum-constants-instead-of-magic-numbers
created: 2018-04-26T16:48:28.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

Using "Magic numbers" in your code makes it confusing and really hard to maintain.

<!--endintro-->

::: bad  
![Figure: Bad example - "Magic Number" works, but is a bad idea](MagicNumberBad.png)  
:::

::: good  
![Figure: Good example - Add Enum](enumClass.png)  
:::

::: good  
![Figure: Good example - No Magic Number, looks good and is easy to manage](MagicNumberGood.png)  
:::
