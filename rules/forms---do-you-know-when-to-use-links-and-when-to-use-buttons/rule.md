---
type: rule
title: Forms - Do you know when to use links and when to use buttons?
uri: forms---do-you-know-when-to-use-links-and-when-to-use-buttons
created: 2014-12-04T20:13:43.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p style="margin-top&#58;7px;margin-bottom&#58;7px;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;1.4em;color&#58;#000000;">It seems nearly all web developers are confused whether they should use hyperlinks or buttons on forms. The recommendation is that whenever data is being submitted (e.g. Save, Cancel, Apply) you should use a button, otherwise use a link.</p><p style="margin-top&#58;7px;margin-bottom&#58;7px;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;1.4em;color&#58;#000000;">This is because hyperlinks indicate navigation - &quot;If I click this link, I'll be taken somewhere else&quot;.</p><p style="margin-top&#58;7px;margin-bottom&#58;7px;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;1.4em;color&#58;#000000;">Whereas a button indicates that something is being processed - &quot;When I click this, I'm agreeing that something is being submitted&quot;​​</p> </span>

<h4>Note&#58; If you are using an automated link checker</h4><p>It is important you use buttons for updating or deleting data on your website. The main reason is problems will occur when you run a link checker (we run <a href="/ssw/LinkAuditor/"> SSW Link Auditor</a>), and you have data driven pages with &quot;Update&quot; or &quot;Delete&quot; hyperlinks. The link checker will try to go to all associated links and potentially delete a lot of data from your website database.</p><p>But you say &quot;My Delete links have JavaScript protection e.g. Are you sure you want to delete?&quot;. It is still no good because link checkers ignore all JavaScript validation.</p><p>Thus, we must have&#58;</p><ul><li>Password protected areas on the website when we can update the database records via the web</li><li>All update ability must be via buttons, not hyperlinks (as buttons are known on the web to submit a form).</li></ul><p>That being said, there are a couple of exceptions to this rule.</p><ol><li>If you want the user to be able to right click and &quot;Open in New Window&quot;</li><li>If you want a consistent design feel (and there is no confusion that the link is accepting data)</li></ol><dl class="image"><dt><img src="/WebSites/RulesToBetterWebsitesLayout/PublishingImages/LinksExample.gif" alt="Links Example" /></dt><dd>Figure&#58; An exception to the rule - an &quot;Update&quot; button inside the datagrid would look inconsistent</dd></dl><dl class="badImage"><dt><img src="/WebSites/RulesToBetterWebsitesLayout/PublishingImages/LinkVsButton.gif" alt="Links Vs Button" /></dt><dd>Figure&#58; Bad Example - The &quot;sign in&quot; hyperlink should be a button</dd></dl><dl class="goodImage"><dt><img src="/WebSites/RulesToBetterWebsitesLayout/PublishingImages/Logon.gif" alt="Correct sign in" /></dt><dd>Figure&#58; Good Example - This is a perfect example of how a good sign in screen should look</dd></dl>


