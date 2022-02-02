---
type: rule
title: Do you understand the value of Semantic Versioning?
uri: semantic-versioning
authors:
  - title: Jason Taylor
    url: https://www.ssw.com.au/people/jason-taylor/
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - packages-up-to-date
  - only-export-what-is-necessary
created: 2022-02-02T05:56:54.309Z
guid: 85ee49a3-ac86-432b-8608-1056b42db8bf
---
Semantic versioning (sometimes called SemVer) allows library developers to communicate with those who use the library. In the old days, people would choose version numbers on gut feel or auto generated. With Semantic Versioning, the version number conveys the type of changes since the last release and if any changes break backwards compatibility. That way any developer who looks at it knows the risk level when they update...
            
<!--endintro-->

The structure of Semantic Versioning includes
* A major version e.g. 1.0.0 or 2.0.0
* A minor version e.g. 1.1.0 or 1.2.0
* A patch version e.g. 1.1.1 or 1.1.2

Every release should have a new version so that when users provide feedback or bug reports you know the version they were using.

## How it works - When should I increment each version?

### Patch version

If the current version is 1.1.0 and the new release includes only backwards-compatible bug fixes then the new version number will be 1.1.1 (the patch version has been incremented by 1)

### Minor version

Following on from this, if a new release includes a new backwards-compatible feature the minor version would be incremented by 1 and the patch version is reset to 0, 1.2.0

### Major version

The major version will only be incremented when releasing non-backwards compatible changes. For example, when something has become obsolete or an interface has changed fundamentally.

### Pre-release version

A pre-release version is for when you want to put out a major version but first you want to test out an unstable version with early adopters. You can create a pre-release version by adding a hyphen and some letters e.g. 1.0.0-preview1

## Upgrading packages

As developers we are constantly upgrading the packages we depend on whether it be [yarn](https://yarnpkg.com/), [npm](https://www.npmjs.com/) or [NuGet](https://www.nuget.org/). Understanding Semantic Versioning allows us to upgrade more frequently, for example, if a package Semantic Version indicates there are only bug fixes then why wouldn't we update immediately.

The key benefit of Semantic Versioning is that you can be confident about the impact of upgrading to a particular version of a package. So for example, you can be sure that the version only has bug fixes or that it will have breaking changes.

If we are upgrading to a major version you should check the release notes so you understand what the breaking changes are and how it will impact the solution.

Regardless, of what version you upgrade to, you still need to test your application functions as normal.

## Additional resources

These are some awesome resources for learning more about Semantic Versioning.

[https://semver.org/](Semantic Versioning Documentation)

`youtube: https://youtu.be/embed/rEgevIkqp2o`
**Video: Donovan Brown's talk on Semantic Versioning**
