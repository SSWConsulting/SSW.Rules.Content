---
type: rule
title: Do you reference the issue ID when writing a test to confirm a bugfix?
uri: do-you-reference-the-issue-id-when-writing-a-test-to-confirm-a-bugfix
created: 2020-03-11T20:48:03.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Some bugs have a whole histroy related to them and when we fix them we don't want to lose the rationale for the test. By adding a comment to the test, referencing the bug ID - future developers can see why a test is testing a particular behaviour.<br> </span>

<p class="ssw15-rteElement-CodeArea">​[Test]<br>public void&#160;TestProj11()<br>&#123;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example - The test name is the bug&#160;ID and I don't know what it is meant to test​​​<br></dd><p class="ssw15-rteElement-CodeArea"> ///<br> Test case where a user can cause an application exception on the<br> Seminars webpage<br> 1. User enters a title for the seminar<br> 2. Saves the item<br> 3. Presses the back button<br> 4. Chooses to resave the item<br> See&#58; https&#58;//server/jira/browse/PROJ-11<br> ///<br>[Test]<br>public void TestResavingAfterPressingBackShouldntBreak()<br>&#123;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - The test name is clearer,&#160;good comments for the unit test​​​ give a little context, and there is a&#160;link to original bug<br></dd>


