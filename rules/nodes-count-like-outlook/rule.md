---
type: rule
archivedreason:
title: Data Layout - Do you have nodes count like Outlook?
guid: 8254b1a7-9a7c-4eee-85f0-6dddca76f804
uri: nodes-count-like-outlook
created: 2023-12-11T14:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
  - when-to-use-reporting-services
redirects: []

---

A report with drill through like this should have the number in nodes like Outlook.

<!--endintro-->

::: bad  
![Figure: Bad example - This does not have the nodes count](No_number.jpg)  
:::

::: good  
![Figure: Good example - This does have the nodes count](number.jpg)
:::

Here's how to add nodes count to the textbox with "collapsed(+)" in your report:

In the Expression property of the Textbox, add an expression to show nodes count. Use the following expression:

```sql
--Change the SQL ( or add a new DataSet )
SELECT a.TerritoryID, ( CONVERT ( varchar,a.TerritoryDescription ) + ' (' + CONVERT ( varchar, count ( c.TerritoryID ) ) + ')' ) AS Number, ... FROM Territories a INNER JOIN EmployeeTerritories b ON a.TerritoryID=b.TerritoryID, ... GROUP BY a.TerritoryID, a.TerritoryDescription,...

--Expression to show nodes count

= Fields!Number.Value
```

::: bad  
Bad example - Get the Outlook Node Count look by changing the SQL.
:::

```sql
--Expression to show nodes count

= Fields!Name.Value + "(" + CStr ( CountRows( ) ) + ")"
```

::: good  
Use the CountRows() function to get the Outlook Node Count look
:::

**Note:** The **CountRows** function is one of the several native functions provided by Reporting Services and returns the count of rows within a specified scope. If no scope is specified, it defaults to the innermost scope, which in our case resolves to the static group that defines the values in the data cells.
