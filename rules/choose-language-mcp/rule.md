---
type: rule
tips: ""
title: Do you choose the right language for your MCP tools
uri: choose-language-mcp
authors:
  - title: ""
guid: bd3708fd-2bb4-49a3-842f-49004a5373d9
---
Choosing the right language from your Model Context Protocol (MCP) tool can feel a little bit like finding a needle in the hay stack. Your inundated with options but now the onus is on you to pick the one that is suits your needs. At the same time, choosing the best language for your MCP tools has a directly impact on how and where you choose to expand and optimize.

<!--endintro-->


## MCP Client

### #1 Recommended tool: Python

At SSW at the time of writing we have found the MCP library to be the most stable for creating an MCP client. We generally recommend .NET for building web APIs, but in our experience we've found that the official MCP library for C# is in a state of Flux and the developer experience isn't currently on par with Python.



### What is an MCP client?

An MCP client acts as a bridge between a large language model and the services that language model can consume on the MCP server. The client is responsible for reporting which tools are available on it's corresponding server and providing an interface for the LLMs to invoke these tools.



## MCP Server
### What is an MCP server?

An MCP server contains the services that will be exposed to LLM and consumed by the LLM via the MCP Client. As the MCP Client and MCP Server run independently from one another they can both be written in different languages.

#### Choosing the right

At SSW we haven't found significant differences between the official MCP SDKs in terms of building MCP servers. 

As the ecosystem is evolving quickly we recommend choosing a language that has an actively maintained SDK or community library for MCP (e.g. TypeScript or Python). Each of the following libraries has an official MCP SDK support:

* [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk)
* [Python](https://github.com/modelcontextprotocol/python-sdk)
* [Java](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C#](https://github.com/modelcontextprotocol/csharp-sdk)
* [Go](https://github.com/modelcontextprotocol/go-sdk)
* [PHP](https://github.com/modelcontextprotocol/php-sdk)
* [Ruby](https://github.com/modelcontextprotocol/ruby-sdk)
* [Rust](https://github.com/modelcontextprotocol/rust-sdk)
* [Swift](https://github.com/modelcontextprotocol/swift-sdk)





##### Why does this matter?

Essentially your MCP Client only treats your MCP server as a functional dependency. The language your server is written in could be completely different to your client. The server simply needs to implement the JSON-RPC protocol.



- - -

### Rule of thumb

* **SDK Support:** Lower level Languages such as Rust may have better performance than scripting languages, but may not have official SDKs, making code maintenance more difficult.
* **Native vs Cloud Capabilities:** Consider whether you want to be able to customize your language model locally or remotely you want to be tied to a cloud computing ecosystem (e.g. within Azure).
* **Learning curve:** Once you've evaluated and SDK that meets the needs of your team members it's best to stick to an ecosystem your team already understands. Unless you find that the SDKs in your chosen language don't have the features you want.
* **Performance:** If you are concerned with hosting your own language models, or running your language models locally consider Python for it's hardware acceleration advantages.
