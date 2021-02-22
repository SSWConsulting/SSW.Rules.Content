---
type: rule
archivedreason: 
title: Do you know the standard procedure to troubleshoot if a website is down?
guid: 7eea433a-475a-4c01-a246-a882861d4ba4
uri: the-standard-procedure-to-troubleshoot-if-a-website-is-down
created: 2016-11-25T19:44:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-the-standard-procedure-to-troubleshoot-if-a-website-is-down

---

When a site is down, you have to troubleshoot the problem. During troubleshooting, you might need to restart the IIS services. Here're several steps you can follow.

<!--endintro-->

1. [Restart the website](https&#58;//www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/f38a73eb-9e33-4f71-bcca-a913a125a50e.mspx?mfr=true)
2. If step 1 doesn't work, try to [recycle the application pool](https&#58;//www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/f11b8294-cc42-4e9c-8482-6257bf3b80f2.mspx?mfr=true)  of the site
3. If step 2 doesn't work, try to restart IIS
4. If step 3 doesn't work either, then reboot the web server machine (step 3 or step 4 is a severe action. You  **should get the approval**  of network administrators or ask them to do this)
5. If the site is still not working, turn on the maintenance page and then try to reproduce the problem on the testing site.  **DO NOT**  connect your testing site to the production database. If you need the production database, make a copy of it and restore it to your testing machine.


Still not fixed? Escalate the issue. Please refer to [SSW](https&#58;//www.ssw.com.au/).
