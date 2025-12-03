---
seoDescription: Using canonical tags helps prevent duplicate content issues and ensures search engines index the preferred version of a web page.
type: rule
title: Technical - Do you use canonical tags to prevent duplicate content?
uri: seo-canonical-tags
authors:
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming
  - title: Brady Stroud
    url: https://www.ssw.com.au/people/brady-stroud
created: 2024-03-08T13:42:55.753Z
redirects: []
related:
  - lowercase-urls
guid: 1b5d8749-6291-45ee-9fa3-fda75c17f8d4
---

Using canonical tags is essential for SEO as it helps prevent duplicate content issues, which can negatively impact your website's search engine rankings.

### Why Canonical Tags Are Important

When multiple URLs on your website (or external sites) lead to the same or very similar content, search engines might see this as duplicate content. This can dilute your SEO efforts, as search engines may not know which version to index or might divide the value of that content between multiple pages. To resolve this, the `rel="canonical"` link element is used to specify the "canonical" or "preferred" version of a web page.

<!--endintro-->

### Implementing Canonical Tags

1. **Identify Duplicate Content:** Start by identifying pages on your site that have similar or identical content accessible through different URLs. This could be due to URL parameters, session IDs, or printer-friendly versions of pages.

2. **Choose the Preferred URL:** Decide which version of the URL you want search engines to treat as the authoritative one. This is typically the version you want visitors to see.

3. **Add the Canonical Tag:** On each version of the duplicate pages, add a canonical tag in the `<head>` section pointing to the preferred URL. For example:

  ```html
  <link rel="canonical" href="https://www.example.com/preferred-url" />
  ```

4. **Apply Across Your Site:** Ensure every page has a canonical tag, even if there are no current duplicates. This future-proofs your site against potential duplicate content issues.

### Handling External Duplicate Content

If other sites are reproducing your content (with permission) or if you have multiple domains, use canonical tags to point back to the original content on your site. This helps search engines consolidate ranking signals to the original content.

`youtube: https://youtu.be/8j_hxBw5B4E`  
**Video: Canonical URLs: How Does Google Pick the One? (4 min)**
