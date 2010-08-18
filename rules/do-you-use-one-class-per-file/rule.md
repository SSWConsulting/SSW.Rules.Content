---
type: rule
archivedreason: 
title: Do you use one class per file?
guid: e1c3a18a-a6fe-41af-a652-8facd4eda898
uri: do-you-use-one-class-per-file
created: 2009-05-05T02:03:55.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---



  <p>Each class definition should live in its own file.</p>
<p>Reasons&#58;</p>
<p>Easy to locate class definitions outside the Visual Studio IDE (e.g. SourceSafe, Windows Explorer)</p>

<br><excerpt class='endintro'></excerpt><br>

  <p>The only exception should be - classes that collectively forms one atomic unit of reuse should live in one file. For example&#58;</p>
<dl class="badCode">
    <dt style="width&#58;92.16%;height&#58;806px;">
    <pre>class MyClass
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
    </dt>
    <dd>Bad example - 1 project, 1 file. </dd>
</dl>



