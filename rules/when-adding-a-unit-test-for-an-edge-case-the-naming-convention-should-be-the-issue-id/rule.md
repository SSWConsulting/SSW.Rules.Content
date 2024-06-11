---
seoDescription: When writing tests to confirm bugfixes, it's essential to reference the issue ID in the test name and comments. This provides context for future developers, helping them understand why a particular test exists.
type: rule
title: Do you reference the issue ID when writing a test to confirm a bugfix?
uri: when-adding-a-unit-test-for-an-edge-case-the-naming-convention-should-be-the-issue-id
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-reference-the-issue-id-when-writing-a-test-to-confirm-a-bugfix
created: 2020-03-11T20:48:03.000Z
archivedreason: null
guid: 71a28a7c-3f3f-4cea-b0e4-4f1a5dc58f76
---

Some bugs have a whole history related to them and, when we fix them, we don't want to lose the rationale for the test. By adding a comment to the test that references the bug ID, future developers can see why a test is testing a particular behaviour.

<!--endintro-->

```cs
[Test]
public void TestProj11()
{
}
```

::: bad
Figure: Bad example - The test name is the bug ID and it's unclear what it is meant to test

:::

```cs
///
 Test case where a user can cause an application exception on the
 Seminars webpage
 1. User enters a title for the seminar
 2. Saves the item
 3. Presses the back button
 4. Chooses to resave the item
 See: https://server/jira/browse/PROJ-11
 ///
[Test]
public void TestResavingAfterPressingBackShouldntBreak()
{
}
```

::: good
Figure: Good example - The test name is clearer, good comments for the unit test give a little context, and there is a link to the original bug report

:::
