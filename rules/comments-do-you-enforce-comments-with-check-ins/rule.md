---
seoDescription: Enforce comments with check-ins using Team Foundation Server to improve code transparency and collaboration.
type: rule
archivedreason:
title: Comments - Do you enforce comments with check-ins?
guid: 38313df6-15aa-448a-b978-edc43b582694
uri: comments-do-you-enforce-comments-with-check-ins
created: 2011-11-18T03:52:40.0000000Z
authors:
  - title: David Klein
    url: https://ssw.com.au/people/david-klein
    noimage: true
  - title: Justin King
    url: https://ssw.com.au/people/justin-king
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
  - title: Drew Robson
    url: https://ssw.com.au/people/drew-robson
related: []
redirects: []
---

Team Foundation Server is great, and one of its neat features is enforcing comments when checking in code. Without comments, some of the other built in features like History become redundant without comments.

<!--endintro-->

::: greybox
You should have good comments... if you are struggling use [Excuses For Lazy Coders](http://programmingexcuses.com/) :)
:::

::: bad
![Figure: Bad Example: No Comments against the check-ins we don’t know what changes were made in each revision](15-07-2014 10-21-04 AM.png)
:::

::: good
![Figure: Good Example: Now we can pin point which revision a particular change has been made](15-07-2014 10-24-40 AM.png)
:::

In Visual Studio 2013, to enforce this behaviour, you will need to:

![Figure: Go to Team Explorer | Source Control](15-07-2014 10-41-30 AM.png)

![Figure: Then Check-in Policy | Add](15-07-2014 10-42-21 AM.png)

![Figure: Then select Changeset Comments Policy and OK](15-07-2014 10-42-43 AM.png)

![Figure: Now you have the Changeset Comments Policy applied to your Team Project](15-07-2014 10-42-56 AM.png)

Now the next time someone checks-in some code, they are forced to enter a comment.
