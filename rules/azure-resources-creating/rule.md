---
type: rule
title: Do you know how to create Azure resources?
uri: azure-resources-creating
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
  - do-you-know-how-to-create-azure-resources
created: 2020-10-06T00:13:27.000Z
archivedreason: null
guid: 007dd1f6-8ac6-4840-8f4f-a39c6f847880
---

We’ve been down this road before where developers had to be taught not to manually create databases and tables. Now, in the cloud world, we’re saying the same thing again. **Don’t manually create your Azure resources.**

<!--endintro-->

### Manually Creating Resources

This is the most common and the worst. This is bad because it requires manual effort to reproduce and leaves margin for human error.

* Create resources in Azure and not save a script

::: bad  
![Figure: Bad Example – creating resources manually](azure resources.gif)  
:::

### Manually creating and saving the script

Some people half solve the problem by manually creating and saving the script. This is also bad because it’s like eating ice cream and brushing your teeth – it doesn’t solve the **health** problem.

::: bad  
![Figure: Bad Example – Exporting your Resource Group as an ARM template defined in JSON](create-azure-bad2.png)  
:::

::: bad  
![Figure: Warning - The templates are crazy verbose. They often don't work and need to be manually tweaked](create-azure-bad3.png)  
:::

::: greybox
 **Tip:** Save scripts in a folder called Azure  
:::

::: good  
![Figure: Good example - However you generate your ARM template, save it in an Azure folder like this example (SSW TimePro)](azure folder1.png)  
:::

So if you aren't manually creating your Azure resources, what options do you have?

### Option A: Farmer

[https://compositionalit.github.io/farmer](https://compositionalit.github.io/farmer/)


* It makes creating ARM templates easier 
* It's a great tool
* Simply add a very short and readable F# project in your solution
* Tip: The F# solution of scripts should be in a folder called Azure

`youtube: https://www.youtube.com/embed/8E63s2QlbhA`
**Figure: Farmer was our favourite until Bicep was supported by Microsoft**

### Option B: Bicep by Microsoft (recommended)

[https://github.com/Azure/bicep](https://github.com/Azure/bicep)

* Is free and fully supported by Microsoft
* Has ['az' command line integration](https://docs.microsoft.com/en-us/cli/azure/bicep?view=azure-cli-latest)
* Compiles into an ARM template for deployment
* Much simpler syntax than ARM
* Handles dependencies automatically
* Easiest option if you are deploying Azure App Service or Azure Functions

More info: [Project Bicep – Next Generation ARM Templates](https://devblogs.microsoft.com/devops/project-bicep-next-generation-arm-templates/)

::: good
![Figure: Good Example - Code from the Bicep using Visual Studio Code Extension](Bicep.png)
:::

### Option C: Enterprise configuration management $$$
The other option when moving to an automated Infrastructure as Code (IaC) solution is to move to a paid provider like [Pulumi](https://www.pulumi.com) or [Terraform](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs). These solutions are ideal if you are using multiple cloud providers or if you want to control the software installation as well as the infrastructure. 

* They're both great tools
* Both have free options for limited numbers of users
* Pulumi is better because:
    * Terraform's proprietary ‘HCL’ (Hashicorp Configuration Language), which is as bad as YAML
    * It's a great tool that uses real code (C#, TypeScript, Go, and Python) as infrastructure rather than JSON/YAML

::: good
![Figure: Good Example - Code from the Pulumi Azure NextGen provider demo with Azure resources defined in C#](pulumi3.png)
:::

::: good
![Figure: Good Example - From the console simply run 'pulumi up' to deploy your resources to Azure](pulumi2.png)
:::

::: info
**Tip:** After you’ve made your changes, don’t forget to [visualize your new resources](/azure-resources-visualizing)
:::
