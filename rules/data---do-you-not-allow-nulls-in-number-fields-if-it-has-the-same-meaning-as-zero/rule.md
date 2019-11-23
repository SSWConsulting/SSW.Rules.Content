

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> ​NULLs create difficulty in the middle-tier because you need to add further handling. So avoid them where you can, eg. For a Discount field, make the default 0 and don't allow NULLs.<br> </span>

<p>​This rule should not be applied when a NULL value is valid data. Often times data such as a percent earnings rate on a super fund is nullable because it may not be supplied or relevant. This is very different to it being zero and you have no way to determine real zero values from not supplied data. The hit of doing the work in code is often offset in this case by the validity of query results.<br><br>As a general rule of thumbs, don't use NULL if you cannot distinguish it from another value.<br><br>Q. What is the difference between NULL and 0 in discount field?<br>A. No difference, so don't allow Nulls.<br><br>Q&#58; What is the difference between NULL and 0 in Tumor size?<br>A&#58; Null means unknown and 0 means no tumor, so allow Nulls.<br><br><strong>Note&#58;</strong>&#160;Nulls are evil, but don't go crazy removing nulls. Never invent your own constant eg. -999 to represent a Null.<br></p>


