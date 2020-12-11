---
type: rule
archivedreason: 
title: Do you have consistent way to store a same field?
guid: fe5cf339-9eaf-4e60-9704-de10e59165de
uri: do-you-have-consistent-way-to-store-a-same-field
created: 2014-12-01T00:59:54.0000000Z
authors: []
related: []

---


<p>In Outlook the Street Address is stored as 1 Multi-Line field (with an 
intelligent Address Checker - nice but not essential), yet in Microsoft 
CRM the Street Address is split out across 3 separate single line text 
fields, they should be consistent.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="goodImage"><dt> 
      <img alt="Street Address in Outlook" src="../../assets/GoodExample.jpg" style="margin:5px;width:600px;" /> 
   </dt><dd>Figure: Street Address in Outlook.</dd></dl><dl class="badImage"><dt> 
      <img alt="Street Address in CRM" src="../../assets/BadExample.jpg" style="margin:5px;" /> 
   </dt><dd>Figure: Street Address in CRM.</dd></dl><p> We consider Outlook is friendlier, because:</p><ol><li>The wrong data is entered often when you have Street 1, Street 2, Street 3.</li><li>Often Street 2 and Street 3 is not needed so it is extra clutter for no reason.</li><li>What do you do when you have Street 4.</li><li>It is the same as 
      <a href="http://www.ssw.com.au/SSW/Redirect/Live.htm">http://local.live.com/</a></li></ol><p>Of course, we might be wrong, because:</p><ol><li>Basically, it's not worth the effort - because it goes across multiple places in CRM like Leads and Opportunity (see test results from Adrian).</li><li>Printing labels might be simpler - sizes would be fixed.</li></ol><p class="productBox">We have a suggestion for CRM about this at 
   <a href="http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/CRM.aspx#AddressConsistent"> CRM and Outlook should be consistent with regards to Addresses.</a></p>


