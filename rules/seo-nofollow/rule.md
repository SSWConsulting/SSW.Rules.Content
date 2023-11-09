---
type: rule
title: SEO - Do you tag external URLs with rel=”nofollow”?
uri: seo-nofollow
authors:
  - title: Camilla Rosa Silva
    url: https://ssw.com.au/people/cammy
  - title: Adriana Tavares
    url: https://www.ssw.com.au/people/adriana-tavares
created: 2023-01-30T01:35:31.078Z
guid: b96b7400-8717-4c19-867f-5ad643ba8fd5
---
Dofollow and nofollow links look almost the same to the regular web user. The difference between the two is only noticeable when you dig into the HTML code – the addition of the rel="nofollow” tag is what differentiates both links. The `rel` attribute defines the relationship between a linked resource and the current document.

Google sees the buying or selling of links that pass PageRank as a violation of their Webmaster Guidelines aiming to reward earned links, and not paid links. As this still plays an essential role when it comes to SEO, all paid links should be tagged as “nofollow”. 
            
<!--endintro-->

According to [Google](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify):  

> rel="nofollow": Use this attribute for cases where you want to link to a page but don't want to imply any type of endorsement, including passing along ranking credit to another page.  

Other link attributes that provide webmasters with additional ways to identify to Google Search the nature of particular links are:   

> rel="sponsored": Use the sponsored attribute to identify links on your site that were created as part of advertisements, sponsorships or other compensation agreements.  

> rel="ugc": UGC stands for User Generated Content, and the ugc attribute value is recommended for links within user generated content, such as comments and forum posts.  

## When to use “nofollow”  

As per [Search Engine Journal](https://www.searchenginejournal.com/when-to-use-nofollow-on-links/), you are supposed to tag URLs with nofollow when the other two rel attributes mentioned above, sponsored and UGC, aren’t relevant and you don’t want the link to pass PageRank.  

::: greybox 

**Tip:** It’s possible to automatically tag all links as “nofollow” on a webpage by placing a [robot’s meta tag with the value “nofollow”](https://developers.google.com/search/docs/crawling-indexing/special-tags) in the header. However, the nofollow tag is more usually favoured as it allows one to nofollow some links on the page while leaving others followed, as an example if you add links pointing to your own website.  

::: 

::: bad 

```html
<a href="https://www.microsoft.com/Azure">Azure</a> 
``` 

Figure: Bad example - Nofollow rel tag is not present on the link above
::: 

::: good
```html
<a rel="nofollow" href="https://www.microsoft.com/Azure">Azure</a> 
``` 

Figure: Good example - Nofollow rel was added to the URL to make sure it does not impact the landing page 
::: 
