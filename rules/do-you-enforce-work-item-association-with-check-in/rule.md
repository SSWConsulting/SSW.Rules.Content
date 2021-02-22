---
type: rule
archivedreason: 
title: Do you enforce work item association with check-in?
guid: 50f6576b-571d-490c-8748-6559b6375346
uri: do-you-enforce-work-item-association-with-check-in
created: 2011-11-18T03:52:43.0000000Z
authors:
- title: David Klein
  url: https://ssw.com.au/people/david-klein
- title: Tristan Kurniawan
  url: https://ssw.com.au/people/tristan-kurniawan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
- title: Justin King
  url: https://ssw.com.au/people/justin-king
related: []
redirects: []

---

One of the big advantage of using TFS is end to end traceability, however this requires the developer to do one extra step to link their code (changeset) with requirements (work items). Code is the body of software, while user requirement is the spirit. Work Item association feature helps us to link the spirit and body of software together. This is especially useful when you trying to identify the impact of a bug in term of user requirements.

<!--endintro-->
![No work item associated](WorkItemAss-1.jpg) Figure: Bad Example: No work item is associated with changeset  ![work item associated](WorkItemAss-2.jpg) Figure: Good Example: No work item is associated with changeset  
More Information 
In order to achieve this, developers need to choose the Work Item tab when check-in and "associate" code with a related work item.
![Work item association](WorkItemAss-3.jpg) Figure: Associate Work Item with Changeset  
As the project administrator, you can take one step further to enable "Work Item Check-in Policy" to enforce this rule in your team.
![Work Item Check-in Policy](WorkItemAss-4.jpg) Figure: Always enable the “Work Items check-in policy”
