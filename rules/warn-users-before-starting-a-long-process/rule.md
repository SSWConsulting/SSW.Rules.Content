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

You should never start a long process (&gt;30 seconds) without first giving a warning message to warn the user approximately how long it will take.


::: good  
![Figure: Good example - Code Auditor message warning this is a long process](lengthyoperation.jpg)  
:::

You will need to have 2 things:

1. A table to record processes containing the following fields:
    * ALogRecord (DateCreated, FunctionName, EmpUpdated, ComputerName, ActiveForm, ActiveControl, SystemsResources, ConventionalMemory, FormsCount, TimeStart, TimeEnd, TimeTaken, RecordsProcessed, Avg, Note, RowGuide, SSWTimeStamp)
2. A function to change the number of seconds lapsed to words - see the "1 minute, 9 seconds" in the above messagebox - this requires a SecondsToWords() function shown. See our [code base](https://www.ssw.com.au/ssw/Standards/Rules/RulestoBetterCode.aspx#).



<!--endintro-->
