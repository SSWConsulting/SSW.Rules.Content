---
type: rule
title: Do you conduct a "Test Please" internally and then with the client?
uri: conduct-a-test-please
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: William Liebenberg
    url: https://ssw.com.au/people/william-liebenberg
  - title: Luke Cook
    url: https://ssw.com.au/people/luke-cook
related:
  - do-you-send-as-per-our-conversation-emails
  - do-you-know-when-to-do-use-checked-by-xxx
  - request-a-test-please
  - ask-clients-approval
redirects:
- conduct-a-test-please-internally-and-then-with-the-client
created: 2009-03-02T02:46:56.000Z
archivedreason: null
guid: 537f2847-7144-4d0d-a86d-5dcd224e8f75
---

**Test, test, test!** Testing is the most critical part of any project. Before the delivery of any release, the application must pass an internal "test please". This helps to prevent clients from becoming disillusioned by receiving a bug-riddled application.

<!--endintro-->

![Figure: Do you want users to have good first impressions?](pic16-TestingDoYouWantThemT.gif)  

It's important to understand the [different types of testing](/different-types-of-testing) that you can perform and choose appropriate types for the feature or application you're asked to test.

::: greybox

**Does the "Test Please" principle apply to more than code?**

Yes! A "Test Please", aka peer review, highlights unseen errors, proposes new ideas for consideration or confirms the existing work as the best solution. A peer review can also effect cultural change amongst your development team as developers become more open to critiques of their work and get comfortable with a 'continuous learning' environment. A "Test Please" will also be applied to:

* Brief proposals
* Release plans
* Estimates
* Anything else being sent to a client
* Anything else being sent to an employee of a sensitive nature
* Anything being sent for public consumption, e.g. newsletters, print documents and advertisements.

Always put "test please" in the email subject so readers know they are expected to react quickly.

:::

### Developer responsibilities

1. At the end of a release, prepare a "Test Please" email. Create the email by copying the text from the sample [Test Please Template](/request-a-test-please).
2. Find two testers to test your app. Some teams don't have dedicated testers, so you can designate another developer on the team as a tester.
3. Include a link to the specific GitHub Issue / Azure DevOps PBI so that the testers can know what the [Acceptance Criteria](/acceptance-criteria) is and can test accordingly
4. [Triage](/do-you-send-sprint-forecast-and-sprint-review-retro-emails-to-the-client) any bug/suggestion emails from the testers
5. Make sure that the testers know which build they are testing. The developers may be 3 builds ahead of the testers, but they need to complete a test run on an individual build to make sure that bugs are fixed and that there are no regressions.

    **Note:** Having a good branching strategy and using [ephemeral environments](https://www.youtube.com/watch?v=-KrodXD3lPc) makes testing a feature easy and have confidence in the outcome before allowing the code to be committed to `origin/main`. This protects your `origin/main` branch from contamination by code that does not work.

6. When you receive a "Test Pass" from both testers (and never before), prepare a "DONE Email" for the client.

    **Note:** If you are requested to issue an untested release to a client, clearly state "Has not passed internal testing" in the email.

7. Include "✅ Done" in the reply email or Issue/PBI and briefly explain the work performed and the testing outcome.

### Tester responsibilities

1. Test within the hour - testing is typically urgent.
2. Know what to test - check the Acceptance Criteria on the GitHub Issue / Azure DevOps PBI
3. Be thorough - report any major or minor bugs (remembering to report each [bug/suggestion](/report-bugs-and-suggestions/) in a separate email).
4. "Reply All" to the **original** Test Please request email for each bug or feature you report (to ensure that no issue is reported twice).
5. Specify how you replicated the bug through clear reproduction steps and screenshots.
6. When finished, reply to the "Test Please" email and include "Test Pass (as no critical bugs)" or "Test Failed (as per critical bugs reported)" at the top of the email.

::: email-template
|          |     |
| -------- | --- |
| To:      | Gary |
| Subject: | RE: Test Please - \\Public Folders\All Public Folders\SSWeXtremeEmailsDatabase\SSWCodeAuditor\Release09 |
::: email-content

### Hi Gary,

This was a good version but, unfortunately:

❌ **Test failed**
(as per critical bugs reported in other emails) 
`youtube: https://www.youtube.com/embed/whxbTtkH5GU` 

**Video: Test Failed! (10 sec)**
::: 
:::
::: good  
Figure: Good Example - This is how to reply failed to a "test please" email 
:::

**Note:** If the test to be performed is quick and the tester is available on the spot, consider using a "[checked by](/do-you-know-when-to-do-use-checked-by-xxx)" style instead to save some time.
