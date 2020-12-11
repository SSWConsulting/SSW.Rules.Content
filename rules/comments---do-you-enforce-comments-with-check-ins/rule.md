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

Team Foundation Server is great, and one of its neat features is enforcing comments when checking in code. Without comments, some of the other built in features like History become redundant without comments.  
<!--endintro-->




*You should have good comments… if you are struggling use [this](http://programmingexcuses.com/).*





![](15-07-2014 10-21-04 AM.png) <font class="ms-rteCustom-FigureBad">Figure: Bad Example: No Comments against the check-ins we don’t know what changes were made in each revision </font>

![](15-07-2014 10-24-40 AM.png)
 <font class="ms-rteCustom-FigureGood">Figure: Good Example: Now we can pin point which revision a particular change has been made </font>


In Visual Studio 2013, to enforce this behaviour, you will need to:




![Go to Team Explorer | Source Control](15-07-2014 10-41-30 AM.png)


![Then Check-in Policy | Add](15-07-2014 10-42-21 AM.png)


![Then select Changeset Comments Policy and OK](15-07-2014 10-42-43 AM.png)


![Now you have the Changeset Comments Policy applied to your Team Project](15-07-2014 10-42-56 AM.png)
Now the next time someone checks-in some code, they are forced to enter a comment.
