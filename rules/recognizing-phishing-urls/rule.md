---
seoDescription: Recognizing Phishing URLs - Protect Your Online Identity
type: rule
title: Do you know how to recognize phishing URLs?
uri: recognizing-phishing-urls
authors:
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
created: 2022-03-17T05:47:34.156Z
guid: 668d37e3-deeb-49db-9ad2-043b8c1dbdbd
---

Phishing is a form of social engineering where an attacker tries to convince a victim that a resource they are in control of is a legitimate resource. This is usually achieved through the use of deceptive email messages or websites.

Attackers will often craft a website that looks like a legitimate one for the sole purpose of stealing your username and password (or some other sensitive information). They might, for example, build a website that looks exactly like LinkedIn, so that you think you are logging into LinkedIn, but are in fact giving an attacker your username and password.

<!--endintro-->

A URL is made up of a fully-qualified domain name (FQDN) and a path. The FQDN is the part between the **https://** and the next **/**. Anything after the **/** is part of the path and not the FQDN.

The FQDN is made up of a top-level domain (TLD), a domain, and then a subdomain or subdomains. These move from right to left, so for the address <https://www.ssw.com.au/>, **.com.au** is the TLD, **ssw** is the domain, and **www** is a subdomain.

For the address <https://www.ssw.com.au/people/>, **people** is the path. The path can include all kinds of other characters and parameters.

You should always check that the **domain** matches the service or website you are expecting.

::: greybox
http&#58;//linkedin&#46;com&#46;sggr&#46;ru/someaddress
:::
::: bad
Bad Example – The address has LinkedIn in it, but it is a sub-domain, not the domain
:::

::: greybox
http&#58;//linked-in-hq&#46;com/linkedin/myprofile
:::
::: bad
Bad Example – The address has LinkedIn in it, but it is in the path, not the FQDN. The FQDN is also suspicious
:::

::: greybox
http&#58;//linkedinalerter&#46;com
:::
::: bad
Bad Example – the address has LinkedIn in it, but is not a legitimate LinkedIn site
:::

::: greybox
https&#58;//linkedin&#46;com/someaddress
:::
::: good
Good Example – LinkedIn is a secure domain
:::

If you are curious about a URL, and think it might be legitimate, you can [check the Whois record](https://whois.domaintools.com) to see who owns the domain.

::: bad
![Bad Example – ANZAlerter.com is NOT owned by ANZ](bad-whois.png)
:::

::: good
![Good Example – the domain ANZ.com.au is owned by ANZ](good-whois.png)
:::
