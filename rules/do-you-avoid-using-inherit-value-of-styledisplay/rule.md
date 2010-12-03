

---
authors:

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



