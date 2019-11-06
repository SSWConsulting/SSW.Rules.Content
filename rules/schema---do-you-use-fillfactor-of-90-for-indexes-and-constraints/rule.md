---
type: rule
title: Schema - Do you use FillFactor of 90% for indexes and constraints?
uri: schema---do-you-use-fillfactor-of-90-for-indexes-and-constraints
created: 2019-11-06T17:32:18.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">Indexes should generally have a fillfactor of 90%. If the amount of data stored in the database does not prohibit rebuilding indexes, a fillfactor of 90% should be maintained to increase performance of inserts.​<br></p> </span>

<p class="ssw15-rteElement-P">​A table that expects a lot of insert operations could use a lower fillfactor.​​<br></p>


