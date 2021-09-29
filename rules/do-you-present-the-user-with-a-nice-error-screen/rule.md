---
type: rule
title: Do you present the user with a nice error screen?
uri: do-you-present-the-user-with-a-nice-error-screen
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Jake Bayliss
    url: https://www.ssw.com.au/people/jake-bayliss
related: []
redirects:
  - do-you-present-the-user-with-a-nice-error-screen-(web-only)
  - do-you-present-the-user-with-a-nice-error-screen-web-only
created: 2013-09-11T21:08:47.000Z
archivedreason: null
guid: 4ee8ca41-78bb-40c1-94cc-cf44a3b47622
---

Your users should never see the “yellow screen of death”. Errors should be caught, logged and a user-friendly screen displayed to the user.

<!--endintro-->

::: bad
![Figure: Bad Example – ASP.NET Yellow Screen of Death](error-screen-bad.png)
:::

::: bad 
![Figure: Bad Example - Default exception page](net-core-default.png)
:::

::: good  
![Figure: Good Example - GitHub custom error page](error-screen-good.png)
:::

However, as a developer you still want to be able to view the detail of the exception in your local development environment. 

## How-to set up development environment exception pages in ASP.NET Core

To set up exceptions in your local development environment you need to configure the Developer Exception Page middleware in the request processing pipeline.
Unless you have modified the default template, it should work out of the box. Here are the important lines:

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/Error");
        app.UseHsts();
    }
    ...
}
```

::: good  
![Figure: This is how you set it up in .NET 5](net-core-development.png)
:::

Find out more about exception handling in .NET Core 5 [here](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-5.0).
