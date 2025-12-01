---
seoDescription: Help users enter a URL field by providing clear guidance on expected format and syntax.
type: rule
archivedreason:
title: Do you help the user to enter a URL field?
guid: 10fcd986-a799-4049-85b3-440583b9a6d1
uri: do-you-help-the-user-to-enter-a-url-field
created: 2014-12-16T17:36:25.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

Most developers seem to validate a URL and tell the user what they have done wrong only after the error happens. URL fields should show how the users must enter it.

<!--endintro-->

::: bad  
![Figure: Bad example - Using a validation message to tell the user to enter a correct                         URL](url-field-bad.jpg)  
:::

The better way is to have the user avoid the error with a good default.

::: bad  
![Figure: Bad example - The user has a good chance of entering the URL in the incorrect format](url-field-bad2.jpg)  
:::

::: good  
![Figure: Good example - User immediately knows the format expected](url-field-good.jpg)  
:::
