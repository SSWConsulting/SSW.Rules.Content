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

### Lead Developer responsibilities

Please cc the client in all your "Test Please" emails including internal ones.

1. At the end of a release, prepare a "Test Please" email.  Create the email by copying the text from the sample 
      [Test Please Template](/request-a-test-please) .
2. Get two testers to test your app - if it's a web app, make sure one uses Chrome and the other Firefox.
3. Specify exactly what is required to be tested by adding some bullet points at the top and highlighting in yellow, so it stands out from the template text, e.g.
    * Run Timesheet report
    * Check changing a rate
4. Make sure the testers send only one bug/suggestion per email.
5. [Triage](/do-you-send-sprint-forecast-and-sprint-review-retro-emails-to-the-client) emails as they come in for completion in this release, or a later release.
6. Don't change testers in the middle of a release. It is just sneaky to get a test failed from a tester and then try again by using another tester :-)
7. Make sure that the testers know which build they are testing. The developers may be 3 builds ahead of the testers, but they need to complete a test run on an individual build to make sure that bugs are fixed and that there are no regressions.

**Note:** Having a good branching strategy makes this easy as you can run an Internal and External "Test Please" on your DEV branch before allowing the code to be committed to Main/Trunk. This protects your Main/Trunk branch from contamination by code that does not work.
8. Randomly have the manager do a "Test Please" as well. They give a pass or fail on the job the testers did.
9. When you receive a "Test Pass" from both testers (and never before), prepare a "Test Please" for the client. (If you are requested to issue an untested release to a client, clearly state "Has not passed internal testing" in the email.)

### Tester responsibilities

1. Confirm you are a tester - if the developer did not name you, make sure they correct themselves and resend the "test please" email.
2. Ensure you are working on the Standard Operating Environment specific to the client and using the right browser for web apps.
3. Use [Microsoft Teams, Zoom or Team Viewer](/make-it-easy-to-see-the-users-pc/) if you aren't available locally.
4. Test within the hour - testing is typically urgent.
5. Know what to test.
6. Be thorough - anything from a crash-to-code bug to a minor UI change should be reported (remembering to report each issue/bug/suggestion in a separate email).
7. Classify issues as bugs or suggestions following the [bug/suggestions](/report-bugs-and-suggestions/) rule.
8. "Reply All" for each bug or feature you report (to ensure that no issue is reported twice).
9. Specify how you replicated the bug through clear instructions and screenshots.
10. When finished, reply to the "Test Please" email with "Test Pass (as no critical bugs)" or "Test Failed (as per critical bugs reported)". 

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
