---
type: rule
archivedreason: 
title: UX - Do you rename Azure’s default URL?
guid: 92dd8fc9-110d-4ea6-8340-528f1b1d411e
uri: do-you-always-rename-staging-url-on-azure
created: 2015-03-08T23:23:53.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
- title: Michael Demarco
  url: https://ssw.com.au/people/michael-demarco
- title: Shigemi Matsumoto
  url: https://ssw.com.au/people/shigemi-matsumoto
related: 
  - do-you-have-separate-development-testing-and-production-environments
redirects: []

---

If you use the default Azure staging website URL, it can be difficult to remember and a waste of time trying to lookup the name every time you access it. Follow this rule to increase your productivity and make it easier for everyone to access your staging site.

<!--endintro-->

::: greybox
Default Azure URL:
sugarlearning**-staging**&#46;azurewebsites&#46;net
:::
::: bad
Figure: Bad example - Site using the default URL (hard to remember!!)  
:::

::: greybox
Customized URL:
**staging**&#46;sugarlearning&#46;com
:::
::: good
Figure: Good example - Staging URL with "staging&#46;" prefix  
:::

### How to setup a custom URL

1. Add a CName to the default URL to your DNS server

![Figure: CName being added to DNS for the default URL](2015-03-10_17-13-55.png) 

2. Instruct Azure to accept the custom URL

![Figure: Azure being configured to accept the CName](custom-domains.png)
