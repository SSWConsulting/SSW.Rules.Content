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

Web security patterns are a lot like dating trends. What was cool ten years ago now makes people cringe, and what everyone swore was “forever” sometimes disappears in a few short years. Tokens, cookies, proxies… they’ve all had their moment in the spotlight.

Let’s take a lighthearted but practical tour of how browser security has evolved — from the early days of cookies, to the heyday of SPAs, to the modern approaches.

<!-- endintro -->

## 1. Cookie-Based Authentication (Traditional Web Apps)

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

---

## 2. OAuth 2.0 Implicit Flow (SPAs v1)

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

---

## 3. OAuth 2.0 Authorization Code Flow with PKCE (SPAs v2)

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

---

## 4. API Gateway / Reverse Proxy Security

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

---

## 5. Backend-for-Frontend (BFF)

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

---

## 📊 Summary Comparison Table

| Pattern                     | Era           | Tokens in Browser? | Security Strength | Use Case                                     |
| --------------------------- | ------------- | ------------------ | ----------------- | -------------------------------------------- |
| Cookie-Based Auth           | Oldest        | ❌ No               | ⭐⭐ Medium         | Monolithic/intranet apps, simple sessions    |
| OAuth Implicit Flow         | Early SPAs    | ✅ Yes              | ⭐ Low             | Legacy SPAs with no backend                  |
| Auth Code + PKCE (SPA)      | SPAs v2       | ✅ Yes              | ⭐⭐ Medium         | Serverless SPAs (Netlify, Vercel)            |
| API Gateway / Reverse Proxy | Microservices | ❌ No               | ⭐⭐⭐ High          | Enterprise microservices, multiple frontends |
| Backend-for-Frontend (BFF)  | Modern        | ❌ No               | ⭐⭐⭐⭐ Very High    | Secure modern SPAs needing OAuth/OIDC        |

---

## Conclusion

Each of these patterns reflects its time and context. Cookies kept things simple, Implicit Flow fueled the first wave of SPAs, PKCE added better protections, gateways helped large-scale systems, and newer approaches combine security with modern frontend needs.

There’s no universal “best” — the right choice depends on your architecture, risk tolerance, and future plans. Understanding the trade-offs helps you pick a pattern that matches your app’s needs without getting stuck in yesterday’s trend.
