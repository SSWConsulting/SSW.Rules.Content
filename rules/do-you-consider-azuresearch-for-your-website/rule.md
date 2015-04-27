---
type: rule
title: Do you consider AzureSearch for your website?
uri: do-you-consider-azuresearch-for-your-website
created: 2015-04-27T01:23:12.0000000Z
authors: []

---



<span class='intro'> <p>AzureSearch is <span style="line-height&#58;20.7999992370605px;">designed to work with Azure based data and&#160;runs on ElasticSearch.&#160;You may resist to choose this new service from the&#160;missing&#160;advanced search&#160;features </span>and what seems to be an&#160;expensive&#160;monthly fee ($250 as of today). If so, follow this rule&#58;</p><p>Consider AzureSearch if your Azure website&#58;<br></p><ol><li><span style="line-height&#58;1.6;">Uses SQL Azure (or other Azure based data such as DocumentDB), and</span><br></li><li><span style="line-height&#58;1.6;"><span style="line-height&#58;20.7999992370605px;">Does not require advanced search features.</span><br></span></li></ol><div><div>Keep in mind that 1)&#160;hosting of a&#160;full-text search service (such as&#160;ElasticSearch) will cost&#160;you labour for&#160;setting up&#160;and maintaining the infrastructure, and 2)&#160;a single Azure VM can cost you up to $450.&#160;Do not drop AzureSearch unless the&#160;missing&#160;features&#160;are&#160;absolutely necessary.</div></div> </span>

<p> </p><p class="ssw15-rteElement-P">​ ​​​<br></p><p class="ssw15-rteElement-P"><img src="/SoftwareDevelopment/Rules-to-Better-Azure/SiteAssets/Pages/Consider-AzureSearch-for-your-Azure-website/Untitled2.png" alt="Untitled2.png" style="margin&#58;5px;width&#58;650px;" /><br></p><dd class="ssw15-rteElement-FigureGood"> Figure&#58; Good Example - Azure website using AzureSearch for what it can deliver today </dd><p><br></p><p>​​​​<img src="/SoftwareDevelopment/Rules-to-Better-Azure/SiteAssets/Pages/Consider-AzureSearch-for-your-Azure-website/Untitled.png" alt="Untitled.png" style="margin&#58;5px;width&#58;650px;" /><br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Azure website using ElasticSearch for a simple search that AzureSearch can do</dd>


