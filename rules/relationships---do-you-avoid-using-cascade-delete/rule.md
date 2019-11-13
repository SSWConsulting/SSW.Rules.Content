---
type: rule
archivedreason: 
title: Relationships - Do you avoid using Cascade Delete?
guid: 872e3ec0-a2b7-41bd-aea3-e812e2104c4e
uri: relationships---do-you-avoid-using-cascade-delete
created: 2019-11-13T00:23:04.0000000Z
authors:
- id: 1
  title: Adam Cogan
related:
- relationships---do-you-turn-on-referential-integrity-in-relationships

---


SQL Servers ON DELETE CASCADE functionality can be very dangerous. We recommend not using it. Imagine someone deletes customer and the orders are deleted. If you need to delete records in related tables, do it in code in the application as it gives you more control.​<br>
<br><excerpt class='endintro'></excerpt><br>



