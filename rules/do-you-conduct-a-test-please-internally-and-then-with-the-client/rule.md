---
type: rule
archivedreason: Duplicate of [https://www.ssw.com.au/rules/conduct-a-test-please](/rules/conduct-a-test-please)
title: Do you conduct a "test please" internally and then with the client?
guid: 917e754e-270e-46f0-a325-a942297f919c
uri: do-you-conduct-a-test-please-internally-and-then-with-the-client
created: 2009-03-02T02:46:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- do-you-send-as-per-our-conversation-emails
- do-you-know-when-to-do-use-checked-by-xxx
- quality-do-you-know-how-to-request-a-test-please
redirects: []

---

**Test, test, test!** Testing is the most critical part of any project. Before the delivery of any release the application must pass an internal "test please". Clients quickly become disillusioned if you have delivered a bug-riddled application.

<!--endintro-->

![Figure: Do you want users to have good first impressions?](pic16-TestingDoYouWantThemT.gif)  

There are a number of different types of tests that you can perform:

* **Unit Testing:**     It validates the smallest testable parts of an application. Unit tests do not cover the UI layer. There is no industry standard 3rd party unit test tool but at SSW we use NUnit and Visual Studio Team Test.
* **White Box Testing:**     White box testing or structural testing is done knowing the internal code implementation and targeting specific aspects: for example security risks or a potential performance bottle neck. By looking at the implementation it helps to identify areas where the system could be flawed. Because the tests are designed to match the code, if the implementation changes, the tests will need to change.
* **Black Box Testing:**     Black box testing or functional testing, unlike the White box testing, doesn't rely on the knowledge of the internal code structure. It relies on the software specifications and requirements. The tests use valid and invalid inputs and check that the output is correct.
* **Integration Testing:**     Integration testing is performed when all the software components are put together. This testing should be done after each individual software component has passed unit testing. This type of testing highlights interface problems or misunderstanding of the software specifications where unit tests local to each component actually passed. Automated integration testing is essential and often run overnight due to the time it takes.
* **User Acceptance Testing (UAT):**     UAT or Beta Testing occurs at the end of the software development cycle (this could be at the end of a Scrum Sprint where the software is potentially shippable). As its name points out the end users will test the software and check it meets their acceptance criteria.
* **Security testing:**     Security testing is done to check that a system protects data and maintains confidentiality as intended. The concepts covered by Security testing can include: network mapping, vulnerability scanning, password cracking, confidentiality, integrity, authentication, authorization, availability, non-repudiation and virus scanning.
* **Performance testing:**     Performance Testing is used to determine the responsiveness, the effectiveness of a system under a given workload. Qualitative attributes such as reliability, scalability and interoperability may also be evaluated. Performance testing is often done along with stress testing.
* **Smoke testing:**     Smoke testing is done to ensure the system doesn't have any critical bugs that would make other types of testing unnecessary. This type of testing is generally performed on a new or fixed software. A Smoke test should cover essential parts of the application so it is said to be shallow and broad.

::: greybox

**Does the "Test Please" principle apply to more than code?**
Yes! A "Test Please", aka peer review highlights unseen errors, proposes new ideas for consideration or confirms the existing work as the best solution. A peer review can also effect cultural change amongst your development team as developers become more open to critiques of their work and comfortable with a 'continuous learning' environment. A "Test Please" will also be applied to:

* Brief proposals
* Release plans
* Estimates
* Anything else being sent to a client
* Anything else being sent to an employee of a sensitive nature
* Anything being sent for public consumption - such as newsletters, print documents and or advertisements.

Always put "test please" in the email body so readers know they are expected to react quickly.

:::

###  

   Lead Developer responsibilities

Please cc the client in all your "Test Please" emails including internal ones.

1. At the end of a release, prepare a "Test Please" email.  Create the email by copying the text from the sample [Test Please Template](/request-a-test-please) .
2. Get two testers to test your app - if it's a web app make sure one uses IE and the other Firefox.
3. Specify exactly what is required to be tested by adding some bullet points at the top and highlighting in yellow, so it stands out from the template text. e.g.
    * Run Timesheet report
    * Check changing a rate
4. Make sure the testers send one bug/suggestion per email.
5. [Triage](/do-you-send-sprint-forecast-and-sprint-review-retro-emails-to-the-client) emails as they come in for completion in this release, or a later release.
6. Don't change testers in the middle of a release. It is just sneaky to get a test failed from a tester and then try again by using another tester :-)
7. Make sure that the testers know which build they are testing. The developers may be 3 builds ahead of the testers, but they need to complete a test run on an individual build to make sure that bugs are fixed and that there are no regressions.    Note: Having a good branching strategy makes this easy as you can run an Internal and External "Test Please" on your DEV branch before allowing the code to be committed to Main/Trunk. This protects your Main/Trunk branch from contamination by code that does not work.
8. Randomly have the manager do a "Test Please" as well. He gives a pass or fail on the job the testers did.
9. When you receive a "Test Please Succeeded" from both testers (and never before) prepare a "Test Please" for the client. (If you are requested to issue a non-tested release to a client state "Has not passed internal testing" in the email.)

###  

   Tester responsibilities

1. Confirm you are a tester - If the developer did not name you, make sure he corrects himself and resends the 'test please' email.
2. Ensure you are working on the Standard Operating Environment specific to the client and using the right browser for web apps.
3. Use [Team Viewer](http://www.ssw.com.au/ssw/Standards/DeveloperGeneral/networkTools.aspx#TeamViewer) if you aren't available locally.
4. Test within the hour - testing is typically urgent.
5. Know what to test.
6. Be thorough - anything from a crash-to-code bug to a minor UI change should be reported .(one email at a time)
7. Classify issues accordingly to "this release" or "next release" following the [report bug/enhancement](http://www.ssw.com.au/ssw/Standards/Support/BugReportOrEnhancement.aspx) standard. Any crash to code bugs must be fixed in the current release.
8. "Reply to all" for each bug or feature. (to ensure no issue is reported twice)
9. Specify how you replicated the bug through clear instructions and screenshots.
10. When finished reply to the 'test please' email with "Test Please Succeeded (as no Critical bugs)" or "Test please failed (as per critical bugs reported)".

::: greybox

**Subject:** RE: Test Please - \\Public Folders\All Public Folders\SSWeXtremeEmailsDatabase\SSWCodeAuditor\Release09

Gary,

**Test please failed**

(as per critical bugs reported in other emails)

:::
 **Figure: This is how to reply failed to a "test please" email**

**Note:** If the test to be performed is quick and the tester is available on the spot, consider using a "[checked by](/do-you-know-when-to-do-use-checked-by-xxx)" style instead to save some time.
