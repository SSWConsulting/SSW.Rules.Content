---
type: rule
title: Do you know the standard procedure to troubleshoot if a website is down?
uri: do-you-know-the-standard-procedure-to-troubleshoot-if-a-website-is-down
created: 2016-11-25T19:44:43.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​When a site is down, you have to troubleshoot the problem. During troubleshooting, you might need to restart the IIS services. Here're several steps you can follow.​</p> </span>

<ol><li> 
      <a href="https&#58;//www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/f38a73eb-9e33-4f71-bcca-a913a125a50e.mspx?mfr=true" target="_blank">Restart the website</a><br></li><li>If step 1 doesn't work, try to&#160;<a href="https&#58;//www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/f11b8294-cc42-4e9c-8482-6257bf3b80f2.mspx?mfr=true" target="_blank">recycle the application pool</a>&#160; of the site <br></li><li>If step 2 doesn't work, try to restart IIS<br></li><li>If step 3 doesn't work either, then reboot the web server machine (step 3 or step 4 is a severe action. You&#160;<strong>should get the approval</strong>&#160;of network administrators or ask them to do this) <br></li><li>If the site is still not working, turn on the maintenance page and then try to reproduce the problem on the testing site.&#160;<strong>DO NOT</strong>&#160;connect your testing site to the production database. If you need the production database, make a copy of it and restore it to your testing machine.</li></ol><p>Still not fixed? Escalate the issue. Please refer to&#160;<a href="https&#58;//www.ssw.com.au/" target="_blank">SSW</a>. <br></p>
<a href="https&#58;//www.ssw.com.au/ssw/standardsinternal/inductiontraining/InductionDay3.aspx#Website"> </a>


