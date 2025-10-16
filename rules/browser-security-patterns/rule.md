---
type: rule
title: Do you know the secret life of browser security patterns?
seoDescription: Explore the evolution of browser security patterns, from cookies and OAuth flows to modern Backend-for-Frontend (BFF). Learn when to use each pattern, their pros and cons, and best practices for securing SPAs and web applications.
uri: browser-security-patterns
authors:
  - title: Jeoffrey Fischer
    url: https://www.ssw.com.au/people/jeoffrey-fischer
  - title: Hajir Lesani
    url: https://www.ssw.com.au/people/hajir-lesani
related:
  - choosing-authentication
  - modern-stateless-authentication
created: 2025-10-03T22:40:45.273Z
guid: 715aeb05-0530-49a8-a2ea-ef6f4a5271bb
---

Web security patterns are a lot like fashion trends. What looked sharp ten years ago now feels outdated, and the styles everyone thought would last forever sometimes vanish in a season. Cookies, tokens, proxies - they’ve all had their runway moment.

Let’s take a lighthearted but practical tour of how browser security has evolved - from the early days of cookies, to the heyday of SPAs, to the modern approaches.

<!-- endintro -->

## 1. Cookie-Based Authentication (Traditional Web Apps)

The oldest and most battle-tested approach. Server-rendered apps relied heavily on cookies for session management, long before OAuth and SPAs came along. While simple and effective, cookies had to evolve with new browser features to keep up with modern threats.

📅 **Era:** Early web apps (pre-SPA, server-rendered pages).

🤔 **How it works:**

* Server issued a session cookie after login.
* Browser auto-sent the cookie with every request.

✅ **Pros:**

* Simple, browser-native.
* Strong protection with HttpOnly, SameSite, Secure flags.

❌ **Cons:**

* Doesn’t fit modern SPAs calling multiple APIs.
* Vulnerable to CSRF if unprotected.

💪 **Use Case:**

* Classic monolithic apps.
* Intranets or smaller web apps that don’t need OAuth/OIDC or cross-domain API calls.

::: info

* **HttpOnly cookies** can’t be accessed by JavaScript. This makes them immune to theft via XSS, unlike tokens stored in `localStorage` or `sessionStorage`.  
  → If a token is in localStorage and your app suffers an XSS, an attacker can simply read it. With HttpOnly cookies, the attacker can’t.  
* **SameSite cookies** help prevent CSRF by controlling when cookies are sent with cross-site requests.  
  * `Strict`: Only sent in first-party contexts.  
  * `Lax`: Sent for top-level navigations (good balance).  
  * `None` + `Secure`: Required for third-party usage.
:::

## 2. OAuth 2.0 Implicit Flow (SPAs v1)

As SPAs emerged, developers needed a way to authenticate without a backend. The Implicit Flow was introduced to give client-side apps direct access to tokens - a clever hack for its time, but one that opened the door to serious security issues.

📅 **Era:** Early SPAs (~2012).

🤔 **How it works:**

* Browser handled OAuth directly.
* Tokens delivered in the URL fragment, stored in JS.

✅ **Pros:**

* Enabled serverless SPAs.
* No backend required.

❌ **Cons:**

* Tokens in browser = hacker candy 🍬.
* Highly vulnerable to XSS.
* Deprecated by IETF.

💪 **Use Case:**

* Historically used for early Angular/React apps with no backend.
* Rarely recommended today.

## 3. OAuth 2.0 Authorization Code Flow with PKCE (SPAs v2)

To fix the flaws of the Implicit Flow, PKCE came into play. This was a big leap forward for SPAs, giving them a safer way to obtain tokens directly. But while more secure, it still left the browser holding sensitive tokens.

📅 **Era:** Mid SPAs (~2016).

🤔 **How it works:**

* SPA performed Auth Code flow with PKCE.
* Tokens fetched over XHR and stored client-side.

✅ **Pros:**

* More secure than Implicit (no tokens in URL).
* PKCE stops code interception.

❌ **Cons:**

* Still stores tokens in the browser.
* Vulnerable to XSS and browser sandbox exploits.

💪 **Use Case:**

* Serverless-first SPAs (e.g. static frontends hosted on Netlify, Vercel).
* Useful if you can’t or won’t run a backend.

## 4. API Gateway / Reverse Proxy Security

When applications grew into ecosystems of microservices, authentication had to scale with them. API gateways and reverse proxies emerged as central control points - moving the burden of auth away from the browser and onto infrastructure.

📅 **Era:** Microservices era.

🤔 **How it works:**

* Browser talked to a gateway, not APIs directly.
* Gateway handled OAuth and proxied traffic.

✅ **Pros:**

