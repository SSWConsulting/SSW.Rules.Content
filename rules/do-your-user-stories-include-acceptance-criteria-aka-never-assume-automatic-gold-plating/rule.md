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

<p><strong>Acceptance Criteria </strong>(from the Product Owner) define the exact requirements that must be met for the story to be completed. They answer the question, &quot;How will I know when I’m done with the story?&quot;</p>
<img src="/Management/RulesToBetterScrumUsingTFS/PublishingImages/acceptance-criteria.jpg" alt="A User Story with Acceptance Criteria" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; A User Story with Acceptance Criteria (MSF Agile Template)</span><br>
<p class="ms-rteCustom-GreyBox">When I enter ‘Adam’ in the search box and click ‘Search’ I will see all entries starting with ‘Adam’ in the grid<br>
</p>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example of Acceptance Criteria - Incomplete</span>

<p class="ms-rteCustom-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>
Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid
</p>
<span class="ms-rteCustom-FigureNormal">Figure&#58; OK Example of Acceptance Criteria</span>
<p class="ms-rteCustom-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>
Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br>
Gold Plating - If no results are retuned show a message box ‘No results found’<br>
Gold Plating – Validation&#58; If no search text is entered, the ‘Search’ button should be disabled<br>
Gold Plating – Right clicking on a column header should provide ‘Sort’ functionality<br>
Gold Plating – if a large set of results is returned, display pagination with page numbers and ‘Prev’, ‘Next’ links<br></p>
<span class="ms-rteCustom-FigureGood">&#160;Figure&#58; Good Example of Acceptance Criteria – Including Gold Plating<br>
</span><p></p>



