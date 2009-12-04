---
type: rule
title: Do you use one class per file?
uri: do-you-use-one-class-per-file
created: 2009-05-05T02:03:55.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<p>The only exception should be - classes that collectively forms one atomic unit of reuse should live in one file. For example&#58;<br></p>
<dl class="badCode">
<dt style="width&#58;92.16%;height&#58;806px;"><pre>class MyClass
<br> 
&#123;
<br>
&#160;&#160;&#160;&#160;    ...
<br>
&#125;
<br>
<br>
class MyClassAEventArgs
<br>
&#123;
<br>
    &#160;&#160;&#160;&#160;...
<br>
&#125;
<br>
<br>
class MyClassBEventArgs
<br>
&#123;
<br>
    &#160;&#160;&#160;&#160;...
<br>
&#125;
<br>
<br>
class MyClassAException
<br>
&#123;
<br>
    &#160;&#160;&#160;&#160;...
<br>
&#125;
<br>
<br>
class MyClassBException
<br>
&#123;
<br>
    &#160;&#160;&#160;&#160;...
<br>
&#125;
</pre>
<dd>Bad example - 1 project, 1 file. </dd></dl>


