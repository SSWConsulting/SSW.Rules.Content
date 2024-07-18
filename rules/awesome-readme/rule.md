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
related:
  - awesome-documentation
created: 2024-07-18T13:42:55.753Z
guid: d84cad17-a3d0-4e1f-aaba-f2cd7c950d86
---

Have you ever opened a promising project, only to be lost because the README was unclear? It's a frustrating experience and causes users to quickly give up.

A good README helps others understand what your project does, how to set it up, and how to use it, reducing the learning curve and saving time for everyone involved. See some examples of great READMEs here: <https://github.com/matiassingers/awesome-readme>

<!--endintro-->

`youtube: https://www.youtube.com/watch?v=E6NO0rgFub4&t=345s`
**Video: How To Write a USEFUL README On Github (8 min)**

::: bad
![Figure: Bad example - We've all seen one of these 🤮](readme-bad.jpg)
:::

Let's break down how to write an effective README by following an outline of the necessary components.

## Strong H1 and H2 Titles

Begin with a clear and concise title (H1) followed by a subtitle (H2) that provides a brief one-liner about what your project does, and helps with SEO (so others can find your project).

::: greybox

#### MyProject

##### Efficient Task Management Tool

:::
::: good
Figure: Good example - Clear title and concise subtitle
:::

## Intro Paragraph

Provide an introductory paragraph that dives deeper into what your project does. This is also a great place to include SEO keywords to help people find your project.

::: greybox
MyProject is a web application designed to help users manage their tasks efficiently. It offers features such as task creation, tracking, real-time notifications, and comprehensive reporting.
:::
::: good
Figure: Good example - Detailed introductory paragraph with SEO keywords
:::

## Diagram or Video

Include a diagram or video to visually explain how your project works. This can be a flowchart, system architecture diagram, or a demo video.

::: greybox
![Figure: System architecture diagram](architecture-diagram.jpg)
:::
::: good
Figure: Good example - Visual representation of the project's system architecture
:::

## Installation Instructions for Users

Provide clear instructions on how to install and use your project. This section is aimed at end-users who may not have technical expertise.

::: greybox

##### Installation for Users

1. Download the installer from {{ URL }}.
2. Run the installer and follow the on-screen instructions.
3. Open the application and start managing your tasks.
:::
::: good
Figure: Good example - Simple installation instructions for end-users
:::

## Installation Instructions for Contributors

Give detailed instructions for contributors on how to set up the development environment, build the project, and start contributing.

::: greybox

##### Installation for Contributors

1. Fork the repository and clone it to your local machine:

   ```bash
   git clone https://github.com/username/MyProject.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MyProject
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Build the project:

   ```bash
   npm run build
   ```

5. Start the development server:

   ```bash
   npm start
   ```

:::
::: good
Figure: Good example - Clear installation instructions for contributors
:::

## Contributor Expectations

Outline your expectations for contributors. This includes guidelines for submitting pull requests, coding standards, and any other relevant information.

::: greybox

##### Contributor Expectations

* Ensure all merges are squashed before submitting a pull request.
* Submit an issue before submitting a pull request.
* Follow the pull request template provided in the repository.
:::
::: good
Figure: Good example - Clear expectations for contributors
:::

## Known Issues

This avoids duplicate issues. List known issues or bugs in the project to ensure users and contributors understand what problems are already identified and being worked on.

::: greybox

##### Known Issues

* Notification system occasionally misses updates.
* Reports may not display correctly in Safari browser.
:::
::: good
Figure: Good example - Transparent communication of known issues
:::

## Donations (optional)

Include a section where people can donate to support your project. While time and contributions are invaluable, monetary donations can also help.

::: greybox

##### Support this project

If you find this project useful, consider supporting us by [buying us a coffee](https://www.buymeacoffee.com/).
:::
::: good
Figure: Good example - Simple and clear call for donations
:::
