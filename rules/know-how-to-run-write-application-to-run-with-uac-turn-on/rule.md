---
seoDescription: Run write application to run with UAC turn on requires adding App.Manifest and setting project settings for WindowsUI using requestedExecutionLevel level="requireAdministrator".
type: rule
title: Do you know how to run write application to run with UAC turn on?
uri: know-how-to-run-write-application-to-run-with-uac-turn-on
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:02:00.000Z
guid: d159fc8d-8b7f-4eb3-b6b8-8c193e69ca05
---

Some applications may need to have administrator right for running the application, e.g. create a file, access system library, etc. It will be an issue for the application to run if UAC is turned on. Below is the step to solve the issue:

<!--endintro-->

1. Add App.Manifest into WindowsUI project. It should contain the below code:

```xml
<?xml version="1.0" encoding="utf-8"?>
<asmv1:assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1" xmlns:asmv1="urn:schemas-microsoft-com:asm.v1"
  xmlns:asmv2="urn:schemas-microsoft-com:asm.v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <assemblyIdentity version="1.0.0.0" name="MyApplication.app"/>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
    <security>
      <requestedPrivileges xmlns="urn:schemas-microsoft-com:asm.v3">
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
      </requestedPrivileges>
    </security>
  </trustInfo>
</asmv1:assembly>
```

**App.Manifest**

2. Change the project settings for WindowsUI to use the newly created App.Manifest.

![Figure: Use the newly created App.Manifest](setmanifest.jpg)
