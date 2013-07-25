---
type: rule
title: Do you know how to resolve the broken links caused by page renaming?
uri: do-you-know-how-to-resolve-the-broken-links-caused-by-page-renaming
created: 2013-07-25T00:00:22.0000000Z
authors:
- id: 9
  title: William Yin
- id: 34
  title: Brendan Richards

---



<span class='intro'> ​​Renaming pages in SharePoint site will cause broken links, all requests to old URL will be <span style="white-space&#58;nowrap;">responded&#160;​</span>with a 404 error. </span>

<p>To resolve this issue, there are three ways basically&#58;</p><ul><li><span style="line-height&#58;1.6;">​Add a page every time for a rename…. JavaScr</span><span style="line-height&#58;1.6;">ipt to redirect or META tag​</span><br></li><li><span style="line-height&#58;1.6;">Use custom 404 page to look at a list in SharePoint,&#160;the list contains all the renaming records, the records are automatically maintained via page updating events handler. (We are using this way)</span><br></li><li><span style="line-height&#58;20px;">Wait for MS to fix the problem - <a href="http&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/SharePointTeamServices.aspx#PageAlternativeURLs">support classical&#160;alternative&#160;links for a&#160;page.​</a>&#160;</span></li></ul><p></p><p><br></p>


