---
type: rule
archivedreason: 
title: Do you use HTML "maxlength" attribute to limit number of characters on input fields?
guid: 23fdcce1-e183-490a-afca-378f8db2fa7b
uri: use-html-maxlength-to-limit-number-of-characters
created: 2016-08-24T21:56:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-always-use-the-html-maxlength-attribute-on-input-fields-to-limit-number-of-characters-to-the-length-of-the-field-in-the-table

---

**Rule 1:** Whenever you have a data entry page you should always use the HTML `maxlength` attribute to limit number of characters to the length of the field in the table (except for numbers).

**Rule 2:** Whenever you have a situation where you are using the HTML `textarea` (does not have the `maxlength` property).

<!--endintro-->

Then you need to:

* Add the JavaScript function. E.g. `ValidateLength(control)`
* Add 2 properties to every data control. E.g. `dataType="char" onkeyup="validateLength(this)"`
