---
type: rule
archivedreason: 
title: Comments - Do you enforce comments with check-ins?
guid: 38313df6-15aa-448a-b978-edc43b582694
uri: comments-do-you-enforce-comments-with-check-ins
created: 2011-11-18T03:52:40.0000000Z
authors:
- title: David Klein
  url: https://ssw.com.au/people/david-klein
- title: Justin King
  url: https://ssw.com.au/people/justin-king
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
- title: Tristan Kurniawan
  url: https://ssw.com.au/people/tristan-kurniawan
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects: []

---

Team Foundation Server is great, and one of its neat features is enforcing comments when checking in code. Without comments, some of the other built in features like History become redundant without comments.  
<!--endintro-->




*You should have good comments… if you are struggling use [this](http://programmingexcuses.com/).*




![](15-07-2014 10-21-04 AM.png) 

::: bad
Figure: Bad Example: No Comments against the check-ins we don’t know what changes were made in each revision  
:::

![](15-07-2014 10-24-40 AM.png)
 

::: good
Figure: Good Example: Now we can pin point which revision a particular change has been made  
:::



In Visual Studio 2013, to enforce this behaviour, you will need to:



![](15-07-2014 10-41-30 AM.png)

**Figure: Go to Team Explorer | Source Control**

![](15-07-2014 10-42-21 AM.png)

**Figure: Then Check-in Policy | Add**

![](15-07-2014 10-42-43 AM.png)

**Figure: Then select Changeset Comments Policy and OK**

![](15-07-2014 10-42-56 AM.png)

**Figure: Now you have the Changeset Comments Policy applied to your Team Project**
Now the next time someone checks-in some code, they are forced to enter a comment.
