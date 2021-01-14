---
type: rule
archivedreason: 
title: Do you turn an email into a GitHub Issue before starting work
guid: f866b251-c988-4e30-acc4-f6bac793c1d7
uri: do-you-turn-an-email-into-a-github-issue-before-starting-work
created: 2020-10-27T03:57:22.0000000Z
authors:
- title: Prem Radhakrishnan
  url: https://ssw.com.au/people/prem-radhakrishnan
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Christian Morford-Waite
  url: https://ssw.com.au/people/christian-morford-waite
related: []
redirects: []

---

If a Product Owner sends an email to the development team with a request, that email should be turned into a Github Issue before any work is started or the work is prioritized on the backlog. 



Power Automate has a connector to do this automatically when an email arrives in Outlook. It can create a new Github Issue by parsing the From, To, Subject and body of the email. 




However, at the moment there is a limitation that it doesn't read inline attachments in emails and therefore you have to create your issues manually in Github.


<!--endintro-->

<dl class="image"><br><br>::: ok  <br>![Figure: Power Automate | Connectors | Github](email-to-github-issue2.png)  <br>:::<br></dl><dl class="image"><br><br>::: ok  <br>![Figure: Configure Flow connectors to create a new Github Issue from Outlook](email-to-github-issue1.png)  <br>:::<br></dl>
🔥Warning: This Flow connector does not suport inline images.


<dl class="goodImage"><br><br>::: good  <br>![Figure: Good Example - Github issue created from Outlook using Flow connectors](email-to-github-issue3.png)  <br>:::<br>  
      </dl>

 
<dl class="badImage"><br><br>::: bad  <br>![Figure: Bad Example - Github issue created using Flow - inline attachment shows up as junk characters](email-to-github-issue.png)  <br>:::<br>  
      </dl>


### Related rules


* [Do you know the 3 steps to a PBI?](/do-you-know-the-3-steps-to-a-pbi)
* [Do you know when you use @ mentions in a PBI?](/when-you-use-mentions-in-a-pbi)
