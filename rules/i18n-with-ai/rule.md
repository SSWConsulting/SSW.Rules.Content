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
China has the largest number of native speakers and represents a huge market opportunity. [Want to bring your applications into the Chinese market?](https://www.ssw.com.au/consulting/chinafy-app)
:::

## The expensive confusion: i18n vs l10n

### Internationalization (**i18n**) - The architecture

The word “internationalization” is long, so we shorten it to **i18n** because there are 18 letters between the “i” and “n.”  According to the W3C, internationalization means **designing your product so it can easily adapt to different languages and cultures** before you start translating.  

Think of it like **building a website with a flexible backend**. You set up your framework so it supports multiple languages: text is not hardcoded, date and currency formats can be customized, and layouts can adjust for right-to-left text.  

You are not adding translations yet. You are just making sure the system can handle them later without breaking.  

### Localization (**l10n**) - The implementation

If i18n is the framework, **l10n** is when you actually **fill in the details for each locale**. This is where you add translations, apply regional settings, and adjust visuals such as date formats, currencies, or culturally specific images.  

This step is where you confirm that your internationalized website truly works for users in Japan, Germany, or Brazil, and fix anything that does not fit.

## Common i18n pitfalls

Here are the most frequent pitfalls developers encounter when scaling globally:

#### UX - No language options
* ❌ **Pain:** Users are stuck with one language  
* ✅ **Tip:** Provide a language selector (see rule [Do you always give the user an option to change the locale?](/do-you-always-give-the-user-an-option-to-change-the-locale/))  

#### Character encoding
* ❌ **Pain:** Countries using non-latin scripts might not render correctly - e.g. “Björk” becomes “Bj?rk” or " 田中さん " turns into “???”.  
* ✅ **Tip:** Use UTF-8 end-to-end (database, API, frontend).  
* 💡 **Note:** Modern build tools (Vite, Create React App, Angular CLI) include UTF-8 charset in their HTML templates by default. You should still verify whether it's included in your `index.html` file and configured correctly on the server.  
  
#### UX - Dates & numbers formatting
* ❌ **Issue:** “03/04/2025” has different meanings: it means "March 4" in the US and "April 3" in Europe.  
* ✅ **Tip:** Use `Intl.DateTimeFormat`, `Intl.NumberFormat` or libraries like [date-fns](https://date-fns.org/) instead of parsing strings manually.  

#### UX - Text expansion and contraction
* ❌ **Issue:** German words can be 30–40% longer, while Chinese can compress paragraphs into a handful of characters.  
* ✅ **Tip:** Use responsive layouts and visually check text in different languages

#### Names & forms
* ❌ **Issue:** Some cultures have one name, some have none that fit “first/last” (i.e. Indonesia, Tibet).  
* ✅ **Tip:** Use a single “Full Name” field or make name parts optional.  

#### Infrastructure blind spots
* ❌ **Issue:** Slow performance or broken assets in regions with limited infrastructure.  
* ✅ **Tip:** Optimize delivery globally — [use nearby CDNs](/use-a-cdn/) or smaller bundles.  

#### Cultural symbols
* ❌ **Issue:** Colors can alienate users - white means purity in the West, but death in China.  
* ✅ **Tip:** Test color/icon choices with local users.  

   ::: china
   [Do you know why you should Chinafy your app?](/do-you-know-why-you-should-chinafy-your-app/)
   :::

#### RTL layouts
* ❌ Issue: Arabic and Hebrew languages are written Right-To-Left (RTL)
* ✅ Tip: Test with `direction: rtl; Use a combination of  logical CSS properties (`direction: rtl;`) instead of`left`/`right`
* 💡 Note: Be mindful to also change the images layout, not just the text.
* For instance, Arabic (and Hebrew) language flip entire UI structures, not just text direction (see image below)

   ::: info
   **Tip:**" Arabic accounts for 5% of internet users (300M+).
   :::

   ::: img-medium
   ![Figure: Arabic is one of the top 5 internet languages with 300M+ speakers. Supporting RTL layouts is essential, the UI looks entirely different when switching to Arabic](RTL_mobile.jpg)
   :::

## Choosing the right solution

Choosing the right internationalization solution depends on your project’s complexity, content volume, and update frequency.  
Not every project needs AI - sometimes traditional tools are faster, simpler, and more reliable.  

However, AI can be a huge time-saver for large or dynamic codebases. For example, AI agents can scan your codebase, identify hardcoded strings, generate i18n keys, and even automate translations for multiple languages. This can dramatically reduce manual work and speed up the localization process.

🎥 Check out this video to see how AI can assist developers in creating a fully internationalized website:

`youtube: https://youtu.be/YpVnqI5ljgY?si=jPR7PuV9o6gmneH5&t=491`  
**Video: Apidays Munich 2025 - AI translation + AI agents = i18n made easy By Ben Morss - watch from 8:10 to 16:40 (8 min)**

🔗 More details in the related article: [AI translation + AI agents = i18n made easy (or is it?) - APIscene](https://www.apiscene.io/ai-and-apis/i-agents-i18n-translation-apis/)

### **When to use what**

Below are common scenarios, ordered from simpler to more complex, with tailored solutions ranging from non-AI to AI-assisted approaches:  

| Use Case | Main Challenge | Recommended Solution |
|-----------|----------------|----------------------|
| **Project with zero budget or resources for localization** | Need instant multilingual capability without any setup or cost | **Browser-based translation (Google Translate):** Use browser-based translation for temporary or internal projects. Fast and free, but not suitable for production due to layout and accuracy issues. |
| **Stable product with few supported languages and no AI requirement** | Need professional, accurate translations and full control over language files | **Manual i18n (traditional libraries):** Use libraries like [i18next](https://www.i18next.com/), [FormatJS](formatjs.io), or [Angular i18n](https://angular.dev/guide/i18n) for high-quality, consistent translations managed by developers or translators. |
| **Static website with many pages** | Translating large volumes consistently while keeping layout and SEO intact | **Non-AI:** Use a Translation Management System (TMS) like [Phrase](https://phrase.com/) or [Crowdin](https://crowdin.com/) to manage and reuse translations across pages. |
| **Static blog with frequent new content** | Generating translations for new posts quickly at build time without manual overhead | **AI at build time:** Use AI translation APIs (OpenAI, Claude, Deepl...) in your build pipeline to auto-translate new posts, with optional human review for published content. |
| **Dynamic web app with frequent content updates** | Ensuring new content is translated quickly without blocking releases | **Partly automated:** Connect your TMS to the CI/CD pipeline so new strings trigger translation automatically. |
| **Multi-market e-commerce site** | Adapting prices, currencies, measurements, and promotions for different locales | **Hybrid:** Combine TMS for UI strings with programmatic locale logic for regional data and formatting. |
| **Community or user-generated content platform** | Handling high-volume, informal content with slang and varied writing styles | **AI-assisted:** Use AI translation APIs and apply human review for quality. |
| **Real-time chat or customer support** | Translating conversations instantly while maintaining context and natural flow | **AI real-time translation:** Use streaming translation APIs with conversation context, potentially with human agent oversight for critical issues. |
| **Marketing or SEO-focused content** | Preserving brand tone while adapting keywords and messaging per market | **AI copy assist:** Use AI to draft localized content, then have human editors refine tone and keyword targeting. |

💡 **Tip:** Even with AI, always involve native speakers for critical customer-facing content. AI accelerates translation but cannot fully replace cultural understanding or brand-specific tone.
