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

### Visual Studio
1. Click the dropdown arrow next to the `Start` button:
[](vs-step1.png)

2. Click `Configure Startup Projects...`:
[](vs-step2.png)

3. Select `Multiple Startup Projects`:
[](vs-step3.png)

4. Set the dropdown next to each project you want to start to `Start` and click `Ok`:
[](vs-step4.png)

5. Check that the dropdown next to the `Start` button shows `<Multiple Startup Projects>` and click `Start`:
[](vs-step5.png)

::: greybox  
**Note:** If you change the launch profile Visual Studio **will not** save your configuration and you will have to follow the above steps again.  
:::

### Jetbrains Rider
1. Click the launch profile dropdown in the top right of the window:  
[](rider-step1.png)

2. Click `Edit Configurations...`:  
[](rider-step2.png)

3. Click the `+` button in the top left of the window:  
[](rider-step3.png)

4. Click `Compound`:  
[](rider-step4.png)

5. Give the launch profile a name and add `WebUI` and `WebAPI:https` using the `+` button:
[](rider-step5.png)

6. Ensure your new launch profile is selected and then run the project:  
[](rider-step6.png)

::: greybox  
**Note:** Rider **will** save the launch profile you just created, you can switch back to a single project without losing your configuration.  
:::
