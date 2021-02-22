---
type: rule
archivedreason: 
title: Do you remember the user's last settings?
guid: b33cb7a4-1e67-4c80-a554-689bc22626bf
uri: do-you-remember-the-users-last-settings
created: 2014-12-01T04:05:27.0000000Z
authors: []
related: []
redirects: []

---

The user's last settings should be saved and should be selected as the Default the                     next time a form is opened in many instances. For example:

<!--endintro-->

* Login forms - the last login name should be the Default selected and the cursor should be in the password box. 
      

::: bad  
![Figure: Bad Example - Last Username is not saved](../../assets/BadFormLogin.jpg)  
:::


::: good  
![Figure: Good Example - Last Username is saved](../../assets/GoodFormLogin.jpg)  
:::

* Report criteria forms - e.g. date start and date end fields should be automatically populated


How do I store the settings?

* .NET: Use the 
      [Configuration Block](/do-you-use-configuration-management-application-block) to store the settings.
* Access: Use a local table called 'Control' with one record.
