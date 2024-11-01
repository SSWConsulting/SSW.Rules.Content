---
seoDescription: Learn the essential principles of REST API design to create APIs that are clear, reliable, and secure. Discover tips on naming conventions, idempotency, versioning, pagination, sorting, security, and more to build developer-friendly interfaces that foster trust and ease of use.
type: rule
archivedreason:
title: Do you know the key principles of REST API Design?
guid: f847325c-97a5-48e7-a2ce-8e56b33512d1
uri: rest-api-design
created: 2024-10-25T14:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay/
related:
- choose-the-right-api-tech
- do-you-know-the-common-design-principles-part-1
- do-you-provide-versioning
redirects:
- key-principles-of-rest-api-design

---

REST APIs are everywhere in our daily lives — from social media updates and online shopping to weather forecasts and GPS navigation. These interfaces allow different applications to connect seamlessly, providing the backbone for countless modern conveniences.

<!--endintro-->

`youtube: https://youtu.be/_gQaygjm_hg`
**Video: Good APIs Vs Bad APIs: 7 Tips for API Design (6 min)**

## Recommended configuration for most REST APIs

Building a high-quality API means adhering to best practices that enhance clarity, reliability, and security, creating a more consistent experience for developers and users.

### 1. Security

Most REST APIs are hosted online, and you don't want to rely on "security via obscurity". Ensure you spend time hardening your surface area.  

Common sense approaches include protecting your endpoints via short-lived access tokens (even for seemingly benign functionality), as well as your typical security headers such as:  

* Content-Security-Policy (CSP)  
* Strict-Transport-Security (HSTS)  
* X-Content-Type-Options  
* X-Frame-Options  

Enforce HTTPS for encrypted communication and consider OAuth for user authentication and authorization, protecting against unauthorized access.  

### 2. Clear naming

Choose descriptive, intuitive names for endpoints and parameters following REST conventions.

* Use nouns and verbs logically (e.g., `/api/users` for accessing user data, `/api/users/{id}` for specific user information)
* Endpoints should also use plurals. i.e `/api/users` instead of `/api/user`

This provides a much more consistent API structure when querying both collections and single entities.

### 3. Idempotent requests

Design requests as idempotent operations, where repeating an action yields the same result as performing it once. This avoids unintended actions from repeated requests.

Typically, `GET`, `PUT` and `DELETE` are idempotent by default, but special handling needs to be added to make `POST` requests idempotent.

::: greybox
If a `DELETE` request removes a record, re-sending it should not throw errors if the record is already deleted.
:::

::: good
Figure: Good example - This prevents accidental duplicate data processing
:::

### 4. Pagination

For endpoints that return lists, it's best to apply pagination to prevent overwhelming the client with too much data.

When paging parameters are omitted from the request, the API should apply some sensible defaults (e.g. page 1, 50 records).

Use query parameters like `?page=` and `?limit=` to specify page numbers and size, offering a more manageable data experience while improving performance.  

### 5. Meaningful query parameter names

When supporting sorting, apply clear query strings. Query params should generally be optional making the API easier to consume.

Consistent sorting parameters allow developers to retrieve and organize data efficiently and minimize confusion in handling API responses.  

```js
`?x=name&y=asc`
```

::: bad
Figure: Bad example - It's impossible to understand what those query string mean!
:::

```jsox
`?sortBy=name&order=asc`
```

::: good
Figure: Good example - Query strings are meaningful
:::

### 6. Simple cross-resource references

For APIs that reference multiple resources (e.g., `userId` in a post endpoint), keep relationships simple to prevent over-complicating endpoints.

Provide clear references or IDs rather than nested data whenever possible to keep API responses readable and easy to follow.  

```js
`api/products?user_id=123&product_id=321`
```

::: bad
Figure: Bad example - Messy query parameter
:::

```js
`api/orders/123/items/456/products/789`
```

::: bad
Figure: Bad example - Overly complicated endpoint
:::

```js
`api/products/789`
```

::: good
Figure: Good example - Clearly defined endpoint
:::

## Optional configurations

These other design choices may only be required in certain circumstances. You should consider the specific use case of your API e.g. public facing or under heavy load.

### 7. Rate limiting  

Rate limiting controls the number of requests per user within a time frame, protecting the API from abuse.

When adding rate limiting you should provide appropriate status codes and messages (e.g., `HTTP 429`) when limits are reached.

### 8. Caching

* Implement caching for frequently requested data to reduce server load and response times
* Cache static data responses at the client or server side where appropriate, especially for resources that don't change frequently
* Use HTTP cache headers like `Cache-Control` and `ETag` to guide clients on when to use cached data or refresh it, balancing speed and data freshness

### 9. Compression

Enabling compression for API responses, especially for large data payloads, reduces bandwidth and improves loading times.  

* Use GZIP or Brotli compression formats, which are widely supported and effective in reducing data sizes

### 10. Versioning  

Introduce versioning from the start (e.g., `/v1/resource`) to maintain backward compatibility when updating the API.

Versioning helps users manage changes without breaking existing implementations, allowing them to adopt new features gradually. There are 3 common ways to implement versioning:  

* Route  
* Query String  
* Header  

For more details, see [Do you provide versioning?](/do-you-provide-versioning)
