---
type: rule
title: Do you know how to handle redirects?
seoDescription: Upgrade your website seamlessly with efficient redirects using
  Cloudflare Workers or Azure Front Door to preserve SEO and traffic during the
  migration.
uri: handle-redirects
authors:
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
related:
  - use-a-cdn
  - use-301-redirect-on-renamed-or-moved-pages
created: 2024-06-14T06:32:40.000Z
archivedreason: null
guid: 746cfdd5-68d6-4080-b4c8-af73daa2769e

---

Whether you’re rebranding, migrating your website to a new technology stack, or simply retiring old content, understanding when and how to implement redirects is crucial to preserve your SEO and avoid potential 404 errors.

<!--endintro-->

## Choosing the right redirect method

Redirects play a key role in guiding users and search engines to the correct content, especially when URLs change or pages are moved. However, not all redirect methods are created equal—each serves a different purpose and can have varying impacts on SEO, user experience, and site performance. Understanding the differences between methods is essential to making informed decisions that align with your website’s goals.

### 1. Client-side redirects

A client side redirect involves responding to the client request with a payload that will send their browser to a different locations. This is usually achieved by sending some JavaScript or a meta tag to the user's browser which will send them to a different location when the page loads. 

#### ✅ Pros

* **Customizability:** It's easy to embed extra code when using this approach. This can be useful if you're hoping to track whether or not the redirects are being hit using Azure Application Insights or Google Analytics
* **Cost:** Compared to alternative options such as using Azure Front Door or Cloudflare, there are no additional costs 

#### ❌ Cons

* **Poor Maintainability**: Compared to an Infrastructure as Code (IaC) approach, this approach makes it difficult to keep track of which redirects were added, who added them and why.

  * Easy to achieve, but poor for SEO and maintenance. Migrating pages in the future would make this approach cumbersome.
  * It's difficult to migrate these redirects to a CDN as opposed to other approaches such as ARM.

``` html
<meta http-equiv="refresh" content="0; url=https://www.northwind.com">
```
::: bad
Figure: Bad example - A client-side redirect achieved by returning a meta refresh
:::

### 2. Server-side redirects

An alternative and more "official" way of handling redirects is to handle them on your server. For instance, Next JS allows you to use middleware to respond to requests with a [redirect](https://nextjs.org/docs/app/building-your-application/routing/redirecting#nextresponseredirect-in-middleware). ASP.NET allows you to return a custom [redirect object](https://learn.microsoft.com/en-us/dotnet/api/system.web.httpresponse.redirect?view=netframework-4.8.1). 

This approach involves modifying the response to incoming requests at the source rather than simply sending HTML that will redirect the user to the appropriate location by proxy.

#### ✅ Pros

* **SEO:** An added benefit of this approach is that you can document that the user was redirected by returning a 300 level response. For example, you can return a 301, which allows you to directs users to your new updated content with minimal impacts on your search engine ranking in Google. For more information see rule on [using "301" code to redirect renamed or moved pages](/use-301-redirect-on-renamed-or-moved-pages).

#### ❌ Cons

* **Availability:** This approach only works for web applications. If you're hosting your website statically, such as in a Blob Storage Account, you will need to rely on a seperate redirect method.

``` js
import { NextRequest, NextResponse } from "next/server";

export function middleware(request: NextRequest): NextResponse {

  const url = request.url

  //Check if we have a redirect for the incoming URL
  const redirect = redirects[url]


  //Return a redirect response if we find a matching redirect
  if(redirect) {
    return NextResponse.redirect(redirect)
  }

  //If we don't have a redirect we allow the request to pass through
  return NextResponse.next()

}

// A list of redirects with the incoming URL on the left and the target on the right
const redirects = {
  "https://northwind.com": "https://schema.com",
  //you can add more redirects here if you need to
}
```
::: good
Figure: Good example - Server-side redirects using middleware in Next JS
:::

### 3. CDN level (global)

CDNs allow you to redirect users at the edge level. This is ideal for global distribution and ease of management. Solutions like Azure Front Door or Cloudflare can be effective.

Learn more on [using a Content Delivery Network (CDN)](/use-a-cdn).

#### ✅ Pros

* **Ease of Maintenance** Using a CDN allows you to keep track of which redirects were added and why.
* **Portability** Because redirects are handled at the edge rather than by your server, there's no need to port redirects if you make changes to your web application.
* **Improved Performance:** Hosting your content on a CDN allows you to respond to requests using a server within the same geography as the user, improving latency.

#### ❌ Cons

* **Increased Cost:** This approach is generally the most expensive of the 3 if you search ranking is of low value. You'll need to pay a subscription fee to a hosting provider to host your website on a CDN.
