---
type: rule
title: Schema - Do you create a consistent primary key column on your tables?
uri: schema---do-you-create-a-consistent-primary-key-column-on-your-tables
created: 2019-11-06T18:21:56.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">​Make sure you created a consistent primary key column named <strong>Id</strong> on your tables.<br></p> </span>

<p class="ssw15-rteElement-CodeArea">Employee.ID, Employee.EmployeeId, Employee.EmployeeID, Employee.Employee_Code, Employee.Employee<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example​​​<br></dd><p class="ssw15-rteElement-CodeArea">​ Employee.Id<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example<br></dd><h3 class="ssw15-rteElement-H3">​​​Why?<br></h3><p class="ssw15-rteElement-P"></p><ul><li>​We shouldn’t capitalise ID (identifier) as it is an abbreviation not an acronym.</li><li>​Using the a​pproach [TableName].Id, e.g. EmployeeId, is redundant as we already know the context of the Id.​<br></li></ul><p></p>


