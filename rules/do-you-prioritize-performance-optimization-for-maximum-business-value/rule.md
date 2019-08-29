

---
authors:
  - id: 1
    title: Adam Cogan
  - id: 34
    title: Brendan Richards
---




<span class='intro'> <p class="ssw15-rteElement-P">Like any development, performance optimization requires development time and should therefore be prioritized for business value.​​<br></p><p class="ssw15-rteElement-P">​Include the following considerations&#58;</p><ul><li>What is the preferred performance for this feature?</li><li>What represents an acceptable performance metric?</li><li>How many users are expected to use this feature within a timeframe?</li><li>What is the business impact of poor performance for this feature?</li><li>Are we planning to significantly change this feature in the near future?<br></li></ul> </span>

<p class="ssw15-rteElement-GreyBox">​Hi Adam,<br><br>As per our conversation, we have identified 2 slow queries&#58;<br>​<br>Query 1&#58; On the “Edit Item” screen (admin only) we have identified 4 separate SQL queries that can be rewritten as one. We estimate that this will reduce the response time by 1.5 seconds. Only a few admin users will be affected<br>Query 2&#58; On the Home page is a query that currently takes 1 second that we can reduce to ½ a second. This affects all users.<br><br>We optimized the &quot;Edit Item&quot;&#160;page because that had the biggest measurable improvement.</p><dd class="ssw15-rteElement-FigureBad">​Bad example&#58; although the admin page has a bigger potential saving, the home page affects all users and therefore probably has a higher business value. Business value should be determined by the Product Owner, not the developer<br><br></dd><p class="ssw15-rteElement-GreyBox">Hi Adam,<br><br>As per our conversation, we have identified a query in the &quot;Save Timesheet&quot;&#160;endpoint that often takes more than 2 seconds to complete – well beyond the project’s 800ms target.<br>However, this entire feature is scheduled to be migrated from MVC to Angular in the next sprint.<br><br>Recommended actions&#58;<br>- We won't optimize the existing implementation<br>- Raise the priority of the Angular migration PBI<br>- Ensure that performance metrics are included in the acceptance criteria of the migration PBI<br><br>1. Please “reply all” with changes or your acceptance.&#160;</p><dd class="ssw15-rteElement-FigureGood">​​Good example&#58; there is little business value in optimizing code that will soon be replaced – but the final decision on business value is left to the Product Owner<br><br></dd>


