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


Team System is great, but there are some standard features in other source control systems that aren’t available. One of the glaring omissions is enforcing comments when checking in code. Without comments, some of the other built in features like History become redundant without comments. 
<br><excerpt class='endintro'></excerpt><br>
<img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/CommentsBad.jpg" alt="" />&#160;<font class="ms-rteCustom-FigureBad" size="+0">Figure&#58; Bad Example&#58; No Comments against the check-ins we don’t know what changes were made in each revision </font><img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/CommentsGood.jpg" alt="" /> <font class="ms-rteCustom-FigureGood" size="+0">Figure&#58; Good Example&#58; Now we can pin point which revision a particular change has been made </font><p>More Information <br>To enforce this behaviour, you will need to&#58; </p>
<ol><li>Install Team Foundation Server Power Tools </li>
<li>Right click the Team Project in Team Explorer &gt; Team Project Settings &gt; Source Control <img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/Enforce1.jpg" alt="" /> </li>
<li>Select the Check-in Policy tab</li>
<li>Click Add </li>
<li>Select the Changeset Comments Policy <br><img class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/Enforce2.jpg" alt="" /> </li></ol>
Now the next time someone checks-in some code, they are forced to enter a comment. 


