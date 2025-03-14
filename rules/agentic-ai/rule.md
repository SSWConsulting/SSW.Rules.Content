---
type: rule
tips: ""
title: Do you build Agentic AI?
seoDescription: Follow the industry best practises on building agentic AI from
  Australia's leading software consultancy.
uri: agentic-ai
authors: []
related:
  - null
guid: e4e963e4-1568-4e47-b184-d2e96bc0f124
---

# AI Agents: The Next Frontier in AI Development

AI agents are autonomous entities powered by AI that can perform tasks, make decisions, and collaborate with other agents. Unlike traditional single-prompt LLM interactions, agents act as specialized workers with distinct roles, tools, and objectives. 

`youtube: https://youtu.be/BlqJ7bnivLE`
**Video: The Year of the AI Agent: Automation to Intelligence | Ulysses Maclaren | SSW User Group (1:30 hr)**

<!--endintro-->

## Why Build Agentic Systems?
- **Automation**: Handle complex, multi-step workflows autonomously.
- **Specialization**: Assign agents to tasks they’re optimized for (e.g., research, coding, analysis).
- **Scalability**: Deploy an "army" of agents to tackle large projects.
- **Collaboration**: Enable agents to communicate and share insights.

---

## How to Build Agents: Framework Comparison

Below is a detailed comparison of popular frameworks for building AI agents:

| Feature                | Semantic Kernel (Microsoft)          | Autogen (Microsoft)                   | LangChain Agents                      | OpenAI Operator                       |
|------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| **Developed By**       | Microsoft                             | Microsoft                             | Community/Open Source                 | OpenAI              |
| **Best For**           | Enterprise workflows, Azure integration | Research/advanced agent collaboration | Flexible, modular AI pipelines       | No-code/low-code rapid prototyping    |
| **Learning Curve**     | Moderate                              | Steep                                 | Steep                                 | Easy                                  |
| **Key Features**       | - Plugins<br>- Planners<br>- Memory   | - Group chat<br>- Customizable roles  | - 100+ tools<br>- Document loaders   | - Click-ops UI<br>- Prebuilt templates|
| **Integration**        | Azure, .NET, Python                   | Python-only                           | Multi-LLM, external APIs             | OpenAI models                         |
| **Stability**          | High (production-ready)               | Medium (experimental features)        | High                                  | Medium (emerging tool)                |
| **Community Support**  | Growing (Microsoft-backed)            | Niche (research focus)                | Largest community                     | Small but growing                     |
| **Unique Selling Point**| Future-proof (Autogen merger planned) | Cutting-edge collaboration features   | Ecosystem flexibility                 | Simplicity for non-devs               |

---

### Key Insights from the Table
1. **Microsoft's Ecosystem**: Semantic Kernel and Autogen will likely merge, making Semantic Kernel the safer long-term bet unless you need Autogen’s experimental group-chat features today.
2. **LangChain Dominance**: Still the most flexible option for developers willing to navigate its complexity.
3. **Operator for Speed**: Best for quick proofs-of-concept without coding.

---

## Framework Recommendations

| Use Case                                  | Recommended Tool                      |
|-------------------------------------------|---------------------------------------|
| Enterprise workflows with Azure           | **Semantic Kernel**                   |
| Advanced research/agent collaboration     | **Autogen** (until SK merger)         |
| Custom pipelines with diverse tools       | **LangChain**                         |
| Marketing/sales team prototyping          | **OpenAI Operator**                   |

---

## The Future of Agent Frameworks
Microsoft’s planned Autogen-Semantic Kernel merger signals a shift toward unified enterprise-grade solutions. Meanwhile, LangChain remains the "Swiss Army knife" for developers, and tools like OpenAI Operator democratize agent creation for non-technical users.

*Choose based on your team’s skillset and project requirements.*
