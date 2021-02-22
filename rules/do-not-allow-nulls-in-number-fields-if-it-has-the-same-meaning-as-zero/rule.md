---
type: rule
archivedreason: 
title: Data - Do you not allow NULLs in number fields if it has the same meaning as zero?
guid: 38603633-dab2-4677-8e72-58da2bfcb182
uri: do-not-allow-nulls-in-number-fields-if-it-has-the-same-meaning-as-zero
created: 2019-11-23T00:38:31.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- data-do-you-not-allow-nulls-in-number-fields-if-it-has-the-same-meaning-as-zero

---

NULLs create difficulty in the middle-tier because you need to add further handling. So avoid them where you can, eg. For a Discount field, make the default 0 and don't allow NULLs.

<!--endintro-->

This rule should not be applied when a NULL value is valid data. Often times data such as a percent earnings rate on a super fund is nullable because it may not be supplied or relevant. This is very different to it being zero and you have no way to determine real zero values from not supplied data. The hit of doing the work in code is often offset in this case by the validity of query results.

As a general rule of thumb, don't use NULL if you cannot distinguish it from another value.

 **Q:**  What is the difference between NULL and 0 in the field "Discount"?
 **A:**  No difference, so don't allow NULL.

 **Q:** What is the difference between NULL and 0 in the field "DailySugarIntake"?
 **A:** NULL means unknown and 0 means no daily sugar intake, so allow NULL.

 **Note:**  Nulls are evil, but don't go crazy removing nulls. Never invent your own constant eg. -999 to represent a Null.
