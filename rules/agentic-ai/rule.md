---
type: rule
tips: ""
title: Do you build Agentic AI?
seoDescription: Follow the industry best practises on building agentic AI from
  Australia's leading software consultancy. Best practises for Autogen, Semantic Kernel, LangChain, LangGraph, OpenAI, and n8n.
uri: agentic-ai
authors:
  - title: Eddie Kranz
    url: https://www.ssw.com.au/people/eddie-kranz
related:
  - avoid-ai-hallucinations
  - use-semantic-kernel
guid: e4e963e4-1568-4e47-b184-d2e96bc0f124
---

AI agents are autonomous entities powered by AI that can perform tasks, make decisions, and collaborate with other agents. Unlike traditional single-prompt LLM interactions, agents act as specialized workers with distinct roles, tools, and objectives.

`youtube: https://youtu.be/BlqJ7bnivLE`
**Video: The Year of the AI Agent: Automation to Intelligence | Ulysses Maclaren | SSW User Group (1:30 hr)**

<!--endintro-->

## Why Build Agentic Systems?

* **Automation**: Handle complex, multi-step workflows autonomously.
* **Specialization**: Assign agents to tasks they're optimized for (e.g., research, coding, analysis).
* **Scalability**: Deploy an "army" of agents to tackle large projects.
* **Collaboration**: Enable agents to communicate and share insights.

- - -

## Leading Agent Frameworks Comparison

| Feature            | [Autogen](https://microsoft.github.io/autogen/stable/) ⭐️ | [OpenAI Agents](https://openai.github.io/openai-agents-python/) | [LangGraph](https://www.langchain.com/langgraph)           | [n8n](https://n8n.io/)                                |
| ------------------ | ------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------- | ----------------------------------------------------- |
| **Developed By**   | Microsoft                                              | OpenAI                                                       | LangChain                                                  | n8n                                                   |
| **Best For**       | Multi-agent conversations, flexible agent topologies    | Production-ready pipelines with OpenAI models                | Complex stateful workflows, cyclical execution patterns    | No-code AI workflow automation                        |
| **Learning Curve** | Medium                                                  | Low                                                          | High                                                       | Low (visual interface)                                |
| **Key Features**   | - Conversational agents<br>- Event-driven<br>- Group chat | - Agent SDK<br>- Native handoffs<br>- Built-in tracing<br>- Guardrails | - Graph-based workflows<br>- State management<br>- Human-in-loop<br>- Time-travel debugging | - Visual workflow editor<br>- 400+ integrations<br>- AI nodes |
| **Integration**    | Python, various LLMs                                   | Python/JS, OpenAI ecosystem                                  | Python/JS, LangChain ecosystem                            | No-code interface, LangChain under the hood          |
| **Production Ready** | Research-focused                                      | Yes, built for production                                    | Yes, enterprise-grade                                      | Yes, for workflow automation                          |

*Note: Microsoft is planning to merge [Semantic Kernel](https://www.ssw.com.au/rules/use-semantic-kernel/) and AutoGen into a unified framework, combining enterprise Azure workflows with advanced agent capabilities.*

- - -

## When to Choose Each Framework

When choosing a framework for building agents, you need to be aware of the tradeoff between customisability and ease of use.

For example, n8n is a no-code solution that is only really useful for automating simple workflows, while frameworks like LangGraph offer deeper control but with a steeper learning curve.

The closer you get to the raw LLM API requests, the more customisable you can make it – however, this will often come at the cost of additional development effort.

### OpenAI Agents SDK

The OpenAI Agents SDK is ideal when:

* You require a straightforward, production-grade framework that's easy to learn
* Your existing stack already includes OpenAI models and you want seamless integration
* You need strong tracing and debugging capabilities built into the framework
* You're building for production environments

### LangGraph

Consider LangGraph when:

* Your project involves intricate, recurring workflows requiring sophisticated state handling
* You're developing systems with multiple interconnected agents
* You have prior experience with the LangChain ecosystem
* You benefit from visualizing your agent workflows graphically
* You need enterprise-grade reliability

### AutoGen ⭐️

AutoGen shines when:

* Your application requires dynamic conversation flows between multiple agents
* You're creating systems with diverse conversational agents working together
* You value the backing of Microsoft's research division
* You're working on research projects needing flexible agent interactions

### n8n

Choose n8n if:

* You need a no-code solution for building simple agent workflows
* You want a visual, drag-and-drop interface
* You have team members without coding experience who need to participate
* You're creating marketing, sales, or design team prototypes

## Language Limitations and Considerations

Most of the leading agent frameworks today, including AutoGen, LangGraph, and OpenAI Agents SDK, primarily use Python as their development language. This presents a challenge for organizations like SSW that predominantly use .NET and C#.

For C# developers, the most promising path forward is through **Semantic Kernel**. Microsoft is currently working on integrating AutoGen's capabilities into Semantic Kernel, which will allow .NET developers to leverage cutting-edge agent technology using C#. This integration is expected to bring the powerful multi-agent capabilities of AutoGen to the familiar and enterprise-ready .NET ecosystem.

**Our recommendation:** While waiting for the full Semantic Kernel integration, we recommend C# developers start experimenting with AutoGen in Python. The knowledge and patterns you learn will transfer directly to Semantic Kernel's implementation once it's complete, as Microsoft is directly incorporating AutoGen's architecture.

```python
# Example AutoGen code that will be portable to Semantic Kernel in future
import autogen

# Define agents
assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config={"model": "gpt-4o"}
)

user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    human_input_mode="NEVER"
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="How can I build a simple C# web app with an LLM backend?"
)
```

For a glimpse of how Semantic Kernel is already beginning to integrate with AutoGen, see this example:

```python
import asyncio
import os

from autogen import ConversableAgent
from semantic_kernel.agents.autogen.autogen_conversable_agent import AutoGenConversableAgent

async def main():
    cathy = ConversableAgent(
        "cathy",
        system_message="Your name is Cathy and you are a part of a duo of comedians.",
        llm_config={
            "config_list": [
                {
                    "model": "gpt-4o-mini", 
                    "temperature": 0.9, 
                    "api_key": os.environ.get("OPENAI_API_KEY")
                }
            ]
        },
        human_input_mode="NEVER",  # Never ask for human input.
    )

    joe = ConversableAgent(
        "joe",
        system_message="Your name is Joe and you are a part of a duo of comedians.",
        llm_config={
            "config_list": [
                {
                    "model": "gpt-4o", 
                    "temperature": 0.7, 
                    "api_key": os.environ.get("OPENAI_API_KEY")
                }
            ]
        },
        human_input_mode="NEVER",  # Never ask for human input.
    )

    # Create the Semantic Kernel AutoGenAgent
    autogen_agent = AutoGenConversableAgent(conversable_agent=cathy)

    async for content in autogen_agent.invoke(
        recipient=joe, 
        message="Tell me a joke about NVDA and TESLA stock prices.", 
        max_turns=3
    ):
        print(f"# {content.role} - {content.name or '*'}: '{content.content}'")


if __name__ == "__main__":
    asyncio.run(main())
```

**Figure: How AutoGen agents can be used in Semantic Kernel**
