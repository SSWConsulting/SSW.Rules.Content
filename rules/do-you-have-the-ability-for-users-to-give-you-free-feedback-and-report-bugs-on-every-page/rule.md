---
type: rule
archivedreason: 
title: Do you have the ability for users to give you free feedback and report bugs on every page?
guid: 1d7bc725-0223-4545-a028-166f8972f317
uri: do-you-have-the-ability-for-users-to-give-you-free-feedback-and-report-bugs-on-every-page
created: 2015-02-13T02:19:04.0000000Z
authors: []
related: []
redirects: []

---

How come there are so many pages I see that don't have an email address on the page?       Every page on your site should have an email hyperlink.

Even better make it easy for visitors to report the actual page they are referring       to. A simple mail link will give users an easy way to report bugs or give feedback       (check out the bottom of this page). By putting this code in your footer template,       users will see this link on every page.

<!--endintro-->

&lt;a href="mailto:infomation@\*\*\*.com.au?subject=FeedBack&body=&lt;%=Request.ServerVariables("URL")%&gt;"&gt;       Feedback Please &lt;/a&gt;
