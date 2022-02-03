---
type: rule
title: Do you understand the value of Semantic Versioning?
uri: semantic-versioning
authors:
  - title: Jason Taylor
    url: https://www.ssw.com.au/people/jason-taylor/
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Adam Cogan
    url: "www.ssw.com.au/people/adam-cogan "
  - title: Andrew Harris
    url: www.ssw.com.au/people/andrew-harris
related:
  - packages-up-to-date
  - only-export-what-is-necessary
  - ways-to-version
created: 2022-02-02T05:56:54.309Z
guid: 85ee49a3-ac86-432b-8608-1056b42db8bf
---
Semantic versioning (sometimes called SemVer) allows library developers to communicate with those who use the library. In the old days, people would choose version numbers on gut feel or they would auto generate them. With Semantic Versioning, the version number conveys the type of changes since the last release and if any changes break backwards compatibility. **That way any developer who looks at the version number immediately knows the risk level when they update...**

<!--endintro-->

The structure of Semantic Versioning includes

* A major version e.g. 1.0.0 or 2.0.0
* A minor version e.g. 1.1.0 or 1.2.0
* A patch version e.g. 1.1.1 or 1.1.2

Every release should have a new version, so that when users provide feedback or bug reports, you know the version they were using.

## How it works - when should I increment each version?

### Major version ✨🐛

The major version will only be incremented when releasing non-backwards compatible changes (either features or bugs). For example, when something has become obsolete or an interface has changed fundamentally. When the Major version is incremented the minor and patch version both reset to 0. 

So 3.4.9 would go to 4.0.0

### Minor version ✨

If a new release includes a new backwards-compatible feature the minor version would be incremented by 1 and the patch version is reset to 0.

So 1.1.6 would go to 1.2.0

### Patch version 🐛

Patches are not for features, they are only for backwards-compatible bug fixes. In that case only the patch version is incremented.

So 2.2.0 would go to 2.2.1

### Pre-release version 😎

A pre-release version is for when you want to put out a major version but first you want to test out a beta version with early adopters. You can create a pre-release version by adding a hyphen and some letters 

So a pre-release version might look like 1.0.0-preview1

## Upgrading packages

As developers we are constantly upgrading the packages we depend on whether it be [yarn](https://yarnpkg.com/), [npm](https://www.npmjs.com/) or [NuGet](https://www.nuget.org/). Understanding Semantic Versioning allows us to upgrade more frequently, for example, if a package Semantic Version indicates there are only bug fixes then why wouldn't we update immediately.

The key benefit of Semantic Versioning is that you can be confident about the impact of upgrading to a particular version of a package. So, if you see the third number change, you can be sure it only has bug fixes. 

On the other hand, if you see the first number change, you can be sure it will have breaking changes. If you are upgrading to a major version you should check the release notes.

Regardless, of what version you upgrade to, you still need to test your application functions as normal.

## Additional resources

These are some awesome resources for learning more about Semantic Versioning.

[Semantic Versioning Documentation](https://semver.org)

`youtube: https://youtu.be/embed/rEgevIkqp2o`
**Video: The ever dapper and handsome Donovan Brown's talk on Semantic Versioning**