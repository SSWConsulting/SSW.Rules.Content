---
seoDescription: Do you use a Content Delivery Network (CDN) to reduce network latency and improve page load times for your users?
type: rule
archivedreason:
title: Do you use a Content Delivery Network (CDN)?
guid: 8312c849-88a5-4745-82e7-739127d6e9f8
uri: do-you-use-cdn-for-js-files
created: 2019-05-16T06:32:40.0000000Z
authors:
  - title: Barry Sanders
    url: https://ssw.com.au/people/barry-sanders
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Shane Ye
    url: https://ssw.com.au/people/shane-ye
  - title: Aman Kumar
    url: https://ssw.com.au/people/aman-kumar
related: []
redirects:
  - do-you-use-a-content-delivery-network-cdn
  - do-you-use-a-content-delivery-network-(cdn)
---

If your site takes too long to load, there is a high chance your users will not wait for it to finish loading and abandon viewing it. It is therefore important that we use techniques to make pages load as quickly as possible. One of these techniques is to use a Content Delivery Network (CDN) to reduce the network latency for delivering pages, images, javascript and CSS libraries to users. This results in faster page load times and a better experience for your users.

<!--endintro-->

### What is a CDN?

CDN is short for a Content Delivery Network. It is a system of distributed servers (network) that deliver pages and other Web content to a user, based on the geographic locations of the user, the origin of the webpage and the content delivery server.

### Why use a CDN?

A website may be hosted in a particular region, but have the majority of its users coming from an entirely different region – for example, if your site is hosted in North America, GTmetrix(A free tool that analyzes your page's speed performance) might report fast speeds based on our default test location, but if a good chunk of your users come from China, their speed will not be as fast as you experience it to be.
Using a CDN can improve your user’s experience in terms of speed, and as we know – speed matters!
Ensuring a consistent experience for all your users is important.
CDNs not only ensure a faster experience to your users, but they also help to prevent site crashes in the event of traffic surges – CDNs help to distribute bandwidth across multiple servers, instead of allowing one server to handle all traffic.

### How to choose a CDN?

When selecting a Content Delivery Network (CDN) for your website, you face the challenge of ensuring robust edge-level redirects and effective caching to speed up your site. Unfortunately, not all CDNs provide these functionalities seamlessly, making it difficult to find one that meets these critical needs.

### Front Door as Your CDN

Front Door is a good option, but it has some notable downsides regarding redirects and caching that you should be aware of:

✅ Pros:

* **Easy Integration**: Seamlessly integrates with other Azure services.
* **Flexible Origin Handling**: Better handling for origin groups on a route level (e.g., /people can be hosted on a different server).

❌ Cons:

* **Limited Redirects**: Front Door restricts bulk redirects with a [limit of 800 resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) per resource group.
* **Time-Consuming Deployments**: Deployments using Bicep can take a long time, sometimes up to hours.
* **Lack of Flexibility**: It doesn’t offer much flexibility for custom redirects, such as using regular expressions.
* **Painful Cache Purging**: Cache purging can be unreliable and can take up to 15 minutes.
* **High Costs**: It is quite expensive compared to other CDNs.

To overcome these issues, we can use Cloudflare.

### Cloudflare

Cloudflare is known for its Distributed Denial-of-Service (DDoS) protection and Web Application Firewall (WAF), along with a host of other options.

✅ Pros:

* **Easy Deployment**: Simple deployment through Wrangler. (it takes a few seconds to deploy workers)
* **Flexible Redirects**: More flexible in handling bulk and customizable redirects using [Cloudflare Workers](https://developers.cloudflare.com/workers/).
* **Enhanced Security**: Provides better WAF protection and secure DDoS mitigation.
* **Cost-Effective**: Much cheaper than other CDNs.
* **Efficient Caching**: Better caching options.
* **Instant Cache Purging**: Offers an instant purging option for caches.

❌ Cons:

* No built-in integration with Azure Services

Also consider where your user base is located and which CDN providers support those locations. For example, some CDNs are not fast or reliable when accessed from China (due to the Great Firewall).

#### Which CDNs work well from China?

1. <https://cdnjs.cloudflare.com> (recommended)
2. <http://www.staticfile.org/>
3. <http://www.bootcdn.cn/>
4. <https://intl.cloud.baidu.com/product/cdn.html>
5. <http://lib.sinaapp.com/>
6. <http://cdnjs.net/>
7. <https://www.cloudflare.com/network/china/> (Cloudflare’s China Service)
8. <https://www.akamai.com>

#### Which ones do not work well from China?

1. <https://maxcdn.bootstrapcdn.com>
2. <https://ajax.googleapis.com>

::: bad
![Figure: Bad example, jquery.min.js from GoogleAPIs failed to load](5-28.4.png)
:::

::: good
![Figure: Good example, jquery.min.js from CDNJS isn't block and is very fast](5-28.5.png)
:::
