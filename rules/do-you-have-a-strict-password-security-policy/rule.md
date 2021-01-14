---
type: rule
archivedreason: 
title: Do you have a strict password security policy?
guid: 4bc01f63-9631-4dec-ab28-aa17d89387d3
uri: do-you-have-a-strict-password-security-policy
created: 2017-07-10T20:55:19.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects:
- have-a-strict-password-security-policy

---

We recommend enforcing strict password policies.

Below is a capture of the settings we use:

![](ADSecurityPolicy.png)

<!--endintro-->

When passwords have to be changed they must meet the following minimum requirements:

* Not contain all or part of the user's account name
* Be at least six characters in length
* Contain characters from three of the following four categories:
    * English uppercase characters (A through Z)
    * English lowercase characters (a through z)
    * Base 10 digits (0 through 9)
    * Non-alphanumeric characters (e.g., !, $, #, %)


Rember it is always good to use an even number for password length ;) https://www.troyhunt.com/how-long-is-long-enough-minimum-password-lengths-by-the-worlds-top-sites/



Complexity requirements are enforced when passwords are changed or created.




Every 180 days clients will be required to change their password, they can change it when:

* Login to their computer
* Terminal server to another computer
* VPN


This allows users to change their password by making a VPN connection to the office.

We also enforce a lockout policy so if a user gets their password wrong 5 times, their account will be locked out for 15 minutes.

If you want to change your password sooner, press [ctrl] [alt] [delete] then click "Change Password" button.
