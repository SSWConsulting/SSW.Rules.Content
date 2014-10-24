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


<p class="p1">CRM Workflows have always been a great option to create, update and delete data when a certain action has occurred, eg&#58; When a customer is created, create a task for sales to update contact information. This is an example of an asynchronous workflow ie&#58; it occurs after the record is created at some time determined by CRM.</p><p class="p1">CRM 2013 adds real-time (synchronous) workflows. These workflows run in sync with the record. An example of this might be a setting a Lead’s Estimated Value too high (say greater than $100,000), if a user enters a value greater than $100,000 the value isn’t going to be accepted.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​First Create the Workflow (don’t forget to uncheck the Run this workflow in the background)&#58;</p><dl class="image"><dt><img src="/PublishingImages/realtime-workflow.png" alt="" /></dt><dd>Figure&#58; Create the Workflow </dd></dl><p class="p1">Second, set the properties of the workflow&#58;</p><p class="p1">In this example it’s set to when ‘Est Value’ field changes<br>
If ‘Est Value’ is greater than $100,000 then stop and cancel</p><dl class="image"><dt><img src="/PublishingImages/realtime-workflow-2.png" alt="" /></dt><dd>Figure&#58; Stop and cancel if ‘Est Value’ greater than $100,000</dd></dl><p class="p1">​Once the Real-Time workflow is <strong>Activated</strong> the ‘Est Value’ field will no longer accept values above $100,000. This is a simple example but in versions prior to CRM2013 this would have been implemented in Javascript or Plugin Code.</p><p class="p1">Using the Real-Time Workflow saves a lot of time and effort.</p><dl class="image"><dt><img src="/PublishingImages/realtime-workflow-3.png" alt="" /></dt><dd>Figure&#58; Lead cannot be saved if Est value is greater than $100,000</dd></dl>


