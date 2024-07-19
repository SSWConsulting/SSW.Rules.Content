---
seoDescription: Learn how to create an awesome README file that clearly communicates your project's purpose, setup instructions, and usage guidelines.
type: rule
title: Do you have an awesome README?
uri: awesome-readme
authors:
  - title: Seth Daily
    url: https://www.ssw.com.au/people/seth-daily
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
related:
  - awesome-documentation
created: 2024-07-18T13:42:55.753Z
guid: d84cad17-a3d0-4e1f-aaba-f2cd7c950d86
---

Have you ever opened a promising project, only to be lost because the README was unclear? It's a frustrating experience and causes you to quickly give up.

Crafting a README is not a one-size-fits-all endeavor. The content that makes a README truly great varies significantly depending on who your audience is and what type of project you're showcasing.

<!--endintro-->

**Why Audience Matters:**

- **Internal Enterprise Software**: Your README needs to cater to developers and stakeholders within your organization. Focus on clear documentation, internal processes, and how the software fits into the company's ecosystem.
- **Public Open Source Projects**: Your README becomes your project's public face. It needs to attract potential users and contributors, highlighting the project's value, ease of use, and community engagement opportunities.

**Why Repository Type Matters:**

- **Packages/Libraries**: Explain how to install, import, and use the package's functionalities. Provide code examples and API documentation.
- **CLI Tools**: Focus on installation instructions, command-line usage, and helpful examples for different use cases.
- **Web Applications**: Highlight the app's features, screenshots, and setup instructions. Consider adding live demos or links to hosted versions.

By tailoring your README to the specific audience and repository type, you create a more effective document that serves the needs of your readers, whether they are colleagues, potential users, or open-source contributors.

## Examples of Great READMEs

These are examples of what you could include in your README, depending on the audience and repository type, This doesn't mean you need to include all of these sections, but they can serve as a guide to help you create a more effective README.

Some of these would be their own document, that could be linked to from the README.

### Internal Enterprise Software README

- **Clear Purpose**: Concisely state the software's purpose, its role within the organization, and the problems it solves.
- **Quick Start**: Step-by-step instructions for getting the software up and running in a development environment.
- **Technical Overview**: High-level architecture diagram, technology stack, and dependencies.
- **Development Workflow**: Guidelines for setting up a development environment, contributing code, running tests, and deploying updates.
- **Troubleshooting**: Common issues and their solutions.
- **Contact Information**: Who to contact for support, questions, or reporting bugs (normally captured as Issues onto the backlog).
- **Documentation Links**: Links to internal wikis, Confluence pages, or other relevant documentation.
- **Onboarding Resources**: Guides or tutorials for new team members to understand the codebase and contribute effectively.
- **Code Style Guide**: (Optional) If applicable, link to or briefly summarize the coding conventions used in the project.

### Public Open Source Project README

- **Project Title and Description**: A concise, engaging description of the project, its goals, and the problems it solves.
- **Badges**: Visually display project status (e.g., build passing, license, code coverage).
- **Features**: Highlight the key features and benefits of the software.
- **Screenshots/GIFs**: Visual aids (if applicable) to demonstrate the software in action.
- **Installation**: Clear, step-by-step instructions for different operating systems and environments.
- **Usage Examples**: Code snippets or scenarios demonstrating how to use the software.
- **Contributing Guidelines**: How to report issues, submit pull requests, and the code review process.
- **Code of Conduct**: (Recommended) Establish community standards and expectations for behavior.
- **License**: Clearly state the open source license under which the project is released.
- **Community**: Links to forums, chat rooms, or mailing lists for getting help or discussing the project.
- **Acknowledgments**: Thank contributors and any projects that your project depends on.

## Getting Started with your README

It can be overwhelming to start writing a README from scratch.

::: bad
![Figure: Bad example - We've all seen one of these 🤮](readme-bad.jpg)
:::

To avoid a README like above, you can look at the GitHub repository [github.com/matiassingers/awesome-readme](https://github.com/matiassingers/awesome-readme) for a lot of examples and tools that can help with inspiration for your README.

You can also take a look at this video showcasing some of the tools and examples used

`youtube: https://www.youtube.com/watch?v=a8CwpGARAsQ`
**Video: How To Create Beautiful and Useful ReadMe Documents For GitHub (7 min)**

A great tool to help you build your README is [GitHub Simp](https://readmi.xyz/). It provides a simple editor to create a README with a live preview, and you can export it to Markdown or HTML.

::: good
![Figure - Sample readme Generated with https://readmi.xyz/](github-simp-example.png)
:::

You can also try [readme.so](https://readme.so/), which offers a similar service with more customization options which is maintained by [Katherine Oelsner](https://github.com/octokatherine) from GitHub.
