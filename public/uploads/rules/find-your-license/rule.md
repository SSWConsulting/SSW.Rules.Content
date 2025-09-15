---
seoDescription: Discover the best license for your open-source project on GitHub and ensure financial sustainability while supporting the open-source community.
type: rule
title: Do you know the best license for your project?
uri: find-your-license
authors:
  - title: Tylah Kapa
    url: https://www.ssw.com.au/people/tylah-kapa/
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay/
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming/
created: 2024-04-05T03:45:24.386Z
guid: d4f35ecb-7e7f-4f96-af43-b4c8b9e9eb72
related: []
redirects: []
archivedreason: null
---

Some companies want to keep their projects closed-source in order to profit from their products. However, there are several benefits to keeping the source open including:

- Community contribution and feedback
- Allowing controlled free use of your products

We want our projects to be financially sustainable while supporting the open-source space. Let's take a look at the licensing options for open-source projects on GitHub.

<!--endintro-->

:::info
This is not legal advice. If you want to explore your options around licensing your projects please consult your lawyer.
:::

## Option 1 - No License

As per GitHub's [documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository), no author is obligated to choose a license for their project. Without a license, the default copyright laws will apply.

### Pros

- No Effort: No effort required on the author's part.
- Some control: Retains some control of the source-code.

### Cons

- Not Permissive: Generally, users will have no permission from the author to use, modify or share the software. However, GitHub allows users to Fork and view code as a part of their terms.

## Option 2 - MIT

The [MIT License](https://choosealicense.com/licenses/mit/) is a well known license trusted by many open-source projects.

Examples include:

- [Dotnet](https://github.com/dotnet/runtime/blob/main/LICENSE.TXT)
- [Ruby on Rails](https://github.com/rails/rails/blob/main/MIT-LICENSE)

### Pros

- Permissive: Allows for commercial and private use as well as distribution and modification of the author's software.
- Collaboration + Community: Promotes an open and collaborative environment with community feedback.
- Short and simple: The text of the license is simple and quick to understand.

### Cons

- Limited Patent Protection: The MIT License doesn't include explicit patent grants or protections.
- Lack of clarity on Trademarks: The license doesn't address the use of Trademarks associated with the software

## Option 3 - Copyleft (e.g. GPL)

A copyleft license like the [Gnu Public License](https://choosealicense.com/licenses/gpl-3.0/) promote and protect the principals of open-source software. Though they may also introduce complexities and potential limitations that users may be deterred by.

Examples include:

- [Ansible](https://github.com/ansible/ansible/blob/devel/COPYING)
- [Bash](https://git.savannah.gnu.org/cgit/bash.git/tree/COPYING)

### Pros

- Collaboration + Community: Promotes an open and collaborative environment with community feedback.
- Protection Against Exploitation: Guards against consumers taking the source code and making proprietary modifications in a closed environment.

### Cons

- Complexity: Some developers and organizations may find a copyleft license to be too complex and stringent.
- Perceived Risk: Copyleft licenses may discourage contributors or participators through perceived risk.

## Option 4 - Proprietary

Companies often use a proprietary license when they prefer to have fine-grained control over their intellectual property.

Examples include:

- [Mozilla](https://www.mozilla.org/en-US/MPL/)
- [Duende](https://duendesoftware.com/license)

### Pros

- Better control: Authors have fine-grained control over their source code and how it's used.
- Benefits of community development: Authors can still benefit from the community engaging with their source code

### Cons

- Cost: Drafting and iterating upon your license will cost time and money.
- Bad actors: Authors will need to be vigilant of bad actors abusing the license and choose to pursue them.

## Option 5 - Functional Source License (FSL)

Sentry introduced the [FSL](https://fsl.software/) as a way to support the open-source community whilst retaining control over their IP.

Examples of projects with this license include:

- [Sentry](https://github.com/getsentry/self-hosted/blob/master/LICENSE.md)
- [GitButler](https://github.com/gitbutlerapp/gitbutler/blob/master/LICENSE.md)

### Pros

- Protection: Retains control over source code for up to 2 years
- Free and Open-Source Software (FOSS) Values: Automatically converts to MIT/Apache 2.0 licensing after 2 years
- Continual Iteration: Pushes the author to continually iterate on their project or risk third-parties competing with a forked version of the project.

### Cons

- Not strictly Open-Source: While Sentry values FOSS, this license does not meet the strict definition of open-source.
