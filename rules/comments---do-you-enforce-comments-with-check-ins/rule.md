---
type: rule
archivedreason: 
title: Comments - Do you enforce comments with check-ins?
guid: 38313df6-15aa-448a-b978-edc43b582694
uri: comments---do-you-enforce-comments-with-check-ins
created: 2011-11-18T03:52:40.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
- id: 38
  title: Drew Robson
related: []

---


​Team Foundation Server is great, and one of its neat features is enforcing comments when checking in code. Without comments, some of the other built in features like History become ​redundant without comments. 
<br><excerpt class='endintro'></excerpt><br>
<div><em><br></em></div><div><em>You should have good comments… if you are struggling use <a href="http://programmingexcuses.com/">this​​</a>.</em><br></div><div><br></div><img src="15-07-2014 10-21-04 AM.png" alt="15-07-2014 10-21-04 AM.png" style="margin:5px;width:650px;" /> <font class="ms-rteCustom-FigureBad" size="+0">Figure: Bad Example: No Comments against the check-ins we don’t know what changes were made in each revision </font>​<div><img src="15-07-2014 10-24-40 AM.png" alt="15-07-2014 10-24-40 AM.png" style="margin:5px;width:650px;" /><br> <font class="ms-rteCustom-FigureGood" size="+0">Figure: Good Example: Now we can pin point which revision a particular change has been made </font><p><br></p><p>In Visual Studio 2013, to enforce this behaviour, you will need to:</p><p><br></p><p><img src="15-07-2014 10-41-30 AM.png" alt="15-07-2014 10-41-30 AM.png" style="margin:5px;" /><br></p><p><strong>Figure: Go to Team Explorer | Source Control</strong></p><p><img src="15-07-2014 10-42-21 AM.png" alt="15-07-2014 10-42-21 AM.png" style="margin:5px;line-height:20.799999237060547px;width:650px;" /><br></p><p><strong>Figure: Then Check-in Policy | Add</strong></p><p><img src="15-07-2014 10-42-43 AM.png" alt="15-07-2014 10-42-43 AM.png" style="margin:5px;line-height:20.799999237060547px;" /><br></p><p><strong>Figure: Then select Changeset Comments Policy and OK</strong></p><p><img src="15-07-2014 10-42-56 AM.png" alt="15-07-2014 10-42-56 AM.png" style="margin:5px;width:650px;" /><br></p><p><strong>Figure: Now you have the Changeset Comments Policy applied to your Team Project</strong></p>​Now the next time someone checks-in some code, they are forced to enter a comment. </div>


