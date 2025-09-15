---
seoDescription: .NET developers can customize their project settings by adding a local configuration file, isolating changes and preventing app breakage for team members.
type: rule
archivedreason:
title: Do you add a local configuration file for developer-specific settings?
guid: 3687d1f8-1a96-476c-898e-a363fa4ae599
uri: add-local-configuration-file-for-developer-specific-settings
created: 2019-01-11T19:45:12.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Brendan Richards
    url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
  - do-you-add-a-local-configuration-file-for-developer-specific-settings
---

With .NET Core, we've got a new, extensible configuration system for our projects. This is easily extended and has out-of-the-box support for many configuration sources including JSON files, per-environment overrides, command-line parameters, and environment variables.

A common source of pain when working in a team is when different team members require different connection strings in order to run the project locally. If the developer modifies settings and then accidentally pushes that change into source control, the app might break for other developers.

<!--endintro-->

Resolve this by:

![Figure: #1 Create an appsettings.Local.json file. Set this to be ignored by your source code control system](local-config-file-1.png)

![Figure: #2 Add code to apply this configuration file in Program.cs](local-config-file-2.jpg)

Now, any new developer that needs a custom connection string (or any other configuration setting) can create their own appsettings.Local.json file without affecting any other team member’s configuration.
