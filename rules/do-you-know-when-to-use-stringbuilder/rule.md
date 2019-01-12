---
type: rule
title: Do you know when to use StringBuilder?
uri: do-you-know-when-to-use-stringbuilder
created: 2019-01-12T01:08:17.0000000Z
authors: []

---



<span class='intro'> ​​A String object is immutable - this means if you append two Strings together, the result is an entirely new String, rather than the original String being modified in place.&#160; This is inefficient because creating new objects is slower than altering existing objects.&#160; Using StringBuilder to append Strings modifies the underlying Char array rather than creating a new String.&#160; Therefore, whenever you are performing multiple String appends or similar functions, you should always use a StringBuilder to improve performance.<br>
<br>
<p><a href="https&#58;//docs.microsoft.com/en-us/dotnet/api/system.text.stringbuilder">See here</a> for more details.</p>​<br> </span>

<p>​A String object is immutable - this means if you append two Strings together, the result is an entirely new String, rather than the original String being modified in place.&#160; This is inefficient because creating new objects is slower than altering existing objects.&#160; Using StringBuilder to append Strings modifies the underlying Char array rather than creating a new String.&#160; Therefore, whenever you are performing multiple String appends or similar functions, you should always use a StringBuilder to improve performance.<br></p><p><br></p><p class="ssw15-rteElement-CodeArea">String&#160;s&#160;= &quot;&quot;;<br>for (int i = 0; i &lt; 1000; i ++) &#123;<br>&#160; s += i;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad">​​​Figure&#58; Bad example - This inefficient&#160;code results in 1000 new String objects being created unnecessarily.<br></dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-CodeArea">StringBuilder sb = new StringBuilder();<br>for (int i = 0; i &lt; 1000; i ++) &#123;<br>&#160; sb.append(i);<br>&#125;​</p><dd class="ssw15-rteElement-FigureGood">​Figure&#58; Good example - This efficient&#160;code only uses one StringBuilder object.<br></dd>


