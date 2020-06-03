---
type: rule
title: Do you use image styles to ensure great looking content?
uri: do-you-use-image-styles-to-ensure-great-looking-content
created: 2015-10-13T00:27:47.0000000Z
authors: []

---



<span class='intro'> <p>Many people will simply &quot;plonk&quot; an image onto a web page in between or next to a block of text. This interrupts the flow of the page and gives a disjointed, unprofessional impression.</p><p>A good technique is to set a CSS style to images. This style will be consistent and easy to be used by any person who might edit the website content.</p> </span>

<dl class="badImage"><dt>
      <img src="/PublishingImages/imageWithoutStyles.jpg" alt="Image without styles" />
   </dt><dd>Figure&#58; Bad Example - The image has no styles</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/imageWithStyles.jpg" alt="Image with styles" />
   </dt><dd>Figure&#58; Good Example - The image has CSS driven margin, padding, borders</dd></dl><p>It's also important to choose the correct semantic formatting for images. Different HTML codes might give the same look and feel, but the best way to add images to your page is using 
   <strong>&lt;dl&gt;</strong>, 
   <strong>&lt;dt&gt;</strong> and 
   <strong>&lt;dd&gt;</strong> tags.</p><dl class="badCode"><dt><pre>    &lt;div class=&quot;badImage&quot;&gt;
        &lt;img src=&quot;Images/imageWithoutStyles.jpg&quot; alt=&quot;Image without styles&quot; /&gt;
        &lt;span&gt;Figure&#58; Bad Example - The image has no styles&lt;/span&gt;
    &lt;/div&gt;   
                    </pre></dt><dd>Figure&#58; Bad Example - Inserting images and captions inside &lt;div&gt; tags</dd></dl><dl class="goodCode"><dt><pre>    &lt;dl class=&quot;badImage&quot;&gt;
        &lt;dt&gt;&lt;img src=&quot;Images/imageWithoutStyles.jpg&quot; alt=&quot;Image without styles&quot; /&gt;&lt;/dt&gt;
        &lt;dd&gt;Figure&#58; Bad Example - The image has no styles&lt;/dd&gt;
    &lt;/dl&gt;   
                    </pre></dt><dd>Figure&#58; Good Example - Using the &lt;dl&gt;, &lt;dt&gt; and &lt;dd&gt; tags for images</dd></dl>​


