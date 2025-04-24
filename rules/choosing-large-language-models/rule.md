---
type: rule
title: Do you pick the best Large Language Model for your project?
seoDescription: When choosing an AI model for your application, it's crucial to
  try out different Large Language Models (LLMs) before committing. Learn how to
  do this efficiently with platforms like GitHub Models.
uri: choosing-large-language-models
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/ulysses-maclaren
  - title: Caleb Williams
    url: https://www.ssw.com.au/people/caleb-williams
  - title: Isaac Lombard
    url: https://www.ssw.com.au/people/isaac-lombard
  - title: Eddie Kranz
    url: https://www.ssw.com.au/people/eddie-kranz
  - title: Luke Cook
    url: https://www.ssw.com.au/people/luke-cook
  - title: Lewis Toh
    url: https://www.ssw.com.au/people/lewis-toh
guid: e6891815-5e9b-4626-a1f7-42f13ce53aec
---

When building an AI-powered solution, developers will inevitably need to choose which Large Language Model (LLM) to use. Many powerful models exist (Llama, GPT, Gemini, Mistral, Grok, DeepSeek, etc.), and they are always changing and subject to varying levels of news and hype.

When choosing one for a project, it can be hard to know which to pick, and if you're making the right choice - being wrong could cost valuable performance and UX points.

Because different LLMs are good at different things, it's essential to test them on your specific use case to find which is the best.

<!--endintro-->

`youtube: https://www.youtube.com/embed/sVELvhGdSfs?si=KdSIZiLbwaxPT3MP`
**Video: Choosing the Right AI Model? GitHub Models Makes It Easy! | Isaac Lombard & Caleb Williams | Rules (3 min)**

## Challenges in Implementing AI

* **Decision fatigue** - There's  an overwhelming number of Language Models to choose from
* **Different implementations** - Not all models use the same libraries
* **Tweaking parameters** - To get the best result involves testing different parameters such as the temperature (creativity), token limit, and more
* **Cost accumulates rapidly** - Costs from API calls during testing can accumulate, particularly with large prompts or frequent calls

Ultimately you need to test against different models to find one that fits your use case.

## AI Model Hubs - Experiment with different models

These platforms simplify testing and deploying different AI models from a variety of service providers, helping developers make informed decisions. Some of these allow developers to test model responses interactively in a browser with configurable parameter settings.

### [Azure AI Foundry](https://ai.azure.com/) (⭐ Recommended for Production)

* Provides access to a variety of foundation models from different providers
* Allows side-by-side evaluation of models within the Azure ecosystem
* Enables fine-tuning and optimization for specific business needs

### [GitHub Models](https://github.com/marketplace/models) (⭐ Recommended for Development)

* **Free offering, rate-limited for development purposes.**
* Easy Model Switching – Change models with a single API parameter using the Azure AI Inference library
* Flexible Model Choices – Select larger models for power or compressed (e.g. distilled or quantized) models for efficiency
* Broad Ecosystem – GitHub Models simplifies testing and selecting the best LLMs
* Available models include models from...

  * OpenAI (GPTs)
  * Microsoft (Phi)
  * Meta (Llama)
  * and more...

### [AWS SageMaker AI](https://aws.amazon.com/sagemaker/)

* Supports training, deploying, and managing LLMs at scale
* Offers built-in model evaluation and cost management features
* Enables model fine-tuning and hosting for enterprise AI solutions

### Other tools to compare models

#### [GroqCloud Playground](https://console.groq.com/playground)

* Free, rate-limited API and browser tool
* Provides a low-latency inference environment for running various LLMs

#### **[OpenAI Playground](https://platform.openai.com/playground/chat?models=gpt-4o)**

Free for use browser tool which lets you test out OpenAI model configurations and get associated code snippets. Has access to cutting edge features (real-time and assistants APIs).

#### **[LM Studio](https://lmstudio.ai/)**

Self-hosted offering. No additional costs for using the language model. High hardware costs, available models are limited by your hardware configuration. You the need to download models individually. For enterprise applications with high security needs.

## Using GitHub Models as a development tool

![Figure: GitHub Models makes life easy](https://github.com/user-attachments/assets/f8fdca43-fd0c-4a16-a37d-b1d322752712)

GitHub Models provides you with a free, rate-limited key you can use for practical tests in your application during development.

GitHub Models supports a large amount of language models within the same ecosystem. The development cost of switching from one model to another is minimal, assuming you're using the Azure AI Inference API. Switching from one model to another is as simple as changing an API parameter. Your code implementation can stay the same.

You have the option to choose between most major language models. You can experiment by submitting prompts to find the best fit for your scenario.

For example, you may be building a chatbot and find that GPT 4o mini provides suitable responses and that you don't need to invest in the extra compute costs involved with running a larger model.

## Deploying to production

Once you've identified the best model for your needs, GitHub Models simplifies deployment. You can:

1. Generate a **production key** for your app
2. Start incurring costs **only when you go live**

This approach allows you to make an informed decision before committing financially, ensuring you're using the right AI model for your application.

In effect, GitHub Models is the lite version of Azure's AI Foundry – it can even use the same API.
