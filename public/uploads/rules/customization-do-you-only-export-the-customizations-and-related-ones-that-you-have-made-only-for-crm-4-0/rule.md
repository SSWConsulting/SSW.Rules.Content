---
seoDescription: Customize CRM schema wisely, only exporting and importing changes to specific entities or relationships to avoid unexpected overriding of existing customizations.
type: rule
archivedreason:
title: Customization - Do you only export the customizations and related ones that you have made?
guid: e1de3a90-811b-457d-91fd-ac3e780b9833
uri: customization-do-you-only-export-the-customizations-and-related-ones-that-you-have-made-only-for-crm-4-0
created: 2012-12-10T18:20:38.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
  - customization-do-you-only-export-the-customizations-and-related-ones-that-you-have-made-(only-for-crm-4-0)
  - customization-do-you-only-export-the-customizations-and-related-ones-that-you-have-made
---

Sometimes less is better, CRM customizations are cumulative, this means that a customization that you import will override your existing schema. So if you're only working on for example Account entity, you should only export the Account entity's customization and any related entities in any new relationship that you have added to the schema. This avoids unexpected overriding existing entity's customization that potentially can break your CRM system.

<!--endintro-->

Account entity has relationships with pretty much every other entity in CRM.

You could also export all the customizations and then just import the customization and the related ones that you have made changes. However, this requires you taking an extra effort to take note of which customizations that you have made changes.

In CRM2011, there is  dependencies as solution items. It depends on the circumstances whether to make it a managed or unmanaged solution. E.g. ISV v.s. one man shop.

If you are an ISV and shipping solutions to the marketplace, you have no choice but to use managed solutions. If you are a CRM consultant and building a repeatable industry solution that you want to service many customers with, use managed solutions. If you are an enterprise development shop and building a departmental xRM application that is going to have multiple installations in different orgs, use managed solutions. If you are building integration components for back-office systems, use managed solutions for those.

\*In all other cases, use unmanaged solutions\*.
