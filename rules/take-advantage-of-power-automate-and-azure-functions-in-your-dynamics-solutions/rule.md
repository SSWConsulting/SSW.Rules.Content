---
type: rule
archivedreason: 
title: Do you take advantage of Power Automate and Azure Functions in your Dynamics solutions?
guid: 9a044ebd-5619-4952-9186-67c5981c1c59
uri: take-advantage-of-power-automate-and-azure-functions-in-your-dynamics-solutions
created: 2020-06-29T20:18:00.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
- do-you-take-advantage-of-power-automate-and-azure-functions-in-your-dynamics-solutions

---


<p class="ssw15-rteElement-P">Dynamics has come a long way since the early days and now sits under ​Power Platform. So why not take advantage of all the capabilities to make Dynamics sing. Prior to Power Automate and Azure Functions, a Dynamics developer would use a combination of Workflows (synchronous and asynchronous) and Plugins to extend the system.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">​​Power Automate</h3><p>While there is are still some limited scenarios for using Workflows (Power Automate doesn't yet support synchronous execution) and Plugins (again synchronous support), Microsoft is shepherding developers toward Microsoft Flow (Power Automate) for automation tasks, and this is a great thing.<br></p><p>Case for Power Automate instead of regular Dynamics workflows:</p><ul><li>A massive number of 
      <a href="https://australia.flow.microsoft.com/en-us/connectors/%22%20%5co%20%22https://australia.flow.microsoft.com/en-us/connectors/">connectors</a> from Act! to Zendesk and everything in between</li><li>Can't find the connector you need? No problem, create a 
      <a href="https://docs.microsoft.com/en-us/connectors/custom-connectors/define-blank%22%20%5co%20%22https://docs.microsoft.com/en-us/connectors/custom-connectors/define-blank">Custom Connector</a> or just use a generic HTTP request</li><li>Intuitive debugging experience, see errors immediately, fix and re-run failed flow</li><li>Visually much nicer UI compared to Dynamics Workflow experience</li></ul><p>The case against Power Automate instead of regular Dynamics workflows:</p><ul><li>No real-time workflow support, so if real-time workflows are needed then Dynamics workflows are the only solution for now</li></ul><h3 class="ssw15-rteElement-H3">Azure Functions<br></h3><p>Previously when there was a more complex operation that needed to happen, for example, a complex scoring requirement for customer sentiment this logic would be contained in a plugin. Most Dynamics developers avoid writing plugins as they're a huge time sink, difficult to debug, and just not cool. The cool kids write the complex logic in Azure Functions.</p><p>The case for Azure Functions instead for Dynamics plugins:</p><ul><li>The developer requires zero Dynamics experience to implement an Azure Function (useful to have Dynamics experience but it's not an impediment)<br></li><li>An Azure Function is a WebAPI endpoint and can be called by other applications<br></li><li>Very smooth debugging experience<br></li><li>Application Insights built-in</li><li>The Dynamics layer can be abstracted away, Azure Function can implement the logic only</li><li>Power Automate can sit in the middle of Dynamics and the Azure Function as the glue layer</li></ul><p>The case against Azure Function instead of regular Dynamics Plugins:</p><ul><li>Plugins can register against many Pre and Post events whereas an Azure Function is a WebAPI endpoint</li><li>Azure Functions are a 
      <a href="https://azure.microsoft.com/en-au/pricing/calculator/%22%20%5co%20%22https://azure.microsoft.com/en-au/pricing/calculator/">paid</a> Azure service, while extremely cost-effective, it is still an additional cost <br></li></ul><dl class="image"><dt>
      <img src="dynamics-workflow-editor.png" alt="dynamics-workflow-editor.png" style="width:750px;" /></dt><dd>Figure: Dynamics Workflow Editor</dd></dl><dl class="image"><dt><img src="flow-editor.png" alt="flow-editor.png" /></dt><dd>Figure: Flow Editor</dd></dl>​ 


