---
type: rule
title: Do you chose efficient anchor names?
uri: do-you-chose-efficient-anchor-names
created: 2016-08-05T19:57:36.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> These are the things you should consider when creating an anchor link&#58;<br> </span>

<ol><li><strong>Meaningful</strong>- When you use named anchors in a web page, use meaningful names. When you are sending the URL by email it helps indicate what you are talking about, and in addition, list numbers often change. An anchor like &quot;#13&quot; becomes incorrect when the order changes.</li>
                    <br>
                    <li><strong>Case sensitive</strong>- Are &quot;http&#58;//www.ssw.com.au/ssw/NETUG/DeveloperLinks.aspx<span style="background&#58;yellow;">#usergroups</span>&quot; and &quot;http&#58;//www.ssw.com.au/ssw/NETUG/DeveloperLinks.aspx<span style="background&#58;yellow;">#UserGroups</span>&quot; the same? The answer is &quot;no&quot;&#160;because they might be not case sensitive when they test them in IE, but are in other browsers. An efficient way of checking this is to run is to run <a href="/ssw/Standards/DeveloperGeneral/WebdevelopmentTools.aspx#BrokenLinks"> SSW Link Auditor</a> and fix the errors reported in the broken local links' section.<br></li>
                    <br>
                    <li><strong>No spacing</strong>- When you are defining an anchor name, make sure there are no spaces within the name. <br><br><dd class="ssw15-rteElement-FigureBad"> Bad&#58; &lt;a name=&quot;Some Anchor Name&quot;&gt; <br></dd><dd class="ssw15-rteElement-FigureGood"> Good&#58; &lt;a name=&quot;SomeAnchorName&quot;&gt; <br></dd></li>
                    <br>
                    <li><strong>Don't start with a #</strong>- When you are defining an anchor name you DO NOT use a #.<br>When you are referencing an anchor you DO use a #.<br>This is a common mistake&#160;because the # is used on the &quot;href&quot;.<br><br><dd class="ssw15-rteElement-FigureBad"> Bad&#58; &lt;a name=&quot;#SomeAnchorName&quot;&gt; <br></dd><dd class="ssw15-rteElement-FigureGood"> Good&#58; &lt;a name=&quot;SomeAnchorName&quot;&gt; <br></dd></li></ol><p class="ssw15-rteElement-YellowBorderBox">We have a program called <a href="https&#58;//www.ssw.com.au/ssw/codeauditor/" target="_blank">SSW Code Auditor</a> to check for #3 and #​4 on this rule.</p>​<br>


