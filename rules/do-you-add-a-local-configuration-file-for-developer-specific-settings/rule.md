---
type: rule
title: Do you add a local configuration file for developer-specific settings?
uri: do-you-add-a-local-configuration-file-for-developer-specific-settings
created: 2019-01-11T19:45:12.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p>With .NET Core, we've got a new, extensible configuration system for our projects. This is easily extended and has out-of-the-box support for many configuration sources including JSON files, per-environment overrides, command-line parameters, and environment variables.</p><p>A common source of pain when working in a team is when different team members require different connection strings in order to run the project locally. If the developer modifies settings and then accidentally pushes that change into source control, the app might break for other developers.</p> </span>

<p>Resolve this by&#58;</p><dl class="image"><dt><img src="/PublishingImages/local-config-file-1.png" alt="local-config-file-1.png" /></dt><dd>Figure&#58; #1 Create an appsettings.Local.json file. Set this to be ignored by your source code control system</dd></dl><dl class="image"><dt><img src="/PublishingImages/local-config-file-2.jpg" alt="local-config-file-2.jpg" /></dt><dd>Figure&#58; #2 ​Add code to apply this configuration file in Program.cs</dd></dl><p>Now, any new developer that needs a custom connection string (or any other configuration setting) can create their own appsettings.Local.json file without affecting any other team member’s configuration.</p>


