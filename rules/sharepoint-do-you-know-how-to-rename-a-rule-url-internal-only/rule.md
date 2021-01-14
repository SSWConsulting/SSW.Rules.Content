---
type: rule
archivedreason: 
title: SharePoint - Do you know how to rename a rule URL? (internal only)
guid: b1965bfe-f960-463d-8ca1-67ddbbf8b2b0
uri: sharepoint-do-you-know-how-to-rename-a-rule-url-internal-only
created: 2015-09-11T06:13:01.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- rename-a-rule
- sharepoint-do-you-know-how-to-rename-a-rule-url-(internal-only)

---

Every rule page has two URLs:

* Physical URL - e.g. https://rules.ssw.com.au/<mark>Pages/</mark>tweet-rules-you-follow<mark>.aspx</mark>
* Friendly URL - e.g. https://rules.ssw.com.au/tweet-rules-you-follow

Please follow the below instruction to rename one or both of them.



<!--endintro-->

### Rename Physical URL

1. Please check the KB at    [http://www.ssw.com.au/ssw/kb/KB.aspx?KBID=Q114 5379](http://www.ssw.com.au/ssw/kb/KB.aspx?KBID=Q1145379)


### Rename Friendly URL

1. Go to "Term Store Management Tool" at [https://rules.ssw.com.au/\_layouts/15/termstore manager.aspx](/_layouts/15/termstoremanager.aspx), use "search" to find and select the old friendly URL term store item: <dl class="ssw15-rteElement-ImageArea"> <img src="find-friendly-url-item.jpg" alt="find-friendly-url-item.jpg" style="margin:5px;width:650px;"> </dl>
2. <dl class="ssw15-rteElement-ImageArea">Double click the term store item label to rename it, SharePoint will automatically convert "white space" to "-". e.g. "tweet rules you follow" will be generated with a friendly URL "tweet-rules-you-follow":<br><img src="rename-term-store-item.jpg" alt="rename-term-store-item.jpg" style="margin:5px;"></dl>
3. <dl class="ssw15-rteElement-ImageArea">Click "TERM DRIVEN PAGES" to double check the generated friendly URL is correct:<br><img src="check-generated-friendly-url.jpg" alt="check-generated-friendly-url.jpg" style="margin:5px;width:650px;"></dl>
4. <dl class="ssw15-rteElement-ImageArea"> Open browser to validate the renamed friendly URL is working well (aka not seeing 404 error):<br><img src="validate-friendly-url-in-browser.jpg" alt="validate-friendly-url-in-browser.jpg" style="margin:5px;width:650px;"> </dl>


### Redirection

The ‘auto redirect’ feature only applies to ‘physical URL’, but not to ‘friendly URL’. 
When you change a 'friendly URL',  you should follow the below steps to make the old friendly URL be redirected to the new friendly URL.

1. <dl class="ssw15-rteElement-ImageArea">Go to "Ribbon" | "Page URLs"<br><img src="redirection01.png" alt="redirection01.png" style="margin:5px;"><br></dl>
2. <dl class="ssw15-rteElement-ImageArea">Click "Add  a friendly URL to this page", then click the 'tag' icon<br><img src="redirection02.png" alt="redirection02.png" style="margin:5px;width:808px;"><br></dl>
3. <dl class="ssw15-rteElement-ImageArea">In the "Select: Add Terms" dialog, click "Add New Item", input the old friendly URL, then double click it to ensure you select it<br><img src="redirection03.png" alt="redirection03.png" style="margin:5px;"><br></dl>
4. <dl class="ssw15-rteElement-ImageArea">Click the "Add" button to add the old friendly URL, it will be redirected to the new friendly URL. (TEST: In browser, open the old friendly URL to confirm it's redirected to the new friendly URL)<br><img src="redirection04.png" alt="redirection04.png" style="margin:5px;width:560px;"><br></dl>
5. <dl class="ssw15-rteElement-ImageArea"><span style="line-height:21px;">On the "Page URLs" page, you should be able to see multiple friendly URLs associated to current page.<br></span><img src="redirection05.png" alt="redirection05.png" style="margin:5px;width:808px;"><br></dl>
