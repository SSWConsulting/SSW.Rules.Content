---
type: rule
title: Do you know how to run LLMs locally?
seoDescription: Learn how to run large language models locally using Ollama and Microsoft Foundry Local for enhanced privacy, control, and offline capabilities.
uri: run-llms-locally
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
related:
  - use-ai-responsibly
  - best-ai-tools
  - choosing-large-language-models
created: 2025-07-17T21:00:00.000Z
guid: 2b7d9e5f-3a1c-4f6e-9d2a-8c4e5f6a7b8c
---

While cloud-based AI services like [OpenAI](https://openai.com/), [Claude](https://claude.ai/), and [Gemini](https://gemini.google.com/) offer convenience and power, running large language models (LLMs) locally provides significant advantages for privacy-conscious developers, businesses with sensitive data, and those who need offline capabilities.

<!--endintro-->

## Why run LLMs locally?

Local LLMs ensure your data never leaves your machine, provide consistent performance without internet dependencies, and offer cost savings for high-volume usage.

### ✅ Benefits of local LLMs

* **Enhanced privacy** - Your code and data never leave your machine
* **Offline capabilities** - Work without internet connectivity
* **Cost control** - No per-token charges for high-volume usage
* **Customization** - Full control over model selection and fine-tuning
* **Consistent performance** - No API rate limits or service outages
* **Compliance** - Easier to meet regulatory requirements for data handling

### ❌ Limitations to consider

* **Hardware requirements** - Need sufficient RAM and GPU for good performance
* **Model size constraints** - Smaller models may have reduced capabilities
* **Setup complexity** - Requires technical knowledge for initial configuration
* **Updates** - Must manually update models and software

## Ollama vs Microsoft Foundry Local

Two main platforms simplify running local LLMs: Ollama for its ease of use, and Microsoft Foundry for its enterprise integration.

There are two primary platforms for running LLMs locally, each with distinct advantages:

### Ollama - The Open Source Champion

**[Ollama](https://ollama.com)** is an open-source platform that makes running LLMs locally incredibly simple:

**✅ Pros:**

* **Easy installation** - Single command installation via package managers
* **Extensive model library** - Supports 100+ models including [Llama 3.3](https://ollama.com/library/llama3.3), [Gemma 2](https://ollama.com/library/gemma2), [Mistral](https://ollama.com/library/mistral), and [CodeLlama](https://ollama.com/library/codellama)
* **Simple CLI interface** - Run models with just `ollama run modelname`
* **Docker support** - Easy containerized deployment
* **Active community** - Large open-source community and frequent updates
* **Cross-platform** - Works on macOS, Windows, and Linux
* **Resource efficient** - Optimized for consumer hardware

**❌ Cons:**

* **Limited enterprise features** - Basic management and monitoring tools
* **No official support** - Community-driven support only
* **Performance optimization** - May require manual tuning for optimal performance

### Microsoft Foundry Local - The Enterprise Solution

**[Microsoft Foundry Local](https://azure.microsoft.com/en-us/products/ai-foundry/?WT.mc_id=AI-MVP-33518)** is a local version of Azure AI Foundry, designed for enterprise scenarios:

**✅ Pros:**

* **Enterprise-grade** - Built for business environments with proper management tools
* **Microsoft ecosystem** - Seamless integration with Microsoft development tools
* **OpenAI-compatible API** - Drop-in replacement for OpenAI API calls
* **Professional support** - Backed by Microsoft's enterprise support
* **Security focused** - Built with enterprise security requirements in mind
* **Compliance ready** - Designed to meet various regulatory requirements

**❌ Cons:**

* **Windows-focused** - Primarily designed for Windows environments
* **Limited model selection** - Fewer models compared to Ollama
* **Complexity** - More complex setup and configuration
* **Cost** - May require licensing for enterprise features
* **Resource requirements** - Higher system requirements

## Local models for code completion

Local LLMs excel at providing code completion and assistance. Here are popular options:

### IDE Extensions using local models

**[Continue](https://continue.dev/)** - Open-source VS Code and JetBrains extension:

* Supports both Ollama and custom local models
* Provides autocomplete, chat, and edit features
* Configurable to use local models like CodeLlama or StarCoder

**[Tabby](https://tabby.tabbyml.com/)** - Self-hosted AI coding assistant:

* Runs as a local server with a web interface
* Supports multiple code completion models
* Can be integrated with VS Code extensions
* Excellent for teams wanting shared local AI

### Recommended models for code completion

For the most up-to-date list of available models, check the [Ollama library](https://ollama.com/library) which contains hundreds of models optimized for local execution.

Here are some popular coding models to get you started:

* [CodeLlama](https://ollama.com/library/codellama) - Meta's specialized coding model (7B/70B)

* [StarCoder](https://ollama.com/library/starcoder2) - Open-source code generation model (3B/15B)

* [Codestral](https://ollama.com/library/codestral) - designed by Mistral for code generation tasks

## Best practices

* **Start with a ~7B parameter model** - Models like codellama:7b or llama3:8b are a great baseline for performance on consumer hardware (e.g., a MacBook with 16GB+ RAM)
* **Benchmark models on your tasks** - A model that excels at writing prose may not be the best for generating C# code. Test a few to see what works best for your needs.
* **Consider hybrid approaches** - Use local models for sensitive data, cloud for complex tasks

Running LLMs locally provides developers with powerful AI capabilities while maintaining control over their data and environment. Whether you choose Ollama for simplicity or Foundry Local for enterprise features, local LLMs are becoming an essential tool for modern development workflows.
