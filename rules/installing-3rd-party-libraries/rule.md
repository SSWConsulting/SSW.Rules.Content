---
type: rule
title: Do you check before installing 3rd party libraries?
uri: installing-3rd-party-libraries
authors:
  - title: Chris Clement
    url: https://www.ssw.com.au/people/chris-clement
related:
  - do-you-know-the-correct-license-to-use-for-open-source-software
  - monitor-packages-for-vulnerabilities
  - package-audit-log
  - document-discoveries
created: 2022-09-29T06:41:32.765Z
guid: 5e456c50-2105-470d-9c2c-b744b1bd578a
---
Efficient software developers don't reinvent the wheel and know the right libraries to use. Using an existing and well-tested library will speed up development time.

However, there are scenarios where the libraries integrated in a project bring overhead in the future. For example, if a project is using a NuGet package that is no longer being maintained and does not support the latest .NET version. This incompatibility would force the development team to refactor the code to use another library if they wish to use the latest version of .NET.

<!--endintro-->

`youtube: https://www.youtube.com/embed/1LPK3jgga_c`

Looking for the right library can help to minimize the chances of a project hitting these scenarios. Here are some of the common things to check before installing a library:

![](3rd-party-check-logos_1710232021941.png)

### 1. Is it valuable?

Only install libraries that bring big value to the project.

❌ Libraries for trivial functions (e.g. `is-odd` - checking if a number is odd or not)

❌ Installing multiple libraries with duplicate use-cases (e.g. installing two component libraries [Angular Material](https://material.angular.io) and [NG-ZORRO Ant Design](https://ng.ant.design/docs/introduce/en))

✅ One library for one use-case
e.g. one for component, one for authentication

✅ Libraries providing complex or standard use cases that have been tested thoroughly 
e.g. validating credit card numbers, validating email format

### 2. Is it actively maintained?

The next thing to consider is the library’s lifespan. The last thing that we want is to integrate a library into our project only to find out that next month it will no longer be supported.

Couple of things to check:

✅ High download count – Frequently used libraries are more likely to be supported longer.

✅ Recently updated – Checking the library’s last updated date is a good start to decide whether the library is actively maintained or not.

✅ Good maintainers profile – Libraries sponsored by big companies (e.g. Angular by Google) or established names would be more likely to last longer than a library maintained by an unknown person.

✅ Low GitHub issues count – Many unresolved serious issues may be an indicator that the library is not actively maintained.

::: bad
![Figure: Bad example - Unmaintained library - little to no activity - https://github.com/douglasgsouza/mat-row-keyboard-selection/pulse/monthly](lib-not-maintained.png)
:::

::: good
![Figure: Good example #1 - Popular npm library with lots of stars and recently updated- https://github.com/date-fns/date-fns](lib-well-maintained.png)
:::

::: good
![Figure: Good example #2 - Well maintained and active library - https://github.com/date-fns/date-fns/pulse/monthly](lib-well-maintained-2.png)
:::

### 3. Is it compatible?

Most libraries are only built for a specific version of a runtime / framework.

e.g. The npm library `@angular/material@14.2.3` is only targeted for Angular 14 and NuGet library `Microsoft.EntityFrameworkCore` `v6.0.7` only supports .NET 6.

It is important to check the compatibility to make sure that the library will work as intended. 

Although some libraries can work with older framework versions, it’s a good idea to avoid being in this situation as this could introduce unintended bugs which increase the overhead in debugging your code.

### 4. Is it high quality?

Next is to dive deep down into the details and check for the quality of the library itself.

Here are things to check:

✅ Maintainer's profile - A high profile maintainer with a good presence in the community or who is doing a lot of contribution provides a good boost of confidence in the library.

✅ Presence of unit tests and good coverages - This improves our confidence that the code will not break across versions

✅ Changelogs and versioning - Good changelogs between releases enable developers to check for any potential breaking changes.

### 5. Is it an appropriate license?

Not all libraries available on [npmjs](https://npmjs.com) and [NuGet](https://nuget.org) are free to use. The library license can range from free-to-use to paid.

Always check the license associated with the package before deciding to use it in production. You can check common available licenses on [choosealicense.com](https://choosealicense.com).

::: bad
![Figure: Bad example - npm - uncommon license, need to check for conditions and fees - https://npmjs.com/package/highcharts](npm-bad-license.png)
:::

::: bad
![Figure: Bad example - NuGet – uncommon license, need to check for conditions and fees - https://nuget.org/packages/PDFTron.NET.x64](nuget-bad-license.png)
:::

::: good
![Figure: Good example - npm - MIT License, free to use - https://npmjs.com/package/date-fns](npm-good-license.png)
:::

::: good
![Figure: Good example - NuGet – MIT License, free to use - https://nuget.org/packages/Newtonsoft.Json/13.0.1](nuget-good-license.png)
:::

### 6. What are the bundle characteristics?

Client-side applications (Angular, React, or Blazor WASM) benefit hugely from reducing the size of the code that a user needs to download (also known as bundles) to run our application. 

Installing and using many libraries can increase the size of our application's bundle and slow down these client-side applications. Staying aware of the bundle characteristics and optimising the size where possible can ensure that we keep our application start-up quick.

#### JavaScript projects

There are tools out there to help us figure out the impact of installing a library on our end bundle size 
e.g. [BundlePhobia](https://bundlephobia.com) or [BundleJs](https://bundlejs.com)

On top of this, we can also check for a library’s tree-shaking capability. Tree-shaking is a process to remove unused code from a library in the final bundle.

Unfortunately, there's no easy way to know if a library is tree-shakable other than to read the documentation and experiment with tools such as [BundleJs](https://bundlejs.com) to see the final bundle size when importing several items from the library.

#### .NET Projects

Unfortunately, there are no tools available yet to check for bundle size of NuGet packages.

To reduce the final build size, .NET provide a built in feature  [Trimmer](https://learn.microsoft.com/en-us/dotnet/core/deploying/trimming/trimming-options?pivots=dotnet-6-0), but these needs to be done carefully as apps that use reflection might not work as expected. [Read more about Trimmer](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/configure-trimmer?view=aspnetcore-6.0).

### 7. Have you documented the decision?

* **Have a 2nd pair of eyes** - Lastly before deciding to install the library, check with another developer that is experienced in the scope of your project (e.g. look for a senior JavaScript developer's opinion if the project is an Angular project). Having a 2nd qualified person to agree with your decision is a good indicator that you are picking a good library.
* **[Document the decision](/document-discoveries)** - Always keep track of the reasoning when developers decided to go with a particular library instead of another one. This helps future developers working on a project to maintain the project. Future developers will have better context and will be able to make a better decision should there be any situational or business requirement changes. A [package audit log](/package-audit-log) is a great way to record all the decisions.

::: good
![Figure: Good example - A markdown file should include your reasons to assist future developers](md-reasons.png)
:::