* Centralized security.
* Simplifies microservice-heavy environments.

❌ **Cons:**

* Heavy infrastructure.
* Not tailored to a single frontend.

💪 **Use Case:**

* Enterprises with multiple frontends + microservices.
* Teams already using API gateways (Kong, Apigee, AWS API Gateway).

## 5. Backend-for-Frontend (BFF)

The modern favorite. BFFs combine the simplicity of cookies with the security of OAuth. By keeping tokens server-side and giving the browser only safe cookies, BFFs drastically reduce the attack surface for SPAs.

📅 **Era:** Modern standard (~2020+).

🤔 **How it works:**

* Each frontend gets its own backend (BFF).
* BFF handles OAuth/OIDC, keeps tokens server-side.
* Browser only receives a secure, HTTP-only cookie.

✅ **Pros:**

* SPA never sees tokens → no XSS token theft.
* Works with modern browser restrictions (no 3rd-party cookies).
* Tailored to a frontend → smaller attack surface.
* Built-in CSRF defense.

❌ **Cons:**

* Adds an extra backend component.
* One BFF per frontend.

💪 **Use Case:**

* Modern SPAs (React, Vue, Blazor, Angular).
* Apps needing secure API calls + OAuth/OIDC integration.
* Teams that value high security and standards compliance.

## 6. Content Security Policy (CSP)

Even with secure authentication, XSS remains one of the biggest threats to web apps. That’s where CSP comes in. It acts as a browser-enforced guardrail, letting you tightly control which scripts, styles, and resources are allowed to run. Think of it as a whitelist for your frontend - reducing the blast radius if malicious code ever sneaks in.

📅 **Era:** Introduced in 2012, now a modern standard supported by all major browsers.  

🤔 **How it works:**

* Developers configure a `Content-Security-Policy` HTTP header.  
* Browser enforces rules on what scripts, styles, iframes, fonts, and other resources can load and execute.  
* Inline code can only run if explicitly whitelisted via **nonces** or **hashes**.  

✅ **Pros:**

* Strong protection against XSS and script injection.  
* Forces developers to use safer script-loading practices.  
* Can limit damage if an attacker injects malicious code.  

❌ **Cons:**

* Misconfiguration can easily break apps (e.g., when loading external resources).  
* Allowing `unsafe-inline` or `unsafe-eval` weakens CSP significantly.  
* Adds complexity when working with third-party libraries/CDNs.  

💪 **Use Case:**

* Any modern app handling sensitive data.  
* Especially valuable for SPAs that are more exposed to XSS due to client-side rendering.  
* Works best when paired with other defenses (e.g., HttpOnly cookies, BFF).  

## 📊 Summary Comparison Table

| Pattern                     | Era           | Tokens in Browser? | Security Strength | Use Case                                     |
| --------------------------- | ------------- | ------------------ | ----------------- | -------------------------------------------- |
| Cookie-Based Auth           | Oldest        | ❌ No               | ⭐⭐ Medium         | Monolithic/intranet apps, simple sessions    |
| OAuth Implicit Flow         | Early SPAs    | ✅ Yes              | ⭐ Low             | Legacy SPAs with no backend                  |
| Auth Code + PKCE (SPA)      | SPAs v2       | ✅ Yes              | ⭐⭐ Medium         | Serverless SPAs (Netlify, Vercel)            |
| API Gateway / Reverse Proxy | Microservices | ❌ No               | ⭐⭐⭐ High          | Enterprise microservices, multiple frontends |
| Backend-for-Frontend (BFF)  | Modern        | ❌ No               | ⭐⭐⭐⭐ Very High    | Secure modern SPAs needing OAuth/OIDC        |
| Content Security Policy (CSP)| Always       | N/A                 | ⭐⭐⭐⭐ Very High    | All modern apps to mitigate XSS              |

## Conclusion

Each of these patterns reflects its time and context. Cookies kept things simple, Implicit Flow fueled the first wave of SPAs, PKCE added better protections, gateways helped large-scale systems, and newer approaches combine security with modern frontend needs.  

**But don’t forget**: authentication is only half the story. Pairing modern auth patterns (like BFF with HttpOnly cookies) with **defensive browser features like CSP** is what makes the difference between “secure enough” and “battle-hardened.”  

There’s no universal “best” - the right choice depends on your architecture, risk tolerance, and future plans. Understanding the trade-offs helps you pick a pattern that matches your app’s needs without getting stuck in yesterday’s trend.

There’s no universal “best” - the right choice depends on your architecture, risk tolerance, and future plans. Understanding the trade-offs helps you pick a pattern that matches your app’s needs without getting stuck in yesterday’s trend.
