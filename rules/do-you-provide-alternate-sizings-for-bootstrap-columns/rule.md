---
type: rule
title: Do you provide alternate sizings for Bootstrap columns?
uri: do-you-provide-alternate-sizings-for-bootstrap-columns
created: 2014-06-18T05:04:12.0000000Z
authors:
- id: 37
  title: Ben Cull
- id: 38
  title: Drew Robson

---



<span class='intro'> <span style="line-height&#58;20.799999237060547px;">​​​​​​Bootstrap provides a powerful, responsive layout with its rows and columns.</span> </span>

<p>The common&#160;way to use Bootstrap's layout system&#160;is to create a basic grid which will appear as horizontal columns on the desktop but then stack on a smaller screen such as mobiles. This is done with a single set of .col-md-* classes.</p><dl class="badImage"><dt>
      <img src="/PublishingImages/23-06-2014%2012-47-33%20PM.png" alt="" style="width&#58;400px;" /> 
   </dt><dd>Figure&#58; Bad example -&#160;create the default stacking layout with Bootstrap</dd></dl><dl class="badImage"><dt>
      <img src="/PublishingImages/23-06-2014%201-04-08%20PM.png" alt="23-06-2014 1-04-08 PM.png" style="margin&#58;5px;" />
   </dt><dd>Figure&#58;​ Bad example - the default stacking behavior on small devices</dd></dl><p>Did you know you can have more control over the responsive layout by including multiple column classes? The ability to control the layout across multiple screen sizes is a powerful tool within Bootstrap. For example, if you don't want your columns to stack on smaller devices, use the smaller grid classes by adding additional column classes (e.g. .col-xs-* .col-sm-*) to the respective &lt;div&gt;s. </p><dl class="goodImage"><dt>
      <img src="/PublishingImages/23-06-2014%2012-45-30%20PM.png" alt="23-06-2014 12-45-30 PM.png" style="width&#58;400px;" />
   </dt><dd>Figure&#58; Good example -&#160;add additional column classes to your columns</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/23-06-2014%201-14-39%20PM.png" alt="23-06-2014 1-14-39 PM.png" style="margin&#58;5px;" />
   </dt><dd>​Figure&#58; Good example - On a smaller device, these columns now arrange horizontally as desired</dd></dl>


