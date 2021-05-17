---
type: rule
archivedreason: 
title: Management - Do you know who has authority?
guid: 6fbff901-97cc-4f48-82d0-de4e30b8c37f
uri: management-do-you-know-who-has-authority
created: 2009-02-19T02:27:53.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Ok, once a project gets going, you can end up dealing with many people on the client side. From the Boss to the Business Decision Maker (we call them the "Product Owner") through to Mary the receptionist (aka "users"), everyone has something to say about the software as it is being developed. However, when you are working on a Time & Materials basis in a rapid development environment with continually changing specs, you have to be certain that the work you are doing is authorised by the person who signs the cheques.

<!--endintro-->


::: email-template
|          |     |
| -------- | --- |
| To:      | Angelo |
| Cc:      | John, Sophie |
| Bcc:     | ZZZ |
| Subject: | Changes Requested by Sophie |  
::: email-content
As per our conversation, Sophie has requested the following changes to your application: modifying rptContractRenewal to include the "MaidenName" field from the ClientContact Table, and positioning right next to the Surname field.

Please let us know ASAP if you don't want this problem fixed.

Thanks,
John
[www.ssw.com.au](http&#58;//www.ssw.com.au/)
:::
:::
 **Figure: Sample Change Request Confirmation email** So, say Alan from Accounts would like the Username and Password authentication to have a "remember me" checkbox for the Accounts module. This sounds reasonable, but it doesn't mean that you should charge right in and start coding.
As an example, this is how we govern this process:

* At the beginning of the project one of the client staff is assigned as Product Owner. This person has full authority from the Business Decision Maker of the client as to what work is IN or OUT. Every new item of work must be authorized by this Product Owner.
* Whenever someone who ISN'T the Product Owner makes a request for work, the Product Owner must be CC'd. If Mary the receptionist has not done this, the developer sends the email again to himself, and CC's the Product Owner (CC'ing other relevant people - if they may give feedback on the task) to let them know about the request.
* We make the assumption that the task is good to go, so it is the Product Owner's job to make sure that they reply ASAP if they don't want the problem fixed.
