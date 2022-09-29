---
type: rule
title: Do you check before installing 3rd party libraries?
uri: installing-3rd-party-libraries
authors:
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement
related:
  - do-you-know-the-correct-license-to-use-for-open-source-software
created: 2022-09-29T06:41:32.765Z
guid: 5e456c50-2105-470d-9c2c-b744b1bd578a

---

Efficient software developers don't reinvent the wheel and know the right libraries to use. Using an already existing code that someone has written for our use case will speed up development time.

However, there are scenarios where the npm or NuGet libraries that you have integrated in a project brings overhead in the future. For example, the project is using a NuGet package is no longer being maintained and does not support the latest .NET version. This forces the development team to refactor the code to use another library in order to upgrade to the newest .NET.

Looking for the right library can help to minimise the chances of a project hitting these scenarios. Here are some of the common things to check before installing a library.


### 1. Value
Only install libraries that brings huge value to the project. Avoid installing libraries for these kind of usage:

❌ Libraries for trivial functions (e.g. `is-odd` - checking if a number is odd or not)

❌ Installing multiple libraries with duplicate use-cases (e.g. installing two component libraries `ngx-bootstrap` and `angular-material`)


Instead, look for these good usage candidates:

✅ One library for one use-case

✅ Libraries providing a complex standard use case and has been tested thoroughly (e.g. validating credit card number, validating email format).


### 2. Maintainability
Next thing to consider is the library’s lifespan. The last thing that we want is to integrate a library into our project to find out on next month that it is no longer supported.


Couple of things to check:

✅ High download count – Frequently used libraries are more likely to be supported longer

✅ Good maintainers profile – Library sponsored by big companies or names would like to last longer than a library maintained by a single person (e.g. React by Facebook).

✅ Updated recently – Checking the library’s last updated date is a good start to decide whether the library is actively maintained or not.

✅ Low GitHub issues count – Many unresolved serious issues is a good indicator that it is not actively maintained.

Another option for a company is to consider sponsoring the library. This supports the community and can improve the maintainability of a library.


### 3. Compatibility
Most libraries are built only for a specific version of a runtime / framework that they are targeting to.

E.g. the npm library `@angular/material@14.2.3` is only targeted for Angular 14 and nuget library `Microsoft.Extensions.DependencyInjection` `v6.0.0` only supports .NET 6.

This is important to make sure that the library is working as intended. 
Although some libraries can work on older versions, it’s a good idea to avoid being in this situation as this could introduce unintended bug which increases the overhead in debugging your code.


### 4. Quality
Next is to dive deep down into the details and check for the quality of the library itself.

Here are things to check:
- The maintainers's profile
  A great maintainers profile. Maintainers with a good presence in the community or doing a lot of contribution is a good boost of confidence in the library.

- Presence of a unit test and good coverages in the code.
  This improves our confidence that the code would less likely to break across versions

- Changelogs and versioning
  An excellent library will show a proper changelog between releases, allowing developers to check for any potential breaking changes.


### 5. Licensing
Not all libraries available are free to use. Depending on the license provided with the library, it can range from a free-to-use to a paid license.
Always check the license associated with the package before deciding to use it in production. You can check of common available licenses here on [Choosealicense.com](https://choosealicense.com/).


::: bad
![Figure: npm - uncommon license, need to check for conditions and fees](npm-bad-license.png)
:::

::: bad
![Figure: NuGet – uncommon license, need to check for conditions and fees](nuget-bad-license.png)
:::

::: good
![Figure: npm - MIT License, free to use](npm-good-license.png)
:::

::: good
![Figure: NuGet – MIT License, free to use](nuget-good-license.png)
:::


### 6. Bundle Characteristic
A huge benefit for client-side applications (Angular, React, or Blazor WASM) is to reduce the size of the code that a user needs to download (also known as bundles) to run our application. 
Installing and using many libraries can deteriorate this experience and increase the size of our application's bundle. 

#### JavaScript projects:
There are tools out there to help us figuring the cost of installing a library to our end bundle size (e.g. [BundlePhobia](https://bundlephobia.com) or [BundleJs](https://bundlejs.com)).

On top of this, we can also check for a library’s tree-shaking capability. Tree-shaking is a term commonly used on JavaScript which is a process to remove unused code from a library in the final bundle. Below is one handy tool for npm packages that we can use to quick-check for its tree-shaking capability.

```sh
npx is-esm [package-name]
```

::: bad
![Figure: Moment library is not tree-shakable, costing a huge bundle size in the production build](is-esm-bad.png)
:::

::: good
![Figure: date-fns library is tree-shakable, which can produce smaller bundle size in the production build](is-esm-good.png)
:::

### .NET Projects:
Unfortunately, there are no tools available yet to check for bundle size for nuget packages.

However, .NET provide built in feature to reduce the bundle size called [Trimmer](https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/trimming-options?pivots=dotnet-6-0), but these needs to be done carefully as apps that use reflection might not work as expected. [Read more about Trimmer here](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/configure-trimmer?view=aspnetcore-6.0).
