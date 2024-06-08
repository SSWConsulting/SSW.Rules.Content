---
type: rule
archivedreason: 
title: Customization - Do you have a naming convention for your customization back up? (CRM 4 only)
guid: d451d1d3-d0b7-4a93-bb1e-e00caa884cda
uri: customization-do-you-have-a-naming-convention-for-your-customization-back-up-crm-4-only
created: 2012-12-10T18:22:46.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- customization-do-you-have-a-naming-convention-for-your-customization-back-up-(crm-4-only)

---

Keeping track of CRM customization changes is just as difficult as back-end database           changes. We have a rule [Is a Back-end structural change going to be a hassle?](/do-you-stop-dealing-with-data-and-schema) which provide you an           example how you should keep track of back-end changes. You can apply this rule to           CRM changes and use a naming convention on each customization backup file to identify           and keep track of your changes.

Your customization file name should be:

[IncrementalNumber]\_[Entity]\_[Date].zip,           for example: 001\_account\_29042009.zip

The file's name can tell you which entity           you made changes and which date the changes were made. The incremental number will           provides us step by step instruction on how to produce the current CRM system from           a vanilla Microsoft Dynamics CRM.

CRM2011 has significant improvements in this area with Solutions. In CRM 2011 we use versioned solutions along with source control.



<!--endintro-->
