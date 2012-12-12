---
type: rule
archivedreason: 
title: Do you really know what a Jira Workflow is?
guid: a373924e-a029-401d-a976-0a4f2d0791be
uri: do-you-really-know-what-a-jira-workflow-is
created: 2009-08-27T00:29:49.0000000Z
authors: []
related: []

---


The workflow controls how an issue is taken from creation to closure via a Done or Not Done governing who does what at what point.&#160; The workflow has several states in which a given number of transitions (actions within a state) can be taken by different people according to their role. 

<br><excerpt class='endintro'></excerpt><br>

  <br>
<br>
<p>&#160;Here is a description of the main states of the SSW workflow&#58;</p>
<ol>
    <li>New - When a new issue on your dashboard, it is either completley new, just assigned to you, just re-opened, just answered or just brought out of Deferred. Whatever the reason you should immediately either&#58;
    <ul>
        <li>Assign it to somebody else&#160;; this leaves it in New </li>
        <li>Question - asks the Reporter a question about the issue which puts it in Questioned state </li>
        <li>Update - this allows you yo set fields such as Priority, Due Date etc. without changing the status </li>
        <li>Acknowledge - this puts it in Acknowledged State and means that you know about it and will do it as specified. If you can't make a due date set or an estimate has been made that is unrealistic; you should Question the reporter. </li>
        <li>Progress - this puts it in the state of progressing and means that you are working on it and it will be completed as requested (due date/release number/time estimate) </li>
        <li>Block - puts it in Blocked state awaiting some other event </li>
        <li>Resolve Issue - this means that you have completed the task including checking in any code etc. </li>
    </ul>
    </li>
    <li>The normal workflow is New, Acknowledged, Progressing, Resolved, Closed. </li>
    <li>An issue can be Questioned from New, Acknowledged or Progressing states; on Answer it returns to New </li>
    <li>An issue can also be Blocked from New, Acknowledged or Progressing states. It can be brought off Blocked by either Acknowledge, Progress or Resolve </li>
    <li>An issue can be Deferred only by the Reporter from Acknowledged or Questioned states; if the Assignee wants it Deferred, they should ask the Reporter via a Question. </li>
    <li>From Resolved state, the Reporter then closes the issue if satisfied with the outcome; otherwise it can be reopened. If it is a Development issue; the Reporter should test Defects on Local Staging and new development in ClientDev. Other issues are closed according to whether the reporter is satisfied with the resolution. </li>
</ol>
<p>The following digram shows the main flows&#58;</p>
<p><img width="522" height="578" src="/PublishingImages/Workflow.png" alt="" style="width&#58;612px;height&#58;650px;" /></p>
<p>(A table further defining the workflow&#160;this will appear here in due course)
&#160;&#160;&#160;
&#160;&#160;&#160;
&#160;&#160;&#160;
&#160;&#160;&#160;
&#160;&#160;&#160;
&#160;&#160;&#160;
&#160;</p>



