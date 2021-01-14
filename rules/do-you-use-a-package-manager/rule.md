---
type: rule
archivedreason: 
title: Do you use a package manager?
guid: 761d75b9-55e6-48bc-bc80-2e02149508a0
uri: do-you-use-a-package-manager
created: 2016-06-17T06:29:18.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []

---

A package manager is a collection of software tools that automate the process of installing, upgrading, configuring, and uninstalling computer programs in a consistent manner. [Chocolatey](https://chocolatey.org/) is a great package manager, easy to use way to manage software on Windows. 

<!--endintro-->


::: ok  
![](chocolatey.png)  
:::

To get started with Chocolatey open up Command Prompt in Administrative mode, type in:


```
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
```


Alternatively, [install Chocolatey via their website](https://chocolatey.org/install).

Alternatives: Homebrew on a Mac
