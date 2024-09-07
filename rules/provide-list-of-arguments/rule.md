---
seoDescription: When developing command-line applications, providing a list of arguments and help on usage is crucial for effective user interaction.
type: rule
title: Do you provide list of arguments?
uri: provide-list-of-arguments
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T03:41:00.000Z
guid: d0bd94cb-018e-4144-a1ad-492a1d499ea1
---

When you develop an application that supports command line, you must provide a list of arguments / help on how to use the application through command line.

It can be as easy as typing: `\[ApplicationName].exe /?` for listing the arguments.

<!--endintro-->

::: bad
![Figure: Bad example - Do no provide supported argument through /?](nolistofarguments.jpg)
:::

::: good
![Figure: Good example - Provide supported argument through /?](listofarguments.jpg)
:::
