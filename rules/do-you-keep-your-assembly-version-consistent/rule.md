---
type: rule
title: Do you keep your Assembly Version Consistent?
uri: do-you-keep-your-assembly-version-consistent
created: 2009-04-28T07:03:16.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<dl class="badCode">
<dt><pre>[assembly&#58; AssemblyVersion(<span style="background-color&#58;#ffff00;">&quot;2.0.*&quot;</span>)]<br>
[assembly&#58; AssemblyFileVersionAttribute(<span style="background-color&#58;#ffff00;">&quot;1.0.0.3&quot;</span>)]
</pre>
<dd>Bad example - the common assembly versioning method. </dd></dl>
<dl class="goodCode">
<dt><pre>[assembly&#58; AssemblyVersion(<span style="background-color&#58;#ffff00;">&quot;2.0.*&quot;</span>)]<br>
[assembly&#58; AssemblyFileVersionAttribute(<span style="background-color&#58;#ffff00;">&quot;2.0.*&quot;</span>)]
</pre>
<dd>Good example - the best way for Assembly versioning. </dd></dl>


