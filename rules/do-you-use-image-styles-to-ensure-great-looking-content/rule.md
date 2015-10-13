---
type: rule
archivedreason: 
title: Do you use image styles to ensure great looking content?
guid: ae1ff7c9-9c67-4428-a8e7-5eec7e3c182b
uri: do-you-use-image-styles-to-ensure-great-looking-content
created: 2015-10-13T00:27:47.0000000Z
authors: []
related: []
redirects: []

---


<p>Many people will simply &quot;plonk&quot; an image onto a web page in between or next to a block of text. This interrupts the flow of the page and gives a disjointed, unprofessional impression.</p><p>A good technique is to set a CSS style to images. This style will be consistent and easy to be used by any person who might edit the website content.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img src="/PublishingImages/imageWithoutStyles.jpg" alt="Image without styles" />
   </dt><dd>Figure&#58; Bad Example - The image has no styles</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/imageWithStyles.jpg" alt="Image with styles" />
   </dt><dd>Figure&#58; Good Example - The image has CSS driven margin, padding, borders</dd></dl><p>It's also important to choose the correct semantic formatting for images. Different HTML codes might give the same look and feel, but the best way to add images to your page is using 
   <strong>{ltHTMLChar}dl{gtHTMLChar}</strong>, 
   <strong>{ltHTMLChar}dt{gtHTMLChar}</strong> and 
   <strong>{ltHTMLChar}dd{gtHTMLChar}</strong> tags.</p><dl class="badCode"><dt><pre>    {ltHTMLChar}div class=&quot;badImage&quot;{gtHTMLChar}
        {ltHTMLChar}img src=&quot;Images/imageWithoutStyles.jpg&quot; alt=&quot;Image without styles&quot; /{gtHTMLChar}
        {ltHTMLChar}span{gtHTMLChar}Figure&#58; Bad Example - The image has no styles{ltHTMLChar}/span{gtHTMLChar}
    {ltHTMLChar}/div{gtHTMLChar}   
                    </pre></dt><dd>Figure&#58; Bad Example - Inserting images and captions inside {ltHTMLChar}div{gtHTMLChar} tags</dd></dl><dl class="goodCode"><dt><pre>    {ltHTMLChar}dl class=&quot;badImage&quot;{gtHTMLChar}
        {ltHTMLChar}dt{gtHTMLChar}{ltHTMLChar}img src=&quot;Images/imageWithoutStyles.jpg&quot; alt=&quot;Image without styles&quot; /{gtHTMLChar}{ltHTMLChar}/dt{gtHTMLChar}
        {ltHTMLChar}dd{gtHTMLChar}Figure&#58; Bad Example - The image has no styles{ltHTMLChar}/dd{gtHTMLChar}
    {ltHTMLChar}/dl{gtHTMLChar}   
                    </pre></dt><dd>Figure&#58; Good Example - Using the {ltHTMLChar}dl{gtHTMLChar}, {ltHTMLChar}dt{gtHTMLChar} and {ltHTMLChar}dd{gtHTMLChar} tags for images</dd></dl>​


