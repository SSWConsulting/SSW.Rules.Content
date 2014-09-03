---
type: rule
archivedreason: 
title: Do you know not to delete expired domain users?
guid: 98edbc01-a677-423d-84af-1a11fa5a689e
uri: do-you-know-not-to-delete-expired-domain-users
created: 2014-09-03T19:35:18.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>
                    When an employee leaves or a domain account expires, disable the account, never delete it, as&#58;
                </p><ul><li>Some LOB application such as CRM maintain a reference to the AD domain user GUID</li><li>During the migration or restoration of CRM, users stored in the database are verified against AD and problems may occur if they no longer exist</li></ul>​
<br><excerpt class='endintro'></excerpt><br>



