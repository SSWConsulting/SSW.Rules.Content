---
type: rule
archivedreason: 
title: Do you name your Azure resources correctly?
guid: ff423950-2e2e-46b2-bfa5-ef9d69e83774
uri: name-your-azure-resources-correctly
created: 2020-06-25T22:36:42.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-name-your-azure-resources-correctly

---

Organizing your cloud assets starts with good names. It is best to use all lower case and use “-“ and not put the Resource Type in the name. Different resource types can be identified by the resource icon.

<!--endintro-->

Azure defines [naming rules and restrictions for Azure resources](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules).


::: bad  
![Bad Example: This is using a mixture of upper case and lower case letters, plus specifying the resource type](bad-azure-naming.png)  
:::


::: good  
![Good Example:  Use lowercase letters and ”-”](good-azure-naming.png)  
:::
