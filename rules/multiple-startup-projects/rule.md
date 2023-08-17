---
type: rule
archivedreason: 
title: Do you set multiple startup projects?
guid: abe10968-bfa3-4113-862b-918774c89492
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

3. Select `Multiple Startup Projects`:

4. Set the dropdown next to each project you want to start to `Start` and click `Ok`:

5. Check that the dropdown next to the `Start` button shows `<Multiple Startup Projects>` and click `Start`:

### Jetbrains Rider
1. Click the launch profile dropdown in the top right of the window:  


2. Click `Edit Configurations...`:  


3. Click the `+` button in the top left of the window:  


4. Click `Compound`:  


5. Give the launch profile a name and add `WebUI` and `WebAPI:https` using the `+` button:


6. Ensure your new launch profile is selected and then run the project:  
