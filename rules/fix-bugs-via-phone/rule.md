---
seoDescription: Fix bugs efficiently by reproducing issues quickly and consulting clients only when necessary to resolve problems.
type: rule
title: Do you fix bugs with a phone call?
uri: fix-bugs-via-phone
authors:
  - title: Penny Walker
    url: https://ssw.com.au/people/penny-walker
related:
  - fix-bugs-first
  - report-bugs-and-suggestions
redirects:
  - do-you-fix-bugs-with-a-phone-call
created: 2020-03-25T23:32:52.000Z
archivedreason: null
guid: b839ae1f-631c-4a3f-a983-116eba48806f
---

While developers might not enjoy fixing bugs, it’s an important part of what they need to do. Fixing bugs interrupts the flow of new development work, so it’s good to deal with bug fixes as quickly as possible.

<!--endintro-->

Imagine this familiar scenario:

::: greybox
You receive a bug report...  
you read it, try to reproduce it, and try to fix it.

If you can’t reproduce it, you then call the client and ask them to walk you through it.  
Then you fix it - if they were able to reproduce the issue.  
:::
::: bad
Bad example - Time spent trying to reproduce the bug by yourself
:::

The bug may have been reported poorly with not enough information to help you easily reproduce it or it might be a bug that's dependent on something specific to your client's environment.

A slightly different approach can save some time and effort:

::: greybox
You receive a bug report...  
you read it and only try to reproduce it if there are clear steps in the bug report - timebox reproducing the bug to 5 minutes

If there are no reproduction steps in the bug report or you've spent 5 minutes unsuccessfully trying to reproduce it, then call the client and ask them to reproduce the issue. You have some good context for this conversation thanks to your effort in trying to reproduce it already.

If they are able to reproduce it, then you fix it.   
:::
::: good
Good example - Calling the bug reporter if you can't easily reproduce the issue
:::

Sometimes the client can’t reproduce the issue, or it turns out that the problem was external, e.g. an internet connectivity issue and not related to the product. In this case, there is nothing to fix, and you can close the bug report and get back to whatever you were supposed to be focusing on that day. In this case, we’ve fixed a bug with a phone call. We’ve also shown the client that we’re really responsive and care about issues that they encounter.

::: greybox
**Tip**: You can help your clients to understand how to provide better bug reports by using the ideas in the
[Do you know how to report bugs and give suggestions?](/report-bugs-and-suggestions) rule.
:::

[Prioritizing communication](/make-yourself-available-on-different-communication-channels) is paramount and this is another great way of doing that.
