---
type: rule
archivedreason: 
title: Do you know which check-in policies to enable?
guid: e39f79a6-5370-4bd9-af67-00d71906294d
uri: do-you-know-which-check-in-policies-to-enable
created: 2011-11-18T03:52:26.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
related: []

---


<p>Check-in policies are a great tool to enforce quality code before it hits your source control repository. SSW recommends that the following check-in policies be enabled by default on your project&#58; </p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>Changeset Comments Policy - To enforce that all check-in contain comments </li>
<li>SSW Code Auditor - To enforce coding standards and best practices before check-in </li>
<li>Testing Policy - To enforce that unit tests should all pass before code can be checked-in </li>
<li>SSW Code Auditor - To enforce coding standards and best practices before check-in </li>
<li>Code Analysis Policy – To enforce that code analysis rules are not broken</li>
<li>Testing Policy - To enforce that unit tests should all pass before code can be checked-in</li>
<li>Builds Policy – To enforce that the developer has built the project end to end before they check-in </li></ol>
<p><b>More Information</b></p>
<p>To enable these policies&#58; </p>
<ol><li>Right click the <strong>Team Project in Team Explorer &gt; Team Project Settings &gt; Source Control</strong></li>
<li>Select the check-in policies above </li>
<li>Click <strong>OK</strong></li></ol>
<dl><dt><img alt="Chose check in policy" src="/PublishingImages/SC_TFSCI.jpg" /></dt>
<dd>Figure&#58; Chose check-in policies in TFS </dd></dl>



