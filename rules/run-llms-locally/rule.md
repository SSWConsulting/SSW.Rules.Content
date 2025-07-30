---
type: rule
tips: ""
title: Do you run LLMs locally for enhanced privacy and control?
seoDescription: Learn how to run large language models locally using Ollama and Microsoft Foundry Local for enhanced privacy, control, and offline capabilities.
uri: run-llms-locally
authors:
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
related:
  - use-ai-responsibly
  - best-ai-tools
created: 2025-07-17T21:00:00.000Z
guid: 2b7d9e5f-3a1c-4f6e-9d2a-8c4e5f6a7b8c
---

While cloud-based AI services like [OpenAI](https://openai.com/), [Claude](https://claude.ai/), and [Gemini](https://gemini.google.com/) offer convenience and power, running large language models (LLMs) locally provides significant advantages for privacy-conscious developers, businesses with sensitive data, and those who need offline capabilities.

Local LLMs ensure your data never leaves your machine, provide consistent performance without internet dependencies, and offer cost savings for high-volume usage.

<!--endintro-->

## Why run LLMs locally?

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

There are two primary platforms for running LLMs locally, each with distinct advantages:

### Ollama - The Open Source Champion

**[Ollama](https://ollama.com/)** is an open-source platform that makes running LLMs locally incredibly simple:

**Pros:**

* **Easy installation** - Single command installation via package managers
* **Extensive model library** - Supports 100+ models including [Llama 3.3](https://ollama.com/library/llama3.3), [Gemma 2](https://ollama.com/library/gemma2), [Mistral](https://ollama.com/library/mistral), and [CodeLlama](https://ollama.com/library/codellama)
* **Simple CLI interface** - Run models with just `ollama run modelname`
* **Docker support** - Easy containerized deployment
* **Active community** - Large open-source community and frequent updates
* **Cross-platform** - Works on macOS, Windows, and Linux
* **Resource efficient** - Optimized for consumer hardware

**Cons:**

* **Limited enterprise features** - Basic management and monitoring tools
* **No official support** - Community-driven support only
* **Performance optimization** - May require manual tuning for optimal performance

```bash
# Install Ollama (macOS)
brew install ollama

# Run a model
ollama run llama3.3

# List available models
ollama list

# Pull a specific model
ollama pull codellama:7b
```

### Microsoft Foundry Local - The Enterprise Solution

**[Microsoft Foundry Local](https://azure.microsoft.com/en-us/products/ai-foundry/?WT.mc_id=AZ-MVP-33518)** is a local version of Azure AI Foundry, designed for enterprise scenarios:

**Pros:**

* **Enterprise-grade** - Built for business environments with proper management tools
* **Microsoft ecosystem** - Seamless integration with Microsoft development tools
* **OpenAI-compatible API** - Drop-in replacement for OpenAI API calls
* **Professional support** - Backed by Microsoft's enterprise support
* **Security focused** - Built with enterprise security requirements in mind
* **Compliance ready** - Designed to meet various regulatory requirements

**Cons:**

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

**CodeLlama (7B/13B)** - Meta's specialized coding model:

```bash
ollama pull codellama:7b
# or for larger contexts
ollama pull codellama:13b
```

**StarCoder** - Open-source code generation model:

```bash
ollama pull starcoder:7b
```

**Deepseek-Coder** - Excellent for code understanding:

```bash
ollama pull deepseek-coder:6.7b
```

## Getting started with local LLMs

### Option 1: Quick start with Ollama

1. **Install Ollama:**

   ```bash
   # macOS
   brew install ollama
   
   # Windows (via installer)
   # Download from https://ollama.com/download
   
   # Linux
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Run your first model:**

   ```bash
   ollama run llama3.3:8b
   ```

3. **Set up code completion:**
   * Install [Continue extension](https://marketplace.visualstudio.com/items?itemName=Continue.continue) in VS Code
   * Configure it to use Ollama in settings
   * Start coding with local AI assistance

### Option 2: Enterprise setup with Foundry Local

1. Download and install Microsoft Foundry Local from Microsoft
2. Configure your local environment according to Microsoft's documentation
3. Set up API endpoints for your development tools
4. Configure security and compliance settings

## Best practices

* **Choose the right model size** - Balance capability with hardware constraints
* **Monitor resource usage** - Watch CPU, RAM, and GPU utilization
* **Keep models updated** - Regularly update to latest versions
* **Backup configurations** - Save your local setup configurations
* **Test performance** - Benchmark different models for your use cases
* **Consider hybrid approaches** - Use local models for sensitive data, cloud for complex tasks

Running LLMs locally provides developers with powerful AI capabilities while maintaining control over their data and environment. Whether you choose Ollama for simplicity or Foundry Local for enterprise features, local LLMs are becoming an essential tool for modern development workflows.
