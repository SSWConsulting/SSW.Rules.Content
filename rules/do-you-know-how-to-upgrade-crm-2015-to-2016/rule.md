---
seoDescription: Upgrade Microsoft Dynamics CRM 2015 to 2016 with improved navigation and Power BI integration.
type: rule
archivedreason:
title: Do you know how to upgrade CRM 2015 to 2016
guid: 8623800a-0a9a-49a3-9edc-2d01c78c4dfe
uri: do-you-know-how-to-upgrade-crm-2015-to-2016
created: 2016-01-22T04:02:32.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
---

CRM 2016 has many improvements over it's predecessors, including Power BI integration, improved navigation, and the new Outlook extension.

The procedure for upgrading CRM 2015 to 2016 is:

<!--endintro-->

1. Apply Windows Update on CRM and Database servers

2. Go to CRM server | Deployment Manager | Disable CRM organization
   ![Figure: Disable organization](disable_org.png)

3. Back up CRM organization database and configuration database

4. Go to CRM server | Control Panel | Uninstall "Microsoft Dynamics CRM Reporting Extensions"
   ![Figure: Uninstall CRM Reporting Extensions](uninstall_reportingextensions.png)

5. Download [CRM 2016 Server installation file](https://www.microsoft.com/en-us/download/details.aspx?id=50372) and start the upgrade

   ![Figure: Select the demo organization to be upgraded](upgrade_demoorg.png)

   **Note:** It's better to have an empty demo organization to be upgraded first, so that you can test if the server upgrade has no issues.

   ![Figure: Successfully upgraded CRM server](upgrade_successfully.png)
   ![Figure: Quick test on the demo organization](test_demo_org.png)
   ![Figure: Upgrade business organization](upgrade_businessOrg.png)
   ![Figure: Successfully upgrade organization](upgrade_org_successfully.png)

7. Go to CRM setup directory | SrsDataConnector | Install 'Microsoft Dynamics CRM Reporting Extensions"
   ![Figure: Install CRM Reporting Extensions](install_reporting_extensions.png)
   ![Figure: Successfully upgraded to CRM2016](upgrade_to_crm2016.png)

::: info
If using Email Router, do the following 2 steps to upgrade Email Router to 2016
:::

7. Go to CRM server | Uninstall "Microsoft Dynamics CRM 2015 Email Router"
   ![Figure: Uninstall Email Router 2015](uninstall_emailRouter.png)

8. Download [CRM 2016 Email Router](https://www.microsoft.com/en-us/download/details.aspx?id=50373) and install
   ![Figure: Install required components for Email Router 2016](install_emailRouter.png)
   ![Figure: Successfully installed Email Router 2016](emailRouter_installtionFinish.png)
   ![Figure: Configure Email Router](configurate_emailrouter_2.png)

You're now ready to roll with Microsoft Dynamics CRM 2016. If you had any trouble with this guide, please let us know with a rating of this rule.
