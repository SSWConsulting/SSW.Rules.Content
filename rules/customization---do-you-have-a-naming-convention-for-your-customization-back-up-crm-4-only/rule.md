---
type: rule
title: Customization - Do you have a naming convention for your customization back up? (CRM 4 only)
uri: customization---do-you-have-a-naming-convention-for-your-customization-back-up-crm-4-only
created: 2012-12-10T18:22:46.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 32
  title: Mehmet Ozdemir

---



<span class='intro'> <p>
          Keeping track of CRM customization changes is just as difficult as back-end database
          changes. We have a rule <a href="/do-you-stop-dealing-with-data-and-schema">
            Is a Back-end structural change going to be a hassle?</a> which provide you an
          example how you should keep track of back-end changes. You can apply this rule to
          CRM changes and use a naming convention on each customization backup file to identify
          and keep track of your changes.&#160;</p><p>Your customization file name should be&#58;&#160;</p><p>[IncrementalNumber]_[Entity]_[Date].zip,
          for example&#58; 001_account_29042009.zip&#160;</p><p>The file's name can tell you which entity
          you made changes and which date the changes were made. The incremental number will
          provides us step by step instruction on how to produce the current CRM system from
          a vanilla Microsoft Dynamics CRM.
        </p><p>CRM2011 has significant improvements in this area with Solutions. In CRM 2011 we use versioned solutions along with source control.</p><p><br></p> </span>




