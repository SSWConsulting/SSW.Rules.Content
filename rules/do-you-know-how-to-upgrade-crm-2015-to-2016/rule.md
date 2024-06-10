---
seoDescription: Upgrade Microsoft Dynamics CRM 2015 to 2016 with improved navigation and Power BI integration.
type: rule
archivedreason:
title: Do you know how to upgrade CRM 2015 to 2016
guid: 8623800a-0a9a-49a3-9edc-2d01c78c4dfe
uri: do-you-know-how-to-upgrade-crm-2015-to-2016
created: 2016-01-22T04:02:32.0000000Z
authors: []
related: []
redirects: []
---

CRM 2016 has many improvements over it's predecessors, including Power BI integration, improved navigation, and the new Outlook extension.

The procedure for upgrading CRM 2015 to 2016 is:

<!--endintro-->

1. Apply Windows Update on CRM and Database servers

2. Go to CRM server | Deployment Manager | Disable CRM organization
   ![](disable_org.png)**Figure: Disable organization** ** <strong>
   </strong> **
3. Back up CRM organization database and configuration database

4. Go to CRM server | Control Panel | Uninstall "Microsoft Dynamics CRM Reporting Extensions"
   ![](uninstall_reportingextensions.png)**Figure: Uninstall CRM Reporting Extensions**

5. Download [CRM 2016 Server installation file](https://www.microsoft.com/en-us/download/details.aspx?id=50372) and start the upgrade
   ![](upgrade_demoorg.png)**Figure: Select the demo organization to be upgraded**
   Note: It's better to have an empty demo organization to be upgraded first, so that you can test if the server upgrade has no issues.
   ![](upgrade_successfully.png)**Figure: Successfully upgraded CRM server** ![](test_demo_org.png) **Figure: Quick test on the demo organization** ** <strong><img src="upgrade_businessOrg.png" alt="upgrade_businessOrg.png" style="margin:5px;width:683px;height:169px;">Figure: Upgrade business organization</strong> <strong><dl class="ssw15-rteElement-ImageArea"> <strong><img src="upgrade_org_successfully.png" alt="upgrade_org_successfully.png" style="margin:5px;width:496px;height:363px;">Figure: Successfully upgrade organization</strong> <strong><dl class="ssw15-rteElement-ImageArea"> <strong>
   </strong> </dl></strong> </dl></strong> **
6. Go to CRM setup directory | SrsDataConnector | Install 'Microsoft Dynamics CRM Reporting Extensions"
   ![](install_reporting_extensions.png)**Figure: Install CRM Reporting Extensions** <img src="upgrade_to_crm2016.png" alt="upgrade_to_crm2016.png" style="margin:5px;width:698px;height:354px;"> <strong>Figure: Successfully upgraded to CRM2016</strong>

<p class="ssw15-rteElement-InfoBox">If using Email Router, do the following 2 steps to upgrade Email Router to 2016
</p>
7. Go to CRM server | Uninstall "Microsoft Dynamics CRM 2015 Email Router"
![](uninstall_emailRouter.png)**Figure: Uninstall Email Router 2015** ** <strong>
</strong> ** 
8. Download [CRM 2016 Email Router](https://www.microsoft.com/en-us/download/details.aspx?id=50373) and install
![](install_emailRouter.png) **Figure: Install required components for Email Router 2016** ![](emailRouter_installtionFinish.png) **Figure: Successfully installed Email Router 2016** ** <strong><img src="configurate_emailrouter_2.png" alt="configurate_emailrouter_2.png" style="margin:5px;width:381px;height:525px;"> Figure: Configure Email Router</strong> ** 
You're now ready to roll with Microsoft Dynamics CRM 2016. If you had any trouble with this guide, please let us know with a rating of this rule.
