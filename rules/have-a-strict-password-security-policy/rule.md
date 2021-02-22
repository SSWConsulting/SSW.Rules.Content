---
type: rule
archivedreason: 
title: Do you have a strict password security policy?
guid: 4bc01f63-9631-4dec-ab28-aa17d89387d3
uri: have-a-strict-password-security-policy
created: 2017-07-10T20:55:19.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects:
- do-you-have-a-strict-password-security-policy

---


<p>We recommend enforcing strict password policies.<br></p><p>Below is a capture of the settings we use:​​</p><p><br><img src="ADSecurityPolicy.png" alt="ADSecurityPolicy.png" style="margin:5px;width:808px;" /><br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>When passwords have to be changed they must meet the following minimum requirements:<br></p><ul><li>Not contain all or part of the user's account name</li><li>Be at least six characters in length</li><li>Contain characters from three of the following four categories:<br></li><ul><li>English uppercase characters (A through Z)</li><li>English lowercase characters (a through z)</li><li>Base 10 digits (0 through 9)<br></li><li>Non-alphanumeric characters (e.g., !, $, #, %) <br></li></ul></ul><div>Rember it is always good to use an even number for password length ;) https://www.troyhunt.com/how-long-is-long-enough-minimum-password-lengths-by-the-worlds-top-sites/​<br><br></div><div>Complexity requirements are enforced when passwords are changed or created.<br></div><p><br></p><p>​Every 180 days clients will be required to change their password, they can change it when:<br></p><ul><li>Login to their ​computer<br></li><li>Terminal server to another computer</li><li>VPN</li></ul><p>This allows users to change their password by making a VPN connection to the office.<br></p><p>We also enforce a lockout policy so if a user gets their password wrong 5 times, their account will be locked out for 15 minutes.​<br></p><p>If you want to change your password sooner, press [ctrl] [alt] [delete] then click "Change Password" button.<br><br></p>


