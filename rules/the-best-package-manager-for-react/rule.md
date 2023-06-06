---
type: rule
title: Do you know the best package manager for React?
uri: the-best-package-manager-for-react
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - do-you-keep-your-npm-packages-up-to-date
redirects:
  - do-you-know-the-best-package-manager-for-react
created: 2017-08-15T23:12:15.000Z
archivedreason: null
guid: b6564f50-7525-40d8-9a98-cc7619bcc854
---
When working with JavaScript packages there are 3 common choices:

<!--endintro-->

::: bad
![Figure: Bad Example - npm is the backbone of JavaScript development but after the left-pad disaster of 2016 lots of developers wanted more power](npm-logo.jpg)
:::

::: good
![Figure: Good Example - Yarn is fast and enables offline support - If you've installed a package before, you can install it again without any internet connection (no more left-pad disasters)](yarn-logo.jpg)
:::

::: good
![Figure: Good Example - pnpm has significantly faster package install times than the previous two - it links package directories to a global cache of previously installed packages, meaning the same package won't be fetched twice between projects, which saves a lot of disk space. This makes pnpm great for large JavaScript projects.](pnpm-logo.png)
:::