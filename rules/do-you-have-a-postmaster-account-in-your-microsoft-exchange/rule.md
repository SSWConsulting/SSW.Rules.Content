---
type: rule
archivedreason: 
title: Do you have a postmaster account in your Microsoft Exchange?
guid: 9e146833-e2da-4b07-9692-f3c6971f61fd
uri: do-you-have-a-postmaster-account-in-your-microsoft-exchange
created: 2015-04-10T18:59:46.0000000Z
authors:
- id: 47
  title: Stanley Sidik
related: []

---


<h3>​What is a postmaster account? </h3><p class="p1">It is an RFC mandated specification email address use to identify the administrator of a mail server. Any errors in email processing are directed to the postmaster address.</p><p class="p1">The email received at this address is sent to the mail server administrator, in our case the SysAdmins. </p>
<br><excerpt class='endintro'></excerpt><br>
<p class="p1">At SSW we have configured 
   <a href="mailto:postmaster@ssw.com.au"> 
      <span class="s1">postmaster@ssw.com.au</span></a> as a distribution group, with mail server administrators as members of this distribution group.</p><dl class="image"><dt><img src="postmaster.png" alt="postmaster.png" /></dt><dd>Figure: Group members of postmaster@ssw.com.au​</dd></dl>


