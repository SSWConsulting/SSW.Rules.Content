---
type: rule
archivedreason: 
title: Schema - Do you use Bit/Numeric data type correctly?
guid: dc80624c-10d3-4141-bb84-aa5b159a84cd
uri: use-bit-numeric-data-type-correctly
created: 2019-11-05T23:02:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- schema-do-you-use-bit-numeric-data-type-correctly

---


<b>​​​1. Bit data type</b><div><b><br></b><p class="ssw15-rteElement-P">Bit data from 0 to 1 (2 values only). Storage size is 1 byte.</p><p class="ssw15-rteElement-P">Columns of type&#160;bit&#160;cannot have indexes on them.&#160; Also, SQL Server 7 only allows True or False values in a&#160;bit&#160;column. SQL 2000 introduced the ability to store NULL as well. Applications built for SQL Server 7 often do not expect this behaviour and may create subtle runtime errors.</p><div><div><p class="ssw15-rteElement-P">​​Columns of type&#160;bit&#160;should be prefixed with &quot;Is&quot; or a &quot;Should&quot; ie. IsInvoiceSent (y/n) or ShouldInvoiceBeSent (y/n) you can tell easily which way the boolean is directed.&#160;[<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=4be22043-306c-4c6f-b9b6-ec2ff37be97e">more information on naming conve​ntions​</a>]<br></p>This being said, fields of this type should generally be avoided because often a field like this can contain a date i.e. DateInvoiceSent (Date/Time) is prefered over InvoiceSent (y/n). If a date is inappropriate then we still recommend an int field over a bit field anyway, because bits are a pain in the butt &#58;-)<br></div></div><div><br></div></div>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P"><b>2. ​Tinyint data type</b></p><p class="ssw15-rteElement-P">Integer data from 0 through 255. Storage size is 1 byte.<br></p><p class="ssw15-rteElement-P"><b>3. Smallint data type</b></p><p>Integer data from -2^15 (-32,768) through 2^15-1 (32,767). Storage size is 2 bytes.</p><p class="ssw15-rteElement-P"><b>4.&#160;Int data type</b></p><p class="ssw15-rteElement-P">Integer (whole number) data from -2^31 (-2,147,483,648) through 2^31-1 (2,147,483,647). Storage size is 4 bytes. The SQL-92 synonym for int is integer.</p><p class="ssw15-rteElement-P"><b>5. Bigint data type</b></p><p class="ssw15-rteElement-P">Integer (whole number) data from -2^63 (-9223372036854775808) through 2^63-1 (9223372036854775807). Storage size is 8 bytes.​​<br><br></p><p class="ssw15-rteElement-P"><strong>Recommended&#58;</strong><br></p><ul><li>Use smallint datatype instead of bit datatype - so it can be indexed;</li><li>Use int datatype, where possible, instead of bigint datatype - for saving disk space;</li><li>Use smallint datatype, where possible, instead of int datatype - for saving disk space;</li><li>Use tinyint datatype, where possible, instead of smallint datatype - for saving disk space;</li></ul>


