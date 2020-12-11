---
type: rule
archivedreason: 
title: Do you apply Tags to your Azure Resource Groups?
guid: 12857600-8e86-466e-8ab7-079e018c2263
uri: do-you-apply-tags-to-your-azure-resource-groups
created: 2019-12-23T22:00:09.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 73
  title: Kaique Biancatti
related: []

---

To help maintain order and control in your Azure environment, applying tags to resources and resources groups is the way to go.

Azure has the Tag feature, which allows you to apply different Tag Names and values to Resources and Resource Groups:

<!--endintro-->
<dl class="image">&lt;dt&gt;<img src="tags-in-resources-group.png" alt="tags-in-resources-group.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Little example of Tags in Resource Groups</dd></dl>
You can leverage this feature to organize your resources in a logical way, not relying in the names only. E.g.

* **Owner tag:** You can specify who owns that resource
* **Environment tag:** You can specify which environment that resource is in


**Tip:** Do not forget to have a strong naming convention document stating how those tags and resources should be named. You can use this Microsoft guide as a starter point:     [Recommended naming and tagging conventions](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/naming-and-tagging).
