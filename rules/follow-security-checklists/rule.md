---
type: rule
archivedreason: 
title: Do you follow Security Checklists?
guid: 0726a6a5-1ece-49e1-aa70-95a03a5bdc65
uri: follow-security-checklists
created: 2018-06-20T15:18:50.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects:
- do-you-follow-security-checklists

---

The following checklist is a good example of areas to focus on:

* Run penetration tests with SSLLabs.com to check how exposed your servers are
* Look for passwords in .config and code (SSW Code Auditor can help)
* Authentication process of identifying who the user is
* Authorization what the user can do within the application
* Licensing to control the usage of the software
* Validation of all inputs in the system (cross site scripting (XSS) and SQL injection)
* No in memory generation of SQL statements (and are they using a good ORM)
* Encryption of passwords and any sensitive data
* Software Licensing protection mechanisms (and a recommendation to a subscription model)
* Methodologies and best practices to reduce your exposure to hostile attacks
* Logging who is doing what and when (audit trails)


There is a more comprehensive list here on GitHub: [A practical security guide for web developers](http&#58;//bit.ly/SecurityGuide-Checklist).


<!--endintro-->
