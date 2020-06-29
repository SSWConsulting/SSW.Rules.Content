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
  <p>Most teams are getting the hang of User Stories that have subtasks. Unfortunately the same can’t be said about acceptance criteria. <br>It is so important because real user stories tell a team when the task is done.</p>
<p>Also, Product Owners should not get heartburn because ‘obvious’ functionality was not included. All requirements should be specified in the Acceptance Criteria.</p><p>For example, Product Owners should not assume things like&#58;</p>
<ul>
    <li>they will get a message that says ‘no records found’ or</li>
    <li>the grid will support features such as pagination or sorting</li>
</ul>
<p>They must be specified in the Acceptance Criteria if required.</p>
<p>There are 2 parts to getting this right. The Acceptance Criteria, then the Acceptance Tests&#58;</p>
 </span>

<dl class="image"><dt> <img src="DevsAndUsers.jpg" alt="DevsAndUsers.jpg" /> </dt><dd>Figure&#58; You need a common language to communicate in</dd></dl><p>
   <strong>Acceptance Criteria </strong>(from the Product Owner) define the exact requirements that must be met for the story to be completed. They answer the question, &quot;How will I know when I' m done with the story?&quot;</p><dl class="image"><dt> <img src="acceptance-criteria.jpg" alt="A User Story with Acceptance Criteria" class="ms-rteCustom-ImageArea" /> </dt><dd>Figure&#58; A User Story with Acceptance Criteria (MSF Agile Template)​<br></dd></dl><p class="ssw15-rteElement-GreyBox">When I enter ‘Adam’ in the search box and click 'Search' I will see all entries starting with 'Adam' in the grid.</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example of Acceptance Criteria - Incomplete <br></dd><p class="ssw15-rteElement-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br></p><dd class="ssw15-rteElement-FigureNormal"> Figure&#58; OK Example of Acceptance Criteria</dd><p class="ssw15-rteElement-GreyBox">Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br>Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br>Gold Plating - If no results are retuned show a message box ‘No results found’<br>Gold Plating – Validation&#58; If no search text is entered, the ‘Search’ button should be disabled<br>Gold Plating – Right-clicking on a column header should provide ‘Sort’ functionality<br>Gold Plating – if a large set of results is returned, display pagination with page numbers and ‘Prev’, ‘Next’ links<br></p><dd></dd><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Good Example of Acceptance Criteria – Including Gold Plating <br></dd><p>For tiny stories, you can omit acceptance criteria. Sometimes you just need a screenshot, or even better a video.</p><p class="ssw15-rteElement-GreyBox">See screenshot and video.<br>Screenshot – <a href="/Documents/13_Anvil_1408_Customer.pdf">see PDF</a><br>Video - <a href="http&#58;//www.youtube.com/watch?v=M3FH4D9QuzU" title="http&#58;//www.youtube.com/watch?v=M3FH4D9QuzU" target="_blank">http&#58;//ww w.youtube.com/watch?v=M3FH4D9QuzU </a></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example for a simple change – just include a screen capture and/or video <br></dd> <br>


