---
type: rule
title: Customization - Do you only export the customizations and related ones that you have made?
uri: customization---do-you-only-export-the-customizations-and-related-ones-that-you-have-made
created: 2012-12-10T18:20:38.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 32
  title: Mehmet Ozdemir

---



<span class='intro'> <p>Sometimes less is better, CRM customizations are cumulative, this means that a customization that you import will override your existing schema. So if you're only working on for example Account entity, you should only export the Account entity's customization and any related entities in any new relationship that you have added to the schema. This avoids unexpected overriding existing entity's customization that potentially can break your CRM system.<br></p> </span>

<p>Account entity has relationships with pretty much every other&#160;entity&#160;in CRM.<br></p><p>You could also export all the customizations and then just import the customization and the related ones that you have made changes. However, this requires you taking an extra effort to take note of which customizations that you have made changes.</p><p>In CRM2011, there is&#160; dependencies as solution items. It depends on the circumstances whether&#160;to make it a managed or unmanaged solution. E.g. ISV v.s. one man shop.</p><p>If you are an ISV and shipping solutions to the marketplace, you have no choice but to use managed solutions. If you are a CRM consultant and building a repeatable industry solution that you want to service many customers with, use managed solutions. If you are an enterprise development shop and building a departmental xRM application that is going to have multiple installations in different orgs, use managed solutions. If you are building integration components for back-office systems, use managed solutions for those.&#160;</p><p>*In all other cases, use unmanaged solutions*. <br></p>


