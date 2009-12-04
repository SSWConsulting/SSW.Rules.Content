---
type: rule
archivedreason: 
title: Do you keep your Assembly Version Consistent?
guid: 9615f20a-8b4e-4666-beb8-c7da8dfb358e
uri: do-you-keep-your-assembly-version-consistent
created: 2009-04-28T07:03:16.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>
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


