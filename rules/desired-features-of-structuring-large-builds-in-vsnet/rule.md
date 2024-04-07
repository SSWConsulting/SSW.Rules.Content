---
type: rule
title: Do you know the desired features of structuring large Builds in VS.NET?
uri: desired-features-of-structuring-large-builds-in-vsnet
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:53:00.000Z
guid: e576f1eb-076a-4371-a505-12cf0d4c38fb
---

The desired features of structuring large Builds in VS.NET:
            
<!--endintro-->

1. **Scalable** - The project should allow continuous additions to the structure
   - Developers should be able to keep adding to the structure

2. **Multiple Versions** - The project should support multiple product releases
   - The structure should be able to allow developers to work on the next release while there is still work in progress for a previous release of another section of the project
   - Developers can work side by side with different versions in parallel (i.e. at the same time)

3. **Efficient** - The build should be as quick as possible
4. **Reliability** - Builds should be reproducible on any machine and reliable
5. **Switchable** - The project should be able to switch between debug release and other versions
   - The project should be able to activate without debug.
   - A config should be made for a demo build.
   - It should support a full release.

