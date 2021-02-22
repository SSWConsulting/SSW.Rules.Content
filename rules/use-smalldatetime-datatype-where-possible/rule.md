---
type: rule
archivedreason: Rule no longer required - Information here is already covered in our other date time rules
title: Schema - Do you use "smalldatetime datatype", where possible, instead of "datetime datatype"?
guid: e08b8a5e-9ad1-4640-8b0e-d818e29296b3
uri: use-smalldatetime-datatype-where-possible
created: 2019-11-06T00:25:07.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-use-smalldatetime-datatype-where-possible-instead-of-datetime-datatype

---

Most applications do not require the range and precision offered by the DateTime data type. When was the last time you needed to enter an order past the year of 2079? So you end up with better data integrity. Most business applications never need dates outside the range of 1900-2079.

<!--endintro-->

**More Information:** 
In addition (I don't really care about this) but I get a smaller database.
DateTime type takes up 8 bytes. It can store dates ranging from January 1, 1753, to December 31, 9999, with time values rounded to increments of .000, .003, or .007 milliseconds.

A SmallDateTime type takes up only 4 bytes, as a consequence, it can only store dates ranging from January 1, 1900, through June 6, 2079, with accuracy to the minute. With a million records each with two date fields, you could save 8MB of storage space. More space could actually be saved if you have indices on those columns. So that is about 1 cent worth today :-)
