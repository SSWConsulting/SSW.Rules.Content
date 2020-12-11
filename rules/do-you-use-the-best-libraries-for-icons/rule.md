---
type: rule
archivedreason: 
title: Do you use the best libraries for icons?
guid: a18dd243-d1ab-4a1a-bcc3-53ee3bc96e06
uri: do-you-use-the-best-libraries-for-icons
created: 2014-06-18T05:00:53.0000000Z
authors:
- id: 37
  title: Ben Cull
- id: 38
  title: Drew Robson
- id: 1
  title: Adam Cogan
related: []

---

When building a web application, it is common that you will need icons in the UI. Traditionally, this has been done with images (e.g. png, jpg) which leads to a lot of resource management.

<!--endintro-->
<dl class="badImage">&lt;dt&gt; 
      <img alt="23-06-2014 11-20-02 AM.png" src="23-06-2014 11-20-02 AM.png" style="margin:5px;width:550px;"> 
   &lt;/dt&gt;<dd>Figure: Bad example - using images for application icons can generate a lot of pain<br></dd></dl>
This is simplified if you are using  **Bootstrap** , as it comes with a font-based icon library you can use in your web application. However, there is an even better third-party font-based icon library you should use when using Bootstrap:     [Font Awesome](https://fontawesome.com/).

Font Awesome provides scalable vector icons that can be customized purely through CSS and some are completely free for commercial projects. This is great if you’re tight on implementation deadlines and need generic icons in a hurry. In the ideal world, a specifically custom-designed icon set is the way to go.

Using it on your project is easy, just use your email and register on their website: [Get Started](https://fontawesome.com/start). Then you will be able to download and serve locally or use a CDN.

There are hundreds of icons. Here are a few commonly used ones:
<dl class="image">&lt;dt&gt;<p><i id="yui_3_17_2_1_1403220586594_514" class="fa fa-trash-o fa-4x"> </i> 
         <i class="fa fa-plus fa-4x"></i> 
         <i id="yui_3_17_2_1_1403220586594_665" class="fa fa-refresh fa-4x"></i> 
         <i id="yui_3_17_2_1_1403220586594_667" class="fa fa-ok fa-4x"></i> 
         <i class="fa fa-remove fa-4x"></i> 
         <i class="fa fa-code fa-4x"></i> 
         <i class="fa fa-cloud-download fa-4x"> </i> 
         <br></p>&lt;/dt&gt;<dd>Figure: Examples of Font Awesome icons<br></dd></dl>Read the  ["Basic Use" documentation](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use).

If you are using  **Azure** , there is an awesome icon collection with several options for you to use: http://code.benco.io/icon-collection/

<dl class="image">&lt;dt&gt; 
         <img alt="18-06-2014 2-33-45 PM.png" src="18-06-2014 2-33-45 PM.png" style="margin:5px;">  
      &lt;/dt&gt;<dd>Figure: Good example - a 5x scaled paper plane icon added to a Web Application<br></dd></dl>
Also check out Eric Phan's blog for more info: http://ericphan.net/blog/2013/10/15/javascript-corner-font-awesome .
