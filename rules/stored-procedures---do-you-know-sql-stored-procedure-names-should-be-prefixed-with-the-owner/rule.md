

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>Always specify the schema prefix when creating stored procedures. This way you know that it will always be dbo.procedure_name no matter who is logged in when it is created.</p><p>There are 2 other benefits to including the schema prefix on all object references&#58;</p><ol><li>This prevents the database engine from checking for an object under the users schema first</li><li>Also avoids the issue where multiple plans are cached for the exact same statement/batch just because they were executed by users with different default schemas​.<br></li></ol><br> </span>

<p>Aaron Bertrand agrees with this rule -&#160;<a href="https&#58;//sqlblog.org/2008/10/30/my-stored-procedure-best-practices-checklist">My stored procedure &quot;be​st practices&quot; checklist</a>.</p><p class="ssw15-rteElement-CodeArea">CREATE PROCEDURE procCustomer_Update @CustomerID INT, ….. BEGIN​ </p><dd class="ssw15-rteElement-FigureBad">
Figure&#58; Bad example​​
</dd><p class="ssw15-rteElement-CodeArea">​​​CREATE PROCEDURE dbo.procCustomer_Update @CustomerID INT, ….. BEGIN </p><dd class="ssw15-rteElement-FigureGood">
Figure&#58; Good example​​​​<br></dd>


