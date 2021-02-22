---
type: rule
archivedreason: 
title: Do you warn users before starting a long process?
guid: 9f0f545d-1ecc-48f2-b36a-3aa1ca659531
uri: warn-users-before-starting-a-long-process
created: 2018-04-25T20:50:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-warn-users-before-starting-a-long-process

---


<p>You should never start a long process (&gt;30 seconds) without first giving a warning message to warn the user approximately how long it will take.</p><dl class="goodImage"><dt><img src="lengthyoperation.jpg" alt="lengthyoperation.jpg" />​<br></dt><dd>Figure: Good example - Code Auditor message warning this is a long process</dd></dl><p>You will need to have 2 things:</p><ol><li>A table to record processes containing the following fields:<br></li><ul><li>ALogRecord (DateCreated, FunctionName, EmpUpdated, ComputerName, ActiveForm, ActiveControl, SystemsResources, ConventionalMemory, FormsCount, TimeStart, TimeEnd, TimeTaken, RecordsProcessed, Avg, Note, RowGuide, SSWTimeStamp)</li></ul><li>A function to change the number of seconds lapsed to words - see the "1 minute, 9 seconds" in the above messagebox - this requires a SecondsToWords() function shown. See our <a href="https://www.ssw.com.au/ssw/Standards/Rules/RulestoBetterCode.aspx#">code base</a>.</li></ol>​<br>
<br><excerpt class='endintro'></excerpt><br>



