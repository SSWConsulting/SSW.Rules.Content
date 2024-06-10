---
seoDescription: Test regular expressions to ensure future changes don't break existing requirements.
type: rule
title: Do you test your regular expressions?
uri: test-regular-expressions
authors:
  - title: Igor Goldobin
    url: https://ssw.com.au/people/alumni/igor-goldobin
created: 2024-03-09T01:35:11.086Z
guid: 6be11005-f82a-48ba-8300-460284be1df5
---

Everyone writes unit tests for their code, because it helps developer to make changes in future without breaking existing functionalities. The same goes for regular expressions. A good regular expression will have a set of test cases to make sure any future changes does not invalidate existing requirements.

<!--endintro-->

You should not fix a regular expression until we have added a good and a bad test case.

If your application is driven by regular expressions, you need a good test harness. Here is an example of a test harness we use in CodeAuditor.

![Figure: Test Harness for regular expressions in CodeAuditor](codeauditorregextester.gif)
