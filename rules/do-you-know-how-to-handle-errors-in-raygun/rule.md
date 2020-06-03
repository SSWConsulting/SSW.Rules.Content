---
type: rule
title: Do you know how to handle errors in Raygun?
uri: do-you-know-how-to-handle-errors-in-raygun
created: 2016-12-30T03:34:50.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 3
  title: Eric Phan

---



<span class='intro'> <p class="ssw15-rteElement-P">Your team should always be ensuring that the health of the application is continually improving.<br></p><p class="ssw15-rteElement-P">The best way to do that is to check the exceptions that are being logged in the production application. Every morning, fix the most serious bug logged over the last week. After it is fixed then email yesterday's application health to the Product Owner.&#160;<br></p> </span>

<p>There's traditional error logging software like Log4Net or Elmah, but they just give you a wall of errors that are duplicated and don't give you the ability to mark anything as complete. You'll need to manually clear out the errors and move them into your task tracking system (TFS/VisualStudio.com).</p><p>This is where RayGun or Application Insights comes into the picture. RayGun gives you the following features&#58;</p><ul><li>Grouping exceptions<br></li><li>Ignoring/filtering exceptions<br></li><li>Triaging exceptions (mark them as resolved)<br></li><li>Integrations to TFS/VisualStudio.com to create a Bug, Slack<br></li><li>Tracking the exceptions to a deployment<br></li><li>See which errors are occurring the most often</li></ul><dl class="badImage"><dt><img src="/SiteAssets/how-to-handle-errors-in-raygun/elmah.gif" alt="elmah.gif" /></dt><dd> Figure&#58; Bad Example - Elmah gives you a wall of exceptions and no way to flag exceptions as completed</dd> </dl>
<p class="ssw15-rteElement-GreyBox">
    <b>Hi Adam, </b><br>Please find below the Raygun Health Check for TimePro&#58;<br><img src="/PublishingImages/Raygun-health-check-for-TimePro-in-the-past-7-days.jpg" alt="Raygun-health-check-for-TimePro-in-the-past-7-days.jpg" style="margin&#58;5px;width&#58;800px;height&#58;192px;" /></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Raygun health check for TimePro in the past 7 days&#160;</dd><p class="ssw15-rteElement-GreyBox">​<img src="/SiteAssets/how-to-handle-errors-in-raygun/2.png" alt="2.png" style="margin&#58;5px;width&#58;800px;height&#58;189px;" /></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Resolved issues in the past 7 days​<br></dd><p class="ssw15-rteElement-GreyBox"><img src="/SiteAssets/how-to-handle-errors-in-raygun/3.jpg" alt="3.jpg" style="margin&#58;5px;width&#58;800px;" />&#160;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; The next issue to be worked on​<br></dd><p class="ssw15-rteElement-GreyBox">&lt;This email is from&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=6d5e516d-1f5e-4baa-929c-2c45b9bfa15e">https&#58;//rules.ssw.com.au/how-to-handle-errors-in-raygun/ </a>&gt;​<br></p><dd class="ssw15-rteElement-FigureNormal">
   Figure&#58; Email with Raygun application health report​​​&#160;<br><br></dd>


