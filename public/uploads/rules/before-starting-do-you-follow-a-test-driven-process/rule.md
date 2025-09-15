---
seoDescription: Developers ensure code quality by following a test-driven process, involving continuous integration and gated check-in.
type: rule
archivedreason:
title: Before starting - Do you follow a Test Driven Process?
guid: 786cd996-54da-4864-9362-26893d5acb4d
uri: before-starting-do-you-follow-a-test-driven-process
created: 2011-11-18T03:52:57.0000000Z
authors:
  - title: Justin King
    url: https://ssw.com.au/people/justin-king
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
related: []
redirects:
  - (before-starting)-do-you-follow-a-test-driven-process
---

Never allow a situation where a developer can check outcode and the code does not compile – or the unit tests are not all green. This is called “breaking the build” and the punishment in our office is 20 push-ups and fixing broken links for an hour!

<!--endintro-->

1. Check out
2. Compile
3. Develop
4. Compile
5. Check-In

Figure: Bad example - wrong process
![Figure: Before you start cooking prepare all your ingredients. Before you start coding, "Get Latest" the right way](BeforeCoding.jpg)

1. Get latest
2. Compile
3. Run Unit Tests
4. If Tests pass then start developing
5. Check out
6. Develop
7. Compile
8. Run Unit Tests
9. Get Latest (Always do a Get Latest before checking in as code you didn't change could break your code)
10. Compile
11. Run Unit Tests
12. Check-In if all tests passed
13. Wait for gated check-in (GC) to complete
14. Reconcile your workspace if it was successful
15. Check that Continuous Integration (CI) build was successful(If GC was skipped)

Figure: Good example - right process
\*\*
\*\*

**Note:** You should have both a Gated-Check-in (GC) and a Continuous Integration (CI) build on every branch.
