---
type: rule
title: Do you containerize your dev environment?
uri: dev-containers
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
related:
  - do-you-make-instructions-at-the-beginning-of-a-project-and-improve-them-gradually
created: 2022-11-30T03:26:46.980Z
guid: 3c013217-0b18-40e2-bdad-0139242d9e3f
---
Developers love the feeling of getting a new project going for the first time. Unfortunately, the process of making things work is often a painful experience. Every developer has a different setup on their machine so it is common for a project to require slightly different steps.

The old proverb is "Works on my machine!".

Luckily, there is a way to make all development environments 100% consistent. 
            
<!--endintro-->

Dev containers let you define all the tools needed for a project in a programmatic manner. That gives 2 benefits:
* Consistent isolated environments
* Pre-installed tools with correct settings

### How does it work?
Dev containers are setup with a few files in the repo:

* devcontainer.json - This specifies the launch instructions for your container
* [Dockerfile](https://docs.docker.com/engine/reference/builder/) 
* [Docker-compose.yml](https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples)

These files define an image to use, tools to install and settings to configure.

Once those files are configured, you can simply open VS Code and run a command to get it running on your laptop.

### Where can I find out what to do?

Microsoft has a great [tutorial](https://learn.microsoft.com/en-us/training/modules/use-docker-container-dev-env-vs-code/) and [documentation](https://code.visualstudio.com/docs/devcontainers/containers) on how to get it running.

### Where to run it?
Dev containers can be run locally with VS code, which works awesome if you have a powerful machine to work with already. However, sometimes you might need to give an environment to people who don't have powerful machines or you might want people to develop on tablets.

In those cases, [GitHub Codespaces](https://github.com/features/codespaces) can help by providing a powerful cloud machine to run your dev container on. 
