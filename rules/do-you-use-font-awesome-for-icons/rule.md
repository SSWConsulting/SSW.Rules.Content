---
type: rule
title: Do you use Font Awesome for icons?
uri: do-you-use-font-awesome-for-icons
created: 2014-06-18T05:00:53.0000000Z
authors:
- id: 37
  title: Ben Cull
- id: 38
  title: Drew Robson

---



<span class='intro'> <span style="line-height&#58;20.799999237060547px;">​</span><div class="ms-rtestate-read ms-rte-wpbox"><div class="ms-rtestate-notify  ms-rtestate-read 44097510-f8d6-47f4-8ca1-e0cac144ac75" id="div_44097510-f8d6-47f4-8ca1-e0cac144ac75"></div><div id="vid_44097510-f8d6-47f4-8ca1-e0cac144ac75" style="display&#58;none;"></div></div><span style="line-height&#58;20.799999237060547px;">​​​​​​​​Bootstrap comes with a good font-based icon library to use in your web application, but there is an even better one you should use whenever you are using Bootstrap.</span>​ </span>

​ 
<p>When building a web application, it is common that you will need icons in the UI. Traditionally, this has been done with images (e.g. png, jpg) which leads to a lot of resource management.</p><dl class="badImage"><dt>
      <img src="/PublishingImages/23-06-2014%2011-20-02%20AM.png" alt="23-06-2014 11-20-02 AM.png" style="margin&#58;5px;width&#58;550px;" />
   </dt><dd>Figure&#58; Bad example - using images for application icons</dd></dl><p>This is simplified if you are using Bootstrap, as it comes with a font-based icon library you can use in your web application. However, there is an even better third-party font-based icon library you should use when using Bootstrap.</p><p>
   <span style="line-height&#58;1.6;">Font Awesome provides scalable vector icons which can be customized purely through CSS and is completely free for commercial projects.&#160;This is great if you’re tight on implementation deadlines, but is no replacement for a specifically designed icon set. However if you need generic icons in a hurry, then use Font Awesome.</span></p><p>Using it on your project is easy, just add the following stylesheet to your app&#58;​</p><pre class="source-code" style="font-family&#58;monaco, menlo, consolas, 'courier new', monospace;word-wrap&#58;break-word;padding&#58;9.5px;border-top-left-radius&#58;4px;border-top-right-radius&#58;4px;border-bottom-right-radius&#58;4px;border-bottom-left-radius&#58;4px;margin-bottom&#58;10px;word-break&#58;break-all;overflow&#58;auto;background-color&#58;#f5f5f5;"><span class="cm-tag" style="color&#58;#117700;">&lt;link </span><span class="cm-attribute" style="color&#58;#0000cc;">href</span>=<span class="cm-string" style="color&#58;#11aa11;">&quot;//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css&quot;</span> <span class="cm-attribute" style="color&#58;#0000cc;">rel</span>=<span class="cm-string" style="color&#58;#11aa11;">&quot;stylesheet&quot; /</span><span class="cm-tag" style="color&#58;#117700;">&gt;​</span></pre><p>Then you have access to over 350 icons. Here are a few commonly used ones&#58;</p><dl class="image"><dt><p>​​​<i class="fa fa-trash-o fa-4x" id="yui_3_17_2_1_1403220586594_514">​​​</i><i class="fa fa-plus fa-4x"></i><i class="fa fa-refresh fa-4x" id="yui_3_17_2_1_1403220586594_665"></i><i class="fa fa-ok fa-4x" id="yui_3_17_2_1_1403220586594_667"></i><i class="fa fa-remove fa-4x"></i><i class="fa fa-code fa-4x"></i><i class="fa fa-cloud-download fa-4x">​​​</i>​<br></p></dt><dd>Figure&#58; Examples of Font Awesome icons</dd><p>​​​The HTML is easy, e.g.&#160;&lt;i class=&quot;fa fa-trash-o&quot;&gt;&lt;/i&gt;​ to add the above trashbin icon.</p><p>​You can also download and reference Font Awesome locally.</p><dl class="image"><dt>
         <img src="/PublishingImages/23-06-2014%2011-08-06%20AM.png" alt="23-06-2014 11-08-06 AM.png" style="margin&#58;5px;width&#58;550px;" />
      </dt><dd>Figure&#58; After adding Font Awesome from NuGet, two lines of code add the below&#160;icon​</dd></dl><dl class="image"><dt>
         <img src="/PublishingImages/18-06-2014%202-33-45%20PM.png" alt="18-06-2014 2-33-45 PM.png" style="margin&#58;5px;" />
      </dt><dd>Figure&#58; A 5x scaled paper plane icon has been added to my Web Application</dd></dl><p>You can get Font Awesome from NuGet or 
      <a href="http&#58;//fortawesome.github.io/Font-Awesome/">http&#58;//fortawesome.github.io/Font-Awesome/</a>.​</p><p>Also check out Eric Phan's blog for more info&#58;&#160;<a>http&#58;//ericphan.net/blog/2013/10/15/javascript-corner-font-awesome​​</a>.</p> ​​</dl>


