---
type: rule
archivedreason: 
title: SharePoint - Do you know how to rename a rule URL? (internal only)
guid: b1965bfe-f960-463d-8ca1-67ddbbf8b2b0
uri: rename-a-rule
created: 2015-09-11T06:13:01.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- sharepoint-do-you-know-how-to-rename-a-rule-url-internal-only
- sharepoint-do-you-know-how-to-rename-a-rule-url-(internal-only)

---


<p>​​​​​Every rule page has two URLs:<br></p><ul><li><span style="line-height:1.6;"><span class="ssw15-rteStyle-Caption">Physical URL</span> - e.g. https://rules.ssw.com.au/<span class="ssw15-rteStyle-Highlight">Pages/</span>tweet-rules-you-follow<span class="ssw15-rteStyle-Highlight">.aspx </span></span><br></li><li><span style="line-height:1.6;"><span class="ssw15-rteStyle-Caption">Friendly URL</span> - </span><span style="line-height:1.6;">e.g. https://rules.ssw.com.au/tweet-rules-you-follow </span><br></li></ul><span style="line-height:20.8px;">Please follow the below instruction to rename one or both of them.</span><br><p></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Rename Physical URL</h3> 
<span style="line-height:1.6;background-color:initial;"> <ol><li> 
         <span style="line-height:1.6;background-color:initial;"> Please check the KB at  </span> <span style="line-height:1.6;background-color:initial;"></span> <a href="http://www.ssw.com.au/ssw/kb/KB.aspx?KBID=Q1145379" target="_blank" style="line-height:1.6;background-color:initial;">http://www.ssw.com.au/ssw/kb/KB.aspx?KBID=Q114 5379</a><br></li></ol></span> 
<h3 class="ssw15-rteElement-H3">Rename Friendly URL</h3><ol><li> 
      <span style="line-height:1.6;"> </span> <span style="line-height:1.6;"> Go to "Term Store Management Tool" at </span><span style="line-height:1.6;"></span><a href="/_layouts/15/termstoremanager.aspx" target="_blank" style="line-height:1.6;">https://rules.ssw.com.au/_layouts/15/termstore manager.aspx</a>, use "search" to find and select the old friendly URL term store item: <dl class="ssw15-rteElement-ImageArea"> <img src="find-friendly-url-item.jpg" alt="find-friendly-url-item.jpg" style="margin:5px;width:650px;" /> </dl></li><li><dl class="ssw15-rteElement-ImageArea">Double click the term store item label to rename it, SharePoint will automatically convert "white space" to "-". e.g. "tweet rules you follow" will be generated with a friendly URL "tweet-rules-you-follow":<br><img src="rename-term-store-item.jpg" alt="rename-term-store-item.jpg" style="margin:5px;" /></dl></li><li><dl class="ssw15-rteElement-ImageArea">Click "TERM DRIVEN PAGES" to double check the generated friendly URL is correct:<br><img src="check-generated-friendly-url.jpg" alt="check-generated-friendly-url.jpg" style="margin:5px;width:650px;" /></dl></li><li><dl class="ssw15-rteElement-ImageArea"> Open browser to validate the renamed friendly URL is working well (aka not seeing 404 error):<br><img src="validate-friendly-url-in-browser.jpg" alt="validate-friendly-url-in-browser.jpg" style="margin:5px;width:650px;" /> </dl></li></ol><h3>Redirection</h3>
<p>The ‘auto redirect’ feature only applies to ‘physical URL’, but not to ‘friendly URL’. <br><span style="line-height:1.6;">When you change a 'friendly URL',  you should follow the below steps to make the old friendly URL be redirected to the new friendly URL.</span></p><ol><li><dl class="ssw15-rteElement-ImageArea">Go to "Ribbon" | "Page URLs"<br><img src="redirection01.png" alt="redirection01.png" style="margin:5px;" /><br></dl></li><li><dl class="ssw15-rteElement-ImageArea">Click "Add  a friendly URL to this page", then click the 'tag' icon<br><img src="redirection02.png" alt="redirection02.png" style="margin:5px;width:808px;" /><br></dl></li><li><dl class="ssw15-rteElement-ImageArea">In the "Select: Add Terms" dialog, click "Add New Item", input the old friendly URL, then double click it to ensure you select it<br><img src="redirection03.png" alt="redirection03.png" style="margin:5px;" /><br></dl></li><li><dl class="ssw15-rteElement-ImageArea">Click the "Add" button to add the old friendly URL, it will be redirected to the new friendly URL. (TEST: In browser, open the old friendly URL to confirm it's redirected to the new friendly URL)<br><img src="redirection04.png" alt="redirection04.png" style="margin:5px;width:560px;" /><br></dl></li><li><dl class="ssw15-rteElement-ImageArea"><span style="line-height:21px;">On the "Page URLs" page, you should be able to see multiple friendly URLs associated to current page.<br></span><img src="redirection05.png" alt="redirection05.png" style="margin:5px;width:808px;" /><br></dl></li></ol>​​


