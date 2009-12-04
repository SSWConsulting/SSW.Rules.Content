---
type: rule
archivedreason: 
title: Do you make your projects regenerated easily?
guid: 53973958-2e13-4328-a323-db702f6084f1
uri: do-you-make-your-projects-regenerated-easily
created: 2009-06-09T06:43:07.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>
<p>Code generators can be used to generate whole Windows and Web interfaces, as well as data access layers and frameworks for business layers, making them an excellent time saver. However making the code generators generate your projects for the first time takes much time and involves lots of configurations.</p>
<p>In order to make it easier to do the generation next time, we recommend you putting the command line of operations into a file called &quot;_Regenerate.bat&quot;. When you want to generate it next time, just run the bat file and all things are done in a blink.</p>
<dl class="code">
<dt><pre>cs D&#58;\DataDavidBian\Personal\New12345\NetTiers.csp</pre></dt>
<dd>Figure&#58; An example of command line of Code Smith for NorthWind</dd></dl>
<p>Thus &quot;_Regenerate.bat&quot; file must exist in your projects (of course so must other necessary resources).</p>
<dl class="goodImage">
<dt><img style="border-right&#58;0px solid;border-top&#58;0px solid;border-left&#58;0px solid;border-bottom&#58;0px solid;" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/RegenerateBat.jpg" border="0" /></dt>
<dd>Figure&#58; Good - Have _Regenerate.bat in the solution</dd></dl>


