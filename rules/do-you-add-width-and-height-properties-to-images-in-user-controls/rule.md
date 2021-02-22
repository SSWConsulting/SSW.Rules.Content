---
type: rule
archivedreason: 
title: Do you add width and height properties to images in user controls?
guid: 37a314af-230c-4831-bc9b-04fd27fc271f
uri: do-you-add-width-and-height-properties-to-images-in-user-controls
created: 2015-10-13T00:41:12.0000000Z
authors: []
related:
- do-you-exclude-width-and-height-properties-from-image-references-in-content
redirects: []

---

Framework pages (i.e., user controls and common layout files)  **should** have width and height properties specified for all images 		that are used. This means that the page's layout will be rendered correctly while loading and when the user has images turned off in their browser.

Images that have a height and width property set can improve your page’s load times by a few milliseconds.                  However, this will cause problems for any responsive behaviour of the page and should be used when appropriate.                  It is exceedingly unusual for an image in the site layout to not be placed using CSS, so it’s likely if this rule applies to you, you should switch to CSS and background-property.

<!--endintro-->


```
<img src="TopBar_Row1_Col2.gif" />
```

Figure: Bad Example - User controls does not contain width and height properties

```
<img src="TopBar_Row1_Col2.gif" width="86" height="20" />
```

Figure: Good Example - User controls contains width and height properties
We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
