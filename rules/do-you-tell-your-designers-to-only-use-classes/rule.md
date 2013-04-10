---
type: rule
archivedreason: 
title: Do you tell your designers to only use classes?
guid: 516aac5a-c691-4e58-af66-a87f8105e44a
uri: do-you-tell-your-designers-to-only-use-classes
created: 2013-04-10T21:08:06.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


<p>In Sitefinity you can alter the appearance and content areas on your webpage using &quot;Layouts&quot;. These layouts are basically just Divs with sizes applied.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt> 
      <img alt="Use classes only" src="/WebSites/RulesToBetterSitefinity/PublishingImages/sitefinity-class-only.jpg" /> 
   </dt><dd>Figure&#58; You have the ability to assign a Class to a Div only. No other customisations can be made</dd></dl><p>Additionally, Sitefinity will hard code the widths of the layout and there is no way to stop it.<br> The hack work around is to manually remove the widths via JQuery&#58;</p><div class="greyBox"><p>$(&quot;.sf_colsOut&quot;).css(&quot;width&quot;, &quot;&quot;);</p></div>


