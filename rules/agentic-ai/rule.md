---
type: rule
tips: ""
title: Do you build Agentic AI?
seoDescription: Follow the industry best practises on building agentic AI from
  Australia's leading software consultancy.
uri: agentic-ai
authors: []
related:
  - avoid-ai-hallucinations
guid: e4e963e4-1568-4e47-b184-d2e96bc0f124
---
# AI Agents: The Next Frontier in AI Development

AI agents are autonomous entities powered by AI that can perform tasks, make decisions, and collaborate with other agents. Unlike traditional single-prompt LLM interactions, agents act as specialized workers with distinct roles, tools, and objectives. 

`youtube: https://youtu.be/BlqJ7bnivLE`
**Video: The Year of the AI Agent: Automation to Intelligence | Ulysses Maclaren | SSW User Group (1:30 hr)**

<!--endintro-->

## Why Build Agentic Systems?

* **Automation**: Handle complex, multi-step workflows autonomously.
* **Specialization**: Assign agents to tasks they’re optimized for (e.g., research, coding, analysis).
* **Scalability**: Deploy an "army" of agents to tackle large projects.
* **Collaboration**: Enable agents to communicate and share insights.

- - -

## How to Build Agents: Framework Comparison

| Feature                 | Semantic Kernel (Microsoft)                     | Autogen (Microsoft)                  | LangChain                              | LangGraph (LangChain)                                      | OpenAI Operator                          |
| ----------------------- | ----------------------------------------------- | ------------------------------------ | -------------------------------------- | ---------------------------------------------------------- | ---------------------------------------- |
| **Developed By**        | Microsoft                                       | Microsoft                            | LangChain Inc                          | LangChain Inc                                              | OpenAI/3rd Parties                       |
| **Best For**            | Enterprise Azure workflows                      | Research/agent swarms                | Modular AI pipelines                   | Stateful workflows                                         | No-code prototyping                      |
| **Learning Curve**      | Moderate                                        | Steep                                | Moderate                               | Steep                                                      | Easy                                     |
| **Key Features**        | \- Plugins<br>- Planners<br>- Azure integration | \- Group chat<br>- Agent negotiation | \- 100+ tools<br>- Document processing | \- Cyclic workflows<br>- Error handling<br>- Human-in-loop | \- Drag-and-drop UI<br>- Prebuilt agents |
| **State Management**    | Basic                                           | Session-based                        | Limited                                | **Advanced**                                               | None                                     |
| **Integration**         | .NET, Python, Azure                             | Python                               | Python/JS, 100+ tools                  | LangChain ecosystem                                        | OpenAI API                               |
| **Stability**           | Production-ready                                | Beta (v1.0.14)                       | Mature (v0.1.0+)                       | New (v0.0.12)                                              | Early-stage                              |
| **Agent Collaboration** | Sequential                                      | **Group chat**                       | Sequential                             | **Cycles/Recursion**                                       | Linear                                   |

### Key Insights from the Table

1. **Microsoft's Ecosystem**: Semantic Kernel and Autogen will likely merge, making Semantic Kernel the safer long-term bet unless you need Autogen’s experimental group-chat features today.
2. **LangChain Dominance**: Still the most flexible option for developers willing to navigate its complexity.
3. **Operator for Speed**: Best for quick proofs-of-concept without coding.

- - -

## Framework Recommendations

| Use Case                              | Recommended Tool              |
| ------------------------------------- | ----------------------------- |
| Enterprise workflows with Azure       | **Semantic Kernel**           |
| Advanced research/agent collaboration | **Autogen** (until SK merger) |
| Custom pipelines with diverse tools   | **LangChain**                 |
| Marketing/sales team prototyping      | **OpenAI Operator**           |

- - -

## The Future of Agent Frameworks

Microsoft’s planned Autogen-Semantic Kernel merger signals a shift toward unified enterprise-grade solutions. Meanwhile, LangChain remains the "Swiss Army knife" for developers, and tools like OpenAI Operator democratize agent creation for non-technical users.
