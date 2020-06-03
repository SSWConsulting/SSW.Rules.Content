---
type: rule
title: 'Do you avoid using mailto: on your website?'
uri: do-you-avoid-using-mailto-on-your-website
created: 2016-11-16T17:15:31.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Don't ever display valid individual email addresses or mailto&#58;'s on a website. Nasty people on the web have created &quot;Email Harvesting&quot; tools. These programs search public areas on the Internet to compile, capture, or otherwise &quot;harvest&quot; lists of email addresses from web pages, newsgroups, and chat rooms. Any email address that is spelled out can be captured and therefore gets attacked with spam.<br></p><p>The best way to avoid it is not to display valid individual email addresses in text format (especially in the form of &quot;mailto&#58;&quot;) on your website.&#160;</p> </span>

<p>​​<br></p><p class="ssw15-rteElement-CodeArea">e.g. FirstnameSurname@ssw.com.au&#160;</p><dd class="ssw15-rteElement-FigureBad"> Figure&#58; Bad way&#160;- normal email address in text format<br></dd><h3 class="ssw15-rteElement-H3">&#160;Better way&#58; encryption technique&#160;</h3><ol><li>Store email addresses in the web.config file<br></li><p class="ssw15-rteElement-CodeArea">&lt;configuration&gt; <br>&lt;appSettings&gt; <br>&lt;add key=&quot;SampleEncodedEmailAddress&quot; value=&quot;David@sample.com.au&quot; /&gt; ...&lt;/appSettings&gt; &lt;/configuration&gt;</p><li>Encode them on the server using the BitConverter class&#160;<br></li><p class="ssw15-rteElement-CodeArea">Dim email As String = ConfigurationSettings.AppSettings(&quot;SampleEncodedEmailAddress&quot;) Application(&quot;SampleEncodedEmailAddress&quot;) = BitConverter.ToString( _ ASCIIEncoding.ASCII.GetBytes(email)).Replace(&quot;-&quot;, &quot;&quot;)</p><li>Decode on the client with a JavaScript function in the JavaScript<br></li><p class="ssw15-rteElement-CodeArea">&lt;a id=&quot;linkContact&quot; href=&quot;javascript&#58;sendEmail('44617669644073616D706C652E636F6D2E6175')&quot;&gt;CONTACT David&lt;/a&gt;​<br></p></ol><p class="ssw15-rteElement-YellowBorderBox">We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.</p><p>​<br></p>


