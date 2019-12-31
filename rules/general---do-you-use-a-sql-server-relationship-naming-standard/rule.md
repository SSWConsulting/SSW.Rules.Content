---
type: rule
title: General - Do you use a SQL Server Relationship Naming Standard?
uri: general---do-you-use-a-sql-server-relationship-naming-standard
created: 2019-12-31T05:04:48.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> ​This standard outlines the procedure on naming Relationships at SSW for SQL Server. Use this standard when creating new Relationships or if you find an older Relationship that doesn't follow that standard.<br> </span>

<p>​​Do you agree with them all? Are we missing some? Let us know what you think.<br></p><h3 class="ssw15-rteElement-H3">Syntax</h3><p>Relationship names are to have this syntax&#58;<br>[PrimaryTable] - [ForeignTable]<br>[&#160; &#160; &#160; &#160; 1&#160; &#160; &#160; &#160;] - [&#160; &#160; &#160; &#160; 2&#160; &#160; &#160; &#160;]<br><br>[1] The table whose columns are referenced by other tables in a one-to-one or one-to-many relationship.<br>Rather than accepting the default value i.e. ClientAccount_FK01 that is given from upsizing.</p><p>&lt;figure&gt;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - using the&#160;default relationship name<br></dd><p class="ssw15-rteElement-P">​We recommend using Prod-ClientAccount.<br></p><p class="ssw15-rteElement-P">&lt;figure&gt;<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - using a more descriptive relationship name<br></dd><p><br></p><p>​The good thing is when you look at the relationship from the other side it is there as well.<br>&lt;figure&gt;<br></p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Relationship name on shown on other table<br></dd><p class="ssw15-rteElement-P">We also believe in using Cascade Updates - but never cascade deletes.<br></p>


