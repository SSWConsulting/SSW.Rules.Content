

---
uri: relationships---do-you-set-not-for-replication-when-creating-a-relationship
title: Relationships - Do you set Not For Replication when creating a relationship?
created: YYYY-11-DD 01:05:06
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> When NOT FOR REPLICATION is used with a Foreign Key relationship, the integrity of the relationship is not checked while the Replication Agent is logged in and performing replication operations. This allows changes to the data (such as cascading updates) be propagated correctly.<br> </span>




