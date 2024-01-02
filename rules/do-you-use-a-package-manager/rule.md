---
type: rule
title: Do you use a package manager?
uri: do-you-use-a-package-manager
authors:
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
  - title: Daniel Mackay
    url: https://github.com/danielmackay
related: []
redirects: []
created: 2016-06-17T06:29:18.000Z
archivedreason: null
guid: 761d75b9-55e6-48bc-bc80-2e02149508a0
---
A package manager is a collection of software tools that automate the process of installing, upgrading, configuring, and uninstalling computer programs in a consistent manner.

<!--endintro-->

## Option 1: Chocolatey (Recommended)

Chocolatey is a great package manager. It is an easy-to-use way to manage software on Windows. 

![Figure: installing Git with Chocolatey](chocolatey.png)

To get started, open PowerShell and [follow the instructions on the Chocolatey website](https://chocolatey.org/install).

::: info

It is better to run Chocolatey in PowerShell - it may work in Command Prompt, but you're likely to have permission issues.

:::

![Figure: Chocolatey installation page](choco-install.jpg)

## Option 2: Winget

[Winget](https://learn.microsoft.com/en-us/windows/package-manager/) is Microsoft's own package manager that developers can use to discover, install, upgrade, remove and configure a curated set of applications.

Winget can be installed from the [Microsoft Store.](https://www.microsoft.com/p/app-installer/9nblggh4nns1#activetab=pivot:overviewtab)

Once installed you can search for a tool with:

```bash
winget search {{ APP NAME }}
```

And then install the tool with:

```bash
winget install {{ APP NAME }}
```

For example:

![Figure: Installing powertoys via winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/images/install.png "Installing powertoys via winget")

For more information see [MS Learn](https://learn.microsoft.com/en-us/windows/package-manager/winget/).

## Option 3: Homebrew

[Homebrew](https://brew.sh/) is the preferred option when on a Mac. Head to their website for installation instructions: https://brew.sh/

![Figure: Homebrew installed](homebrew.png)