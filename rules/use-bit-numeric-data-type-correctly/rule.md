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

### 1. Bit data type

Bit data from 0 to 1 (2 values only). Storage size is 1 byte.

Columns of type bit cannot have indexes on them.

Columns of type bit should be prefixed with "Is" or a "Should" ie. `IsInvoiceSent (y/n)` or `ShouldInvoiceBeSent (y/n)` you can tell easily which way the boolean is directed. See [more information on naming conventions](/object-name-should-follow-your-company-naming-conventions).

This being said, fields of this type should generally be avoided because often a field like this can contain a date i.e. `DateInvoiceSent (Date/Time)` is prefered over `InvoiceSent (y/n)`. If a date is inappropriate then we still recommend an int field over a bit field anyway, because bits are a pain!

<!--endintro-->

### 2. Tinyint data type

Integer data from 0 through 255. Storage size is 1 byte.

### 3. Smallint data type

Integer data from -2^15 (-32,768) through 2^15-1 (32,767). Storage size is 2 bytes.

### 4. Int data type

Integer (whole number) data from -2^31 (-2,147,483,648) through 2^31-1 (2,147,483,647). Storage size is 4 bytes. The SQL-92 synonym for int is integer.

### 5. Bigint data type

Integer (whole number) data from -2^63 (-9223372036854775808) through 2^63-1 (9223372036854775807). Storage size is 8 bytes.

**Recommendations:**

* Use smallint datatype instead of bit datatype - so it can be indexed;
* Use int datatype, where possible, instead of bigint datatype - for saving disk space;
* Use smallint datatype, where possible, instead of int datatype - for saving disk space;
* Use tinyint datatype, where possible, instead of smallint datatype - for saving disk space;
