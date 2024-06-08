---
type: rule
archivedreason: Replaced by https://github.com/SSWConsulting/SSW.Rules.Content/wiki/How-to-Add-and-Edit-Categories-and-Top-Categories
title: SharePoint - Do you know how to create a rule category? (internal only)
guid: cddfc9a1-da16-4918-8280-c9a95add7463
uri: how-to-create-a-rule-category
created: 2014-08-21T20:38:15.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-how-to-create-a-rule-category-(internal-only)
- sharepoint-do-you-know-how-to-create-a-rule-category-internal-only
- sharepoint-do-you-know-how-to-create-a-rule-category-(internal-only)

---

Basically, creating a rule category contains two parts of work.

1. Create a "rule category" in Term Store (e.g. "Rules to Better xxx")
2. Create a "rule summary" page to show all the rule pages belong to this rule category

<!--endintro-->

**1. Create a "rule category" in Term Store (e.g. "Rules to Better xxx")**

1. Open browser, log in to /admin

2) Open termstoremanager, under "ImportTaxonomy" | "RuleCategories", find the right "parent category" (e.g. "Communication"), click "Create Term":
   ![](rulecategor1.jpg)

3) Type the rule category name, e.g. "Rules to Better xxx":
   ![](rulecategor2.jpg)

**2. Create a "rule summary" page to show rule pages belong to this rule category**

1) Go to "Site Setting" | "Add a page" to create a new page:
  ![](rulecategor3.jpg)

2) Type the rule category name in the popup dialog (same as the rule category name created in term store, e.g. "Rules to Better xxx"), then click "Create" button:
  ![Figure: a friendly url will be automatically generated](rulecategor4.jpg)

3) On the new created page, go to "Ribbon" | "Page" | "Page Layout" to change the new created page layout to be "SSW - Rule Summary Page":

  ![](rulecategor5.jpg)

4) "Check in" and "Publish" this "Rule Summary" page, then you should have a page like below,
  
  ![Figure: Any futher created "rule pages" belong to this "rule category" will be listed on this page](rulecategor6.jpg)
