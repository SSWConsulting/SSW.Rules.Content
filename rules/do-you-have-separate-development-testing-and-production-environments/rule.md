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
redirects: []

---

It is important to maintain three separate environments for development, testing and production. Some companies skip the testing server because it can be a hassle to copy new files, register DLLs and deploy backend changes. This will usually result in higher support costs and unhappy users due to simple bugs that could have being found in testing.  
<!--endintro-->

The best solution is to use build scripts (.bat and .vbs files) to automatically create a setup package that can be used to deploy to testing and production environments. For backend changes, you can either include the change scripts with the setup package (if it's a localised database), or run those scripts as part of your deployment process.

Read more about setup packages at [SSW's Wise Standard for Products.](http://www.ssw.com.au/ssw/Standards/wisesetup/WiseStandards.aspx)

**Now make each environment clear.**

Whenever an application has a database, have a visual indicator. I recommend a different background color for each environment

* Red for the  **Development** database
* Yellow for the  **Test** database
* Grey (no colour) for the  **Production** database


**Note:** The Yellow could have been Orange (kind of like traffic lights) but the color palette in Word doesn't give Orange.


![ ](WordColorPallete.gif)  
**Figure: Colors in Word color palette**  


This prevents testers from accidentally entering test data into the production version.  

**Static Site Tip:** Add a "THIS IS THE X ENVIRONMENT" banner header to your **non-production** websites.  
**Windows Forms Tip:** Implement in the base form in the header   
**ASP.NET (at least version 2.0) Tip:** Implement in the master form in the header  
![ ](dev_test_prod_servers.gif)  
**Figure: Spice up your environments with different colors**  
