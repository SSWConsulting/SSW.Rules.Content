---
type: rule
archivedreason: 
title: CRM2013/2015 - Do you use CRM Business Rules to automate forms?
guid: 19da731c-2eaa-4319-85a1-06aa981a1306
uri: crm20132015---do-you-use-crm-business-rules-to-automate-forms
created: 2014-10-24T19:03:18.0000000Z
authors:
- id: 32
  title: Mehmet Ozdemir
related: []

---


<p class="p1">Prior to CRM 2013 if a CRM user wanted to&#58;</p><ul class="ul1"><li class="li3">Show an error message</li><li class="li3">Set a field value</li><li class="li3">Set business required</li><li class="li3">Set field visibility (show/hide fields)</li><li class="li3">Lock or unlock a field&#160;</li></ul><p class="p1">They would normally need to get a CRM developer involved to write JavaScript code to automate these actions.</p><p class="p1">Starting with CRM 2013 (and much improved in CRM 2015), users can now use Business Rules to automate these actions without getting a CRM developer involved.</p>
<br><excerpt class='endintro'></excerpt><br>
<p class="p1">​​Take the following Example&#58;</p><dl class="image"><dt><img src="/Communication/RulesToBetterCRMForUsers/PublishingImages/crm-automated-forms-1.png" alt="" /></dt><dd>Figure&#58; ‘Customer Type Other’ should be hidden and only displayed when Other is selected</dd></dl><p class="p1">To make this work use the following Business Rules&#58;</p><dl class="image"><dt><img src="/Communication/RulesToBetterCRMForUsers/PublishingImages/crm-automated-forms-1.png" alt="" /></dt><dd>Figure&#58; Show the ‘Customer Type Other’ field when Customer Type equals Other</dd></dl><p class="p1">The flip side of the expression also needs to be set where Customer Type doesn’t equal Other to hide the ‘Customer Type Other’ field (you could also optionally clear this field too)</p><dl class="image"><dt><img src="/Communication/RulesToBetterCRMForUsers/PublishingImages/crm-automated-forms-1.png" alt="" /></dt><dd>igure&#58; Hide the ‘Customer Type Other’ field when Customer Type doesn’t equal Other</dd></dl><p class="p1">Finally the last step is to <strong>Activate</strong> the Business Rules. To activate click the activate button on the top right of the tool bar.</p><p class="p1">Now the form will look like this&#58;</p><dl class="image"><dt><img src="/Communication/RulesToBetterCRMForUsers/PublishingImages/crm-automated-forms-1.png" alt="" /></dt><dd>Figure&#58; Great. Now ‘Customer Type Other’ is hidden</dd></dl><dl class="image"><dt><img src="/Communication/RulesToBetterCRMForUsers/PublishingImages/crm-automated-forms-1.png" alt="" /></dt><dd>Figure&#58; And on the other side ‘Customer Type Other’ is visible</dd></dl>

<p class="p1"><strong>Note&#58;</strong> CRM 2015 further improves on this by introducing the if… else… construct, so instead of creating two business rules (one for show and one for hide), this rule can be reduced to just one.</p>


