---
type: rule
archivedreason: 
title: Relationships - Do you set Not For Replication when creating a relationship?
guid: b22e716b-2afb-4932-9877-ff149005a1d7
uri: relationships---do-you-set-not-for-replication-when-creating-a-relationship
created: 2019-11-13T01:05:06.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


When NOT FOR REPLICATION is used with a Foreign Key relationship, the integrity of the relationship is not checked while the Replication Agent is logged in and performing replication operations. This allows changes to the data (such as cascading updates) be propagated correctly.<br>
<br><excerpt class='endintro'></excerpt><br>



