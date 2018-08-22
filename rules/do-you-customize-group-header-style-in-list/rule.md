---
type: rule
title: Do you customize group header style in list
uri: do-you-customize-group-header-style-in-list
created: 2018-08-22T06:07:04.0000000Z
authors:
- id: 9
  title: William Yin

---



<span class='intro'> By default, the group header&#160;of a&#160;list shows bigger font size only&#160;on modern UI, this is fine for one level group. However, if you have two level groups, it could be better to show different header styles between level one and level two group headers.<br> </span>

<p>​To implement this, you will need to inject a custom style to first level group header.​ e.g.</p><p class="ssw15-rteElement-CodeArea">​​.ms-GroupedList-group &gt; .ms-GroupHeader .ms-GroupHeader-title &#123;<br>&#160; &#160; font-weight&#58;600;<br>&#125;​</p><p><em></em></p><p>If you want to make this style available in a &quot;site collection&quot; scope (aka apply to all lists and libraries in a site collection), use a &quot;SharePoint Extension&quot; is not a bad option. Read more details at&#160;<a href="https&#58;//docs.microsoft.com/en-us/sharepoint/dev/spfx/extensions/get-started/serving-your-extension-from-sharepoint">https&#58;//docs.microsoft.com/en-us/sharepoint/dev/spfx/extensions/get-started/serving-your-extension-from-sharepoint</a><br>&#160;<br></p><p>Once deployed, you should be able to see a header style like the below&#58;<br></p><dl class="ssw15-rteElement-ImageArea"><img src="/SiteAssets/do-you-customize-group-header-style-in-list/level%20one%20gorup%20header%20bold.png" alt="level one gorup header bold.png" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Level one group header is bold<br></dd><p><br></p>


