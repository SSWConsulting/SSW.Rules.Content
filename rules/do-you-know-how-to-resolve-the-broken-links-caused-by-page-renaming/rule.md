---
type: rule
archivedreason: 
title: Do you know how to resolve the broken links caused by page renaming?
guid: 737b062f-3514-4520-8209-1ae4d9f109f8
uri: do-you-know-how-to-resolve-the-broken-links-caused-by-page-renaming
created: 2013-07-25T00:00:22.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---


Renaming pages in SharePoint site will cause broken links.<div>All request to old URL will be responsed with a 404 error.</div>
<br><excerpt class='endintro'></excerpt><br>
<p>​Basically there are three ways to handle this issue.</p><p></p><ul><li><span style="line-height&#58;1.6;">Add a page every time for a rename…. JavaScript to redirect or META tag​</span><br></li><li><span style="line-height&#58;1.6;">Use custom 404 page to look at a list in SharePoint,&#160;the list contains all the renaming records, the records are automatically maintained via page updating events handler. (We are using this way)</span><br></li><li><span style="line-height&#58;20px;">Wait for MS to fix the problem - support alternative links for a page. (TODO&#58; link to a suggestion)</span></li></ul><p></p><p><br></p>


