---
type: rule
archivedreason: 
title: Do you know the best way to display code on your website?
guid: edf8e58b-33bb-42a9-aa9a-85c1ca6b74d1
uri: best-way-to-display-code-on-your-website
created: 2016-08-05T18:57:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-the-best-way-to-display-code-on-your-website

---


<p>Any website designer that needs to display code should be aware that there is a very simple method for simply formatting code, and there is a slow and complex method.</p><p>The complex method requires formatting each line with HTML tags (such as {ltHTMLChar}br{gtHTMLChar} and &amp;nbsp;) to ensure the code looks nice and pretty.</p><p>The simpler method uses {ltHTMLChar}pre{gtHTMLChar} tags. Pre (standing for &quot;preformatted&quot;) means that the code is formatted exactly as it is written in the HTML window. This means the page designer can format code in a very simple fashion, without worrying about tags.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​​<strong>Note&#58;</strong><span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;16.8px;">&#160;{ltHTMLChar}code{gtHTMLChar} tags should not be used because they only provide the font Courier - you still have to manually indent all of your code as in the bad code display example below.</span> <br></p><p class="ssw15-rteElement-CodeArea">{ltHTMLChar}font face=&quot;Courier, Times, Arial, Verdana&quot; size=&quot;3&quot;{gtHTMLChar}<br>public class Configuration{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&#123;{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;public static string MySetting{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;&#123;{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;get{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;&#123;{ltHTMLChar}br{gtHTMLChar}<br>{ltHTMLChar}/font{gtHTMLChar}</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad code display example - using {ltHTMLChar}font{gtHTMLChar} </dd><p class="ssw15-rteElement-CodeArea">{ltHTMLChar}code{gtHTMLChar}<br>public class Configuration{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&#123;{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;public static string MySetting{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;&#123;{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;get{ltHTMLChar}br{gtHTMLChar}<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;&#123;{ltHTMLChar}br{gtHTMLChar}<br>{ltHTMLChar}/code{gtHTMLChar}</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad code display example - using {ltHTMLChar}code{gtHTMLChar}</dd><p class="ssw15-rteElement-CodeArea">{ltHTMLChar}pre{gtHTMLChar}<br>public class Configuration<br>&#123;<br>public static string MySetting<br>&#123;<br>get<br>&#123;<br>{ltHTMLChar}/pre{gtHTMLChar}</p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good code display example - using {ltHTMLChar}pre{gtHTMLChar}<br></dd><p><b>Tip&#58;</b>&#160;Do not use auto-format (Ctrl-K, Ctrl-F) in Visual Studio when updating page with {ltHTMLChar}pre{gtHTMLChar} tags, or it will destroy all the code formatting. We have made a suggestion to Microsoft to fix this.<br></p>


