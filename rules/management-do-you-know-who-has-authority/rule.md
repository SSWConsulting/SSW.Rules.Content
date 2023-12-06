---
type: rule
title: Management - Do you know who has authority?
uri: management-do-you-know-who-has-authority
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related: []
redirects: []
created: 2009-02-19T02:27:53.000Z
archivedreason: null
guid: 6fbff901-97cc-4f48-82d0-de4e30b8c37f
---

Ok, once a project gets going, you can end up dealing with many people on the client side. From the Boss to the Business Decision Maker (we call them the "Product Owner") through to Mary the receptionist (aka "users"), everyone has something to say about the software as it is being developed. However, when you are working on a Time & Materials basis in a rapid development environment with continually changing specs, you have to be certain that the work you are doing is authorised by the person who signs the cheques.

<!--endintro-->

::: email-template
|          |     |
| -------- | --- |
| To:      | John, Bob Northwind |
| Cc:      | Sophie |
| Subject: | Changes Requested by Sophie |  
::: email-content
(CC'ing the Product Owner Bob)

### To Myself

As per my conversation with Sophie, she has requested the following changes to the application: modifying the report ContractRenewal to include the "MaidenName" field from the ClientContact Table, and positioning right next to the LastName field.

### Hi Bob

Please let us know ASAP if you don't want this problem fixed.

Thanks,
John

[www.ssw.com.au](http&#58;//www.ssw.com.au/)
:::
:::
 **Figure: Sample Change Request Confirmation email**

So, say Alan from Accounts would like the Username and Password authentication to have a "remember me" checkbox for the Accounts module. This sounds reasonable, but it doesn't mean that you should charge right in and start coding.
The following is the recommended approach to governing this process:

* At the beginning of the project an employee from the client is assigned as Product Owner. This person has full authority as to what work is "in" or "out". Every new item of work should be visible to the Product Owner. ([CC is your friend](/cc-the-client-whenever-possible), [@mention is your friend](/when-you-use-mentions-in-a-pbi))
* Whenever someone who ISN'T the Product Owner makes a request for work, the Product Owner must be CC'd. For example, if Mary the receptionist has not done this, the developer sends the email again to himself, and CC's the Product Owner (and of course other relevant people).
* **Note:** The assumption is made that the task is good to go, so it is the Product Owner's responsibility to reply ASAP if they don't want the problem fixed.
