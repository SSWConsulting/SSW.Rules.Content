---
type: rule
archivedreason: Replaced by GitHub https://github.com/SSWConsulting/SSW.Rules.Content/wiki/How-to-Rename-Rules
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

Every rule page has two URLs:

* Physical URL - e.g. `https://sharepoint.ssw.com.au/<mark>Pages/</mark>tweet-rules-you-follow<mark>.aspx</mark>`
* Friendly URL - e.g. `https://sharepoint.ssw.com.au/tweet-rules-you-follow`

Please follow the below instruction to rename one or both of them.

<!--endintro-->

### Rename Friendly URL

1. Go to "Term Store Management Tool", use "search" to find and select the old friendly URL term store item:  
![](find-friendly-url-item.jpg)

2. Double click the term store item label to rename it, SharePoint will automatically convert "white space" to "-". e.g. "tweet rules you follow" will be generated with a friendly URL "tweet-rules-you-follow":
![](rename-term-store-item.jpg)

3. Click "TERM DRIVEN PAGES" to double check the generated friendly URL is correct:
![](check-generated-friendly-url.jpg)

4. Open browser to validate the renamed friendly URL is working well (aka not seeing 404 error):
![](validate-friendly-url-in-browser.jpg)

### Redirection

The ‘auto redirect’ feature only applies to ‘physical URL’, but not to ‘friendly URL’.
When you change a 'friendly URL',  you should follow the below steps to make the old friendly URL be redirected to the new friendly URL.

1. Go to "Ribbon" | "Page URLs"
![](redirection01.png)

2. Click "Add  a friendly URL to this page", then click the 'tag' icon
![](redirection02.png)

3. In the "Select: Add Terms" dialog, click "Add New Item", input the old friendly URL, then double click it to ensure you select it
![](redirection03.png)

4. Click the "Add" button to add the old friendly URL, it will be redirected to the new friendly URL. (TEST: In browser, open the old friendly URL to confirm it's redirected to the new friendly URL)
![](redirection04.png)

5. On the "Page URLs" page, you should be able to see multiple friendly URLs associated to current page.
![](redirection05.png)
