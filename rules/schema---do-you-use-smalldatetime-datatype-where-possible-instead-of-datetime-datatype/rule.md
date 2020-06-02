

---
uri: schema---do-you-use-smalldatetime-datatype-where-possible-instead-of-datetime-datatype
title: Schema - Do you use "smalldatetime datatype", where possible, instead of "datetime datatype"?
created: YYYY-11-DD 00:25:07
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> <p class="ssw15-rteElement-P">​Most applications do not require the range and precision offered by the DateTime data type. When was the last time you needed to enter an order past the year of 2079? So you end up with better data integrity. Most business applications never need dates outside the range of 1900-2079.​<br></p> </span>

<p><strong>​More Information&#58;</strong><br>In addition (I don't really care about this) but I get a smaller database.<br>DateTime type takes up 8 bytes. It can store dates ranging from January 1, 1753, to December 31, 9999, with time values rounded to increments of .000, .003, or .007 milliseconds.</p><p>A SmallDateTime type takes up only 4 bytes, as a consequence, it can only store dates ranging from January 1, 1900, through June 6, 2079, with accuracy to the minute. With a million records each with two date fields, you could save 8MB of storage space. More space could actually be saved if you have indices on those columns. So that is about 1 cent worth today &#58;-)<br></p>


