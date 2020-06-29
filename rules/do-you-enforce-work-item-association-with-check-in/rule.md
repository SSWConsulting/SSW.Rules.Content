---
type: rule
title: Do you enforce work item association with check-in?
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

---



<span class='intro'> <p>One of the big advantage of using TFS is end to end traceability, however this requires the developer to do one extra step to link their code (changeset) with requirements (work items). Code is the body of software, while user requirement is the spirit. Work Item association feature helps us to link the spirit and body of software together. This is especially useful when you trying to identify the impact of a bug in term of user requirements. </p> </span>

<dl><dt><img alt="No work item associated" src="WorkItemAss-1.jpg" /></dt>
<dd>Figure&#58; Bad Example&#58; No work item is associated with changeset </dd></dl>
<dl><dt><img alt="work item associated" src="WorkItemAss-2.jpg" /></dt>
<dd>Figure&#58; Good Example&#58; No work item is associated with changeset </dd></dl>
<p>More Information <br>In order to achieve this, developers need to choose the Work Item tab when check-in and &quot;associate&quot; code with a related work item. </p>
<dl><dt><img alt="Work item association" src="WorkItemAss-3.jpg" /></dt>
<dd>Figure&#58; Associate Work Item with Changeset </dd></dl>
<p>As the project administrator, you can take one step further to enable &quot;Work Item Check-in Policy&quot; to enforce this rule in your team. </p>
<dl><dt><img alt="Work Item Check-in Policy" src="WorkItemAss-4.jpg" /></dt>
<dd>Figure&#58; Always enable the “Work Items check-in policy”</dd></dl>



