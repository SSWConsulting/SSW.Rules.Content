---
type: rule
title: Form Design - Do you change contact method options from default option group to checkboxes?
uri: form-design---do-you-change-contact-method-options-from-default-option-group-to-checkboxes
created: 2012-12-10T19:31:39.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <dl class="badImage">
          <dt>
            <img src="/PublishingImages/CRMContactMethods.jpg" alt="CRM contact methods" /></dt>
          <dd>
            Figure&#58; Bad Example - By default CRM uses option group for contact's and account's
            contact methods.</dd>
        </dl>
 </span>

 <p>
          As per our rule <a href="http&#58;//www.ssw.com.au/SSW/standards/rules/RulesToBetterInterfacesEdit.aspx#UseCheckBox">
            Do you know when to use CheckBox?</a>. Checkboxes should be used instead of the
          option group since the answer is a boolean type. You can change the option group
          to checkboxes by&#58;
        </p>
        <ol>
          <li>From CRM, go to Settings | Customizations | Customize Entities</li>
          <li>Double-Click &quot;Contact&quot; entity</li>
          <li>Click &quot;Form and Views&quot;</li>
          <li>Double-Click &quot;Form&quot; to edit contact form</li>
          <li>Click &quot;Administration&quot; tab</li>
          <li>Select a contact method field, i.e. Email</li>
          <li>Click &quot;Change Properties&quot;
            <dl class="image">
              <dt>
                <img alt="CRM contact methods form design" src="/PublishingImages/CRMChangeContactMethodsFieldProperties.jpg" /></dt>
              <dd>
                Figure&#58; Select and change the email field's properties.</dd>
            </dl>
          </li>
          <li>Click &quot;Formatting&quot; tab</li>
          <li>Change layout from &quot;Two Columns&quot; to &quot;One Column&quot; and select &quot;Check box&quot; as control
            formatting</li>
          <dl class="image">
            <dt>
              <img alt="CRM email field properties" src="/PublishingImages/CRMChangeContactMethodsFieldProperties.jpg" /></dt>
            <dd>
              Figure&#58; Change layout and control formatting of email field to one column type and
              check box.</dd>
          </dl>
          <li>Repeat steps 6-9 for other contact method</li>
          <li>Repeat steps 3-9 for account entity</li>
        </ol>
        <dl class="goodImage">
          <dt>
            <img alt="CRM contact methods with checkboxes" src="/PublishingImages/CRMContactMethodsWithCheckboxes.jpg" /></dt>
          <dd>
            Figure&#58; Good example - Checkboxes are used for contact methods because they're clear
            and simple.</dd>
        </dl>



