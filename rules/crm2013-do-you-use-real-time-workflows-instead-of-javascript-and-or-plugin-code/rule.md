---
type: rule
archivedreason: 
title: CRM2013 - Do you use Real-Time Workflows instead of Javascript and/or Plugin Code?
guid: 63893db2-5ea7-4b0d-9f96-b3484e58f1f3
uri: crm2013-do-you-use-real-time-workflows-instead-of-javascript-and-or-plugin-code
created: 2014-10-24T16:41:35.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects: []

---

CRM Workflows have always been a great option to create, update and delete data when a certain action has occurred, eg: When a customer is created, create a task for sales to update contact information. This is an example of an asynchronous workflow ie: it occurs after the record is created at some time determined by CRM.

CRM 2013 adds real-time (synchronous) workflows. These workflows run in sync with the record. An example of this might be a setting a Lead’s Estimated Value too high (say greater than $100,000), if a user enters a value greater than $100,000 the value isn’t going to be accepted.

<!--endintro-->

First Create the Workflow (don’t forget to uncheck the Run this workflow in the background):

![Figure: Create the Workflow](realtime-workflow.png)  

Second, set the properties of the workflow:

In this example it’s set to when ‘Est Value’ field changes
 If ‘Est Value’ is greater than $100,000 then stop and cancel

![Figure: Stop and cancel if ‘Est Value’ greater than $100,000](realtime-workflow-2.png)  

Once the Real-Time workflow is  **Activated** the ‘Est Value’ field will no longer accept values above $100,000. This is a simple example but in versions prior to CRM2013 this would have been implemented in Javascript or Plugin Code.

Using the Real-Time Workflow saves a lot of time and effort.

![Figure: Lead cannot be saved if Est value is greater than $100,000](realtime-workflow-3.png)
