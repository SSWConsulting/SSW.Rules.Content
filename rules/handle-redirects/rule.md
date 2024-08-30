---
type: rule
title: Do you know you to handle redirects?
seoDescription: Upgrade your website seamlessly with efficient redirects using
  Cloudflare Workers or Azure Front Door to preserve SEO and traffic during the
  migration
uri: handle-redirects
authors:
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
related:
  - do-you-use-cdn-for-js-files
  - use-301-redirect-on-renamed-or-moved-pages
created: 2024-06-14T06:32:40.000Z
archivedreason: null
guid: 746cfdd5-68d6-4080-b4c8-af73daa2769e
---
When migrating your old website to a new technology stack, maintaining SEO and avoiding potential 404 errors is crucial. Implementing redirects ensures smooth traffic transition and preserves your SEO rankings.

<!--endintro-->

## Choosing the Right Redirect Method


### 1. Client-Side Redirects:

A client side redirect typically involves responding to the client request with a payload that will send their browser to a different locations. This is ususally achieved by sending some Javascript or a meta tag to the user's browser which will send them to a different location when the page loads. 

We generally don't recommend this approach as it becomes very difficult to maintain very quickly. Especially if you're looking to add custom logic, such as tracking whether the redirects were hit in Google Analytics. For instance, if you're web pages are hosted statically and you're only only adding redirects for a couple of pages that had low rankings in Google to begin with it would probably be more cost effective to use a temporary client side redirect and save a buck.

```
<meta http-equiv="refresh" content="0; url=https://www.northwind.com/">
```

**Figure: ❌ Bad Example - A Client Side Redirect achieved by returning a meta refresh**

#### **Pros:**

* **Customizability:** It's easy to embed extra code when using this approach. This can be useful if you're hoping to track whether or not the redirects are being hit using Azure Application Insights or Google Analytics
* **Cost:** Compared to alternative options such as using Azure Front Door or Cloudflare, there are no additional costs 

#### **Cons:**

* **Poor Maintainability**: Compared to an IAC approach, this approach makes it difficult to keep track of which redirects were added, who added them and why.

  * are easy to achieve can Easy but poor for SEO and maintenance. Migrating pages in the future would make this approach cumbersome.
  * It's difficult to migrate these redirects to a CDN as opposed to other approaches such as ARM which handle 

## 2. Server-Side Redirects:

An alternative and more "official" way of handling redirects is to handle them on your server. For instance, Next JS allows you to use middleware to respond to requests with a [redirect](https://nextjs.org/docs/app/building-your-application/routing/redirecting#nextresponseredirect-in-middleware). ASP.Net allows you to return a custom [redirect object](https://learn.microsoft.com/en-us/dotnet/api/system.web.httpresponse.redirect?view=netframework-4.8.1). This approach involves modifying the response to incoming requests at the source rather than simply sending html that will redirect the user to the appropriate location by proxy.

### Pros:

* **SEO:** An added benefit of this approach is that you can document that the user was redirected by returning a 300 level response. For example, you can return a 301, which allows you to directs users to your new updated content with minimal impacts on your search engine ranking in Google. For more information about using a 301 check out the rule [Do you use "301" code to redirect renamed or moved pages?](/rules/use-301-redirect-on-renamed-or-moved-pages/)

#### Cons:

* **Availability:** This approach only works for web applications. If you're hosting your website statically, such as in a Blob Storage Account, it 

```
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
**Figure**: **✅ Good Example - Server side redirects using middleware in Next JS**
## 3. CDN Level (Global)

CDNs allow you to redirect users at the edge level. This is ideal for global distribution and ease of management. Solutions like Azure Front Door or Cloudflare can be effective.

Check out our [SSW rule on CDNs](/do-you-use-cdn-for-js-files)

### Pros:
* **Ease of Maintenance** Using a CDN allows you to keep track 

* **Portability** Because redirects are handled at the edge rather than by your server, there's no need to port redirects if you make changes to your app service.

* **Improved Performance:** Hosting your content on a CDN allows you to respond to requests using a server within the same geography as the user, improving latency.


### Cons: 
* **Increased cost:** This approach is generally the most expensive of the 3 if you search ranking is of low value. You'll need to pay a subscription fee to a hosting provider to host your website on a CDN.
