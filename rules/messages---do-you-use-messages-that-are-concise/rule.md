---
type: rule
archivedreason: 
title: Messages - Do you use messages that are concise?
guid: f388b297-50e5-4df6-a8ff-dc9589133963
uri: messages---do-you-use-messages-that-are-concise
created: 2012-11-27T04:41:51.0000000Z
authors: []
related: []

---

It is important to use terminology that your users will understand. Do not to use technical terms that may confuse your users. Use consistent words and phrasing for similar situations. For example, the following phrases have the same meaning which is the best one?

<!--endintro-->

* Not enough memory.
* There is not enough memory.
* There is not enough free memory.
* Insufficient memory.
* No memory was available.
* Your computer does not have sufficient memory.
* Memory resource is not enough.
* Ran out of memory.
* You may be out of memory.

<dl class="badImage">&lt;dt&gt;<img src="../../assets/Bad-MessageBoxZango.jpg" alt="">&lt;/dt&gt;
<dd>Figure: Bad Example - Is it OK to Cancel?</dd></dl>
Microsoft uses this one:
<dl class="goodImage">&lt;dt&gt;<img src="../../assets/NotEnoughMemory.gif" alt="Not Enough Memory">&lt;/dt&gt;
<dd>Figure: Good Example - Microsoft error message is concise</dd></dl>
Some other message types that Microsoft uses are:


| Message type | Sample message |
| --- | --- |
| Not enough disk space | There is not enough disk space to complete the operation. Delete some unneeded files on your hard disk, and then try again |
| File not found | The program cannot find the file filename |
| Re-running setup | The filename file is missing. Run Setup again to reinstall the missing file. For more information about running Setup, press F1.  |


Consider using or adapting them in your application in similar scenarios. Only include the information that the user needs and will understand.

This also applies to general design principles, read our rule on [Less is more: do you know people scan, not read?](/less-is-more-do-you-know-people-scan-not-read)
