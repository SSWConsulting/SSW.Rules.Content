---
type: rule
title: Do you use the CSS class "form horizontal" to arrange your fields and labels?
uri: do-you-use-the-css-class-form-horizontal-to-arrange-your-fields-and-labels
created: 2014-09-08T20:59:34.0000000Z
authors:
- id: 38
  title: Drew Robson

---



<span class='intro'> <p>You should align labels <strong>next</strong> to the inputs on medium and large displays and <strong>above</strong> inputs on small and extra-small displays.</p> </span>

<p>​Bootstrap makes this easy. Use the css class 
   <strong>form-horizontal </strong>on your html form for it to use this behaviour by default.​</p><dl class="code"><dt>
      <p> &lt;form class=&quot;form-horizontal&quot;&gt;<br>&#160;&#160;&#160; &lt;div class=&quot;form-group&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;label for=&quot;inputEmail3&quot; class=&quot;col-sm-2 control-label&quot;&gt;Email&lt;/label&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;div class=&quot;col-sm-10&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;input type=&quot;email&quot; class=&quot;form-control&quot; id=&quot;inputEmail3&quot; placeholder=&quot;Email&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/div&gt;<br>&#160;&#160;&#160; &lt;/div&gt;<br>&#160;&#160;&#160; &lt;div class=&quot;form-group&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;label for=&quot;inputPassword3&quot; class=&quot;col-sm-2 control-label&quot;&gt;Password&lt;/label&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;div class=&quot;col-sm-10&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;input type=&quot;password&quot; class=&quot;form-control&quot; id=&quot;inputPassword3&quot; placeholder=&quot;Password&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/div&gt;<br>&#160;&#160;&#160; &lt;/div&gt;<br>&lt;/form&gt;​ </p></dt><dd>Figure&#58; Example html using Bootstrap to get the above behaviour</dd></dl><p class="p6">See 
   <a href="http&#58;//getbootstrap.com/css/%22%20%5cl%20%22forms-horizontal"> 
      <span class="s7">http&#58;//getbootstrap.com/css/#forms-horizontal</span></a> for more information.​</p><h3 class="ssw15-rteElement-H3">Related Rule<br></h3><div><ul><li><span style="line-height&#58;20px;"><a href="/WebSites/RulesToBetterWebsitesLayout/Pages/how-to-arrange-forms.aspx">Do you know how to arrange forms?​​​</a><br></span></li></ul></div>


