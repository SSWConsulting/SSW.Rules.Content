---
seoDescription: Prevent spam and protect your email addresses from being scraped by avoiding clear text emails on your website.
type: rule
archivedreason: 
title: Do you avoid clear text email addresses in web pages?
guid: ab0fc8a3-97b0-43ac-b944-9ac6ef9a65a8
uri: avoid-clear-text-email-addresses-in-web-pages
created: 2018-04-23T20:39:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-clear-text-email-addresses-in-web-pages

---

Clear text email addresses in web pages are very dangerous because it gives spam sender a chance to pick up your email address, which produces a lot of spam/traffic to your mail server, this will cost you money and time to fix.

Never put clear text email addresses on web pages.

<!--endintro-->

```html
<!--SSW Code Auditor - Ignore next line(HTML)--> 
<a href="mailto:test@ssw.com.au">Contact Us</a>
```

::: bad
Bad - Using a plain email address that it will be crawled and made use of easily

:::

```html
<a href="javascript:sendEmail('74657374407373772e636f6d2e6175')" onmouseover="javascript:displayStatus('74657374407373772e636f6d2e6175');return true;" onmouseout="javascript:clearStatus(); return true;">Contact Us</a>
```

::: good
Good - Using an encoded email address
:::

**Tip:** If you use Wordpress, use the [Email Encoder Bundle plugin](https://wordpress.org/plugins/email-encoder-bundle) to help you encode email addresses easily.

::: codeauditor
We have a program called [SSW CodeAuditor](https://codeauditor.com) to check for this rule.
:::
