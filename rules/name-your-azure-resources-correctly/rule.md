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
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
- title: Bryden Oliver
  url: https://ssw.com.au/people/bryden-oliver
related: []
redirects:
- do-you-name-your-azure-resources-correctly

---

Organizing your cloud assets starts with good names. It is best to use:

* all lower case 
* use kebab case (“-“ as a separator)
* include which environment the resource is intended for i.e. dev, test, prod, etc.
* do not include the Resource Type in the name (Azure will show this anyway)
* if applicable, include the intended use of the resource in the name e.g. an app service may have a suffix *api*

<!--endintro-->

Azure defines [naming rules and restrictions for Azure resources](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules).

::: bad
![Bad Example: This is using a mixture of upper case and lower case letters, plus specifying the resource type](bad-azure-naming.png)
:::

::: good
![Good Example:  Use lowercase letters and ”-”](good-azure-naming.png)
:::
