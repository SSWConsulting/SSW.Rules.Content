---
type: rule
title: Do you always make file paths @-quoted?
uri: do-you-always-make-file-paths--quoted
created: 2009-05-13T06:57:56.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<p>By inserting an @ character in front of the string, e.g. <b>@&quot;C&#58;\Temp\MyFile.txt&quot;</b>, you can turn off escape sequences, making it behave like VB.NET. File paths should always be stored like this in strings.</p>
<table id="table6" class="clsSSWProductTable" cellspacing="2" summary="Code Auditor" cellpadding="2">
<tbody>
<tr>
<td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.</td></tr></tbody></table>


