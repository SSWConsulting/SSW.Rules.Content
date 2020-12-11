---
type: rule
archivedreason: 
title: Do you enforce work item association with check-in?
guid: 50f6576b-571d-490c-8748-6559b6375346
uri: do-you-enforce-work-item-association-with-check-in
created: 2011-11-18T03:52:43.0000000Z
authors:
- id: 22
  title: David Klein
- id: 6
  title: Tristan Kurniawan
- id: 17
  title: Ryan Tee
- id: 5
  title: Justin King
related: []

---


<p>One of the big advantage of using TFS is end to end traceability, however this requires the developer to do one extra step to link their code (changeset) with requirements (work items). Code is the body of software, while user requirement is the spirit. Work Item association feature helps us to link the spirit and body of software together. This is especially useful when you trying to identify the impact of a bug in term of user requirements. </p>
<br><excerpt class='endintro'></excerpt><br>
<dl><dt><img alt="No work item associated" src="WorkItemAss-1.jpg" /></dt>
<dd>Figure: Bad Example: No work item is associated with changeset </dd></dl>
<dl><dt><img alt="work item associated" src="WorkItemAss-2.jpg" /></dt>
<dd>Figure: Good Example: No work item is associated with changeset </dd></dl>
<p>More Information <br>In order to achieve this, developers need to choose the Work Item tab when check-in and "associate" code with a related work item. </p>
<dl><dt><img alt="Work item association" src="WorkItemAss-3.jpg" /></dt>
<dd>Figure: Associate Work Item with Changeset </dd></dl>
<p>As the project administrator, you can take one step further to enable "Work Item Check-in Policy" to enforce this rule in your team. </p>
<dl><dt><img alt="Work Item Check-in Policy" src="WorkItemAss-4.jpg" /></dt>
<dd>Figure: Always enable the “Work Items check-in policy”</dd></dl>



