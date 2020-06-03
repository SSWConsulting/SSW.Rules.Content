---
type: rule
title: Do you warn users before starting a long process?
uri: do-you-warn-users-before-starting-a-long-process
created: 2018-04-25T20:50:36.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>You should never start a long process (&gt;30 seconds) without first giving a warning message to warn the user approximately how long it will take.</p><dl class="goodImage"><dt><img src="/PublishingImages/lengthyoperation.jpg" alt="lengthyoperation.jpg" />​<br></dt><dd>Figure&#58; Good example - Code Auditor message warning this is a long process</dd></dl><p>You will need to have 2 things&#58;</p><ol><li>A table to record processes containing the following fields&#58;<br></li><ul><li>ALogRecord (DateCreated, FunctionName, EmpUpdated, ComputerName, ActiveForm, ActiveControl, SystemsResources, ConventionalMemory, FormsCount, TimeStart, TimeEnd, TimeTaken, RecordsProcessed, Avg, Note, RowGuide, SSWTimeStamp)</li></ul><li>A function to change the number of seconds lapsed to words - see the &quot;1 minute, 9 seconds&quot; in the above messagebox - this requires a SecondsToWords() function shown. See our&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterCode.aspx#">code base</a>.</li></ol>​<br> </span>




