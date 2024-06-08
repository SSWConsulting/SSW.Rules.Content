---
type: rule
archivedreason: 
title: Do you have separate development, testing and production environments?
guid: 616246d0-1675-4c1c-b4b0-d4352fe818e1
uri: do-you-have-separate-development-testing-and-production-environments
created: 2009-03-10T07:02:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: 
  - do-you-identify-development-test-and-production-crm-web-servers-by-colors
  - azure-resources-creating
  - apply-tags-to-your-azure-resource-groups
  - do-you-identify-development-test-and-production-crm-web-servers-by-colors
  - do-you-always-rename-staging-url-on-azure
  - ephemeral-environments
  - do-you-have-separate-development-testing-and-production-environments
redirects: []

---

It is important to maintain three separate environments for development, testing and production. Some companies skip the testing server because it can be a hassle to copy new files, register DLLs and deploy backend changes. This will usually result in higher support costs and unhappy users due to simple bugs that could have being found in testing.  
<!--endintro-->

::: greybox
The old solution is to use build scripts (.bat and .vbs files) to automatically create a setup package that can be used to deploy to testing and production environments. For backend changes, you can either include the change scripts with the setup package (if it's a localised database), or run those scripts as part of your deployment process.

Read more about setup packages at [SSW's Wise Standard for Products.](http://www.ssw.com.au/ssw/Standards/wisesetup/WiseStandards.aspx)
:::

::: bad
Bad Example - using scripts to deploy your product to different environments
:::

::: greybox
The best way to manage your product across different environments is to use DevOps tools (like Azure DevOps, GitHub Actions, and others) and Infrastructure as Code (IaC).
    
For more information, see our rule: [Do you know how to create Azure resources?](/azure-resources-creating).
:::

::: good
Good Example - use DevOps tools and IaC to deploy to different environments
:::


You should also place the resources for each environment into its own Resource Group, and the resource group should have a tag to easily identify which environment the Resource Group relates to.
    
For more information, see our rule: [Do you apply tags to your Azure Resource Groups?](/apply-tags-to-your-azure-resource-groups).


**Now make each environment clear.**

Whenever an application has a database, have a visual indicator. I recommend a different background color for each environment

* Red for the  **Development** database
* Yellow for the  **Test** database
* Grey (no colour) for the  **Production** database


**Note:** The Yellow could have been Orange (kind of like traffic lights) but the color palette in Word doesn't give Orange.


![ ](WordColorPallete.gif)  
**Figure: Colors in Word color palette**  
    
For more information, see our rule: [Do you identify Development, Test and Production Web Servers by colors?](/do-you-identify-development-test-and-production-crm-web-servers-by-colors)
    
**Note:** Relying on color alone is not accessible for people who are visually impaired. It's important to use other identifiers to distinguish between environments.

For webapps and websites, make the environment clear by using a URL prefix too.

For more information, see our rule: [Do you always rename staging URL on Azure?](/do-you-always-rename-staging-url-on-azure).


This prevents testers from accidentally entering test data into the production version.  

**Static Site Tip:** Add a "THIS IS THE X ENVIRONMENT" banner header to your **non-production** websites.  
**Windows Forms Tip:** Implement in the base form in the header   
**ASP.NET (at least version 2.0) Tip:** Implement in the master form in the header  
![ ](dev_test_prod_servers.gif)  
**Figure: Spice up your environments with different colors**  
