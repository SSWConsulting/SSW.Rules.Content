---
type: rule
archivedreason: 
title: Do you use the Format and InputMask properties on a field?
guid: 7eac0df8-5f3a-486f-b892-8fdf6ff029e6
uri: do-you-use-the-format-and-inputmask-properties-on-a-field
created: 2010-07-23T02:28:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- do-you-use-the-allowzerolength-property-on-a-field-upsizing-problem
- do-you-use-the-caption-property-on-a-field-upsizing-problem
- do-you-have-invalid-defaultvalue-and-validationrule-properties-upsizing-problem
- do-you-use-the-required-property-on-a-field
- do-you-use-a-unique-index-and-the-required-property-on-a-field
- do-you-have-valid-validationtext-propertyupsizing-problem
redirects: []

---

SQL Server and MSDE have no equivalent to the Format or InputMask property in Microsoft Access 2000. As a result, neither property will be upsized when it is encountered by the Upsizing Wizard, nor will any errors be reported in the Upsizing Report. All formatting displayed as a result of using the Format property will be lost when the data is migrated to SQL Server or MSDE.  
<!--endintro-->
