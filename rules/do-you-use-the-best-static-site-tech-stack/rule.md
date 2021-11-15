---
type: rule
title: Do you use the best static site tech stack?
uri: do-you-use-the-best-static-site-tech-stack
authors:
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related: []
redirects:
  - do-you-use-the-best-static-site-generator
  - static-site-generator
created: 2020-01-09T04:00:36.000Z
archivedreason: null
guid: d7c5b443-9f55-4983-ac7b-016c85a6d479
---
Pure HTML pages are the fastest website around.  However, server-side scripting languages enable richer functionality. Static sites solve this problem by providing the best of both worlds. Static sites are

* Cheap
* Easy to use
* Fast

On the other hand, complex functionality can be a bit more limited and time consuming to implement.

Here are some popular static site generators:

| **Name**                     | [Gatsby](https://www.gatsbyjs.com/) (Recommended) | [Next.js](https://nextjs.org/) | [Scully](https://scully.io/)   | [Gridsome](https://gridsome.org/)    | [Statiq](https://statiq.dev/)         | [Jekyll](https://jekyllrb.com/)                                                                              |
| ---------------------------- | ------------------------------------------------- | ------------------------------ | ------------------------------ | ------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Language**                 | [React](https://reactjs.org/)                     | React                          | [Angular](https://angular.io/) | [Vue](https://vuejs.org/)            | [.NET](https://dotnet.microsoft.com/) | [Liquid](https://www.shopify.com/partners/blog/115244038-an-overview-of-liquid-shopifys-templating-language) |
| **Data Handling**            | [GraphQL](https://graphql.org/)                   | Fully customisable             | Fully customisable             | GraphQL                              | Fully customisable                    | Source code data files                                                                                       |
| **Data Sources**             | Filesystems, CMS, APIs, Databases, Local files    | Fully customisable             | Fully customisable             | Source Plugins, APIs, Local files    | Fully customisable                    | Local files                                                                                                  |
| **GitHub Pages Integration** | Seamless deployment via config files              | Requires setup                 | Deployment via GitHub Actions  | Seamless deployment via config files | Deployment via GitHub Actions         | Works out of the box 
| **Netlify CMS integration** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅

<br>

![](ssgs.png)
**Figure: Google trends for the above SSGs. In a substantial lead is Gatsby, followed by Jekyll. The others are much lower, and Statiq is excluded as it has very low search numbers.**

Two examples of static sites in action are [SSW People](https://www.ssw.com.au/people/) and [SSW Rules](https://www.ssw.com.au/rules/).

There are a few hosting options to choose from including:

* [Azure static web apps](https://azure.microsoft.com/en-us/services/app-service/static/) (recommended for small websites)
* [Azure static storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website) (recommended for large websites)
* [Cloud Flare](https://pages.cloudflare.com/)
* [GitHub Pages](https://pages.github.com/)
* [Surge.sh](https://surge.sh/)