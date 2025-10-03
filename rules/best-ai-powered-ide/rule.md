---
type: rule
tips: ""
title: Do you use the best AI Powered IDE?
seoDescription: how to use cursor, vscode, github copilot, the best AI powered IDE
uri: best-ai-powered-ide
authors:
  - title: Eddie Kranz
    url: https://www.ssw.com.au/people/eddie-kranz/
  - title: Lewis Toh
    url: https://www.ssw.com.au/people/lewis-toh/
  - title: Calum Simpson
    url: https://www.ssw.com.au/people/calum-simpson/
related:
  - ai-pair-programming
created: 2025-01-02T12:40:00.000Z
archivedreason: ""
guid: 49ac441c-6882-4c4b-adef-47f4e87ea68c
---
Since the release of [GitHub Copilot](https://github.com/features/copilot) in 2021, we have witnessed a dramatic evolution in how developers work within their IDE. It started with a simple AI autocomplete, and has since progressed to a chat function. AI has now been integrated deeply into IDEs with products like [Cursor](https://www.cursor.com/) and [Windsurf](https://codeium.com/windsurf), embedding an even deeper level of AI Integration within a developer's workflow.

<!--endintro-->

`youtube: https://youtu.be/fVYM10-fpG4?si=JeOx6-jN1Jin-W0n`

**Video: Let Cursor do the coding for you | Calum Simpson | SSW Rules (10 min)**

## Powerful features that AI-Powered IDEs provide

### Code Completion

GitHub Copilot first popularized the 'code completion' feature for AI-powered IDEs. Code completion will try to guess what you are going to write, and suggest how to complete this line – saving time and effort by simply pressing 'tab'.

### Command Generation

In Cursor and Windsurf, you can hit ctrl-K (or command-K), to convert natural language to a bash command. This is very useful for when you have forgotten the exact syntax of a bash command.

![Figure: Cursor Command Generation (ctrl-K)](cursor-command-generation.gif)

### Chat

Chat functionality within an AI-powered IDE adds an intelligent assistant that can offer answers and suggestions without needing to leave the IDE. Unlike generic AI tools, it allows you to add context to your question, such as a file or even codebase, which lets the AI provide more tailored solutions.

#### Specify the level of context

Within the chat for Cursor, you can specify the level of context you would like to include with your prompt. By typing the `@` character, the following menu will appear.

![Figure: Cursor Chat Context, opened by typing `@`](cursor-chat-context.png)

In Cursor, the `@Web` function is very useful for any situations where recent information, or information that the model has not been trained on is needed! You can also use `@Git` to compare diffs with the main branch, to generate a nice PR summary.

### Agent

The Agent function in AI-powered IDEs represents a significant leap in a developer's workflow. It acts as a semi-autonomous coding assistant, capable of directly controlling the IDE (creating/editing files, reading the codebase, searching the web, executing bash commands).

::: bad
![Figure: Bad example - Using ChatGPT with only one instruction, requiring you to copy paste the commands into the IDE](bad-example-chatgpt.png)
:::

::: good
![Figure: Good example - Using Cursor Agent to create a Tina App, with multiple provided instructions](good-example-using-agent.png)
:::

## AI-Powered IDE Comparison

| Feature               | [Cursor](https://www.cursor.com/)                                                        | [IDE + GitHub Copilot](https://github.com/features/copilot)                                    | [Windsurf](https://codeium.com/windsurf)                                        | [GitHub Copilot Workspace](https://githubnext.com/projects/copilot-workspace) |
| --------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Free Version          | • 2000 completions per month<br>• 50 slow premium requests per month                     | • 2000 completions per month<br>• 50 chat messages per month                                   | • 5 premium user prompts<br>• 5 premium Flow Actions                            | ❌                                                                             |
| Price (USD per month) | $20                                                                                      | $10                                                                                            | $15                                                                             | $10 (Bundled with Copilot Pro)                                                |
| AI Model(s)           | • cursor-small (free)<br>• Anthropic Claude (Sonnet, Haiku)<br>• OpenAI (GPT 3.5, 4, 4o) | • Anthropic Claude (Sonnet, Haiku)<br>• OpenAI (GPT 3.5, 4, 4o)                                | • Meta Llama<br>• Anthropic Claude (Sonnet, Haiku)<br>• OpenAI (GPT 3.5, 4, 4o) | OpenAI (GPT 3.5, 4, 4o)                                                       |
| Custom Models         | ❌                                                                                        | ❌                                                                                              | ❌                                                                               | Enterprise Version                                                            |
| Custom Rules          | ✅                                                                                        | ✅                                                                                              | ✅                                                                               | ❌                                                                             |
| Auto-Completion       | ✅                                                                                        | ✅                                                                                              | ✅                                                                               | ✅                                                                             |
| Chat                  | ✅                                                                                        | ✅                                                                                              | ✅                                                                               | ✅                                                                             |
| Agent                 | ✅                                                                                        | ❌                                                                                              | ✅                                                                               | ✅                                                                             |
| Privacy Mode          | ✅                                                                                        | ✅                                                                                              | ✅                                                                               | ✅                                                                             |
| GitHub Integration    | ❌                                                                                        | • Copilot Chat<br>• Auto-generate commit message                                               | ❌                                                                               | • Full Workflow is on GitHub<br>• Generate PR Summary                         |
| Web Searching         | ✅                                                                                        | ❌                                                                                              | ✅                                                                               | ❌                                                                             |
| Supported IDE         | Cursor IDE - Forked VS Code (with VSCode Extensions Supported)                           | • Azure Data Studio<br>• JetBrains IDEs<br>• VS Code<br>• Visual Studio<br>• Neovim<br>• Xcode | Windsurf IDE - Forked VS Code (with VSCode Extensions Supported)                | • Browser based<br>• VSCode Support (GitHub CodeSpace)                        |

::: info
**Tip**: Give each of them a try – most of them have free trials, so you can see which one works best for you. 

If you still have your student status, you can get **GitHub Copilot Pro for free** here: [Free GitHub Copilot Pro access](https://docs.github.com/en/copilot/how-tos/manage-your-account/getting-free-access-to-copilot-pro-as-a-student-teacher-or-maintainer#about-free-github-copilot-pro-access)
:::


## A word of caution

AI is still very much a work in progress. It makes mistakes, especially when working with lesser-known programming languages and frameworks, and will often hallucinate. It is the developer's responsibility to ensure that the code they publish is optimized, and AI tools should only be used for assistance, and not as a direct replacement for a developer.

You wouldn't send an email written by ChatGPT without first checking it for correctness and intention. Similarly, you should not commit any code written by AI without first reading through it, and testing it.

You are solely responsible for the code you commit!

::: info
**Warning:** Whilst Cursor can run VSCode extensions, not all will work e.g. Microsoft licensing restricts the use of the .NET debugger to Microsoft builds of VSCode.
See <https://github.com/dotnet/vscode-csharp/wiki/Microsoft-.NET-Core-Debugger-licensing-and-Microsoft-Visual-Studio-Code>
:::

## Which is best?

As you can see from the comparison table, each of the AI-powered IDEs rival each other in most categories, and you can't go wrong with any of them.

Currently, SSW Developers tend to prefer Cursor, and it seems to have more hype based on [Google Trends](https://trends.google.com.au/trends/explore?q=cursor%20ide,windsurf%20ide&hl=en). However, Windsurf is a formidable competitor in the battle for the best AI-powered IDE.

::: info
**Tip**: Investing in one of these tools may prove to be worthwhile, and you can always claim it as a tax deduction.
:::

Share some details about your experience  with AI assisted development e.g. What tool did you use, what did you use it for, how did you use it, what was the experience like, etc.
