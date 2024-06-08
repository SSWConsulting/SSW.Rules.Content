---
type: rule
archivedreason: Irrelevant as per Marcus, Jean, and Calum
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

Renaming pages in SharePoint site will cause broken links. All requests to the old URL will be responded to with a 404 error. 

<!--endintro-->

Options to resolve this issue are:

* Add a page every time for a rename... add a JavaScript or META tag redirect to the original page
* Use custom 404 page to look at a list in SharePoint, the list contains all the renaming records, the records are automatically maintained via page updating events handler. (We are using this way)
* Wait for MS to fix the problem - [support classical alternative links for a page](https://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/SharePointTeamServices.aspx#PageAlternativeURLs)
