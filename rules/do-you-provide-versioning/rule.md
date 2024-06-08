---
type: rule
archivedreason: 
title: Do you provide versioning?
guid: 3c769da9-79bc-4de4-b078-fb290e77cfe6
uri: do-you-provide-versioning
created: 2014-07-17T21:34:48.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

As an API provider, one of your most important tasks is to make sure that breaking changes will never occur in your API. Making breaking changes will make life difficult for the developers who depend on your service and can easily start causing frustration when things start to break.

<!--endintro-->

There are typically three main ways people provide versioning.

1. **Change the URL:** Append a version number in the path
e.g. [https://developer.github.com/v3/](https&#58;//developer.github.com/v3/)
    1. Best choice for anonymous API access (callers may not be authenticated)
    2. E.g. Github, Twitter
2. **Based upon caller:**The caller has been authenticated and you determine the version of the API based upon the customer's record.
    1. Your URL's never change
    2. Allows you to see the oldest version that customers are using and notifying customers to upgrade
    3. E.g. Salesforce
3. **Custom request header:**You can use the same URL but add a header such as "api-version: 2"
    1. Your URL's never change


All of these methods work well. The above list is in order of our recommendations.

**Option 2** is a viable solution as you only have a few authenticated users that will consume the web service. It also allows you to notify users if they are using an old version that will be decommissioned.

If you are working with objects, keep the object id in the URL and leave everything else to the query string.
