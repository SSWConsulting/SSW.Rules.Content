---
seoDescription: Migrate to System.Text.Json for faster performance and lower memory usage, but check compatibility with Newtonsoft.Json features and default serialisation property name casing.
type: rule
title: Do you check your API serialisation format?
uri: do-you-check-your-api-serialisation-format
authors:
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement/
related:
  - dotnet-upgrade-assistant
  - migrate-from-system-web-to-modern-alternatives
  - migration-plans
  - modernize-your-app
created: 2024-05-13T05:45:10.297Z
guid: 5d3f3d8d-161f-4fdd-9721-e4e9f37de9ac
---

Most REST APIs serialise/deserialise to and from JSON format. To perform this serialisation, a .NET web application typically relies on either `Newtonsoft.Json` or `System.Text.Json`.

Modern .NET applications prefer `System.Text.Json` over `Newtonsoft.Json` - which is commonly found in earlier versions of .NET and .NET Framework projects.
This, however, may break in certain usages.

This issue needs to be addressed when migrating projects from .NET Framework to modern .NET.

<!--endintro-->

The primary reason for switching to `System.Text.Json` is its [faster performance and lower memory usage](https://devblogs.microsoft.com/dotnet/the-convenience-of-system-text-json/) compared to `Newtonsoft.Json`. However, it also breaks compatibility and lacks some features found in `Newtonsoft.Json`.

## The differences

[This Microsoft documentation](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/migrate-from-newtonsoft?pivots=dotnet-9-0#table-of-differences) contains a compiled list of differences between `System.Text.Json` and `Newtonsoft.Json`.

### Notable Things to Check

- ⚠️ **Default Serialisation Property Name Casing**

  Since .NET Core 3.0, the default behaviour for JSON property name serialisation has switched to `camelCase`, whereas earlier versions followed the class's property names as-is (usually in `PascalCase`).
  Couple of options to address this when migrating controllers from legacy endpoints while maintaining compatibility:

  - **Option A:** Implement a per-controller override for migrated legacy APIs to maintain the same behaviour by setting `JsonSerializerOptions.PropertyNamingPolicy = null`, e.g., via a custom attribute using `ActionFilterAttribute`.
  - **Option B:** Apply a global JSON serialisation override to retain `JsonSerializerOptions.PropertyNamingPolicy = null`.

- ⚠️ **No Support for JSON Patch Documents**

  Deserialisation of JSON Patch documents might fail due to [lack of support for JSON Path queries](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/migrate-from-newtonsoft?pivots=dotnet-9-0#json-path-queries-not-supported), e.g., commonly used in legacy `PATCH` endpoints.

- ⚠️ **Limited OData Support**

  OData might not work as expected when using `System.Text.Json`. See more: [Example issues](https://github.com/OData/AspNetCoreOData/issues/424).

- ⚠️ **Limited Support for Date Formats**

  While `System.Text.Json` [supports the ISO 8601-1:2019 format](https://learn.microsoft.com/en-us/dotnet/standard/datetime/system-text-json-support#the-extended-iso-8601-12019-profile-in-systemtextjson) for date and time components, `Newtonsoft.Json` accommodates a broader range of date-time strings. For example, `System.Text.Json` cannot deserialise the format `8:00am February, 24 2024`.
