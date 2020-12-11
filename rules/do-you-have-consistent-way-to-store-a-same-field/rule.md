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

In Outlook the Street Address is stored as 1 Multi-Line field (with an  intelligent Address Checker - nice but not essential), yet in Microsoft  CRM the Street Address is split out across 3 separate single line text  fields, they should be consistent.

<!--endintro-->
<dl class="goodImage">&lt;dt&gt; 
      <img alt="Street Address in Outlook" src="../../assets/GoodExample.jpg" style="margin:5px;width:600px;"> 
   &lt;/dt&gt;<dd>Figure: Street Address in Outlook.</dd></dl><dl class="badImage">&lt;dt&gt; 
      <img alt="Street Address in CRM" src="../../assets/BadExample.jpg" style="margin:5px;"> 
   &lt;/dt&gt;<dd>Figure: Street Address in CRM.</dd></dl>
We consider Outlook is friendlier, because:

1. The wrong data is entered often when you have Street 1, Street 2, Street 3.
2. Often Street 2 and Street 3 is not needed so it is extra clutter for no reason.
3. What do you do when you have Street 4.
4. It is the same as <br>      [http://local.live.com/](http://www.ssw.com.au/SSW/Redirect/Live.htm)


Of course, we might be wrong, because:

1. Basically, it's not worth the effort - because it goes across multiple places in CRM like Leads and Opportunity (see test results from Adrian).
2. Printing labels might be simpler - sizes would be fixed.


We have a suggestion for CRM about this at     [CRM and Outlook should be consistent with regards to Addresses.](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/CRM.aspx#AddressConsistent)
