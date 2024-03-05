---
type: rule
title: Do you follow the boy scout rule?
uri: follow-boy-scout-rule
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-follow-boy-scout-rule
created: 2018-04-30T22:01:51.000Z
archivedreason: null
guid: e7064a56-5702-42fb-b4a3-3c934c6163eb

---

This rule is inspired by a piece from [Robert C. Martin (Uncle Bob)](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html) where he identifies an age old boys scouts rule could be used by software developers to constantly improve a codebase.

<!--endintro-->

Uncle Bob proposed the original rule...

> Always leave the campground cleaner than you found it.

...be changed to

> Always leave the code you've worked on cleaner than you found it.

The reasoning being that no matter how good of a software developer we are, over time, smells creep into code. Be it from tight deadlines, old code that has been changed or appended to in insolation 100's of times over years or just or just newer & better ways of doing things become available.

So each time you touch some code, leave it just a little cleaner than the way you found it.

Here are some simple examples of how you can leave your ~~campsite~~ code cleaner:

1. Remove a compiler warning
2. Remove unused code
3. Improve variable/method naming to make it clearer
4. [DRY](/wrap-the-same-logic-in-a-method-instead-of-writing-it-again-and-again) out some code
5. Restructure a code block to make it more readable
6. Add a test for a missing use case
