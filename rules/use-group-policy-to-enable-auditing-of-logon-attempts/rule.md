---
type: rule
archivedreason: 
title: Do you use Group Policy to enable auditing of log on attempts​?
guid: 88f40e36-75c1-40ae-8884-f86859ae2568
uri: use-group-policy-to-enable-auditing-of-logon-attempts
created: 2019-07-24T20:57:45.0000000Z
authors:
- title: Steven Andrews
  url: https://ssw.com.au/people/steven-andrews
related: []
redirects:
- do-you-use-group-policy-to-enable-auditing-of-logon-attempts

---

It is important as a Network Administrator to know when and where failed log in attempts are coming from. Through Group Policy you can enable "Audit log on events".

<!--endintro-->

1. Create a group policy called 'Logon Auditing Policy'
2. Right click on 'Logon Auditing Policy' and click on Edit to bring up Group Policy Management Editor
3. Select 'Audit account log on events' from Computer Configuration | Policies | Windows Settings | Local Policies | Audit Policy and set to Success, Failure
4. Select 'Audit log on events' from Computer Configuration | Policies | Windows Settings | Local Policies | Audit Policy and set to Success, Failure

![Figure: Select 'Audit log on events'](failed-login-1.png)  

5. Select 'Audit: Force audit policy...' from Computer Configuration | Policies | Windows Settings | Local Policies | Security Options and set to Enabled

![Figure: Select 'Audit: Force audit policy...'](failed-login-2.png)  

![Figure: Successful and Failed log in attempts will now appear in Event Viewer | Security](failed-login-3.png)  
Now when you will have access to seeing success/failed log in attempts on user accounts, these can then be captured and audited with your own internal process or a third party application such as Whats Up Gold, see: [Do you monitor failed log in attempts?](/monitor-failed-login-attempts)
