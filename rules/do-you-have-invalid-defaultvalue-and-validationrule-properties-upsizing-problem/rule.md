---
type: rule
archivedreason: 
title: Do you have invalid DefaultValue and ValidationRule properties (Upsizing problem)?
guid: 793d2978-fd46-45df-b1ab-b1f10187b559
uri: do-you-have-invalid-defaultvalue-and-validationrule-properties-upsizing-problem
created: 2010-07-23T02:12:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- do-you-use-the-allowzerolength-property-on-a-field-upsizing-problem
- do-you-use-the-caption-property-on-a-field-upsizing-problem
- do-you-use-the-format-and-inputmask-properties-on-a-field
- do-you-use-the-required-property-on-a-field
- do-you-use-a-unique-index-and-the-required-property-on-a-field
- do-you-have-valid-validationtext-propertyupsizing-problem
redirects:
- do-you-have-invalid-defaultvalue-and-validationrule-properties-(upsizing-problem)

---

When you upsize a table, the Upsizing Wizard tries to "map" Visual Basic for Applications functions in your DefaultValue and ValidationRule properties to an equivalent TSQL function. If this attempt is not successful, the validation rule or default will be skipped by the Upsizing Wizard. Consider the following:   
<!--endintro-->

* If the Upsizing Wizard fails to map a function in a field's ValidationRule property, only the validation rule is skipped, and the rest of the table is upsized.
* If the Upsizing Wizard fails to map a function in a field's DefaultValue property, the entire table is skipped.
* Access 2000: Validation rules are not upsized





| [Upsizing PRO](http&#58;//www.ssw.com.au/ssw/UpsizingPRO) will check this rule  |
| --- |
