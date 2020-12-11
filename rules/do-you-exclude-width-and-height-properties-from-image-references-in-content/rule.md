---
type: rule
archivedreason: 
title: Do you exclude width and height properties from image references in content?
guid: 3795e298-c889-49e5-b9b1-58dac3d8eaae
uri: do-you-exclude-width-and-height-properties-from-image-references-in-content
created: 2015-10-13T00:44:07.0000000Z
authors: []
related:
- do-you-add-width-and-height-properties-to-images-in-user-controls

---

In the case of content (unlike a site's framework files), specifying the width and height 		properties for images on your web pages can sometimes turn out to be more trouble than it's worth, particularly if the image is likely to 		be changed a few times. Adding fixed widths to your images also destroys your content on any responsive websites.

As a result, we have made a rule that content pages  **should not** have the image dimensions specified in HTML.

We do have one exception to this rule: any HTML content that is to be sent out via email, as Outlook blocks images by default and 		renders them as placeholders with very lengthy alternate text. The page is invariably stretched to widths that make the 		contents of the message somewhat unreadable.

<!--endintro-->
<dl class="badCode">&lt;dt&gt;<pre>&lt;img src=&quot;MyPic.gif&quot; width=&quot;93&quot; height=&quot;25&quot;&gt;</pre>&lt;/dt&gt;<dd>Figure&#58; Bad Example - Including the width and height properties for content images</dd></dl><dl class="goodCode">&lt;dt&gt;<pre>&lt;img src=&quot;MyPic.gif&quot;&gt;</pre>&lt;/dt&gt;<dd>Figure&#58; Good Example - Exclude width and height properties for content images</dd></dl>
We have a program called [SSW Code Auditor](https&#58;//www.ssw.com.au/ssw/CodeAuditor/) to check for this rule.
