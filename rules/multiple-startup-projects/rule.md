---
type: rule
archivedreason: 
title: .NET - Do you set multiple startup projects?
guid: eeb680ed-ae48-4733-962d-bfac17f00dcd
uri: multiple-startup-projects
created: 2023-08-17T12:00:00.0000000Z
authors:
- title: Jack Reimers
  url: https://ssw.com.au/people/jack-reimers
related:
- developer-experience
- project-setup
---

It's common for .NET projects to have multiple projects in a single solution, for example an API and a UI.
Did you know Microsoft Visual Studio and Jetbrains Rider allow you to start as many projects as you want with a single click?

<!--endintro-->

::: bad

### Split Terminals
You can run each project in a seperate terminal 

:::

::: greybox  
**Note:** If you change the launch profile Visual Studio **will not** save your configuration and you will have to follow the above steps again.  
:::

::: greybox  
**Note:** Rider **will** save the launch profile you just created, you can switch between launch profiles without losing your configuration.  
:::
