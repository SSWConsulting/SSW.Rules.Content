---
type: rule
archivedreason: "The class no-longer exists in Bootstrap 4.\nhttps://getbootstrap.com/docs/4.5/components/forms/#form-controls \n\nRelated rule: https://rules.ssw.com.au/how-to-align-your-form-labels"
title: Do you use the CSS class "form horizontal" to arrange your fields and labels?
guid: 5c2ca49f-b126-4f96-a4a0-f3126e91c195
uri: use-css-class-form-horizontal-to-arrange-fields-and-labels
created: 2014-09-08T20:59:34.0000000Z
authors:
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects:
- do-you-use-the-css-class-＂form-horizontal＂-to-arrange-your-fields-and-labels
- do-you-use-the-css-class-form-horizontal-to-arrange-your-fields-and-labels

---


<p>​You should align labels <strong>next</strong> to the inputs on medium and large displays and <strong>above</strong> inputs on small and extra-small displays.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>Bootstrap makes this easy. Use the css class <strong>form-horizontal </strong>on your html form for it to use this behaviour by default.</p><dl class="code"><dt> <p>&lt;form class=&quot;form-horizontal&quot;&gt;<br>&#160;&#160;&#160; &lt;div class=&quot;form-group&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;label for=&quot;inputEmail3&quot; class=&quot;col-sm-2 control-label&quot;&gt;Email&lt;/label&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;div class=&quot;col-sm-10&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;input type=&quot;email&quot; class=&quot;form-control&quot; id=&quot;inputEmail3&quot; placeholder=&quot;Email&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/div&gt;<br>&#160;&#160;&#160; &lt;/div&gt;<br>&#160;&#160;&#160; &lt;div class=&quot;form-group&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;label for=&quot;inputPassword3&quot; class=&quot;col-sm-2 control-label&quot;&gt;Password&lt;/label&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;div class=&quot;col-sm-10&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;input type=&quot;password&quot; class=&quot;form-control&quot; id=&quot;inputPassword3&quot; placeholder=&quot;Password&quot;&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/div&gt;<br>&#160;&#160;&#160; &lt;/div&gt;<br>&lt;/form&gt;</p></dt><dd>Figure&#58; Example html using Bootstrap to get the above behaviour</dd></dl><p class="p6">​See <a href="http&#58;//getbootstrap.com/css/#forms-horizontal"> <span class="s7">http&#58;//getbootstrap.com/css/#forms-horizontal</span></a> for more information.</p><h3 class="ssw15-rteElement-H3">Related Rule<br></h3><div><ul><li><span style="line-height&#58;20px;"><a href=/do-you-know-how-to-arrange-forms>Do you know how to arrange forms? </a><br></span></li></ul></div>


