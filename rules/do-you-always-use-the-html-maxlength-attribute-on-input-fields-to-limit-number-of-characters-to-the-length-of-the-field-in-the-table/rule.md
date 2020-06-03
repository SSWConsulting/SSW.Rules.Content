---
type: rule
title: Do you always use the html maxlength attribute on input fields to limit number of characters to the length of the field in the table?
uri: do-you-always-use-the-html-maxlength-attribute-on-input-fields-to-limit-number-of-characters-to-the-length-of-the-field-in-the-table
created: 2016-08-24T21:56:21.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p><b>Rule 1&#58;&#160;</b>Whenever you have a data entry page you should always use the html maxlength attribute to limit number of characters to the length of the field in the table (except for numbers).</p><p>
      <b>Rule 2&#58;</b>&#160;Whenever you have a situation where you are using&#160;the HTML textarea (does not have the maxlength property) ​
</p> </span>

<p>Then you need to&#58;​<br></p><ul><li>add the JavaScript function eg. ValidateLength(control)</li><li>add 2 properties to every data control&#160; eg. dataType=&quot;char&quot; onkeyup=&quot;validateLength(this)&quot;</li></ul>


