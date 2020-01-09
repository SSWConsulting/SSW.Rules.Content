---
type: rule
archivedreason: 
title: Data - Do you not allow NULLs in number fields if it has the same meaning as zero?
guid: 38603633-dab2-4677-8e72-58da2bfcb182
uri: data---do-you-not-allow-nulls-in-number-fields-if-it-has-the-same-meaning-as-zero
created: 2019-11-23T00:38:31.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


​NULLs create difficulty in the middle-tier because you need to add further handling. So avoid them where you can, eg. For a Discount field, make the default 0 and don't allow NULLs.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>​This rule should not be applied when a NULL value is valid data. Often times data such as a percent earnings rate on a super fund is nullable because it may not be supplied or relevant. This is very different to it being zero and you have no way to determine real zero values from not supplied data. The hit of doing the work in code is often offset in this case by the validity of query results.<br><br>As a general rule of thumb, don't use NULL if you cannot distinguish it from another value.<br><br><strong>Q&#58;</strong>&#160;What is the difference between NULL and 0 in the field &quot;Discount&quot;?<br><strong>A&#58;</strong>&#160;No difference, so don't allow NULL.<br><br><strong>Q&#58;</strong> What is the difference between NULL and 0 in the field &quot;DailySugarIntake&quot;?<br><strong>A&#58;</strong> NULL ​means unknown and 0 means no&#160;daily&#160;sugar intake, so allow NULL.<br><br><strong>Note&#58;</strong>&#160;Nulls are evil, but don't go crazy removing nulls. Never invent your own constant eg. -999 to represent a Null.<br></p>


