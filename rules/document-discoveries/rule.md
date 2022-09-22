---
type: rule
title: Do you document discoveries and decisions?
uri: document-discoveries
authors:
  - title: Tylah Kapa
    url: https://www.ssw.com.au/people/tylah-kapa
created: 2022-09-15T14:07:00.000Z
guid: e625ed0e-b800-4d0d-bc2a-696983b52f84
---

Work can change quickly. When the requirements of a Work Item change, or critical information is found, these details should be accessible to anyone on the Scrum team. 

<!--endintro-->

# When should changes be documented?

It is recommended to update an item as soon as a critical decision or discovery has been made. Some examples include:

* The developer finds a blocking issue hindering the Work Item's progress  
* The Product Owner has asked for changes  
* The developer gets approval to update the UI while working on their changes

Sending an email isn't a bad idea. However, this information will quickly be lost, buried under hundreds of other emails, unseen by anyone who might need to see it later on. Instead, developers should update the PBI that they're working on.  

::: email-template
|          |     |
| -------- | --- |
| To:      | Product Owner|
| Cc:      | Development Team|
| Subject: | Project - Work Item Update |
::: email-content  

### Hi Bob,

As per our conversation, the primary button colour does not conform with the Northwind branding. The colour will be updated to #CC4141.
:::
:::

::: bad
Figure: Bad Example - Sending an email to confirm updates to the PBI.
:::  

::: good  
![Figure: Good Example - Decision is documented in the PBI](./images/document-discoveries-good-example.png "Azure PBI")  
:::  

Using the PBI discussion provides a number of benefits to all developers on the team including: 

::: good  
Providing one source of truth  
:::  
::: good  
Work Item hand-off doesn't need to be an involved process  
:::   
::: good  
Providing a history of the PBI  
:::  
::: good  
Easily accessible by anyone in the team   
:::   
::: good  
Provides proof of approval  
:::   

# Why don't people update the Work Item?  

There are a few reasons why the Work Item might not be updated. For example, a company might have a strong email culture, or the developer could note the change and simply forget. This can cause issues down the line where the work delivered is not as described in the Work Item, and there is no documentation on hand to say that a change was approved, or that a blocker slowed work. 
