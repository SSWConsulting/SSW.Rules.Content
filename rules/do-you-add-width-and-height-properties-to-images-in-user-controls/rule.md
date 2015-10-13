---
type: rule
title: Do you add width and height properties to images in user controls?
uri: do-you-add-width-and-height-properties-to-images-in-user-controls
created: 2015-10-13T00:41:12.0000000Z
authors: []

---



<span class='intro'> <p>Framework pages (i.e., user controls and common layout files) <b>should</b> have width and height properties specified for all images 
   that are used. This means that the page's layout will be rendered correctly while loading and when the user has images turned off in their browser.</p><p>
                Images that have a height and width property set can improve your page’s load times by a few milliseconds. 
                However, this will cause problems for any responsive behaviour of the page and should be used when appropriate. 
                It is exceedingly unusual for an image in the site layout to not be placed using CSS, so it’s likely if this rule applies to you, you should switch to CSS and background-property.
            </p> </span>

<dl class="badCode"><dt><pre>&lt;img src=&quot;TopBar_Row1_Col2.gif&quot; /&gt;</pre></dt><dd>Figure&#58; Bad Example - User controls does not contain width and height properties</dd></dl><dl class="goodCode"><dt><pre>&lt;img src=&quot;TopBar_Row1_Col2.gif&quot; width=&quot;86&quot; height=&quot;20&quot; /&gt;</pre></dt><dd>Figure&#58; Good Example - User controls contains width and height properties</dd></dl><p><span class="productBox">We have a program called <a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.</span></p>


