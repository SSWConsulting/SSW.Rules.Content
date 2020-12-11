---
type: rule
archivedreason: 
title: Do you always use the html maxlength attribute on input fields to limit number of characters to the length of the field in the table?
guid: 23fdcce1-e183-490a-afca-378f8db2fa7b
uri: do-you-always-use-the-html-maxlength-attribute-on-input-fields-to-limit-number-of-characters-to-the-length-of-the-field-in-the-table
created: 2016-08-24T21:56:21.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

**Rule 1: ** Whenever you have a data entry page you should always use the html maxlength attribute to limit number of characters to the length of the field in the table (except for numbers).

**Rule 2:**  Whenever you have a situation where you are using the HTML textarea (does not have the maxlength property)

<!--endintro-->

Then you need to:

* add the JavaScript function eg. ValidateLength(control)
* add 2 properties to every data control  eg. dataType="char" onkeyup="validateLength(this)"
