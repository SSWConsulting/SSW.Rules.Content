---
type: rule
archivedreason: 
title: Do you save the last user's selections?
guid: 960aaeb2-3e78-4bbc-97b4-473433533cec
uri: do-you-save-the-last-users-selections
created: 2014-12-01T01:01:51.0000000Z
authors: []
related: []

---


<p>Below is a report screen that is fairly common that developers create, 
they will make it so every time the page is loaded the user will have to
 reselect their options. To make it simpler the options should be stored
 in a cookie or database and be already pre-selected once the page is 
reloaded, as it is likely they will want to use the same or slightly 
modified query. If they don't then they can simply select what they are 
after anyway.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SampleSelect.jpg" alt="Sample Select" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Bad Example - This is suitable for first view, but not for a return view</dd></dl><dl class="goodImage"><dt>
      <img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/SampleSelect2.jpg" alt="Sample Select 2" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Good Example - Instead, save the users last selection</dd></dl>


