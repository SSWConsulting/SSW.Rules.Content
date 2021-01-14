---
type: rule
archivedreason: 
title: 'Tiny: Do you use "will", not "should"?'
guid: 4b3c2c57-5cbe-43c4-adc2-170ba0d20d05
uri: tiny-do-you-use-will-not-should
created: 2016-04-20T02:23:15.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- use-will-not-should

---

When explaining steps in a process, e.g. Printing a file, make sure to say something "will" happen or is happening. This is especially important when describing your own software, because saying something "should" happen implies that it may or may not happen, i.e. there could be bugs!

<!--endintro-->

::: greybox
To print your document:
1.    Select File | Print. The Print dialog should now show.
2.    Select the number of copies and click Print. The file should now print.  
:::

::: bad
Figure: Bad Example - Using "should" implies uncertainty  
:::

::: greybox
To print your document:
1.    Select File | Print. The Print dialog is shown.
2.    Select the number of copies and click Print. The file will now print.  
:::

::: good
Good example - Using present or future tense implies confidence  
:::

This is \*not\* detected by [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/)because it picks up false positives.
