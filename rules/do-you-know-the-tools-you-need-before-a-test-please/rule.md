

---
uri: do-you-know-the-tools-you-need-before-a-test-please
title: Do you know the tools you need before a "Test Please"?
created: YYYY-02-DD 02:44:26
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> Don't let your client find bugs in production that they would have found if you had asked them to do a 'Test Please' 1st<br>
Better still... Don't let your client find bugs that your internal tester would have found.<br>
Better still... Don't let your t​ester find bugs that a tool could have found?<br>
<br>
So, prior to a version being submitted to the client, these are the 4 steps you should follow&#58; 
 </span>


  <ol>
    <li>Perform automated testing with tools&#58;<br>
    - SSW Link Auditor (for Web Apps) <br>
    - SSW Code Auditor (for all Apps)<br>
    - SSW SQL Auditor (for all Apps with databases)<br>
    - SSW SQL Deploy's Reconcile (for all Apps with databases)&#160;<br>
    - Visual Studio Team System Code Analysis (optional) </li>
    <li>Perform automated testing via Unit Tests <br>
    - nUnit (for Windows Apps), or<br>
    - Visual Studio Team System Unit Tests (for Web Apps) </li>
    <li>Perform an internal &quot;Test Please&quot; (aka &quot;Alpha Testing&quot; e.g. only testing that pages or forms load, not checking the business rules) </li>
    <li>Then send a &quot;Test Please&quot; to the client (aka &quot;Acceptance Testing&quot; to check the business rules) </li>
</ol>



