---
type: rule
title: Do you know how to set up a Vue.js project?
uri: set-up-vue-project
authors:
  - title: Zach Keeping
    url: https://ssw.com.au/people/zach-keeping/
created: 2023-07-13T04:20:50.584Z
guid: bcde10d8-9a57-40c6-af8f-fe594e48c8c2
---
Getting started with a Vue.js project is easy. Here's how you can get up and running quickly:

<!--endintro-->

### create-vue (Recommended)

[create-vue](https://github.com/vuejs/create-vue) is the official and recommended tool for scaffolding a Vue.js project. It uses [Vite](https://vitejs.dev/) (also from Vue creator Evan You) to help quickly and easily set up a Vue.js project to your specifications.

**Note:** this requires Node v16 or higher

1. In your command line, run:

   ```
   npm init vue@latest
   ```
2. This will install and run create-vue. It will then prompt you for a project name and step you through a series of prompts for the features you wish to enable:

   ![Figure: The options provided by create-vue for scaffolding a Vue.js project](screenshot-2023-07-13-at-3.09.18-pm.png)
3. When this completes, you're all done! You will now have a Vue.js project set up in a folder matching the project name you set. To get started running a dev server, execute the following:

   ```
   cd {{ PROJECT_NAME }}
   npm install 
   npm run dev
   ```

### Vue CLI (Not recommended for new projects)

[Vue CLI](https://cli.vuejs.org/) is the official CLI toolchain for Vue.js development using Webpack. Previously, this was the recommended tool for scaffolding a Vue.js project but is now no longer supported, in favour of create-vue and Vite. Unless your project requires Webpack, it is recommended to use create-vue instead.

Scaffolding a project in Vue CLI takes just a few steps:

1. Install Vue CLI:

   ```
   npm install -g @vue/cli
   ```
2. Create a new project using "vue create":

   ```
   vue create {{ PROJECT_NAME }}
   ```
3. You will then be presented with a few options. Here you can choose to get up and running using default presets, or you can manually choose what features you want for your project:

   ![Figure: Top-level options when running "vue create" using Vue CLI](screenshot-2023-07-13-at-3.54.28-pm.png)

   ![Figure: Manually selecting features instead of using a preset](screenshot-2023-07-13-at-3.54.48-pm.png)