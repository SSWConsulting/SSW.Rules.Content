

---
uri: do-you-know-not-to-delete-expired-domain-users
title: Do you know not to delete expired domain users?
created: YYYY-09-DD 19:35:18
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p>
                    When an employee leaves or a domain account expires, disable the account, never delete it, as&#58;
                </p><ul><li>Some LOB application such as CRM maintain a reference to the AD domain user GUID</li><li>During the migration or restoration of CRM, users stored in the database are verified against AD and problems may occur if they no longer exist</li></ul>​ </span>




