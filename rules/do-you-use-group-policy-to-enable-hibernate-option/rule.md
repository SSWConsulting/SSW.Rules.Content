---
type: rule
archivedreason: 
title: Do you use Group Policy to enable Hibernate option
guid: 87d4b718-bc23-4091-a93d-c5708da1a005
uri: do-you-use-group-policy-to-enable-hibernate-option
created: 2016-03-22T23:43:52.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []

---


Group Policy is a fast and effective way to configure Hibernate on multiple PC's
<br><excerpt class='endintro'></excerpt><br>
<p>​To enable Hibernate option in Group Policy open up Group Policy Management. </p><p>1. Create a new Group Policy Object and name it "EnableHibernate"</p><p>2. Right click on "EnableHibernate" and click on Edit to bring up Group Policy Management Editor</p><p>3. Select '<em>Show hibernate in the power options menu</em>' from <strong>Computer Configuration | Policies | Administrator Templates | Windows Component | File Explorer </strong>and set to Enabled<br><img src="HibernateGPO.jpg" alt="HibernateGPO.jpg" style="margin:5px;width:808px;" /><br></p><p>4. Back in Group Policy Management Enable Link for "EnableHibernate"  <br><img src="GPOLink.jpg" alt="GPOLink.jpg" style="margin:5px;width:808px;" /><br></p><p>5. Wait for a few moment for GPO to refresh and apply. Alternatively manually force a GP Update through Command Prompt - GPUpdate /force. Check that Hibernate Option is now in Start Menu.<br><img src="StartHibernateEnabled.jpg" alt="StartHibernateEnabled.jpg" style="margin:5px;" /><br></p><p><br></p>


