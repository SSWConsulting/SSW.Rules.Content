---
type: rule
archivedreason: 
title: Does Your Team Write Acceptance Tests to Verify Acceptance Criteria?
guid: e8e0f82e-bee8-42a5-a880-729986e56ecd
uri: does-your-team-write-acceptance-tests-to-verify-acceptance-criteria
created: 2012-11-08T19:00:32.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---


<p><strong>​Acceptance Tests</strong> (built by the developers) verify that the Acceptance Criteria are met.<br>
The goal is for teams to move beyond manual testing and implement automated testing <br>
eg. CodedUI tests, Telerik Tests etc<br>
 Test cases answer the question, "How do I test and what are the test steps?"</p>
<br><excerpt class='endintro'></excerpt><br>


<img class="ms-rteCustom-ImageArea" alt="Test Cases in a User Story" src="acceptance-criteria-test-cases.jpg" /> 
<span class="ms-rteCustom-FigureNormal">Figure: Test Cases in a User Story  (MSF For Agile Template)</span><br>
<p class="ms-rteCustom-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>
Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br>
Gold Plating - If no results are retuned show a message box ‘No results found’<br>
Gold Plating – Validation: If no search text is entered, the ‘Search’ button should be disabled<br>
Gold Plating – Validation: If the button is disable and search text is entered, the ‘Search’ button becomes enabled<br>
Gold Plating – Right clicking on a column header and using the ‘Sort’ functionality, sorts the data by that column<br>
Gold Plating – if a large set of results is returned, clicking the pagination page numbers shows the correct data<br>
Gold Plating – if a large set of results is returned and we are on page &gt; 1, clicking the ‘Prev’ button goes to the previous page<br>
Gold Plating – if a large set of results is returned and we are on page 1, ‘Prev’ button does not error<br>
Gold Plating – if a large set of results is returned and we are on page &lt; MaxPage, clicking the ‘Next’ button goes to the next page<br>
Gold Plating – if a large set of results is returned and we are on page = MaxPage, clicking the ‘Next’ button does not error<br>
<br>
</p>
<span class="ms-rteCustom-FigureGood"> Figure: Good example - Acceptance Tests</span>

<img class="ms-rteCustom-ImageArea" alt="Test Cases" src="test-cases.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure: The tester sees the Test Cases in Test Manager</span>

<img class="ms-rteCustom-ImageArea" alt="Test Steps" src="test-steps.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure: The tester follows each instruction (aka the Test Steps), and gives it a tick or cross</span>

<h2>Related Resources</h2>
<p><a href="http://www.scrumalliance.org/articles/169-new-to-user-stories" shape="rect">http://www.scrumalliance.org/articles/169-new-to-user-stories</a></p>


