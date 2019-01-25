---
type: rule
title: Comments - Do you comment each property and method?
uri: comments---do-you-comment-each-property-and-method
created: 2018-04-24T17:58:34.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p class="ssw15-rteElement-P">​​​​It's important that you have a consistent code comment standard throughout an application, regardless of language. Therefore, other developers can quickly determine the workings of a function/sub/class/stored procedure. Ideally, the code should be as simple and self-explanatory as possible.<br></p> </span>

<p><b>UPDATE&#58; </b>See Robert Martin Chapter 4&#58; Comments &#160;<a href="https&#58;//www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882">Clean Code&#58; A Handbook of Agile Software Craftsmanship </a><br></p><p>E.g. catch (InteropServices.COMException ex)&#160;//Catch all COM Exceptions from third-party COM component</p><p>In JavaScript and HTML, you should put these comments between the&#160;<br>&lt;HEAD&gt; and &lt;/HEAD&gt;<br>tags.&#160;</p><p>​<br>To delimit the comments (ie top and bottom), you should use the standard block comment markers of&#160;<br>&lt;!--&#160;and --&gt;.&#160;<br><br>A CSS file should be delimited with the block comment marks of&#160;​​<br>/* and */.<br></p><p>If the file contains any function/sub module/class declaration, comments will be contained​​ to each of them containing at least the following&#58;</p><ul><li>function/sub module/class name<br></li><li>role of the function/sub module/class declaration</li></ul><p><strong>Above a method or property declaration&#58;</strong></p><p class="ssw15-rteElement-CodeArea">/// &lt;summary&gt;<br>///&#160;<br>/// &lt;/summary&gt;<br>/// &lt;param&#160;name=&quot;sender&quot;&gt;&lt;/param&gt;<br>/// &lt;param&#160;name=&quot;e&quot;&gt;&lt;/param&gt;<br>/// &lt;remarks&#160;&gt;&lt;/remarks&gt;<br><span style="font-size&#58;1rem;"><br></span></p><p class="ssw15-rteElement-P"><strong>​Bonus - you can automatically generate documentation - but the number of clients that want this is minimal.</strong></p><p><br></p>


