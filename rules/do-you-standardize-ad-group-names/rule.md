---
type: rule
archivedreason: 
title: Do you standardize AD group names?
guid: 6681c17d-fa8f-4187-8bed-a0df63f0e90c
uri: do-you-standardize-ad-group-names
created: 2015-02-16T00:13:41.0000000Z
authors:
- id: 45
  title: Chris Briggs
- id: 47
  title: Stanley Sidik
related: []

---


<p>​​The use of standardised AD Group names is a simple yet crucial step, towards building a more manageable software. Raining in on the number of AD Groups will make it simpler to manage and allow new developers to pick up an existing projecting faster.</p>
<br><excerpt class='endintro'></excerpt><br>
<p> 
   <strong>​You can save yourself countless confused conversations by standardising AD Group Names.​</strong><br></p><p>For example&#58; This is a list of AD groups associated with products.<br></p><p class="ssw15-rteElement-GreyBox">SSWSugarLearningEvents<br> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;"></span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>CodeAuditorAlerts<br> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;"></span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>LinkAuditorDevs </p><dd class="ssw15-rteElement-FigureBad"> 
   Figure&#58; Bad Example – It is difficult to know the correct name for an AD group​ </dd><p class="ssw15-rteElement-GreyBox"> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;"></span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>SugarLearning<br> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;"></span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>SugarLearningEvents<br> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;"></span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>CodeAuditor<br> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;"></span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>CodeAuditorEvents<br> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>​LinkAuditor<br> <span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;"></span><span style="font-size&#58;12px;line-height&#58;19.2000007629395px;background-color&#58;#f5f5f5;">SSW</span>LinkAuditorEvents</p>​ 
<dd class="ssw15-rteElement-FigureGood"> 
   Figure&#58; Good Example – By standardising the names of AD groups it saves confusion. </dd><p>It is recommend by default having two AD groups, use the following table as a guide.</p><table class="normal"><tbody><tr><th>Name</th><th>Type</th><th>Purpose</th></tr><tr><td>SSW&lt;ProductName&gt;</td><td>Distribution group</td><td>This email is using to send emails to the development team for a product.</td></tr><tr><td>SSW​&lt;ProductName&gt;Events</td><td>Mailbox</td><td>Acts as the collection point for all automatic notifications. For example notifications from Elmah and application insights.</td></tr></tbody></table>​​


