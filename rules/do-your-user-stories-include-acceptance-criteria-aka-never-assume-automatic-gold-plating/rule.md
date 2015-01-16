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

<p><strong><img src="/PublishingImages/DevsAndUsers.jpg" alt="DevsAndUsers.jpg" style="margin&#58;5px;" /><br></strong></p><p><strong>Figure&#58; You need a common language to communicate in</strong></p><p> 
   <strong>Acceptance Criteria </strong>(from the Product Owner) define the exact requirements that must be met for the story to be completed. They answer the question, &quot;How will I know when I’m done with the story?&quot;</p><dl class="image"><dt> 
      <img src="/PublishingImages/acceptance-criteria.jpg" alt="A User Story with Acceptance Criteria" class="ms-rteCustom-ImageArea" />
   </dt><dd>Figure&#58; A User Story with Acceptance Criteria (MSF Agile Template)</dd></dl><dl class="bad"><dt><p>When I enter ‘Adam’ in the search box and click ‘Search’ I will see all entries starting with ‘Adam’ in the grid.</p></dt><dd>Figure&#58; Bad Example of Acceptance Criteria - Incomplete</dd></dl><dl class="image"><dt><div class="greyBox"><p>Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br> Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid</p></div></dt><dd>Figure&#58; OK Example of Acceptance Criteria</dd></dl><dl class="good"><dt><p>Positive Test -When I enter ‘Adam’ in the Search box and click ‘Search’ I will see all entries starting with Adam in the Grid<br> Negative Test - When I enter ‘zzz’ in the Search box and click ‘Search’ I will see *no* entries in the Grid<br> Gold Plating - If no results are retuned show a message box ‘No results found’<br> Gold Plating – Validation&#58; If no search text is entered, the ‘Search’ button should be disabled<br> Gold Plating – Right clicking on a column header should provide ‘Sort’ functionality<br> Gold Plating – if a large set of results is returned, display pagination with page numbers and ‘Prev’, ‘Next’ links​</p></dt><dd>Figure&#58; Good Example of Acceptance Criteria – Including Gold Plating<br> </dd></dl><p>For tiny stories, you can omit acceptance criteria. Sometimes you just need a screen shot, or even better a video.</p><dl class="good"><dt><p>See screen shot and video.</p><p>Screen shot – 
         <a href="/Documents/13_Anvil_1408_Customer.pdf">see PDF</a><br> Video - 
         <a href="http&#58;//www.youtube.com/watch?v=M3FH4D9QuzU" title="http&#58;//www.youtube.com/watch?v=M3FH4D9QuzU" target="_blank">http&#58;//ww​w.youtube.com/watch?v=M3FH4D9QuzU​</a></p></dt><dd>Figure&#58; Good Example for a simple change – just include a screen capture and/or video</dd></dl>


