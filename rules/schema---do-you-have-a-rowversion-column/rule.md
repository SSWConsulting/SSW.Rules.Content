---
type: rule
archivedreason: 
title: Schema - Do you have a rowversion column?
guid: fda895fe-2c8c-4e8d-9db7-ced3717bae64
uri: schema---do-you-have-a-rowversion-column
created: 2019-11-06T17:27:42.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 96
  title: Alex Breskin
- id: 99
  title: Christian Morford-Waite
related: []

---


<p class="ssw15-rteElement-P">​SQL Server rowversions&#160;are binary numbers that indicate the relative sequence in which data modifications took place in a database.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">​​All tables should have a rowversion&#160;column to aid concurrency checking. A rowversion&#160;improves update performance because only one column needs to be checked when performing a concurrency check (instead of checking all columns in a table for changes).​<br></p>


