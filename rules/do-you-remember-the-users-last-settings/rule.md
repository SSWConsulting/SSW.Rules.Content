---
type: rule
archivedreason: 
title: Do you remember the user's last settings?
guid: b33cb7a4-1e67-4c80-a554-689bc22626bf
uri: do-you-remember-the-users-last-settings
created: 2014-12-01T04:05:27.0000000Z
authors: []
related: []

---


<p>The user's last settings should be saved and should be selected as the Default the
                    next time a form is opened in many instances. For example:</p>
<br><excerpt class='endintro'></excerpt><br>
<ul><li>Login forms - the last login name should be the Default selected and the cursor should be in the password box. 
      <dl class="badImage"><dt> 
            <img border="0" alt="SSW Time PRO .NET - Login" src="../../assets/BadFormLogin.jpg" style="margin:5px;width:342px;" />
         </dt><dd> Figure: Bad Example - Last Username is not saved</dd></dl><dl class="goodImage"><dt> 
            <img border="0" alt="SSW Time PRO .NET - Login" src="../../assets/GoodFormLogin.jpg" style="margin:5px;width:342px;" />
         </dt><dd> Figure: Good Example - Last Username is saved</dd></dl></li><li>Report criteria forms - e.g. date start and date end fields should be automatically populated</li></ul><p> How do I store the settings? </p><ul><li>.NET: Use the 
      <a href="/do-you-use-configuration-management-application-block"> Configuration Block</a> to store the settings.</li><li>Access: Use a local table called 'Control' with one record.</li></ul>


