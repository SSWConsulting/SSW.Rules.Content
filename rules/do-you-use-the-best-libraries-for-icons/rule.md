---
type: rule
archivedreason: 
title: Do you use the best libraries for icons?
guid: a18dd243-d1ab-4a1a-bcc3-53ee3bc96e06
uri: do-you-use-the-best-libraries-for-icons
created: 2014-06-18T05:00:53.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- best-libraries-for-icons
- do-you-use-font-awesome-for-icons

---

When building a web application, it is common that you will need icons in the UI. Traditionally, this has been done with images (e.g. png, jpg) which leads to a lot of resource management.

<!--endintro-->


::: bad  
![Figure: Bad example - using images for application icons can generate a lot of pain](23-06-2014 11-20-02 AM.png)  
:::

This is simplified if you are using  **Bootstrap** , as it comes with a font-based icon library you can use in your web application. However, there is an even better third-party font-based icon library you should use when using Bootstrap:     [Font Awesome](https://fontawesome.com/).

Font Awesome provides scalable vector icons that can be customized purely through CSS and some are completely free for commercial projects. This is great if you’re tight on implementation deadlines and need generic icons in a hurry. In the ideal world, a specifically custom-designed icon set is the way to go.

Using it on your project is easy, just use your email and register on their website: [Get Started](https://fontawesome.com/start). Then you will be able to download and serve locally or use a CDN.

There are hundreds of icons. Here are a few commonly used ones:


Figure: Examples of Font Awesome icons
Read the  ["Basic Use" documentation](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use).

If you are using  **Azure** , there is an awesome icon collection with several options for you to use: http://code.benco.io/icon-collection/

<dl class="image"><br><br>::: good  <br>![Figure: Good example - a 5x scaled paper plane icon added to a Web Application](18-06-2014 2-33-45 PM.png)  <br>:::<br></dl>
Also check out Eric Phan's blog for more info: http://ericphan.net/blog/2013/10/15/javascript-corner-font-awesome .
