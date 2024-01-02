---
type: rule
title: Do you use Semantic Kernel?
uri: use-semantic-kernel
authors:
  - title: Jack Reimers
    url: https://www.ssw.com.au/people/jack-reimers 
created: 2023-09-27T12:00:00.000Z
guid: 468db2b2-f5a8-40dc-8979-bb86a382d93b
---

There's lots of awesome AI tools being released, but combining these can become very hard as an application scales.  
Semantic Kernel can solve this problem by orchestrating all our AI services for us.

<!--endintro-->

### What is Semantic Kernel?
Semantic Kernel is an open source SDK developed by Microsoft for their Copilot range of AI tools.  
It acts as an orchestration layer between an application and any AI services it may consume, such as the OpenAI API or Azure OpenAI, removing the need to write boilerplate code to use AI.

[Microsoft - What is Semantic Kernel?](https://learn.microsoft.com/en-us/semantic-kernel/overview/)  
[Semantic Kernel - GitHub Repo](https://github.com/microsoft/semantic-kernel)

### Why use Semantic Kernel?
Semantic Kernel offers many benefits over manually setting up your AI services.

* Common AI abstractions
  * Resistant to API changes
  * Services can be easily swapped (i.e. from Azure OpenAI to OpenAI API or vice versa) 
* Faster development time
* Easier maintenance

Using Semantic Kernel, it's easy to set up a basic console chat bot in under 15 lines of code!

```cs
using Microsoft.SemanticKernel;

const string endpoint = Environment.GetEnvironmentVariable("AZUREOPENAI_ENDPOINT")!;
const string key = Environment.GetEnvironmentVariable("AZUREOPENAI_API_KEY")!;
const string model = "GPT35Turbo";

var kernel = Kernel.Builder
    .WithAzureChatCompletionService(model, endpoint, key)
    .Build();

while (true)
{
    Console.WriteLine("Question: ");
    Console.WriteLine(await kernel.InvokeSemanticFunctionAsync(Console.ReadLine()!, maxTokens: 2000));
    Console.WriteLine();
}
```

For a more in depth walkthrough, please see [Stephen Toub's article](https://devblogs.microsoft.com/dotnet/demystifying-retrieval-augmented-generation-with-dotnet/).
