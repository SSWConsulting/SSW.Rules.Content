---
type: rule
archivedreason: 
title: Customization - Do you have only one person making changes to your CRM customization?
guid: e477afd3-08d6-458a-98c4-a99b33b46055
uri: customization-do-you-have-only-one-person-making-changes-to-your-crm-customization
created: 2012-12-10T18:11:23.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects: []

---

With CRM4, customizations cannot be undone and are cumulative, e.g. if you add an attribute on a form and deploy, there is no easy way to remove the attribute from the entity. We have a [suggestion to CRM on this issue](http&#58;//www.ssw.com.au/SSW/Standards/BetterSoftwareSuggestions/CRM.aspx#RemoveAttributeOnForm).

<!--endintro-->

In order to remove the attribute, what you have to do:

1. If attribute is not a required field then go to step 3.
2. Set attribute to be not required field
3. Save and publish the changes
4. Remove attribute from the form
5. Save and publish the changes
6. Remove attribute from the entity
7. Save and publish the changes


Because of this reason, we have to take extra care in tracking and maintaining the CRM customization changes. So the solution:

1. Make someone (that person is called CRM Champion) in charge of schema changes
2. Define security roles so that only this person can make customization changes
3. Everyone else has to send customization changes to the CRM Champion in development team


On larger scale projects, functional design documentation governs the customization and on multiple member project teams, it’s normally the BA(s), who are in charge of designing and configuring CRM. Developers rarely configure the system unless acting in a BA capacity.
