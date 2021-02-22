---
type: rule
archivedreason: 
title: Do you know how to create Azure resources?
guid: 007dd1f6-8ac6-4840-8f4f-a39c6f847880
uri: azure-resources-creating
created: 2020-10-06T00:13:27.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- do-you-know-how-to-create-azure-resources

---


<p>​We’ve been down this road before where developers had to be taught <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=a4ca7d22-069a-4727-b54a-a1cf1d5a5ef4">not to manually create tables and ​databases</a>. Now, in the cloud world, we’re saying the same thing again. Don’t manually create your Azure resources.​<br></p><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"><iframe width="750" height="422" src="https://www.youtube.com/embed/8E63s2QlbhA" frameborder="0"></iframe> </div><p>​<br><br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​Manually​​ Creating Resources<br></h3><p>This is the most common and the worst. This is bad because it requires manual effort to reproduce and leaves margin for human error.<br></p><p></p><ul><li>Create resources in Azure and not save a script<br></li></ul><p></p><dl class="badImage"><dt> 
      <img src="azure resources.gif" alt="create-azure-bad1.png" style="width:609px;" /> 
   </dt><dd>Figure: Bad Example – creating resources manually </dd></dl><h3 class="ssw15-rteElement-H3">Manually creating and saving the script<br></h3><p></p><p>Some people half solve the problem by manually creating and saving the script. This is also bad because it’s like eating ice cream and brushing your teeth – it doesn’t solve the 
   <b>health</b> problem.<br></p><dl class="badImage"><dt> 
      <img src="create-azure-bad2.png" alt="create-azure-bad2.png" style="width:750px;" /> 
   </dt><dd>Figure: Bad Example – Exporting your Resource Group as an ARM template defined in JSON<br><br></dd></dl><p></p><dl class="badImage"><dt> 
      <img src="create-azure-bad3.png" alt="create-azure-bad3.png" style="width:750px;" /> 
   </dt><dd>Figure: Warning - often templates don't work and need to be manually tweaked<br></dd></dl><ul><li> 
      <b>Warning:</b> The templates are crazy verbose<br></li></ul><p></p><p class="ssw15-rteElement-GreyBox">
      <strong>​Tip: </strong>​Save scripts in a folder called Azure​</p><p></p>​
<dl class="goodImage"><dt> 
      <img src="azure folder1.png" alt="create-azure-timepro.png" style="width:750px;height:410px;" /> 
   </dt><dd>Figure: Good example - However you generate your ARM template, save it in an Azure folder like this example (SSW TimePro)<br></dd></dl><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P">So if you aren't manually creating your Azure resources, what options do you have?<br></p><p class="ssw15-rteElement-P"><br></p><h3 class="ssw15-rteElement-H3">​Option A: Terraform<br></h3> 
<a href="https://www.terraform.io/docs/providers/azurerm/index.html">https://www.terraform.io/docs/providers/azurerm/index.html​</a><br>
<ul><li>It’s a great tool<br></li><li>Free for up to 5 users with limited features</li><li>Not recommended because: 
      <ul><li>Pulumi is better<br></li><li>Proprietary ‘HCL’ (Hashicorp Configuration Language) which is as bad as YAML<br></li></ul></li></ul><h3 class="ssw15-rteElement-H3">​Option B: Ansible</h3><p>
   <a href="https://www.ansible.com/">https://www.ansible.com</a></p><ul><li>Proprietary product owned by RedHat</li><li>First red flag – ‘Contact us for pricing’ – a toxic warning sign of their lack of transparency</li></ul><h3 class="ssw15-rteElement-H3">Option C: Bicep by Microsoft<br></h3><p> 
   <a href="https://github.com/Azure/bicep">https://github.com/Azure/bicep</a><br></p><ul><li>Experimental<br></li><li>Not a huge step forward from ARM templates</li><li>But is one to watch</li></ul><h3 class="ssw15-rteElement-H3">Option D: Farmer (Recommended)<br></h3><p> 
   <a href="https://compositionalit.github.io/farmer/">https://compositionalit.github.io/farmer​</a><br></p><ul><li>It's a great tool</li><li>Simply add a very short and readable F# project in your solution </li><li>Tip: The F# solution of scripts should be in a folder called .azure​</li></ul><p></p><dl class="goodImage"><dt> 
      <img src="goldie rules.png" alt="create-azure-good1.png" style="width:750px;height:1050px;" /> 
   </dt><dd>Figure: Good Example – using Farmer to define your ARM template in F# code<br></dd></dl><h3 class="ssw15-rteElement-H3">Option E: Pulumi (Recommended)<br></h3><p>​<a href="https://www.pulumi.com/">https://www.pulumi.com</a></p><ul><li>It's a great tool that uses real code (C#, TypeScript, Go, and Python) as infrastructure rather than JSON​/YAML<br></li><li>Abstracts the entire Azure REST API to the language of your choice (see above)<br></li><li>Includes a tool for converting your existing JSON ARM templates into code: <a href="https://www.pulumi.com/arm2pulumi/" target="_blank">Arm2Pulumi​</a><br></li><li>Free for individual developers (even for commercial use), but is a paid product for teams &gt; 1<br></li></ul><dl class="ssw15-rteElement-ImageArea">
   <img src="pulumi3.png" alt="pulimi1.png" style="margin:5px;width:750px;height:924px;" />
</dl><dd class="ssw15-rteElement-FigureGood">Figure: Good Example - Code from the Pulumi Azure NextGen provider demo​ with Azure resources defined in C#<br></dd><p class="ssw15-rteElement-P">
   <br>
</p><dl class="ssw15-rteElement-ImageArea">
   <img src="pulumi2.png" alt="pulumi2.png" style="margin:5px;width:750px;height:601px;" />
</dl><dd class="ssw15-rteElement-FigureGood">​​Figure: Good Example - From the console simply run 'pulumi up' to deploy your resources to Azure<br></dd><p class="ssw15-rteElement-P">
   <br>
</p><h3 class="ssw15-rteElement-H3"> What’s Mainstream?​</h3><p class="ssw15-rteElement-P">​​​It’s early days so 
   <a href="https://trends.google.com/trends/explore?q=azure%20pulumi%2cazure%20teraform%2cazure%20ansible%2cazure%20farmer%E2%80%8B">not much help (from Google trends)</a> yet.<br></p><dl class="image"><dt>
      <img src="google trends.png" alt="Screen Shot 2020-10-06 at 1.00.12 PM.png" style="width:750px;height:447px;" />
      <br>
   </dt><dd class="ssw15-rteElement-FigureNormal">​Figure: Google Trends shows that Terraform is the most searched for as it’s been around the longest and is well established<br></dd></dl><h3 class="ssw15-rteElement-H3">​General Tips<br></h3><ul><li>After you’ve made your changes, don’t forget to 
      <a href=/azure-resources-visualizing>visualize your new resources</a></li></ul><p>
   <br>
</p>

<br>


