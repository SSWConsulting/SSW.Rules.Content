---
seoDescription: Use Google Tag Manager to manage your website's tags and tracking codes efficiently, without writing complex code.
type: rule
title: Do you use Google Tags Manager (GTM) to manage your tags?
uri: use-google-tag-manager
authors:
  - title: Penny Walker
    url: https://ssw.com.au/people/penny-walker
  - title: Luke Mao
    url: https://www.ssw.com.au/people/luke-mao
  - title: Camilla Rosa Silva
    url: https://www.ssw.com.au/people/camilla-rosa-silva
related: null
created: 2021-06-01T17:30:01.000Z
archivedreason: null
guid: 11013d4b-66d5-4945-ae49-e52ee68a2930
---

Many website integrations will require an HTML tag in added to your website. This can be painful to manage when dealing with the code. To add those tags, we recommend using **Google Tag Manager**.

::: info
Google Tag Manager is a tag management system (TMS) that allows you to quickly and easily update measurement codes and related code fragments collectively known as tags on your website or mobile app.
:::

<!--endintro-->

::: bad
![Figure: Bad example – Vimeo tracking code added in the head of the source code](tracking-code-bad.png)
:::

::: good
![Figure: Good example – Reference to the Google Tag Manager](tracking-code-reference-google-tag-manager.png)
:::

::: good
![Figure: Good example – Vimeo tracking code added through Google Tag Manager](tracking-code-good.png)
:::

Multiple marketing tools can be added in a website using Google Tag manager.

![Figure: All tags are added in new SSW.Website using GTM](trracking-all-tags.png)

Data and analytics result has recorded by Google Analytics on new SSW.Website. Universal Analytics and GA4 are configured in Google Tag Manager.

![Figure: Universal Analytics is collecting data from the website](tracking-universal-analytics.png)

![Figure: GA4 is collecting data from the website](tracking-ga4.png)

Learn more on [Google Tag Manager official site](https://marketingplatform.google.com/about/tag-manager/benefits/).

### Drawbacks

While Google Tag Manager is great for non-tech people to easily embed tracking code, you must be careful to not introduce functionality to the website that may interfere with existing systems.

Some things to consider when adding GTM scripts to a container:

- **Performance** - some scripts may have a large performance impact, and result in the slowing of the site. The more scripts you add, the slower the site becomes.
- **Disconnected functionality** - some functionality may require developer modifications in the code that are not possible in GTM to ensure that it works correctly. (e.g. Application Insights)
