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


​Team Foundation Server&#160;is great,&#160;and one of its neat features is&#160;enforcing comments when checking in code. Without comments, some of the other built in features like History become ​redundant without comments. 
<br><excerpt class='endintro'></excerpt><br>
<div><em><br></em></div><div><em>You should have good comments… if you are struggling use <a href="http&#58;//programmingexcuses.com/">this​​</a>.</em><br></div><div><br></div><img src="/PublishingImages/15-07-2014%2010-21-04%20AM.png" alt="15-07-2014 10-21-04 AM.png" style="margin&#58;5px;width&#58;650px;" />&#160;<font class="ms-rteCustom-FigureBad" size="+0">Figure&#58; Bad Example&#58; No Comments against the check-ins we don’t know what changes were made in each revision </font>​<div><img src="/PublishingImages/15-07-2014%2010-24-40%20AM.png" alt="15-07-2014 10-24-40 AM.png" style="margin&#58;5px;width&#58;650px;" /><br> <font class="ms-rteCustom-FigureGood" size="+0">Figure&#58; Good Example&#58; Now we can pin point which revision a particular change has been made </font><p><br></p><p>In Visual Studio 2013, to enforce this behaviour, you will need to&#58;</p><p><br></p><p><img src="/PublishingImages/15-07-2014%2010-41-30%20AM.png" alt="15-07-2014 10-41-30 AM.png" style="margin&#58;5px;" /><br></p><p><strong>Figure&#58; Go to Team Explorer | Source Control</strong></p><p><img src="/PublishingImages/15-07-2014%2010-42-21%20AM.png" alt="15-07-2014 10-42-21 AM.png" style="margin&#58;5px;line-height&#58;20.799999237060547px;width&#58;650px;" /><br></p><p><strong>Figure&#58; Then Check-in Policy | Add</strong></p><p><img src="/PublishingImages/15-07-2014%2010-42-43%20AM.png" alt="15-07-2014 10-42-43 AM.png" style="margin&#58;5px;line-height&#58;20.799999237060547px;" /><br></p><p><strong>Figure&#58; Then select Changeset Comments Policy and OK</strong></p><p><img src="/PublishingImages/15-07-2014%2010-42-56%20AM.png" alt="15-07-2014 10-42-56 AM.png" style="margin&#58;5px;width&#58;650px;" /><br></p><p><strong>Figure&#58; Now you have the Changeset Comments Policy applied to your Team Project</strong></p>​Now the next time someone checks-in some code, they are forced to enter a comment. </div>


