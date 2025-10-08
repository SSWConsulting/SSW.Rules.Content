---
type: rule
tips: ""
title: Do you use AI to make internationalization easier?
seoDescription: Understand i18n vs l10n. Build software ready for global users
  with tips on encoding, dates, forms, and cultural adaptation.
uri: i18n-with-ai
authors:
  - title: Gilles Pothieu
    url: https://www.ssw.com.au/people/gilles-pothieu
  - title: Chloe Lin
    url: https://www.ssw.com.au/people/chloe-lin
related:
  - add-multilingual-support-on-angular
  - do-you-know-how-to-better-localize-your-application
  - do-you-always-give-the-user-an-option-to-change-the-locale
guid: 7429ba5a-5c49-4b5d-94d0-5c207a33e260
---

Amazon's Swedish website accidentally replaced "rooster" with the Swedish word for male genitals. An Italian company named their international site `powergenitalia.com` instead of `powergen-italia.com` back in 2003. These weren't just translation mistakes, they were internationalization disasters that exposed fundamental marketing failures.

The companies that succeed globally ([Spotify](https://www.nimdzi.com/lessons-in-localization-spotify-expanded), [Netflix](https://www.weglot.com/blog/netflixs-localization-strategy), [Uber](https://www.nimdzi.com/lessons-in-localization-uber/)) don’t just translate. They design from day one for cultural, linguistic, and technical differences.

<!--endintro-->

![Figure: Many top-spoken languages remain underrepresented online, e.g. Chinese represents 13% of the world, but 2.2% of the websites](first_language_vs_web.png)

::: china
China has the largest number of native speakers and represents a huge market opportunity. Check out [Want to bring your applications into the Chinese market?](https://www.ssw.com.au/consulting/chinafy-app)
:::

## The expensive confusion: i18n vs l10n

### **Internationalization** (i18n) - The architecture

The word “internationalization” is long, so we shorten it to **i18n** because there are 18 letters between the “i” and “n.”  According to the W3C, internationalization means **designing your product so it can easily adapt to different languages and cultures** before you start translating.  

Think of it like **building a website with a flexible backend**. You set up your framework so it supports multiple languages: text is not hardcoded, date and currency formats can be customized, and layouts can adjust for right-to-left text.  

You are not adding translations yet. You are just making sure the system can handle them later without breaking.  

### **Localization** (l10n) - The implementation

If i18n is the framework, **l10n** is when you actually **fill in the details for each locale**. This is where you add translations, apply regional settings, and adjust visuals such as date formats, currencies, or culturally specific images.  

This step is where you confirm that your internationalized website truly works for users in Japan, Germany, or Brazil, and fix anything that does not fit.

## Common i18n pitfalls

Here are the most frequent pitfalls developers encounter when scaling globally:

1. **UX - No language options** - Users are stuck with 1 language  

   ✅ Provide a language selector (see rule [Do you always give the user an option to change the locale?](/do-you-always-give-the-user-an-option-to-change-the-locale/))

2. **Character encoding** - All countries using non-latin scripts (japanese, chinese, korean, etc.). E.g. “Björk” becomes “Bj?rk” in Sweden; or " 田中さん " turns into “???” in Japanese.

   ❌ Don't make assumptions about ASCII-only inputs  
   ✅ Use UTF-8 end-to-end (DB, API, frontend)  

   Note: Every modern front-end framework set charset UTF-8 by default, you don't have to think about it. Don't forget to configure it on a "classic website"
  
4. **UX - Dates & numbers** - “03/04/2025” means "March 4" in the US and "April 3" in Europe. Decimal points and commas vary by region and can cost money

   ❌ Don’t parse strings manually  
   ✅ Use `Intl.DateTimeFormat`, `Intl.NumberFormat` or libraries like [date-fns](https://date-fns.org/)  

5. **UX - Text expansion and contraction** - German words can be 30–40% longer, while Chinese can compress paragraphs into a handful of characters  

   ❌ Don’t hardcode pixel widths for buttons or labels  
   ✅ Use responsive layouts and visually check text in different languages

6. **Names & forms** - Some cultures have one name, some have none that fit “first/last” (i.e. Indonesia, Tibet)

   ❌ Don't force “First Name / Last Name” globally  
   ✅ Use a single “Full Name” field, or make name parts optional  

7. **Infrastructure blind spots** - Networks too slow, CDNs not present where your customers are

   ❌ Don’t ship large JS bundles to mobile-first markets  
   ✅ [Use a CDN close to your users](/use-a-cdn/)    
   ✅ Subset fonts or use system fonts
   ✅ In China, use local CDNs to avoid latency from the Great Firewall

8. **Cultural symbols** - White means purity in the West, but death in China. Even colors can alienate users  

   ❌ Don’t assume Western metaphors apply everywhere  
   ✅ Test color/icon choices with local users (white = death in China)

   ::: china
   Check out [Do you know why you should Chinafy your app?](/do-you-know-why-you-should-chinafy-your-app/)
   :::

9. **RTL layouts** - For instance, Arabic language flip entire UI structures, not just text direction (see image below)

   ✅ Test with `direction: rtl;`  
   ✅ Use a combination of  logical CSS properties (`direction: rtl;`) instead of `left`/`right`

   ::: info
   **Tip:**" Arabic accounts for 5% of internet users (300M+). Supporting RTL ("Right-To-Left") means mirroring the entire UI, not just text
   :::

   ::: img-medium
   ![Figure: Arabic is one of the top 5 internet languages with 300M+ speakers. Supporting RTL layouts is essential, the UI looks entirely different when switching to Arabic](RTL_mobile.jpg)
   :::


## Internationalization (i18n) Approaches

### Option A - Browser-based translation (Google Translate)

**Use case:** Prototypes, internal demos, hackathons, no i18n budget project  
Use browser-based Google Translate for instant multilingual support when you have no development time or budget.   

#### ✅ Pros

* Immediate availability with zero development effort  
* No implementation or maintenance costs

#### ❌ Cons

* Poor UX and layout issues  
* Inaccurate translations  
* Potential loss of international users  

### Option B - Manual i18n (traditional libraries)

**Use case:** Multilingual projects that need stability, quality, and full control without relying on AI.
Use libraries like **[i18next](https://www.i18next.com/)**, **[FormatJS](https://formatjs.io/)**, or **[Angular i18n](https://angular.dev/guide/i18n)** to manage translation keys and switch languages.  
This gives developers full control and high-quality results, but requires setup and ongoing translation work.  

#### ✅ Pros

* High-quality, controlled translations  
* Professional multilingual user experience  
* Native language support and better SEO  
* Full control of data

#### ❌ Cons

* Significant development time and delays  
* High translation costs: 0.08–0.15 $AUD per word for professional translators (potentially €5,000–15,000+ per language for a typical app)  
* Ongoing costs for maintaining and updating translations with each new feature  
* Complex maintenance of language files  
* Slow update process for new content  

#### Useful non-AI tools

* **[i18next](https://www.i18next.com/)** (JS/React): Manages translations and language switching  
* **[FormatJS](https://formatjs.io/)**: Dates, numbers, and message formatting  
* **[Globalize.js](https://github.com/globalizejs/globalize)**: Number/date formatting, message translation, plurals  
* **[Angular i18n](https://angular.dev/guide/i18n) / [ngx-translate](https://github.com/ngx-translate/core)**: First-class localization for Angular apps, see Rule [Do you add multilingual support (Angular)](https://www.ssw.com.au/rules/add-multilingual-support-on-angular/)


### **Option C – AI-assisted i18n**

**Use case:** Products that need to scale translations from small teams to global platforms efficiently.  
AI can enhance traditional workflows by automating translation steps, improving quality, and reducing human overhead.  
You can adopt AI at different points in your process:

#### **Workflow automation (TMS + AI)**
Use a **Translation Management System (TMS)** such as **[Phrase](https://phrase.com/)**, **[Lokalise](https://lokalise.com/)**, or **[Crowdin](https://crowdin.com/)**.  
A TMS centralizes translations and glossaries, while AI can pre-translate new strings before human review.

✅ Centralized management and terminology consistency  
❌ Subscription cost and moderate setup overhead  


#### **CI/CD integration (AI in the pipeline)**
Integrate i18n into your **build pipeline** so translations happen automatically during deployment.  
AI handles machine translation and quality checks, then opens PRs for human review.

✅ Faster releases with 80/20 automation  
❌ Requires mature CI/CD and API governance  


#### **Runtime translation (live AI)**
Use **LLM APIs** to translate user-generated or frequently changing content **on the fly**.  
Cache translations and use glossaries to preserve accuracy and tone.

✅ Real-time coverage for global audiences  
❌ Latency, cost variability, and SEO risks if not cached  


## Choosing the right solution

Choosing the right internationalization solution depends on your project’s complexity, content volume, and update frequency.  
Not every project needs AI. Sometimes traditional tools are faster, simpler, and more reliable.  

AI can be a big time-saver for large or dynamic codebases. For example, **AI agents** can:
* Scan your codebase for hardcoded strings  
* Generate i18n keys automatically  
* Pre-translate multiple languages  
* Open pull requests for review

🎥 Check out this video:
`youtube: https://youtu.be/YpVnqI5ljgY?si=jPR7PuV9o6gmneH5&t=491`  
**Video: Apidays Munich 2025 - AI translation + AI agents = i18n made easy By Ben Morss - watch from 8:10 to 16:40 (8 min)**

🔗 More details in the related article: [AI translation + AI agents = i18n made easy (or is it?) - APIscene](https://www.apiscene.io/ai-and-apis/i-agents-i18n-translation-apis/)


### **When to use what**

| Use Case | Main Challenge | Recommended Solution |
|-----------|----------------|----------------------|
| **Static website with many pages** | Translating large volumes consistently while keeping layout and SEO intact | **Non-AI:** Use a Translation Management System (TMS) like Phrase or Crowdin to manage and reuse translations across pages. |
| **Dynamic web app with frequent content updates** | Making sure new content is translated quickly without blocking releases | **Partly automated:** Connect your TMS to the CI/CD pipeline so new strings trigger translation automatically. |
| **Multi-market e-commerce site** | Adapting prices, currencies, measurements, and promotions for different locales | **Hybrid:** Combine TMS for UI strings with programmatic locale logic for regional data and formatting. |
| **Community or user-generated content platform** | Handling massive volumes of diverse content, slang, or informal text | **AI-assisted:** Use machine translation APIs (DeepL, Google Translate) and apply human review for quality. |
| **Global SaaS product** | Keeping UI, emails, and notifications consistent across languages | **AI + Translation Memory:** Use AI for first-pass translations and a Translation Memory to ensure consistent phrasing across components. |
| **Marketing or SEO-focused content** | Preserving brand tone while adapting keywords and messaging per market | **AI copy assist:** Use AI to draft localized content, then have human editors refine tone and keyword targeting. |

💡 **Tip:** Even with AI, always involve native speakers for critical customer-facing content.  
AI accelerates translation but cannot fully replace cultural understanding or brand-specific tone.
