---
type: rule
tips: ""
title: Do you know the challenges of i18n and how AI makes them easier?
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

<!--endintro-->

## The Expensive Confusion: i18n vs L10n

### Internationalization (i18n) - The Architecture

Count the letters between 'i' and 'n' in "internationalization", 18. Hence i18n. The W3C Internationalization Activity defines it as designing products and services so they can easily adapt to specific local languages and cultures.

Think of it like building a house with modular plumbing that could handle any water system globally. You're not installing fixtures yet, just ensuring your foundation won't collapse when someone needs a bidet instead of a toilet.

### Localization (L10n) - The Implementation

If i18n is the blueprint, L10n is choosing the actual fixtures, paint colors, and doorbell tunes for each market. It's where you discover whether your foundation holds.

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

AI agents can do more than just translate. In the video below, Ben Morss shows how they can refine translations, add i18n support to existing sites, and even run full translation workflows. They’re fast helpers for repetitive tasks, but still need humans to check quality and context.

`youtube: https://www.youtube.com/watch?v=YpVnqI5ljgY`  
**Video: Apidays Munich 2025 - AI translation + AI agents = i18n made easy By Ben Morss. (18 min)**

**Scenario 1 — Improving translations via agents**

* Quality can improve through iterative reflection or specialized agents, but gains are inconsistent
* Token costs and latency are high (e.g., 34 seconds and 3000+ tokens for a single line)
* A single pass with a strong translation API often equals or beats expensive multi-agent pipelines

**Scenario 2 — Internationalizing a monolingual site**

* Agent scans code, proposes i18n keys, replaces hardcoded strings, and generates JSON resource files
* More flexible than regex scripts for detecting strings in varied or unpredictable code patterns
* Requires human oversight to validate keys, disambiguate translations, and ensure architectural consistency

**Scenario 3 — Automating the complete translation workflow**

* Agent extracts strings, generates machine translations, and populates a collaborative spreadsheet for human review
* After human approval, agent automatically reintegrates final translations into resource files
* MCPs (Model Capability Providers) simplify manipulation of spreadsheets and Git repos with high-level operations

🔗 More detail in the related article here: [AI translation + AI agents = i18n made easy (or is it?) - APIscene](https://www.apiscene.io/ai-and-apis/i-agents-i18n-translation-apis/)

### AI-powered solutions

Here are some popular and practical solutions that most teams can adopt:

* **Translation QA**  
  Use AI models (e.g., GPT) to catch mistranslations in context.  
  * Example: **[Lokalise AI LQA](https://docs.lokalise.com/en/articles/7945761-ai-lqa)** and **[Smartling AI Translation QA](https://www.smartling.com/)** integrate GPT to automatically review translations and flag errors.  

* **Pseudolocalization & UX testing**  
  Automatically generate pseudo-translations (extra-long text, special characters, RTL mirroring) to stress-test your UI.  
  * Example: **Microsoft/Android pseudolocalization (`en-XA`, `ar-XB`)** and **[Applitools Visual AI](https://applitools.com/)** are widely used to reveal layout issues early.  

* **Context-aware copywriting**  
  Use AI to adapt tone, style, and terminology for different markets, instead of just translating literally.  
  * Example: **[Phrase](https://phrase.com/)** and **[Lokalise](https://lokalise.com/)** offer GPT-powered copy assistance that helps teams create culturally appropriate content.  

* **Cultural review checks**  
  AI can help flag potentially sensitive terms, icons, or symbols before launch.  
  * Example: **[OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)** or **[Perspective API](https://perspectiveapi.com/)** can be used to detect inappropriate or risky wording, with human review as a final step.  
