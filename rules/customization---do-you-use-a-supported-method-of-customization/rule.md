---
type: rule
title: Customization - Do you use a supported method of customization?
uri: customization---do-you-use-a-supported-method-of-customization
created: 2012-12-10T18:24:24.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>
          The Microsoft CRM customization tools make it no longer necessary for you to hack
          ie. write triggers, stored procedures and .aspx pages. In fact if you were to do
          any of these your CRM is unsupported. Changes will not be preserved in any upgrades
          or fixes and Microsoft will not attend to any of your support calls until you revert
          your CRM back to a supported state.
        </p> </span>

<p>
          The common ways to customize are&#58;</p>
          <ol>
            <li>Use the designer to add Entities and Forms (aka Tables and Forms)</li>
            <li>Write SQL Reporting Services Reports</li>
            <li>Write workflows with the CRM designer</li>
            <li>Write workflows with VS.NET and .NET 3.0 WF (new in CRM 4.0)</li>
            <li>Write callouts with VS.NET (the extension points made available)</li>
          </ol>

        <p>
          The diagram below briefly outlines what are possible supported methods of customization.</p>
          <dl class="image">
            <dt>
              <img src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM_CustomizationArchitectrue.jpg" alt=" Microsoft CRM Customization Architecture " /></dt>
            <dd>
              Figure&#58; Microsoft CRM Customization Architecture
            </dd>
          </dl>
          <p>Refer to P19 of the CRM Customization Manual Course 8525A for a more in depth discussion.</p>
<p>PS&#58; For CRM 3.0 you can't find everything on the web - you will need the CRM Customization Manual Course 8525A - you have to buy it from Microsoft &#58;-(</p>


