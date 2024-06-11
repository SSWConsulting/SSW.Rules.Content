---
seoDescription: .NET wrapper compatibility on x64 and x86 platforms requires careful IntPtr management to avoid integer overflows.
type: rule
title: Do you know how to make .NET wrapper work on both x64 and x86 platforms?
uri: do-you-know-how-to-make-net-wrapper-work-on-both-x64-and-x86-platforms
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:02:00.000Z
guid: b82e36db-e95a-4ece-98b4-4a97625c88b3
---

Sometimes, we need to use .NET wrapper to call Windows built-in forms for implementing special functionalities. For example, calling the Directory Object Picker dialog enables a user to select objects from the Active Directory. MSDN provides an article and an example(C++) on [how to calling the Directory Object Picker dialog](https://ssw.com.au/ssw/redirect/msdn/DirectoryObjectPicker.htm), and the CodePlex website gives [a .Net version of implementation(C#)](https://ssw.com.au/ssw/redirect/codeplex/ActiveDirectoryCommonDialogs.htm).

However, all of this implementations only work on x86 platform, and will crash on x64 platform, regarding to this problem, the keynote is to understand the difference of IntPtr in between x64 and x86 platforms.

<!--endintro-->

- In x86 platform, IntPtr = Int32
- In x64 platform, IntPtr = Int64

So, To fix the crash, we should re-write the code below:

```cs
DSOP_SCOPE_INIT_INFO[] scopeInitInfo = new DSOP_SCOPE_INIT_INFO[2];

IntPtr refScopeInitInfo = Marshal.AllocHGlobal(Marshal.SizeOf (typeof (DSOP_SCOPE_INIT_INFO)) * 2);

Marshal.StructureToPtr (scopeInitInfo[0], refScopeInitInfo,true);

Marshal.StructureToPtr(scopeInitInfo[1], (IntPtr)((int)refScopeInitInfo + Marshal.SizeOf(typeof(DSOP_SCOPE_INIT_INFO))), true);
```

::: bad
Bad example - The code above always gets crash in x64 platform, because of an integer overflow and result in a segmentation fault in 64 bits.
:::

```cs
IntPtr refScopeInitInfo = Marshal.AllocHGlobal(Marshal.SizeOf(typeof(DSOP_SCOPE_INIT_INFO)) * 2);

int scopeInitInfoSize = Marshal.SizeOf (typeof (DSOP_SCOPE_INIT_INFO));

int offset = scopeInitInfoSize;

IntPtr scopeInitInfo = (IntPtr)(refScopeInitInfo.ToInt64() + offset);
```

::: good
Good example - The Directory Object Picker dialog works on both x64 and x86 platforms well when using the good code above.
:::

::: bad
![Figure: Bad example - Calling the Directory Object Picker dialog causes crash on x64 platform when using the bad code above](crash.jpg)
:::

::: good
![Figure: Good example - The Directory Object Picker dialog works on both x64 and x86 platforms well when using the good code above](worknormal.jpg)
:::
