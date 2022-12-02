---
type: rule
title: Do you know how to manage and report on exploratory testing?
uri: manage-report-exploratory-testing
authors:
  - title: Lee Hawkins
    url: https://www.ssw.com.au/people/lee-hawkins
related:
  - what-is-exploratory-testing
  - why-testing-cannot-be-completely-automated
created: 2022-12-01T23:32:41.976Z
guid: f4afbf05-4cb8-4e29-a965-0590a3ea1269
---
* Exploratory Testing (ET) gives the tester much more freedom and responsibility in their testing than when following a more scripted approach. 

Putting some structure around ET helps to make the approach more credible and provides a way for managers to track and review testers' work.

Session-based test management (SBTM) is a lightweight approach to the management of exploratory testing effort that defines a set of expectations for what kind of work will be done and how it will be reported. 

>[SBTM is] a way for the testers to make orderly reports and organize their work without obstructing the flexibility and serendipity that makes exploratory testing useful
>     - Jon Bach

            
<!--endintro-->

### Testing in sessions

The "session" is the basic unit of work in exploratory testing (and not, for example, a test case or bug report).


::: greybox
A "session" is an uninterrupted block of reviewable, chartered test effort
:::



Breaking this down:





* By “uninterrupted,” we mean no significant interruptions, no email, meetings, chatting or telephone calls (90 minutes is a common length for such an uninterrupted session - any longer and interruption is almost inevitable)

* By “reviewable,” we mean a report, called a session sheet, is produced that can be examined by a third-party (such as the test lead/manager) that provides information about what happened.
* By “chartered,” we mean that each session is associated with a mission - what we are testing or what types of problems we are looking for (such charters are descriptive but not prescriptive, and kept short, a couple of sentences at most).



It is acknowledged that there are many non-testing distractions throughout the working day (e.g. meetings, email, and other important - and unimportant! - activities), so typically SBTM allows for 4-5 hours of "on session" time per day for each tester. In this way, we allow for non-testing activities and also leave time for the very important post-session debriefing (see below).


Lightweight reporting is a key part of SBTM and while we want to know what tasks happen during a test session, we don’t want the reporting to be too much of a burden (more time testing, less time writing about testing). The session sheet is the output artifact from a session and this is designed to be a very simple standard way of reporting what happened during a session, with a focus on "just enough" detail for debriefing and historical reference, but not too much detail that the tester spends most of their time writing about the session. An example of a session sheet template can be found here and the wiki is an ideal place to store completed session sheets for ease of reference - linking the session sheets back to the user story they relate to then provides a very easy way to trace the testing that was performed for a particular story.


A few simple metrics are captured in the session sheet, often referred to as the "TBS” metrics:


T - Percentage of session time spent on test design and execution

B - Percentage of session time spent investigating problems (bug reporting)

S - Percentage of session time spent setting up for testing (anything else testers do that makes the first two tasks possible, including tasks such as configuring equipment, locating materials, reading manuals, or writing a session report)


These metrics are rough percentages, they are not meant to be accurate to the minute but more designed to reveal whether testing is being blocked by setup problems or overly buggy software not worthy of testing yet.


Apart from the task breakdown metrics, there are three other major parts of the session sheet: bugs, issues, and notes. Bugs are concerns about the quality of the product, along with their identifiers in the bug tracking system. Issues are questions or problems that relate to the test process or the project at large, ready for discussion during debriefing.


Notes are a free-form record of anything else. Notes may consist of test case ideas, function lists, risk lists, or anything else related to the testing that occurs the session. It is the notes that provide "just enough" detail about the testing in the session. Mind maps are sometimes used instead of wordy notes as a visual representation of the test effort and the thought processes of the tester.

### Debriefing


### Metrics & reporting

mention how to use mind maps for reporting

### Tips for getting started


### Further reading

template/example session sheet would be good

**Add your rule to a category**

