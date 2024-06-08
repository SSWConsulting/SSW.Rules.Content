---
type: rule
archivedreason: It is superseded by [https://ssw.com.au/rules/use-environment-newline-to-make-a-new-line-in-your-string](/rules/use-environment-newline-to-make-a-new-line-in-your-string)
title: Do you know that no carriage returns without line feed?
guid: 3c62c8bf-eeab-4a87-9ee4-750be54e34eb
uri: know-that-no-carriage-returns-without-line-feed
created: 2018-04-30T22:26:48.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-that-no-carriage-returns-without-line-feed

---

Text files created on DOS/Windows machines have different line endings than files created on Unix/Linux. DOS uses carriage return and line feed ("\r\n") as a line ending, which Unix uses just line feed ("\n").

<!--endintro-->

::: bad  
![Figure: Bad example](carriage-bad.jpg)  
:::

::: good  
![Figure: Good example](carriage-good.jpg)  
:::
