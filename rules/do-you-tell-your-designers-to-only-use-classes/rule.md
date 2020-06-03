---
type: rule
title: Do you tell your designers to only use classes?
uri: do-you-tell-your-designers-to-only-use-classes
created: 2013-04-10T21:08:06.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>In Sitefinity you can alter the appearance and content areas on your webpage using &quot;Layouts&quot;. These layouts are basically just Divs with sizes applied.</p> </span>

<dl class="image"><dt> 
      <img alt="Use classes only" src="/PublishingImages/sitefinity-class-only.jpg" /> 
   </dt><dd>Figure&#58; You have the ability to assign a Class to a Div only. No other customisations can be made</dd></dl><p>Additionally, Sitefinity will hard code the widths of the layout and there is no way to stop it.<br> The hack work around is to manually remove the widths via JQuery&#58;</p><div class="greyBox"><p>$(&quot;.sf_colsOut&quot;).css(&quot;width&quot;, &quot;&quot;);</p></div>


