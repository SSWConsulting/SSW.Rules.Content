---
type: rule
tips: ""
title: Do you pick the best Large Language Model for your project?
seoDescription: When choosing an AI model for your application, it's crucial to
  try out different Large Language Models (LLMs) before committing. Learn how to
  do this efficiently with platforms like GitHub Models.
uri: choosing-large-language-models
authors:
  - title: ""
guid: e6891815-5e9b-4626-a1f7-42f13ce53aec
---
When building an AI-powered solution, developers will inevitably need to choose which Large Language Model (LLM) to use. Many powerful models exist (Llama, GPT-4o, and Mistral), and they are always changing and subject to varying levels of news and hype.

When choosing one for a project, it can be hard to know which to pick, and if you're making the right choice - being wrong could cost valuable performance and UX points.

Because different LLMs are good at different things, it's essential to test them your specific use case to find which is the best.

Fortunately, there exist good tools to do this **for free**.
`youtube: https://www.youtube.com/embed/iXmf6UDo404?si=LjRyiaygh28dhVlV`
**Video: Choosing the Right AI Model? GitHub Models Makes It Easy! | Isaac Lombard & Caleb Williams | Rules
 (3 min)**

<!--endintro-->

## The challenge of trying out AI models

Many AI providers charge per API call, making it expensive to experiment with different models.

* **Decision Fatigue** There's  a large number of Language models to choose from. The market size is expected to reach 13.52 billion US dollars by 2029.
* **Different implementations** specific to the service provider may create some implementation overhead when adding a model to your application.
* **Fine tuning** each model to get the best result might also be necessary.
* **Cost accumulates rapidly** when testing AI integration, particularly with large prompts or frequent calls.

## AI Model Hubs & LLM Evaluation Platforms

These platforms simplify testing and deploying different AI models from a variety of service providers, helping developers make informed decisions and experiment using different models in their application for testing. Some of these allow developers to test model responses interactively in a browser.

#### Azure AI Foundry (Recommended for production)

- Provides access to a variety of foundation models from different providers.
- Allows side-by-side evaluation of models within the Azure ecosystem.
Enables fine-tuning and optimization for specific business needs.

#### GitHub Models (Recommended for development)

- **Free offering, rate-limited for development purposes.**
- Easy Model Switching – Change models with a single API parameter using the Azure AI Inference library.
- Flexible Model Choices – Select larger models for power or compressed models for efficiency.
- Broad Ecosystem – GitHub Models simplifies testing and selecting the best LLMs.

##### GroqCloud Playground

- Free, rate-limited API.
- Provides a low-latency inference environment for running various LLMs.
- Allows developers to test model responses interactively in a browser.
- Focuses on efficiency and performance, making it ideal for real-time applications.

#### AWS SageMaker AI

- Supports training, deploying, and managing LLMs at scale.
- Offers built-in model evaluation and cost management features.
- Enables model fine-tuning and hosting for enterprise AI solutions.



**[Open AI Playground](https://platform.openai.com/playground/chat?models=gpt-4o)**

**Pros**

* Free for use
* Easy to switch between models
* Provides boilerplate code to get 
* Provides multiple 
  you up and running

**Cons**

* Start incurring costs per API call as soon as you integrate with your code
* Limited to Open AI's language models

**[GroqCloud Playground](https://console.groq.com/playground)**

**Pros**: 

* Support for different models
* Provides API keys
* Includes a [playground](https://console.groq.com/playground) for tweaking different language  model parameters 

**Cons**:

* Limited language model support compared to GitHub Models (i.e. no support for DeepSeek)

**[LM Studio](https://lmstudio.ai/)**

**Pros**

* There are no additional costs involved with using the language model

**Cons**

* Hardware costs for running a language model are high 
* You won't be able to run the full array of models available to you due to compute requirements
* You need to download language models individually before using them

**[GitHub Models](https://github.com/marketplace/models/) (Recommended)**

GitHub Models provides an ecosystem where developers can try out a wide variety of LLMs in one place, including (but not limited to):

* Open AI GPT-4o
* OpenAI GPT-4o mini
* Phi-3
* Phi-3.5
* Phi-4
* AI21 Jamba
* Codestral
* Cohere Command R
* DeepSeek-R1
* Llama-3
* Meta-llama-3
* Ministral
* Mistral

GitHub Models supports a large amount of language models within the same ecosystem. The development cost of switching from one model to another is minimal, assuming you're using the Azure AI inference API. Switching from one model to another is as simple as changing an API parameter. Your code implementation can stay the same.

You have the option to choose between larger or more compressed language models which allows you to experiment by submitting prompts with more or less compressed language models to determine whether that particular model will provide the best value for your scenario. For example, you may be building a chatbot and find that GPT 4o mini provides suitable responses and that you don't need to invest in the extra compute costs involved with running a larger model.

By providing a broad ecosystem of Large Language Models to choose from GitHub Models provides an excellent interface for figuring out which language models are suitable for specific tasks. This is useful for scenarios where you need to choose a broad range of specialized Language Models, such as using [Semantic Kernel](https://www.ssw.com.au/rules/use-semantic-kernel/)

###### Deploying to production

Once you've identified the best model for your needs, GitHub Models simplifies deployment. You can:

1. Generate a **production key** for your app.
2. Start incurring costs **only when you go live**.

This approach allows you to make an informed decision before committing financially, ensuring you're using the right AI model for your application.

## Conclusion

Before selecting an AI model, **test multiple options to evaluate quality, cost, and ease of integration**. Using platforms like GitHub Models can help you explore prototype quickly, experiment with different propts and parameters, and engineer an AI solution **for free**.
