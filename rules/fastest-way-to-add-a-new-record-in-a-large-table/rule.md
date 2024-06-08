---
type: rule
archivedreason: 
title: Microsoft Access - Do you know the fastest way to add a new record in a large table?
guid: 8f5ec0dc-6a1e-4317-aa59-140f98f45f56
uri: fastest-way-to-add-a-new-record-in-a-large-table
created: 2021-06-14T19:18:07.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

When adding a new record should we use **ADO rst.AddNew** or a **SQL INSERT** statement?

<!--endintro-->

The **INSERT** statement will give you better performance because you don't have to create and pass around a recordset object. However the **Recordset** object gives you protection from data conflicts by raising an error if the user tries to update a record that has been modified by another user. Also on an error the **Recordset** object will crash out on the offending line, so you can find the problem easier. And when dealing with a memo field, which may contain single quotes or double quotes the **AddNew** method is easier to construct. But in general if you can do without the data conflict protection and want the performance then use the **ADO** connection object to execute a SQL statement.
