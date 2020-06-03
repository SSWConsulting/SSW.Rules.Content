---
type: rule
title: Customization - Do you export only the customizations of entities that you did customize?
uri: customization---do-you-export-only-the-customizations-of-entities-that-you-did-customize
created: 2012-12-10T19:11:13.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>
          Export each single entity customization and keep each entity customization in a
          separate file, like&#58;
        </p>
        <ul>
          <li>Account_11022009.xml </li>
          <li>Contact_11022009.xml </li>
        </ul> </span>

<p>
          This way, if an entity is changed or broken on the Live environment, you can re-import
          the customization for this entity again, without breaking other entities on live
          environment.
        </p>
        <p>
          Instead of exporting each single entity, you can also export only your customized
          entities in 1 step, and afterwards select what entities to import
        </p>
        <dl class="image">
          <dt>
            <img src="/PublishingImages/CRM_CUS_01.JPG" alt="Import single customization" />
          </dt>
          <dd>
            Figure&#58; You can select the single customization to import
          </dd>
        </dl>


