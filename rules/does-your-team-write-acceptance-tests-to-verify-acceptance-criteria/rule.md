---
type: rule
title: Does Your Team Write Acceptance Tests to Verify Acceptance Criteria?
uri: does-your-team-write-acceptance-tests-to-verify-acceptance-criteria
created: 2012-11-08T19:00:32.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p><strong>​Acceptance Tests</strong> (built by the developers) verify that the Acceptance Criteria are met.<br>
The goal is for teams to move beyond manual testing and implement automated testing <br>
eg. CodedUI tests, Telerik Tests etc<br>
&#160;Test cases answer the question, &quot;How do I test and what are the test steps?&quot;</p> </span>



<img src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/acceptance-criteria-test-cases.jpg" alt="Test Cases in a User Story" class="ms-rteCustom-ImageArea" /> 
<span class="ms-rteCustom-FigureNormal">Figure&#58; Test Cases in a User Story&#160; (MSF For Agile Template)</span><br>
<p class="ms-rteCustom-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>
Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br>
Gold Plating - If no results are retuned show a message box ‘No results found’<br>
Gold Plating – Validation&#58; If no search text is entered, the ‘Search’ button should be disabled<br>
Gold Plating – Validation&#58; If the button is disable and search text is entered, the ‘Search’ button becomes enabled<br>
Gold Plating – Right clicking on a column header and using the ‘Sort’ functionality, sorts the data by that column<br>
Gold Plating – if a large set of results is returned, clicking the pagination page numbers shows the correct data<br>
Gold Plating – if a large set of results is returned and we are on page &gt; 1, clicking the ‘Prev’ button goes to the previous page<br>
Gold Plating – if a large set of results is returned and we are on page 1, ‘Prev’ button does not error<br>
Gold Plating – if a large set of results is returned and we are on page &lt; MaxPage, clicking the ‘Next’ button goes to the next page<br>
Gold Plating – if a large set of results is returned and we are on page = MaxPage, clicking the ‘Next’ button does not error<br>
<br>
</p>
<span class="ms-rteCustom-FigureGood">&#160;Figure&#58; Good example - Acceptance Tests</span>

<img src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/test-cases.jpg" alt="Test Cases" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; The tester sees the Test Cases in Test Manager</span>

<img src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/test-steps.jpg" alt="Test Steps" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; The tester follows each instruction (aka the Test Steps), and gives it a tick or cross</span>

<h2>Related Resources</h2>
<p><a href="http&#58;//www.scrumalliance.org/articles/169-new-to-user-stories" shape="rect">http&#58;//www.scrumalliance.org/articles/169-new-to-user-stories</a></p>


