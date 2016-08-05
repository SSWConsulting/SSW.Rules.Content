---
type: rule
title: Do you know the best way to display code on your website?
uri: do-you-know-the-best-way-to-display-code-on-your-website
created: 2016-08-05T18:57:08.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Any website designer that needs to display code should be aware that there is a very simple method for simply formatting code, and there is a slow and complex method.</p><p>The complex method requires formatting each line with HTML tags (such as &lt;br&gt; and &amp;nbsp;) to ensure the code looks nice and pretty.</p><p>The simpler method uses &lt;pre&gt; tags. Pre (standing for &quot;preformatted&quot;) means that the code is formatted exactly as it is written in the HTML window. This means the page designer can format code in a very simple fashion, without worrying about tags.​<br></p> </span>

<p>​​<strong>Note&#58;</strong><span style="color&#58;#000000;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;16.8px;">&#160;&lt;code&gt; tags should not be used because they only provide the font Courier - you still have to manually indent all of your code as in the bad code display example below.</span> <br></p><p class="ssw15-rteElement-CodeArea">&lt;font face=&quot;Courier, Times, Arial, Verdana&quot; size=&quot;3&quot;&gt;<br>public class Configuration&lt;br&gt;<br>&amp;nbsp;&#123;&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;public static string MySetting&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;&#123;&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;get&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;&#123;&lt;br&gt;<br>&lt;/font&gt;</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad code display example - using &lt;font&gt; </dd><p class="ssw15-rteElement-CodeArea">&lt;code&gt;<br>public class Configuration&lt;br&gt;<br>&amp;nbsp;&#123;&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;public static string MySetting&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;&#123;&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;get&lt;br&gt;<br>&amp;nbsp;&amp;nbsp;&amp;nbsp;&#123;&lt;br&gt;<br>&lt;/code&gt;</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad code display example - using &lt;code&gt;</dd><p class="ssw15-rteElement-CodeArea">&lt;pre&gt;<br>public class Configuration<br>&#123;<br>public static string MySetting<br>&#123;<br>get<br>&#123;<br>&lt;/pre&gt;</p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good code display example - using &lt;pre&gt;<br></dd><p><b>Tip&#58;</b>&#160;Do not use auto-format (Ctrl-K, Ctrl-F) in Visual Studio when updating page with &lt;pre&gt; tags, or it will destroy all the code formatting. We have made a suggestion to Microsoft to fix this.<br></p>


