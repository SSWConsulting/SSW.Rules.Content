---
type: rule
archivedreason: out of date
title: Comments - Do you comment each property and method?
guid: 7fe395e0-d32c-44c2-866e-839684c78966
uri: comment-each-property-and-method
created: 2018-04-24T17:58:34.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- comments-do-you-comment-each-property-and-method

---


<p class="ssw15-rteElement-P">​​​It's important that you have a consistent code comment standard throughout an application, regardless of language. Therefore, other developers can quickly determine the workings of a function/sub/class/stored procedure. Ideally, the code should be as simple and self-explanatory as possible.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p><b>UPDATE&#58; </b>See Robert Martin Chapter 4&#58; Comments &#160;<a href="https&#58;//www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882">Clean Code&#58; A Handbook of Agile Software Craftsmanship </a><br></p><p>E.g. catch (InteropServices.COMException ex)&#160;//Catch all COM Exceptions from third-party COM component</p><p>In JavaScript and HTML, you should put these comments between the&#160;<br>{ltHTMLChar}HEAD{gtHTMLChar} and {ltHTMLChar}/HEAD{gtHTMLChar}<br>tags.&#160;<br><br>To delimit the comments (ie top and bottom), you should use the standard block comment markers of&#160;<br>{ltHTMLChar}!--&#160;and --{gtHTMLChar}.&#160;<br><br>A CSS file should be delimited with the block comment marks of&#160;​​<br>/* and */.<br></p><p>If the file contains any function/sub module/class declaration, comments will be contained​​ to each of them containing at least the following&#58;</p><ul><li>function/sub module/class name</li><li>role of the function/sub module/class declaration</li></ul><p><strong>Above a method or property declaration&#58;</strong></p><p class="ssw15-rteElement-CodeArea">''' {ltHTMLChar}summary{gtHTMLChar}<br>'''&#160;<br>''' {ltHTMLChar}/summary{gtHTMLChar}<br>''' {ltHTMLChar}param&#160;name=&quot;sender&quot;{gtHTMLChar}{ltHTMLChar}/param{gtHTMLChar}<br>''' {ltHTMLChar}param&#160;name=&quot;e&quot;{gtHTMLChar}{ltHTMLChar}/param{gtHTMLChar}<br>''' {ltHTMLChar}remarks&#160;{gtHTMLChar}{ltHTMLChar}/remarks{gtHTMLChar}<br><span style="font-size&#58;1rem;">The comments can be generated automatically by VS.NET<br></span><span style="font-size&#58;1rem;">/// - C#<br></span><span style="font-size&#58;1rem;">''' - VB.NET<br></span><span style="font-size&#58;1rem;">​Bonus - you can automatically generate documentation - but the number of clients that want this is minimal.</span></p><p><br></p>


