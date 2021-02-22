---
type: rule
archivedreason: 
title: Do you consider AzureSearch for your website?
guid: 31fba456-e962-4c9b-8ee4-9de5d3cac8fd
uri: do-you-consider-azuresearch-for-your-website
created: 2015-04-27T01:23:12.0000000Z
authors: []
related: []
redirects: []

---


<p>AzureSearch is <span style="line-height:20.7999992370605px;">designed to work with Azure based data and runs on ElasticSearch. It is still NEW as of today (27/4/2015) and doesn't expose all the advanced search features. You may resist to choose it as your search engine from the missing features </span>and what seems to be an expensive monthly fee ($250 as of today). If this is the case, follow this rule:</p><p><strong>Consider AzureSearch if your website</strong>:<br></p><ol><li><span style="line-height:1.6;">Uses SQL Azure (or other Azure based data such as DocumentDB), and</span><br></li><li><span style="line-height:1.6;"><span style="line-height:20.7999992370605px;">Does not require advanced search features.</span><br></span></li></ol><div><span style="line-height:20.7999992370605px;"><br></span></div><div><p><strong>Consider <strong>ElasticSearch </strong>if your website</strong>:<br></p><ol><li><span style="line-height:1.6;"> Requries advance search features that aren't supported by AzureSearch</span><br></li></ol><div><span style="line-height:20.7999992370605px;"><br></span></div>Keep in mind that 1) hosting of a full-text search service costs you labour to set up and maintain the infrastructure, and 2) a single Azure VM can cost you up to $450. So do not drop AzureSearch option unless the missing features are absolutely necessary for your site</div><div><div><br></div><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p> </p><p class="ssw15-rteElement-P">​ ​​​<br></p><p class="ssw15-rteElement-P">​​​​<img src="9c0754_Untitled2.png" alt="Untitled2.png" style="margin:5px;width:650px;" /><br></p><dd class="ssw15-rteElement-FigureGood"> Figure: Good Example - Azure website using AzureSearch for what it can deliver today </dd><p><br></p><p>​​​​<img src="Untitled.png" alt="Untitled.png" style="margin:5px;width:650px;" /><br></p><dd class="ssw15-rteElement-FigureBad">Figure: Bad Example - Azure website using ElasticSearch for a simple search that AzureSearch can do</dd>


