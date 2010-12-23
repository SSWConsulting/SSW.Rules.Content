---
type: rule
archivedreason: 
title: Do you avoid using "inherit" value of style.display?
guid: a99dd941-f70a-4aa6-8526-fd2ee1b547c7
uri: do-you-avoid-using-inherit-value-of-style-display
created: 2010-12-02T10:35:22.0000000Z
authors: []
related: []
redirects:
- do-you-avoid-using-＂inherit＂-value-of-style-display

---


The property value “inherit” of style.display is not recognized by IE7 and IE7 compatibility mode. So if you use this value in Javascript, it will cause script error in IE7 and IE7 compatibility like&#58;&#160;<br>
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;Message&#58; Could not get the display property. Invalid argument.&quot; <br>
So to make your Javascript and CSS style more compatible and avoid using &quot;inherit&quot; value of style.display&#58;

<br><excerpt class='endintro'></excerpt><br>

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



