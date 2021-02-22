---
type: rule
archivedreason: 
title: Forms - Do you know when to use links and when to use buttons?
guid: 04b05bb8-9727-47b0-ab21-63836ab2ed3d
uri: forms-do-you-know-when-to-use-links-and-when-to-use-buttons
created: 2014-12-04T20:13:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

It seems nearly all web developers are confused whether they should use hyperlinks or buttons on forms. The recommendation is that whenever data is being submitted (e.g. Save, Cancel, Apply) you should use a button, otherwise use a link.

This is because hyperlinks indicate navigation - "If I click this link, I'll be taken somewhere else".

Whereas a button indicates that something is being processed - "When I click this, I'm agreeing that something is being submitted"

<!--endintro-->

#### Note: If you are using an automated link checker

It is important you use buttons for updating or deleting data on your website. The main reason is problems will occur when you run a link checker (we run [SSW Link Auditor](http://www.ssw.com.au/ssw/LinkAuditor/)), and you have data driven pages with "Update" or "Delete" hyperlinks. The link checker will try to go to all associated links and potentially delete a lot of data from your website database.

But you say "My Delete links have JavaScript protection e.g. Are you sure you want to delete?". It is still no good because link checkers ignore all JavaScript validation.

Thus, we must have:

* Password protected areas on the website when we can update the database records via the web
* All update ability must be via buttons, not hyperlinks (as buttons are known on the web to submit a form).


That being said, there are a couple of exceptions to this rule.

1. If you want the user to be able to right click and "Open in New Window"
2. If you want a consistent design feel (and there is no confusion that the link is accepting data)


![Figure: An exception to the rule - an "Update" button inside the datagrid would look inconsistent](LinksExample.gif)  


::: bad  
![Figure: Bad Example - The "sign in" hyperlink should be a button](LinkVsButton.gif)  
:::


::: good  
![Figure: Good Example - This is a perfect example of how a good sign in screen should look](Logon.gif)  
:::
