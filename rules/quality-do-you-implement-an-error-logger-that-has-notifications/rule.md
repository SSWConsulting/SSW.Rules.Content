---
type: rule
archivedreason: 
title: Quality - Do you implement an error logger that has notifications?
guid: 17883825-c36c-4d42-b40d-7b539fecba53
uri: quality-do-you-implement-an-error-logger-that-has-notifications
created: 2012-09-25T18:02:29.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- rules-for-error-handling
redirects: []

---

When building an application for a client, you should implement functionality which will notify you personally whenever it throws an exception and log the issue for review.

<!--endintro-->

There are a few reasons to do this:

* It gives you a sense of ownership of the project
* It makes finding out what's going wrong easier
* You can keep a history so you can see if there are any recurring exceptions
* You can ensure the long term quality of you application
* You are not just washing your hands and leaving at the end of the release

You will find that this will lead to more clients who are happy to use you into the future because they know that you care about their application.
