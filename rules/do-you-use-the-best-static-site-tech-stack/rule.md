---
type: rule
archivedreason: 
title: Do you use the best static site tech stack?
guid: d7c5b443-9f55-4983-ac7b-016c85a6d479
uri: do-you-use-the-best-static-site-tech-stack
created: 2020-01-09T04:00:36.0000000Z
authors:
- title: Matt Wicks
  url: https://ssw.com.au/people/matt-wicks
- title: Piers Sinclair
  url: https://ssw.com.au/people/piers-sinclair
related: []
redirects:
- do-you-use-the-best-static-site-generator
- static-site-generator


---

Pure HTML pages are the fastest website around.  However, server-side scripting languages enable richer functionality. Static sites solve this problem by providing the best of both worlds. Static sites are

*	Cheap
  
*	Easy to use
  
*	Fast

On the other hand, complex functionality can be a bit more limited and time consuming to implement.

Two examples of static sites in action are [SSW People](https://www.ssw.com.au/people/) and [SSW Rules](https://www.ssw.com.au/rules/).

There are a few hosting options to choose from including:

*	[Azure static web apps](https://azure.microsoft.com/en-us/services/app-service/static/) (recommended)

*	[Cloud Flare](https://pages.cloudflare.com/)

*	[GitHub Pages](https://pages.github.com/)

*	[Surge.sh](https://surge.sh/)

There are also many different static site generators:

| **Name** | [Gatsby](https://www.gatsbyjs.com/) | [Jekyll](https://jekyllrb.com/) | [Next.js](https://nextjs.org/) | [Scully](https://scully.io/) | [Gridsome](https://gridsome.org/)
| --- | --- | --- | --- | --- | --- 
| **Language** | React | Liquid | React | Angular | Vue
| **Learning Curve** | Medium | Easy | Hard |
| **Scalability** | Medium | Low | High
| **Data Handling** | GraphQL | Source code data files | Fully customisable
| **GitHub Integration** | Works natively with GitHub as a Datasource | Works out of the box with GitHub Pages | Requires setup
 

*	[Gatsby](https://www.gatsbyjs.com/) (recommended)

    *	React based
  
    *	Lots of plugins
    
    * Data handling via GraphQL
    
    * Works natively with GitHub as a Datasource.
  
*	[Jekyll](https://jekyllrb.com/)
    
    * Liquid based [(Shopify’s templating language)](https://www.shopify.com/partners/blog/115244038-an-overview-of-liquid-shopifys-templating-language)
    
    * Simple to setup
    
    * Out of the box integration with GitHub pages
    
    * Scales poorly
    
    * [Windows is not supported](https://jekyllrb.com/docs/installation/windows/)
  
*	[Next.js](https://nextjs.org/)
    
    * React based
    
    * Server-side rendered pages but can be exported as a static site
    
    * Provides full control over which data handling technology you use
    
    * More scalable than conventional static site generators
* [Gridsome](https://gridsome.org/)
    * Vue.js based  
