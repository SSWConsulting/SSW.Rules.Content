---
seoDescription: Do you provide a strongly typed wrapper for app.config properties to improve code readability and maintainability?
type: rule
title: Do you make a strongly-typed wrapper for app.config?
uri: do-you-make-a-strongly-typed-wrapper-for-appconfig
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T06:51:00.000Z
guid: d4123a64-239a-4251-9a22-1ba31e85b690
---

If your application accesses properties in app.config, you should provide a strongly typed wrapper for the app.config file. The following code shows you how to build a simple wrapper for app.config in an **AssemblyConfiguration** class:

<!--endintro-->

```cs
using System;
using System.Configuration;

namespace SSW.Northwind.WindowsUI
{
   public sealed class AssemblyConfiguration
   {
      // Prevent the class from being constructed
      private AssemblyConfiguration() { }

      public static string ConnectionString
      {
         get
         {
            return
               ConfigurationSettings.AppSettings["ConnectionString"].
               ToString();
         }
      }
   }
}
```

Unfortunately, the [Configuration Block](/do-you-use-configuration-management-application-block) does **not** automatically provide this wrapper.
