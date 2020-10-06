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


<p>We’ve been down this road before where developers had to be taught&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=a4ca7d22-069a-4727-b54a-a1cf1d5a5ef4">not to manually create tables and in databases</a>. Now, in the cloud world, we’re saying the same thing again. Don’t manually create your Azure resources.​<br></p><p class="ssw15-rteElement-P">So what options do you have?​​</p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​Option A&#58; Manually​​<br></h3><ul><li>Create resources in Azure and not save a script</li><li>This is the most common and the worst</li></ul><dl class="badImage"><dt><img src="/PublishingImages/create-azure-bad1.png" alt="create-azure-bad1.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Bad Example – creating resources manually </dd></dl><h3 class="ssw15-rteElement-H3">Option B&#58; Manually creating and saving the script (write ARM template by hand)​<br></h3><p></p><ul><li>This is bad because it’s like eating ice cream and brushing your teeth – it doesn’t solve the problem</li></ul><dl class="badImage"><dt><img src="/PublishingImages/create-azure-bad2.png" alt="create-azure-bad2.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Bad Example – Exporting your Resource Group as an ARM template</dd></dl><ul><li>Often the exported templates don’t work without manually tweaking them</li></ul><dl class="badImage"><dt><img src="/PublishingImages/create-azure-bad3.png" alt="create-azure-bad3.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Figure&#58; Bad Example – Resource types could not be exported</dd></dl><ul><li>The templates are crazy verbose</li><li>Save scripts in a folder called .azure</li></ul><dl class="image"><dt><img src="/PublishingImages/create-azure-timepro.png" alt="create-azure-timepro.png" style="width&#58;750px;" /></dt><dd>Figure&#58; TimePro with the .azure folder </dd></dl><h3 class="ssw15-rteElement-H3">​Option C&#58; Using Terraform</h3><ul><li>It’s a great tool</li><li>Free for up to 5 users with limited features</li><li>Not recommended because&#58; 
      <ul><li>Pulumi is better</li><li>Proprietary ‘HCL’ (Hashicorp Configuration Language) which is as bad as YAML</li><li>​https&#58;//www.terraform.io/docs/providers/azurerm/index.html</li></ul></li></ul><h3 class="ssw15-rteElement-H3">​Option D&#58; Using Ansible</h3><ul><li>Proprietary product owned by RedHat</li><li>First red flag – ‘Contact us for pricing’ – a toxic warning sign of their lack of transparency</li><li>
      <a href="https&#58;//www.ansible.com/">https&#58;//www.ansible.com</a><br></li></ul><h3 class="ssw15-rteElement-H3">Option E&#58; Bicep</h3><ul><li>Microsoft’s own product</li><li>Not a huge step forward from ARM templates</li><li>But is one to watch</li></ul><h3 class="ssw15-rteElement-H3">Option F&#58; Using Farmer (Recommended)</h3><dl class="goodImage"><dt><img src="/PublishingImages/create-azure-good1.png" alt="create-azure-good1.png" /></dt><dd>Figure&#58; Good Example – using Farmer to generate your ARM template</dd></dl><ul><li>https&#58;//compositionalit.github.io/farmer/</li><li>Put an F# project in your solution</li><li>Save scripts in a folder called .azure</li></ul><h3 class="ssw15-rteElement-H3">Option G&#58; Using Pulumi (Recommended)</h3><ul><li>It’s a great tool (real code C#, TypeScript, Go, and Python as infrastructure, rather than JSON)</li><li>Abstracts the entire Azure REST API to the language of your choice (see above)</li><li>Free for individual developers (even for commercial use), but is a paid product for teams {gtHTMLChar} 1</li><li>When not to use Pulumi&#58; 
      <ul><li>When you work in a team {gtHTMLChar} 1<br></li></ul></li><li>​<a href="https&#58;//www.pulumi.com/">https&#58;//www.pulumi.com</a><br></li></ul><h3 class="ssw15-rteElement-H3"> What’s Mainstream?​</h3><p class="ssw15-rteElement-P">​​​It’s early days so 
      <a href="https&#58;//trends.google.com/trends/explore?q=azure%20pulumi%2cazure%20teraform%2cazure%20ansible%2cazure%20farmer%E2%80%8B">not much help (from Google trends)</a> yet.</p><p><b>Tip&#58;</b> After you’ve made your changes, don’t forget to 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=d494984e-5089-43e2-bc4d-917fd9248148">visualize your new resources</a>.</p>



