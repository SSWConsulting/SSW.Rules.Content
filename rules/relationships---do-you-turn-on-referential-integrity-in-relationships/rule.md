---
type: rule
archivedreason: 
title: Relationships - Do you turn on referential integrity in relationships?
guid: b90d91f8-46fb-45b7-947b-c8ce43621844
uri: relationships---do-you-turn-on-referential-integrity-in-relationships
created: 2019-11-12T23:56:31.0000000Z
authors:
- id: 1
  title: Adam Cogan
related:
- relationships---do-you-avoid-using-cascade-delete
- relationships---do-you-use-update-cascade-when-creating-a-relationship

---


<p>​Cascading referential integrity constraints allow you to define the actions SQL Server takes when a user attempts to delete or update a key to which existing foreign keys point. The REFERENCES clauses of the CREATE TABLE and ALTER TABLE statements support ON DELETE and ON UPDATE clauses&#58;<br></p><ul><li>[ ON DELETE &#123; CASCADE | NO ACTION &#125; ]</li><li>[ ON UPDATE &#123; CASCADE | NO ACTION &#125; ]</li></ul><p class="ssw15-rteElement-P">NO ACTION is the default if ON DELETE or ON UPDATE is not specified.​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​Relationships should always have referential integrity turned on. If you turned it on after data has been added, you may have data in your database that violates your referential integrity rules.<br></p><dl class="image"><dt><img src="/PublishingImages/ReferentialIntegrityCheck.jpg" alt="ReferentialIntegrityCheck.jpg" /></dt><dd>Figure&#58; Recommended referential integrity constraints</dd></dl>


