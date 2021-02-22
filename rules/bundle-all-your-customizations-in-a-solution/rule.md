---
type: rule
archivedreason: 
title: Do you bundle all your customizations in a Solution (Model Driven)?
guid: 38997e97-94f6-4c79-9b40-f5f353227d0f
uri: bundle-all-your-customizations-in-a-solution
created: 2020-10-28T19:00:49.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-bundle-all-your-customizations-in-a-solution-model-driven
- do-you-bundle-all-your-customizations-in-a-solution-(model-driven)

---


<p class="ssw15-rteElement-P">When customizing a Model-Driven App all changes should be in a solution. A solution holds all customization being carried out by the maker, whether it be any custom entities, processes, business rules, or modifications to existing OOTB entities.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​Solutions can be used to move these customizations between environments, eg. from development à testing à production.  </p><p>Solutions can also be used to deploy changes in a managed (testing, production) and unmanaged (development) environment. Managed solutions can be thought of in simple terms and an installer can be installed and uninstalled.</p><p>Differences between Managed and Unmanaged solutions:</p><ul><li>When a Managed solution is uninstalled, all artifacts including data are removed​<br></li><li>Unmanaged solutions will install the changes but deleting the solution will leave the changes intact, so think of it as an additive change</li><li>To completely remove all customizations in an Unmanaged solution every customized item needs to be manually deleted</li></ul><dl class="image"><dt>
      <img src="solutions-custom.png" alt="solutions-custom.png" style="width:750px;" />
   </dt><dd>Figure: Solution show all customizations, make it very easy to move changes between environments<br></dd></dl><h3>Related Rule<br></h3><ul><li><a href=/create-a-solution-and-use-the-current-environment-when-creating-flow-for-dynamics>​Do you create​ a Solution and use the "Current Environment" when creating Flow for Dynamics?</a><br></li></ul>


