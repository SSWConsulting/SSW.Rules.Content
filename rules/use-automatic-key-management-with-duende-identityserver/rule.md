---
seoDescription: Automatically manage keys and simplify IdentityServer configuration with out-of-the-box features in version 5.
type: rule
archivedreason:
title: Do you use Automatic Key management with Duende IdentityServer?
guid: b045ffb9-254e-49e0-a971-31a4f6eb4ae7
uri: use-automatic-key-management-with-duende-identityserver
redirects:
  - use-automatic-key-management-with-duende-identityServer
created: 2021-03-17T09:45:07.0000000Z
authors:
- title: Anthony Nguyen
  url: https://ssw.com.au/people/anthony-nguyen/
- title: William Liebenberg
  url: https://ssw.com.au/people/william-liebenberg/
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related:

---

When using IdentityServer 5 (aka Duende IdentityServer), you don't need to use `UseDeveloperSigningCredentials()` anymore as it is now enabled by default.

<!--endintro-->

```cs
services.AddIdentityServer()
    .AddInMemoryClients(new List<Client>())
    .AddInMemoryIdentityResources(new List<IdentityResource>())
    .AddInMemoryApiResources(new List<ApiResource>())
    .AddInMemoryApiScopes(new List<ApiScope>())
    .AddTestUsers(new List<TestUser>())
    .AddDeveloperSigningCredential();
```

::: bad
Figure: Bad example - you don't need to use `.AddDevelopersSigningCredential()` anymore
:::

When using version 5, instead of using `IdentityServer4.AccessTokenValidation()`, you should use the out of the box `AddAuthentication(("Bearer").AddJwtBearer("Bearer")` from .NET 5

```cs
services.AddAuthentication("Bearer")
    .AddIdentityServerAuthentication("Bearer", options =>
    {
        options.ApiName = "api1";
        options.Authority = "https://localhost:5000";
    });
```

::: bad
Figure: Bad example - don't use `IdentityServer4.AccessTokenValidation` package as it is deprecated.
:::

```cs
services.AddAuthentication("Bearer") 
  .AddJwtBearer("Bearer", options =>
    {
      options.Audience = "api1";
      options.Authority = "https://localhost:5000";
    });
```

::: good
Figure: Good example - use `AddJwtBearer("Bearer")` instead
:::
