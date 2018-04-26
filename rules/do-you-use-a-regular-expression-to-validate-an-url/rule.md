---
type: rule
title: Do you use a regular expression to validate an URL?
uri: do-you-use-a-regular-expression-to-validate-an-url
created: 2018-04-26T17:31:11.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> A regex is the best way to verify an URI.<br><br> </span>

<p class="ssw15-rteElement-CodeArea">public bool IsValidUri(string uri)<br>&#123;<br>try&#160;<br>&#123;&#160;<br>Uri testUri = new Uri(uri);&#160;<br>return true;&#160;<br>&#125;&#160;<br>catch (UriFormatException ex)<br>&#123;&#160;<br>return false;&#160;<br>&#125;&#160;<br>&#125;&#160;<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example of verifying URI​​​<br></dd><p class="ssw15-rteElement-CodeArea">public bool IsValidUri(string uri)&#160;<br>&#123;&#160;<br>// Return true if it is in valid Uri format.<br>return System.Text.RegularExpressions.Regex.IsMatch( uri,@&quot;^(http|ftp|https)&#58;//([^\/][\w-/&#58;]+\.?)+([\w- ./?/&#58;/;/\%&amp;=]+)?(/[\w- ./?/&#58;/;/\%&amp;=]*)?&quot;);&#160;<br>&#125;&#160;</p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good example of verifying URI&#160;<br></dd><p>You should have unit tests for it, see our&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx">Rules to Better Unit Tests</a>&#160;for more information.​<br><br></p>


