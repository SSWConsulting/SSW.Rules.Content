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
redirects: []

---


<p>In the case of content (<a href="#ImagesSizeProperties1">unlike a site's framework files</a>), specifying the width and height 
			properties for images on your web pages can sometimes turn out to be more trouble than it's worth, particularly if the image is likely to 
			be changed a few times. Adding fixed widths to your images also destroys your content on any responsive websites.</p><p>As a result, we have made a rule that content pages <b>should not</b> have the image dimensions specified in HTML.</p><p>We do have one exception to this rule&#58; any HTML content that is to be sent out via email, as Outlook blocks images by default and 
			renders them as placeholders with very lengthy alternate text. The page is invariably stretched to widths that make the 
			contents of the message somewhat unreadable.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badCode"><dt><pre>&lt;img src=&quot;MyPic.gif&quot; width=&quot;93&quot; height=&quot;25&quot;&gt;</pre></dt><dd>Figure&#58; Bad Example - Including the width and height properties for content images</dd></dl><dl class="goodCode"><dt><pre>&lt;img src=&quot;MyPic.gif&quot;&gt;</pre></dt><dd>Figure&#58; Good Example - Exclude width and height properties for content images</dd></dl><p><span class="productBox">We have a program called <a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.</span></p>


