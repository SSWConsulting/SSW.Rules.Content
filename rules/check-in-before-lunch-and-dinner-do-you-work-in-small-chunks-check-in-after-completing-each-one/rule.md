---
seoDescription: Developers should work in small chunks and check-in regularly, before leaving their workstation or after completing each task, to ensure code stability and ease of merging with other developers.
type: rule
archivedreason:
title: Do you work in small chunks & check in after completing each one?
guid: a9f4bf75-4ea9-4e79-944e-fb3a4693076c
uri: check-in-before-lunch-and-dinner-do-you-work-in-small-chunks-check-in-after-completing-each-one
created: 2011-11-18T03:52:27.0000000Z
authors:
  - title: David Klein
    url: https://ssw.com.au/people/david-klein
    noimage: true
  - title: Justin King
    url: https://ssw.com.au/people/justin-king
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
related: []
redirects:
  - (check-in-before-lunch-and-dinner)-do-you-work-in-small-chunks-check-in-after-completing-each-one
  - do-you-work-in-small-chunks-check-in-after-completing-each-one
---

Frequently developers work on long or difficult features/bugs and leave code checked out for days or worse still, weeks.

1. What happens if your laptop hard drive dies?
2. What happens if you call in sick?
3. How can you pair program if not sharing your changesets?

<!--endintro-->

![Figure: Eating one big meal every three days gives you a bellyache... (aka check in small portions regularly, one large check-in after a few days will give you a headache)](Check-InRegularly.jpg)

That's why source code should be checked in regularly. We recommend a check-in:

* Immediately after completing a piece of functionality, where the
  [code compiles and passes the unit tests](/after-work-do-you-only-check-in-code-when-it-has-compiled-and-passed-the-unit-tests)Before lunch or dinner
* Before leaving your workstation for an extended period of time

If the changes would break the build or are in a state that cannot be put into the main trunk, then this code should be put into a [shelveset](http://msdn.microsoft.com/en-us/library/ms181403.aspx) (sometimes referred to as 'sandbox') in source control.
Another good reason to check-in regularly is that it makes it easier to merge your changes with other developers. If all developers check-in lots of changes in one go, you will spend a lot of your time resolving conflicts instead of doing work.

Tip: How can you enforce regular check-ins? Monitor them using a [report to see who has not checked in](/tfs-master-do-you-have-a-report-to-see-who-has-not-checked-in).
