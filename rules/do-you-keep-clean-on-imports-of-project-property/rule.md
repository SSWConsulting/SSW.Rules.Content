---
type: rule
title: Do you keep clean on Imports of Project Property?
uri: do-you-keep-clean-on-imports-of-project-property
created: 2009-04-27T09:22:16.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <p>This is because IntelliSense lists will be harder to use and navigate with too many imports. For example if in VB.NET, Microsoft.VisualBasic would be a good item to have in the imports list, because it will be used in most areas of your application.</p>
<p>To remove all the default imports, load Project Property page and select Common properties - Imports. </p>
<img class="ms-rteCustom-ImageArea" alt="Imports VB" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/ImportsVB.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Using aliases with the Imports Statement</span>
<p>The Import statement makes it easier to access methods of classes by eliminating the need to explicitly type the fully qualified reference names. Aliases let you assign a friendlier name to just one part of a namespace.</p>
<p>For example, the carriage return-line feed sequence that causes a single piece of text to be displayed on multiple lines is part of the ControlChars class in the Microsoft.VisualBasic namespace. To use this constant in a program without an alias, you would need to type the following code&#58; </p>
<pre class="brush&#58;c-sharp;">    MsgBox(&quot;Some text&quot; &amp; Microsoft.VisualBasic.ControlChars.crlf _
    &amp; &quot;Some more text&quot;)</pre>
<p>Imports statements must always be the first lines immediately following any Option statements in a module. The following code fragment shows how to import and assign an alias to the Microsoft.VisualBasic.ControlChars namespace&#58;</p>
<pre class="brush&#58;c-sharp;">Imports CtrlChrs=Microsoft.VisualBasic.ControlChars</pre>
<span class="ms-rteCustom-FigureNormal">Future references to this namespace can be considerably shorter&#58;</span>
<pre class="brush&#58;c-sharp;">MsgBox(&quot;Some text&quot; &amp; CtrlChrs.crlf &amp; &quot;Some more text&quot;)</pre>
<p>If an Imports statement does not include an alias name, elements defined within the imported namespace can be used in the module without qualification. If the alias name is specified, it must be used as a qualifier for names contained within that namespace.</p>



