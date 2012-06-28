---
type: rule
title: Do Your User Stories Include Acceptance Criteria? (aka Never assume automatic Gold Plating)
uri: do-your-user-stories-include-acceptance-criteria-aka-never-assume-automatic-gold-plating
created: 2011-05-30T08:13:44.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> 
  <p>Most teams are getting the hang of User Stories that have sub tasks. Unfortunately the same can’t be said about acceptance criteria. <br>
It is so important because real user stories tell a team when the task is done.</p>
<p>Also Product Owners should not get heartburn because ‘obvious’ functionality was not included. All requirements should be specified in the Acceptance Criteria.<br>
For example, Product Owners should not assume things like&#58;</p>
<ul>
    <li>they will get a message that says ‘no records found’ or </li>
    <li>the grid will support features such as pagination or sorting </li>
</ul>
<p>They must be specified in the Acceptance Criteria if required.</p>
<p>There are 2 parts to getting this right. The Acceptance Criteria, then the Acceptance Tests&#58;</p>
 </span>


  <p>•&#160;<strong>Acceptance Criteria </strong>(from the Product Owner) define the exact requirements that must be met for the story to be completed. They answer the question, “How will I know when I’m done with the story?” </p>
<img class="ms-rteCustom-ImageArea" alt="A User Story with Acceptance Criteria" src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/acceptance-criteria.jpg" /> <font size="-0" class="ms-rteCustom-FigureNormal">Figure&#58; A User Story with Acceptance Criteria (MSF Agile Template)</font><br>
<font size="-0" class="ms-rteCustom-GreyBox">When I enter ‘Adam’ in the search box and click ‘Search’ I will see all entries starting with ‘Adam’ in the grid<br>
</font><br>
<font size="-0" class="ms-rteCustom-FigureBad">Figure&#58; Bad Example of Acceptance Criteria - Incomplete</font>
<p>&#160;</p>
<p><font size="-0" class="ms-rteCustom-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>
Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br>
</font><br>
<font size="-0" class="ms-rteCustom-FigureNormal">Figure&#58; OK Example of Acceptance Criteria</font>&#160;<br>
<font size="-0" class="ms-rteCustom-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>
Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br>
Gold Plating - If no results are retuned show a message box ‘No results found’<br>
Gold Plating – Validation&#58; If no search text is entered, the ‘Search’ button should be disabled<br>
Gold Plating – Right clicking on a column header should provide ‘Sort’ functionality<br>
Gold Plating – if a large set of results is returned, display pagination with page numbers and ‘Prev’, ‘Next’ links</font><br>
<font size="-0" class="ms-rteCustom-FigureGood">&#160;Figure&#58; Good Example of Acceptance Criteria – Including Gold Plating<br>
</font><br>
•&#160;<strong>Acceptance Tests</strong> (built by the developers) verify that the Acceptance Criteria are met.<br>
The goal is for teams to move beyond manual testing and implement automated testing <br>
eg. CodedUI tests, Telerik Tests etc<br>
&#160;Test cases answer the question, “How do I test and what are the test steps?” </p>
<img class="ms-rteCustom-ImageArea" alt="Test Cases in a User Story" src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/acceptance-criteria-test-cases.jpg" /> <font size="-0" class="ms-rteCustom-FigureNormal">Figure&#58; Test Cases in a User Story&#160; (MSF For Agile Template)</font><br>
<font size="-0" class="ms-rteCustom-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>
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
</font><br>
<font size="-0" class="ms-rteCustom-FigureGood">&#160;Figure&#58; Good example - Acceptance Tests</font><br>
<strong>Related Resources</strong><br>
<a shape="rect" href="http&#58;//www.scrumalliance.org/articles/169-new-to-user-stories">http&#58;//www.scrumalliance.org/articles/169-new-to-user-stories</a>

<img class="ms-rteCustom-ImageArea" alt="Test Cases" src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/test-cases.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; The tester sees the Test Cases in Test Manager</span>

<img class="ms-rteCustom-ImageArea" alt="Test Steps" src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/test-steps.jpg" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; The tester follows each instruction (aka the Test Steps), and gives it a tick or cross</span>


