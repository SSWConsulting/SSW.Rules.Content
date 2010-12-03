---
type: rule
title: Do you avoid using "inherit" value of style.display?
uri: do-you-avoid-using-inherit-value-of-styledisplay
created: 2010-12-02T10:35:22.0000000Z
authors: []

---



<span class='intro'> The property “inherit” of JavaScript is not recognized by IE7 and IE7 compatibility mode. So if you use this property, it always causes script error in IE7 and IE compatibility. 
 </span>


  <dl class="badCode">
    <dt style="width&#58;50%;">
    <pre>divLoading.style.display = &quot;inherit&quot;; </pre>
    </dt>
    <dd>Bad code - inherit property </dd>
</dl>
<dl class="goodCode">
    <dt style="width&#58;50%;">
    <pre>divLoading.style.display = &quot;block&quot;; </pre>
    </dt>
    <dd>Good code - block property </dd>
</dl>



