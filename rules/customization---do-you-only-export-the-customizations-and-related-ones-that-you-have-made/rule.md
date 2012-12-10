---
type: rule
archivedreason: 
title: Customization - Do you only export the customizations and related ones that you have made?
guid: e1de3a90-811b-457d-91fd-ac3e780b9833
uri: customization---do-you-only-export-the-customizations-and-related-ones-that-you-have-made
created: 2012-12-10T18:20:38.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 32
  title: Mehmet Ozdemir
related: []

---


<p>
          Sometimes less is better, CRM customizations are cumulative, this means that a customization
          that you import will override your existing schema. So if you're only working on
          for example Account entity, you should only export the Account entity's customization
          and any related entites in any new relationship that you have added to the schema.
          This avoids unexpected overriding existing entity's customization that potentially
          can break your CRM system.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>
          You could also export all the customizations and then just import the customization
          and the related ones that you have made changes. However this requires you taking
          an extra effort to take note of which customizations that you have made changes.</p>


