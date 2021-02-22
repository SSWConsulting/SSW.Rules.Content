---
type: rule
archivedreason: 
title: Do you know how to handle errors in Raygun?
guid: ffd7161f-7cac-435d-ae26-8ec42651b59b
uri: how-to-handle-errors-in-raygun
created: 2016-12-30T03:34:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-know-how-to-handle-errors-in-raygun

---


<p class="ssw15-rteElement-P">Your team should always be ensuring that the health of the application is continually improving.<br></p><p class="ssw15-rteElement-P">The best way to do that is to check the exceptions that are being logged in the production application. Every morning, fix the most serious bug logged over the last week. After it is fixed then email yesterday's application health to the Product Owner. <br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>There's traditional error logging software like Log4Net or Elmah, but they just give you a wall of errors that are duplicated and don't give you the ability to mark anything as complete. You'll need to manually clear out the errors and move them into your task tracking system (TFS/VisualStudio.com).</p><p>This is where RayGun or Application Insights comes into the picture. RayGun gives you the following features:</p><ul><li>Grouping exceptions<br></li><li>Ignoring/filtering exceptions<br></li><li>Triaging exceptions (mark them as resolved)<br></li><li>Integrations to TFS/VisualStudio.com to create a Bug, Slack<br></li><li>Tracking the exceptions to a deployment<br></li><li>See which errors are occurring the most often</li></ul><dl class="badImage"><dt><img src="elmah.gif" alt="elmah.gif" /></dt><dd> Figure: Bad Example - Elmah gives you a wall of exceptions and no way to flag exceptions as completed</dd> </dl>
<p class="ssw15-rteElement-GreyBox">
    <b>Hi Adam, </b><br>Please find below the Raygun Health Check for TimePro:<br><img src="Raygun-health-check-for-TimePro-in-the-past-7-days.jpg" alt="Raygun-health-check-for-TimePro-in-the-past-7-days.jpg" style="margin:5px;width:800px;height:192px;" /></p><dd class="ssw15-rteElement-FigureGood">Figure: Raygun health check for TimePro in the past 7 days </dd><p class="ssw15-rteElement-GreyBox">​<img src="2.png" alt="2.png" style="margin:5px;width:800px;height:189px;" /></p><dd class="ssw15-rteElement-FigureGood">Figure: Resolved issues in the past 7 days​<br></dd><p class="ssw15-rteElement-GreyBox"><img src="3.jpg" alt="3.jpg" style="margin:5px;width:800px;" /> </p><dd class="ssw15-rteElement-FigureGood">Figure: The next issue to be worked on​<br></dd><p class="ssw15-rteElement-GreyBox">&lt;This email is from <a href=/how-to-handle-errors-in-raygun>https://rules.ssw.com.au/how-to-handle-errors-in-raygun/ </a>&gt;​<br></p><dd class="ssw15-rteElement-FigureNormal">
   Figure: Email with Raygun application health report​​​ <br><br></dd>


