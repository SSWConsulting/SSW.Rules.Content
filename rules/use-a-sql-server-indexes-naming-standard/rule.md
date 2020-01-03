---
type: rule
archivedreason: 
title: General - Do you use a SQL Server Indexes Naming Standard?
guid: 2448a989-ea55-4780-bfd8-aa8d0add8bde
uri: use-a-sql-server-indexes-naming-standard
created: 2019-12-31T04:47:26.0000000Z
authors: []
related: []
redirects:
- general-do-you-use-a-sql-server-indexes-naming-standard

---


​​​This standard outlines the procedure on naming Indexes at SSW for SQL Server. Use this standard when creating new Indexes or if you find an older Index that doesn't follow that standard.<br><div><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p><strong>​Note&#58;</strong> There is not a lot of use naming Indexes - we only do it when we are printing out documentation or using the 'Index Tuning Wizard' - then it becomes really handy.<br>Do you agree with them all? Are we missing some?&#160;Let us know&#160;what you think.</p><p>Index names are to have this syntax&#58;<br>[pkc_] [TableName] by [FieldName]<br>[&#160; &#160;1&#160; ] [&#160; &#160; 2&#160; &#160; &#160; &#160; ]&#160; &#160; &#160; [&#160; &#160; 3&#160; &#160; &#160; &#160;]<br>[1] All indexes must have a corresponding prefix.</p><table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr class="ssw15-rteTableEvenRow-default"><td class="ssw15-rteTableEvenCol-default" style="width&#58;50%;">​<strong>Prefix</strong><br></td><td class="ssw15-rteTableOddCol-default" style="width&#58;50%;">​<strong>Type</strong><br></td></tr><tr class="ssw15-rteTableOddRow-default"><td class="ssw15-rteTableEvenCol-default">​pkc_<br></td><td class="ssw15-rteTableOddCol-default">​Primary Key, Clustered<br></td></tr><tr class="ssw15-rteTableEvenRow-default"><td class="ssw15-rteTableEvenCol-default">​pknc_<br></td><td class="ssw15-rteTableOddCol-default">​Primary Key, Non Clustered<br></td></tr><tr class="ssw15-rteTableOddRow-default"><td class="ssw15-rteTableEvenCol-default">​ncu_<br></td><td class="ssw15-rteTableOddCol-default">​Non Clustered, Unique<br></td></tr><tr class="ssw15-rteTableEvenRow-default"><td class="ssw15-rteTableEvenCol-default">​cu_<br></td><td class="ssw15-rteTableOddCol-default">Clustered, Unique<br></td></tr><tr class="ssw15-rteTableOddRow-default"><td class="ssw15-rteTableEvenCol-default" rowspan="1">​nc_<br></td><td class="ssw15-rteTableOddCol-default" rowspan="1">​Non Clustered (Most Common)<br></td></tr><tr class="ssw15-rteTableFooterRow-default"><td class="ssw15-rteTableFooterEvenCol-default" rowspan="1">​<br></td><td class="ssw15-rteTableFooterOddCol-default" rowspan="1">​<br></td></tr></tbody></table><p><br>​Make unique index name if possible. Ie. ProductName<br>[2] The name of the table that the Index refers to.<br>[3] The name of the column(s) that the Index refers to.</p><p class="ssw15-rteElement-GreyBox">​​Index 'BillingID'<br>Primary Key 'aaaaaClient_PK'<br></p><dd class="ssw15-rteElement-FigureBad">​​Figure&#58; Bad Example<br></dd><p class="ssw15-rteElement-GreyBox">​​​​'nc_ClientDiary_BillingID'<br>'pknc_ClientDiary_ClientID'<br></p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good Example<br></dd>


