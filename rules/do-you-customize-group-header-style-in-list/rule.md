---
type: rule
archivedreason: 
title: Do you customize group header style in list
guid: 2858ed44-275e-4129-884b-420d967a13d4
uri: do-you-customize-group-header-style-in-list
created: 2018-08-22T06:07:04.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects: []

---


By default, the group header of a list shows bigger font size only on modern UI, this is fine for one level group. However, if you have two level groups, it could be better to show different header styles between level one and level two group headers.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>​To implement this, you will need to inject a custom style to first level group header.​ e.g.</p><p class="ssw15-rteElement-CodeArea">​​.ms-GroupedList-group &gt; .ms-GroupHeader .ms-GroupHeader-title {<br>    font-weight:600;<br>}​</p><p><em></em></p><p>If you want to make this style available in a "site collection" scope (aka apply to all lists and libraries in a site collection), use a "SharePoint Extension" is not a bad option. Read more details at <a href="https://docs.microsoft.com/en-us/sharepoint/dev/spfx/extensions/get-started/serving-your-extension-from-sharepoint">https://docs.microsoft.com/en-us/sharepoint/dev/spfx/extensions/get-started/serving-your-extension-from-sharepoint</a><br> <br></p><p>Once deployed, you should be able to see a header style like the below:<br></p><dl class="ssw15-rteElement-ImageArea"><img src="level one gorup header bold.png" alt="level one gorup header bold.png" style="margin:5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Level one group header is bold<br></dd><p><br></p>


