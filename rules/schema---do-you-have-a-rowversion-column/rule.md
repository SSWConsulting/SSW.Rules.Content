

---
authors:
  - id: 1
    title: Adam Cogan
  - id: 96
    title: Alex Breskin
  - id: 99
    title: Christian Morford-Waite
---




<span class='intro'> <p class="ssw15-rteElement-P">​SQL Server rowversions&#160;are binary numbers that indicate the relative sequence in which data modifications took place in a database.​<br></p> </span>

<p class="ssw15-rteElement-P">​​All tables should have a rowversion&#160;column to aid concurrency checking. A rowversion&#160;improves update performance because only one column needs to be checked when performing a concurrency check (instead of checking all columns in a table for changes).​<br></p>


