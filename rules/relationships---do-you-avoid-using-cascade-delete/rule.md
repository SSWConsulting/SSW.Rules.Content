

---
uri: relationships---do-you-avoid-using-cascade-delete
title: Relationships - Do you avoid using Cascade Delete?
created: YYYY-11-DD 00:23:04
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> ​SQL Servers ON DELETE CASCADE functionality can be very dangerous. We recommend not using it. Imagine someone deletes customer and the orders are deleted. If you need to delete records in related tables, do it in code in the application as it gives you more control.​<br> </span>




