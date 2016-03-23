---
type: rule
title: Do you use Group Policy to enable Hibernate option
uri: do-you-use-group-policy-to-enable-hibernate-option
created: 2016-03-22T23:43:52.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> Group Policy is a fast and effective way to configure Hibernate&#160;on multiple PC's </span>

<p>​To enable Hibernate option in Group Policy open up Group Policy Management.&#160;</p><p>1.&#160;Create a new Group Policy Object and name it &quot;EnableHibernate&quot;</p><p>2. Right click on &quot;EnableHibernate&quot; and click on Edit to bring up Group Policy Management Editor</p><p>3. Select '<em>Show hibernate in the power options menu</em>' from&#160;<strong>Computer Configuration | Policies | Administrator Templates | Windows Component | File Explorer&#160;</strong>and set to Enabled<br><img src="/SiteAssets/do-you-use-group-policy-to-enable-hibernate-option/HibernateGPO.jpg" alt="HibernateGPO.jpg" style="margin&#58;5px;width&#58;808px;" /><br></p><p>4. Back in Group Policy Management Enable Link for&#160;&quot;EnableHibernate&quot; &#160;<br><img src="/SiteAssets/do-you-use-group-policy-to-enable-hibernate-option/GPOLink.jpg" alt="GPOLink.jpg" style="margin&#58;5px;width&#58;808px;" /><br></p><p>5. Wait for a few moment for GPO to refresh and apply. Alternatively manually force a GP Update through Command Prompt - GPUpdate /force. Check that Hibernate Option is now in Start Menu.<br><img src="/SiteAssets/do-you-use-group-policy-to-enable-hibernate-option/StartHibernateEnabled.jpg" alt="StartHibernateEnabled.jpg" style="margin&#58;5px;" /><br></p><p><br></p>


