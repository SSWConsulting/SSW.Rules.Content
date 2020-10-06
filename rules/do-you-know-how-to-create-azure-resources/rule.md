---
type: rule
archivedreason: 
title: Do you know how to create Azure resources?
guid: 007dd1f6-8ac6-4840-8f4f-a39c6f847880
uri: do-you-know-how-to-create-azure-resources
created: 2020-10-06T00:13:27.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 97
  title: Matt Goldman
related: []

---


<p>We’ve been down this road before where developers had to be taught&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=a4ca7d22-069a-4727-b54a-a1cf1d5a5ef4">not to manually create tables and in databases</a>. Now, in the cloud world, we’re saying the same thing again. Don’t manually create your Azure resources.​<br></p><p class="ssw15-rteElement-P">So what options do you have?​​</p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​Option A&#58; Manually​​<br></h3><p>This is the most common and the worst<br></p><p></p><ul><li>Create resources in Azure and not save a script<br></li></ul><p></p><dl class="badImage"><dt>
      <img src="/PublishingImages/create-azure-bad1.png" alt="create-azure-bad1.png" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Bad Example – creating resources manually </dd></dl><h3 class="ssw15-rteElement-H3">Option B&#58; Manually creating and saving the script (write ARM template by hand)​<br></h3><p></p><p>This is bad because it’s like eating ice cream and brushing your teeth – it doesn’t solve the 
   <b>health</b>&#160;problem.<br></p><dl class="badImage"><dt>
      <img src="/PublishingImages/create-azure-bad2.png" alt="create-azure-bad2.png" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Bad Example – Exporting your Resource Group as an ARM template</dd></dl><ul><li>Often the exported templates don’t work without manually tweaking them</li></ul><dl class="badImage"><dt>
      <img src="/PublishingImages/create-azure-bad3.png" alt="create-azure-bad3.png" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Figure&#58; Bad Example – Resource types could not be exported</dd></dl><ul><li>
      <b>Warning&#58;</b> The templates are crazy verbose<br></li></ul><dl class="goodImage"><dt>
      <img src="/PublishingImages/create-azure-timepro.png" alt="create-azure-timepro.png" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Good example - TimePro with the .azure folder<br></dd></dl><h3 class="ssw15-rteElement-H3">​Option C&#58; Using Terraform</h3>
<a href="https&#58;//www.terraform.io/docs/providers/azurerm/index.html">https&#58;//www.terraform.io/docs/providers/azurerm/index.html​</a><br> 
<ul><li>It’s a great tool</li><li>Free for up to 5 users with limited features</li><li>Not recommended because&#58; 
      <ul><li>Pulumi is better</li><li>Proprietary ‘HCL’ (Hashicorp Configuration Language) which is as bad as YAML​Option D&#58; Using Ansible<br></li></ul></li></ul><h3 class="ssw15-rteElement-H3">​Option D&#58; Using Ansible</h3><p> 
   <a href="https&#58;//www.ansible.com/">https&#58;//www.ansible.com</a></p><ul><li>Proprietary product owned by RedHat</li><li>First red flag – ‘Contact us for pricing’ – a toxic warning sign of their lack of transparency</li></ul><h3 class="ssw15-rteElement-H3">Option E&#58; Bicep<br></h3><p>
   <a href="https&#58;//github.com/Azure/bicep">https&#58;//github.com/Azure/bicep</a><br></p><ul><li>Microsoft’s own product</li><li>Not a huge step forward from ARM templates</li><li>But is one to watch</li></ul><h3 class="ssw15-rteElement-H3">Option F&#58; Using Farmer (Recommended)<br></h3><p>
   <a href="https&#58;//compositionalit.github.io/farmer/">https&#58;//compositionalit.github.io/farmer​</a><br><br></p><dl class="goodImage"><dt>
      <img src="/PublishingImages/create-azure-good1.png" alt="create-azure-good1.png" />
   </dt><dd>Figure&#58; Good Example – using Farmer to generate your ARM template</dd></dl><ul><li>
      <span style="background-color&#58;initial;">Simply add a very short and readable F# project in your solution&#160;</span></li><li>
      <span style="background-color&#58;initial;"><b>Tip&#58;</b> The F# solution of scripts should be in a folder called .azure<br></span></li></ul><h3 class="ssw15-rteElement-H3">Option G&#58; Using Pulumi (Recommended)</h3><p>​<a href="https&#58;//www.pulumi.com/">https&#58;//www.pulumi.com</a></p>​ 
<ul><li>It's a great tool (real code C#, TypeScript, Go, and Python as infrastructure, rather than JSON)</li><li>Abstracts the entire Azure REST API to the language of your choice (see above)</li><li>Free for individual developers (even for commercial use), but is a paid product for teams &gt; 1</li><li>When not to use Pulumi&#58; 
      <ul><li>When you work in a team &gt; 1<br></li></ul></li></ul><h3 class="ssw15-rteElement-H3"> What’s Mainstream?​</h3><p class="ssw15-rteElement-P">​​​It’s early days so 
   <a href="https&#58;//trends.google.com/trends/explore?q=azure%20pulumi%2cazure%20teraform%2cazure%20ansible%2cazure%20farmer%E2%80%8B">not much help (from Google trends)</a> yet.<br></p><dl class="image"><dt><img src="/PublishingImages/Screen%20Shot%202020-10-06%20at%201.00.12%20PM.png" alt="Screen Shot 2020-10-06 at 1.00.12 PM.png" style="width&#58;750px;" /></dt></dl>
<h3 class="ssw15-rteElement-H3">​General Tips<br></h3><ul><li>After you’ve made your changes, don’t forget to 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d494984e-5089-43e2-bc4d-917fd9248148">visualize your new resources</a><br></li><li>Save scripts in a folder called .azure​</li></ul>


