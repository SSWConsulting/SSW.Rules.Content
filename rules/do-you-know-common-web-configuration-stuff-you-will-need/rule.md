---
type: rule
title: Do you know common web configuration stuff you will need?
uri: do-you-know-common-web-configuration-stuff-you-will-need
created: 2009-06-16T01:41:30.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<p class="MsoNormal"><span lang="EN-US">You should always use a SPConfigModification class to modify your web.config – never tell your user or administrator to make changes manually!&#160; This also allows them to switch off a feature from SharePoint knowing that the changes had been reverted.</span></p><span style="font-family&#58;'calibri', 'sans-serif';font-size&#58;11pt;" lang="EN-US">For developers – you must test your SPConfigModification carefully, mismatched XPath will cause problems in your web.config and create duplicate entries!</span>


