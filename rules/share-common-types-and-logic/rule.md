---
type: rule
title: Do you share common types and logic?
uri: share-common-types-and-logic
authors:
  - title: Jason Taylor
    url: https://ssw.com.au/people/jason-taylor
  - title: Brady Stroud
    url: https://ssw.com.au/people/brady-stroud
related: []
redirects:
  - do-you-share-common-types-and-logic
created: 2021-09-07T00:00:00.000Z
archivedreason: null
guid: cd07d952-b9ac-4f8e-a819-693288fd45f1
---
Due to Blazor using C#, your client and server can share the same model library - sharing behavior and data.

This will reduce the amount of code you need to write, and make it easier to maintain. 

<!--endintro-->

To share your classes between the client and server, just create a class library and reference it in your client and server projects.

See https://github.com/bradystroud/BlazorCodeSharingExample as an example.

### References

* [Blazor (Microsoft Docs)](https://docs.microsoft.com/en-us/aspnet/core/blazor)