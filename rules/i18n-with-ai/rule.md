---
type: rule
tips: ""
title: Do you use AI to make internationalization easier?
seoDescription: i18n, L10n, internationalization, localization, W3C standards
uri: i18n-with-ai
authors:
  - title: Gilles Pothieu
    url: https://www.ssw.com.au/people/gilles-pothieu
  - title: Chloe Lin
    url: https://www.ssw.com.au/people/chloe-lin/
related:
  - add-multilingual-support-on-angular
  - do-you-know-how-to-better-localize-your-application
  - do-you-always-give-the-user-an-option-to-change-the-locale
guid: 7429ba5a-5c49-4b5d-94d0-5c207a33e260
---

Amazon's Swedish website accidentally replaced "rooster" with the Swedish word for male genitals. An Italian company named their international site powergenitalia.com instead of powergen-italia.com back in 2003. These weren't just translation mistakes, they were internationalization disasters that exposed fundamental marketing failures.

The companies that succeed globally ([Spotify](https://www.nimdzi.com/lessons-in-localization-spotify-expanded), Netflix, Uber) don’t just translate. They design from day one for cultural, linguistic, and technical differences.

![Figure: Mismatch between number of native speakers and supported website languages. Many top-spoken languages remain underrepresented online.](first_language_vs_web.png)

<!--endintro-->

## The Expensive Confusion: i18n vs L10n

### Internationalization (i18n) - The Architecture

Count the letters between 'i' and 'n' in "internationalization", 18. Hence i18n. The W3C Internationalization Activity defines it as designing products and services so they can easily adapt to specific local languages and cultures.

Think of it like building a house with modular plumbing that could handle any water system globally. You're not installing fixtures yet, just ensuring your foundation won't collapse when someone needs a bidet instead of a toilet.

### Localization (L10n) - The Implementation

If i18n is the blueprint, L10n is choosing the actual fixtures, paint colors, and doorbell tunes for each market. It's where you discover whether your foundation holds.

![Figure: Languages most frequently used for web content as of February 2025. English dominates, but many markets require multilingual support.](web_content_languages_2025.png)

## Common i18n Issues

Here are the most frequent pitfalls developers encounter when scaling globally:

* **Text expansion & contraction**: German words can be 30–40% longer, while Chinese can compress paragraphs into a handful of characters.
* **Character encoding**: “Björk” becomes “Bj?rk” or 田中さん turns into “???.”
* **RTL layouts**: Arabic and Hebrew flip entire UI structures, not just text direction.  
* **Names & forms**: Some cultures have one name, some have none that fit “first/last.”
* **Dates & numbers**: “03/04/2025” means March 4 in the US, April 3 in Europe, or something else in Japan. Decimal points and commas vary by region and can cost money.  
* **Cultural symbols**: White means purity in the West, but death in China. Even colors can alienate users.  
* **Infrastructure blind spots**: Fonts too large, networks too slow, CDNs not present where your customers are.

![Figure: Arabic is one of the top 5 internet languages with 300M+ speakers. Supporting RTL layouts is essential, the UI looks entirely different when switching to Arabic.](RTL_mobile.jpg)

## General Tips

* **Localize time & numbers properly**
  ❌ Don’t parse strings manually
  ✅ Use `Intl.DateTimeFormat`, `Intl.NumberFormat` or libraries like [date-fns](https://date-fns.org/)  

* **Design elastic UIs**
  ❌ Don’t hardcode pixel widths for buttons or labels  
  ✅ Use flex layouts, `min-width`, `word-break`

* **Use Unicode everywhere**  
  ❌ No assumptions about ASCII-only inputs
  ✅ UTF-8 end-to-end (DB, API, frontend)  

* **Plan for RTL**
Arabic accounts for 5% of internet users (300M+). Supporting RTL means mirroring the entire UI, not just text.
  ✅ Test with `direction: rtl;` CSS  
  ✅ Use logical CSS properties (`inline-start`/`inline-end`) instead of `left`/`right`  

* **Simplify forms**  
  ❌ Never force “First Name / Last Name” globally
  ✅ Use a single “Full Name” field, or make name parts optional  

* **SEO & URLs**  
  ✅ Test regexes and sitemaps with non-Latin domains (IDNs)  
  ✅ Configure hreflang tags correctly  
  ✅ Research local search engines (Baidu, Yandex, Naver)

* **Check cultural assumptions**  
  ❌ Don’t assume Western metaphors apply everywhere
  ✅ Test color/icon choices with local users (white = death in China)  

* **Optimize performance globally**
  ❌ Don’t ship a 5MB JS bundle to mobile-first markets
  ✅ Use a CDN close to your users
  ✅ In China, use local CDNs to avoid latency from the Great Firewall  
  ✅ Subset fonts or use system fonts  

::: greybox  
Check out our rules [Use a CDN for Internationalization](https://www.ssw.com.au/rules/use-a-cdn/)
:::

## Non-AI tools

* **[i18next](https://www.i18next.com/)** (JS/React): Manages translations and language switching  
* **[FormatJS](https://formatjs.io/)**: Dates, numbers, and message formatting  
* **[Globalize.js](https://github.com/globalizejs/globalize)**: Number/date formatting, message translation, plurals  
* **Angular i18n / ngx-translate**: First-class localization for Angular apps, see Rule [Do you add multilingual support (Angular](https://www.ssw.com.au/rules/add-multilingual-support-on-angular/)

## AI-tools (recommended)

### Exploring AI Agents in i18n

Internationalizing an app after you’ve hardcoded strings everywhere is one of the toughest real-world i18n challenges. In this video, Ben Morss shows how **AI agents** can scan your codebase, create i18n keys, and automate translations.

`youtube: https://youtu.be/YpVnqI5ljgY?si=jPR7PuV9o6gmneH5&t=491`  
**Video: Apidays Munich 2025 - AI translation + AI agents = i18n made easy By Ben Morss. (Watch 8:10 – 16:40)**

In this part, Ben Morss shows how an AI agent can internationalize a monolingual site by:

* Scanning the codebase to detect hardcoded strings
* Proposing i18n keys and replacing literals with t() function calls.
* Generating JSON resource files and populating them with translations.
* Opening a pull request so humans can review and approve.

🔗 More detail in the related article here: [AI translation + AI agents = i18n made easy (or is it?) - APIscene](https://www.apiscene.io/ai-and-apis/i-agents-i18n-translation-apis/)

### Choosing the Right i18n Strategy by Project Size

Your i18n strategy should match your project’s size, requirements, and resources. Use the guide below to find the best fit.

#### 1. Small Project — Essentials (POC)  

**Approach:** Minimal setup. Extract strings, machine translate, quick human check.  
**Stack:** use [traditional non-AI i18n approaches](https://www.ssw.com.au/rules/i18n-with-ai/#3-useful-tools)
✅ Cheap, fast, avoids future i18n debt  
❌ Manual releases, limited scalability, brand/tone risks  

#### 2. Medium Project — Step Further with TMS  

**Approach:** Add a lightweight Translation Management System (TMS) like Phrase, Lokalise, or Crowdin. Enables glossary, screenshots, workflows.  
**Stack:** TMS + pseudolocalization tests.  
✅ Centralized management, easier scaling, better consistency  
❌ Licensing costs, more process overhead  

#### 3. Large Project — AI in CI/CD

**Approach:** Automate translations in the build pipeline. Machine translate → AI QA pass → human spot-check → auto-commit.  
**Stack:** CI/CD pipeline + TMS + LLM QA.  
✅ 80/20 automation, faster releases, consistent quality  
❌ Needs strong CI/CD setup, token costs, prompt governance  

#### 4. Enterprise Project — Full-Blown Live LLM Translation  

**Approach:** Dynamic runtime translations (best for UGC, long-tail docs). Cache aggressively and use guardrails.  
**Stack:** LLM API + caching + glossary/do-not-translate rules.  
✅ Instant coverage, great for user content and fast-changing text  
❌ Latency, cost variability, SEO/quality risks, heavy monitoring needed  

## Buyer’s Guide Table

| Project Size       | Stack Suggestion                 | Why                                            | Caveats                                  |
|--------------------|----------------------------------|------------------------------------------------|------------------------------------------|
| Small project      | i18next, Angular i18n/ngx-translate| ✅ Cheapest way to get started, avoids i18n debt | ❌ Manual, hard to scale, tone issues     |
| Medium project     | TMS (Phrase/Lokalise) + pseudoloc| ✅ Centralized control, consistent translations | ❌ Adds license cost + extra process      |
| Large project      | TMS + CI/CD integration + AI QA  | ✅ Automation + speed, 80/20 human/AI workflow  | ❌ Needs mature CI/CD, token costs        |
| Enterprise project | TMS for UI + Live LLM for content| ✅ Instant coverage for UGC + long-tail pages   | ❌ Latency, cost drift, SEO monitoring    |
