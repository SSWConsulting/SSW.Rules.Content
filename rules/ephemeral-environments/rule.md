---
type: rule
title: Do you use Ephemeral environments for clean and isolated testing?
uri: ephemeral-environments
authors:
  - title: William Liebenberg
    url: https://ssw.com.au/people/william-liebenberg
related: []
created: 2023-10-12T17:33:21.000Z
archivedreason: null
guid: 3e317372-c200-4cfb-9afd-6264d3a88bf6

---

Ephemeral environments are like temporary, disposable workspaces created for a specific purpose, and they're often thrown away once they're no longer needed. Here's how they come in handy across various tasks:

`youtube: https://www.youtube.com/watch?v=-KrodXD3lPc`  
**Video: Use ephemeral development environments for mission-critical workloads on Azure (2 min)**

<!--endintro-->

## Testing

They're particularly useful for creating isolated testing environments. Imagine running a test to ensure a new feature works as expected. Ephemeral environments allow you to spin up a clean, separate space to run that test without affecting your main application. Once the test is complete, the environment is discarded, ensuring a fresh start for each test run.

## CI/CD

In the world of Continuous Integration and Continuous Deployment, these environments are a game-changer. They enable you to automatically build, test, and deploy applications, ensuring everything runs as expected before going live. The environment is created on-demand for the pipeline, then discarded once it's done.

## Feature Development

For developers working on new features or bug fixes, ephemeral environments provide a sandbox to experiment and test changes without risking the stability of the main application. It's like having a safe space to try out new ideas, which can be thrown away once the development work is finished.

## Training and Demos

Ephemeral environments are also great for creating temporary setups for training sessions or product demos. They can be configured with the necessary data and settings, providing a consistent experience for each session, and then removed afterward.

In summary, ephemeral environments offer a versatile solution for ensuring clean, isolated, and repeatable workspaces across testing, development, and demonstrations in software applications.
