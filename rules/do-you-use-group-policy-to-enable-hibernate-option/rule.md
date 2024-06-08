---
type: rule
archivedreason: 
title: Do you use Group Policy to enable Hibernate option?
guid: 87d4b718-bc23-4091-a93d-c5708da1a005
uri: do-you-use-group-policy-to-enable-hibernate-option
created: 2016-03-22T23:43:52.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []

---

Group Policy is a fast and effective way to configure Hibernate on multiple PC's.

<!--endintro-->

To enable Hibernate option in Group Policy open up Group Policy Management.

1. Create a new Group Policy Object and name it "EnableHibernate"

2. Right click on "EnableHibernate" and click on Edit to bring up Group Policy Management Editor

3. Select '*Show hibernate in the power options menu*' from  **Computer Configuration | Policies | Administrator Templates | Windows Component | File Explorer** and set to Enabled
   ![](HibernateGPO.jpg)

4. Back in Group Policy Management Enable Link for "EnableHibernate"  
   ![](GPOLink.jpg)

5. Wait for a few moment for GPO to refresh and apply. Alternatively manually force a GP Update through Command Prompt - GPUpdate /force. Check that Hibernate Option is now in Start Menu
   ![](StartHibernateEnabled.jpg)
