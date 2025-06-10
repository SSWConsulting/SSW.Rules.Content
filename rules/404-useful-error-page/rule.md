---
type: rule
title: Do you have a useful 404 error page?
seoDescription: Enhance your ASP.NET site's user experience with a custom 404
  error page that redirects visitors effectively.
uri: 404-useful-error-page
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
related:
  - 404-error-avoid-changing-the-url
redirects:
  - do-you-replace-the-404-error-with-a-useful-error-page
created: 2016-08-11T17:30:01.000Z
archivedreason: null
guid: a006213a-e97b-46a7-a66b-beb52b205533
---
Error page, you say? But you worked so hard to make sure everything runs perfectly! The thing is, even the best sites aren’t immune to the occasional misstep. Sometimes users just type a URL wrong. It happens.

A well-designed custom error page encourages surfers to remain in your site and help them to the right page. Although it's possible to redirect error codes straight to your homepage, that doesn't tell visitors what's going on. 

A branded 404 (error) page also reinforces your identity and keeps the user experience consistent, even when things go wrong. It shows professionalism and helps maintain trust.

Consider adding a button to your homepage here, or your site's search functionality if applicable.

<!--endintro-->

::: bad
![Figure: Bad example - Unhandled error](404-bad.png)
:::

::: good
![Figure: Good example - Custom error page](404-good.png)
:::

::: good
![Figure: Good example - Playful branding turns an error case into a less negative experience](mailchimp-404.png)
:::

## .NET Core (Server-Side)

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    // Turn on error handling middleware
    app.UseExceptionHandler("/Error");
}

// Use status code page routes (eg. /Error/404, /Error/500)
app.UseStatusCodePagesWithReExecute("/Error/{0}");

// Turn on routing
app.UseRouting();

// Map your endpoints
app.MapGet("/Error/{statusCode}", async (HttpContext httpContext, int statusCode) =>
{
    // Preserve the status code in the response
    httpContext.Response.StatusCode = statusCode;

    if (statusCode == 404)
    {
        // Return a custom "404 Not Found" response        
        httpContext.Response.ContentType = "text/html";
        await httpContext.Response.WriteAsync("<h1>Sorry, we couldn’t find that page.</h1>");
    }
    else
    {
        // For other status codes, return a generic error
        httpContext.Response.ContentType = "text/html";
        await httpContext.Response.WriteAsync($"<h1>An error occurred (status code: {statusCode}).</h1>");
    }
});

// Any endpoint mappings or other middleware
app.MapGet("/", () => "Hello World!");

app.Run();
```

::: good
Figure: Good example - Wildcard routing of unrecognised paths
:::

## Angular (Client-Side)

Inside your Angular project you can update the app-routing module to catch any unrecognised paths

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  // ... your other routes here ...
  { path: '**', component: NotFoundComponent } // wildcard route
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: false })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

::: good
Figure: Good example - Wildcard routing of unrecognised paths
:::

```html
<!-- not-found.component.html -->
<div class="not-found">
  <h1>404 - Page Not Found</h1>
  <p>We’re sorry, but we couldn’t find the page you requested.</p>
  <a routerLink="/">Go back to Home</a>
</div>
```

::: good
Figure: Good example - The custom 404 html page
:::

## React.js (Client-Side)

```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
import NotFound from './NotFound';

function App() {
  return (
    <Router>
      <Routes>
        {/* Your valid routes: */}
        <Route path="/" element={<Home />} />
        {/* Add other valid routes here */}

        {/* "Catch-all" or wildcard route for anything that doesn't match */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
```

::: good
Figure: Good example - The custom 404 pages
:::

## ASP .NET

```xml
<customErrors mode="Off"></customErrors>
```

::: bad
Figure: Bad example - The default code on web.config
:::

```xml
<customErrors mode="RemoteOnly" defaultRedirect="/ssw/ErrorPage.aspx">
<error statusCode="404" redirect="/ssw/SSWCustomError404.aspx">
</customErrors>
```

::: good
Figure: Good example - The custom code in the web.config
:::

For ASP.NET website, the detailed information would be presented to the remote machines when an unhandled error occurs if the customErrors mode is off.

This error information is useful for the developer to do debugging. However, it would leak out some confidential information which could be used to get into your system by the hackers. We can assume that if a SQL exception occurs by accident, which may expose database sensitive information (e.g. connection string; SQL script). So, to prevent these leaks, you should set the "mode" attribute of the tag &lt;customerrors&gt; to "RemoteOnly" or "On" in the web.config file and create a user-friendly customized error page to replace the detailed error information.

```xml
<customErrors mode="RemoteOnly" defaultRedirect="GenericErrorPage.htm"></customErrors>
```

::: good
Figure: Good example - Turning on "customErrors" protects sensitive information against Hacker
:::
