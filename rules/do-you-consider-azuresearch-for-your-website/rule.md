---
type: rule
archivedreason: 
title: Search - Do you consider Azure Search for your website?
guid: 31fba456-e962-4c9b-8ee4-9de5d3cac8fd
uri: do-you-consider-azuresearch-for-your-website
created: 2015-04-27T01:23:12.0000000Z
authors: 
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

AzureSearch is designed to work with Azure based data and runs on ElasticSearch. It doesn't expose all the advanced search features. You may resist to choose it as your search engine from the missing features and what seems to be an expensive monthly fee ($250 as of today). If this is the case, follow this rule:

**Consider AzureSearch if your website**:
- Uses SQL Azure (or other Azure based data such as DocumentDB), and
- Does not require advanced search features

**Consider ElasticSearch if your website**:
- Requires advance search features that aren't supported by AzureSearch

Keep in mind that:
1. Hosting of a full-text search service costs you labour to set up and maintain the infrastructure, and 
2. A single Azure VM can cost you up to $450. So do not drop AzureSearch option unless the missing features are absolutely necessary for your site

<!--endintro-->

::: good
![Figure: Good example - Azure website using AzureSearch for what it can deliver today ](9c0754_Untitled2.png)
:::

::: bad
![Figure: Bad example - Azure website using ElasticSearch for a simple search that AzureSearch can do](Untitled.png)
:::
