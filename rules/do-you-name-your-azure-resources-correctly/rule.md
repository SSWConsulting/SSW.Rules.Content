---
type: rule
archivedreason: 
title: Do you name your Azure resources correctly?
guid: ff423950-2e2e-46b2-bfa5-ef9d69e83774
uri: do-you-name-your-azure-resources-correctly
created: 2020-06-25T22:36:42.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Organizing your cloud assets starts with good names. It is best to use all lower case and use “-“ and not put the Resource Type in the name. Different resource types can be identified by the resource icon.

<!--endintro-->

Azure defines [naming rules and restrictions for Azure resources](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules).
<dl class="badImage">&lt;dt&gt;<img src="bad-azure-naming.png" alt="bad-azure-naming.png" style="width:750px;">&lt;/dt&gt;<dd>Bad Example: This is using a mixture of upper case and lower case letters, plus specifying the resource type  </dd></dl><dl class="goodImage">&lt;dt&gt;<img src="good-azure-naming.png" alt="good-azure-naming.png" style="width:750px;">&lt;/dt&gt;<dd>Good Example:  Use lowercase letters and ”-”</dd></dl>
