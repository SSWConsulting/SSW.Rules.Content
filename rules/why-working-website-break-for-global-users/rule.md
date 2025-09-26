---
type: rule
tips: ""
title: i18n, L10n, internationalization, localization, W3C standards
seoDescription: Best practices for keeping your content and images self-contained in TinaCMS + Next.js, with three options and a recommended setup.
uri: why-your-website-might-break-for-global-users
authors:
  - title: Gilles Pothieu
    url: https://www.ssw.com.au/people/gilles-pothieu
  - title: Chloé Lin
    url: https://www.ssw.com.au/people/chloe-lin/
related:
  - add-multilingual-support-on-angular
  - do-you-know-how-to-better-localize-your-application
  - do-you-always-give-the-user-an-option-to-change-the-locale
guid: 7429ba5a-5c49-4b5d-94d0-5c207a33e260
---

### Why your perfectly working website might be completely broken for global users

[Amazon's Swedish website](https://www.theguardian.com/technology/2020/oct/29/amazon-hits-trouble-with-sweden-launch-over-lewd-pussy-translation) accidentally replaced "rooster" with the Swedish word for male genitals. [An Italian company](https://powgenproject.org/it/) named their international site powergenitalia.com instead of powergen-italia.com back in 2003. These weren't just translation mistakes—they were internationalization disasters that exposed fundamental architectural failures.

The [World Wide Web Consortium (W3C)](https://www.w3.org/International/) has been working on these problems since 1994, establishing standards that make the web work for everyone, everywhere. The difference between companies that successfully expand globally and those that retreat in embarrassment isn't translation quality—it's understanding the difference between building for one culture and architecting for all of them.

`youtube: https://www.youtube.com/watch?v=-m9KHI1Fg0w`
**Video: Introduction to Internationalization -i18n (4mn)**

<!--endintro-->

## The Expensive Confusion: i18n vs L10n

### **Internationalization (i18n)** - The Architecture
Count the letters between 'i' and 'n' in "internationalization"—18. Hence i18n. The [W3C Internationalization Activity](https://www.w3.org/International/) defines it as designing products and services so they can easily adapt to specific local languages and cultures.

Think of it like building a house with modular plumbing that could handle any water system globally. You're not installing fixtures yet—just ensuring your foundation won't collapse when someone needs a bidet instead of a toilet.

### **Localization (L10n)** - The Implementation
If i18n is the blueprint, L10n is choosing the actual fixtures, paint colors, and doorbell tunes for each market. It's where you discover whether your foundation holds.

## The Hidden Complexity

### **Character Encoding: When Names Become Question Marks**

A developer in Austin builds a contact form. Works perfectly—until, for instance, Björk tries to enter her name and it becomes "Bj?rk." Or when 田中さん submits information and your database stores "???."

If your system can't handle a customer's actual name, they won't complain—they'll just leave.

### **The German Problem**

English: "Speed limit"  
German: "Geschwindigkeitsbegrenzung"  
Your button: 💥

German text expands 30-40% on average. Russian text is wider. Chinese text is denser—four characters might need 20 English words to explain. Twitter had to rebuild their entire character [counting system](https://developer.twitter.com/en/docs/counting-characters) because 140 Latin characters ≠ 140 Chinese characters.

### **RTL: Everything Backwards**

Facebook's Arabic interfacemirrors everything. The logo stays the same but moves to the right. Progress bars fill right-to-left. Even shadows flip. Your back button? Now on the right.

![Figure: Arabic Facebook homepage](facebook_arabic.png)

Interesting article about mirroring design for Arabic users: https://blog.prototypr.io/mirroring-how-to-design-for-arabic-users-a1dbcd3aa566



### **Names: Your Form's Cultural Bias**

| **Culture** | **Name Structure** | **Your Form Fails Because...** |
|-------------|-------------------|--------------------------------|
| **Iceland** | Patronymic system | No family name exists |
| **Indonesia** | Single name only | "Last name" is required |
| **Netherlands** | Particles matter | "van der Berg" sorts under 'B' |

[Airbnb's solution](https://airbnb.design/international-typography/): Single "Full Name" field. They learned after losing bookings in markets where forms wouldn't accept local names.

### **Date Confusion Matrix**

"03/04/2025" means:
- Americans: "March 4th"
- Europeans: "April 3rd"
- Japanese: "What year era?"

A European product launch could easily see poor results if a discount is labeled to expire on “03/04,” since many customers might think the offer ended on 3 April rather than 4 March.

### **Numbers: Where Commas Cost Millions**

European enters "1.234" (one thousand)  
American system reads "1.234" (one point two)  
You've undercharged by 99.9%

[Indian numbering](https://en.wikipedia.org/wiki/Indian_numbering_system): 12,34,567  
Swiss formatting: 1'234.56  
Your DECIMAL(10,2) database column: Inadequate

## Success Stories

### **[Spotify's Smooth Expansion](https://www.nimdzi.com/lessons-in-localization-spotify-expanded/?utm_source=chatgpt.com)**
Built i18n from day one. Payment methods auto-adapt: credit cards in US, SEPA in EU, carrier billing in emerging markets. Local music categories appear automatically.

### Netflix's Content Strategy

[Subtitles handle mid-sentence](https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide?utm_source=chatgpt.com) direction changes. Thumbnail images [change by local](https://netflixtechblog.com/artwork-personalization-c589f074ad76). Search understands local names for international content.

### **Uber's Market Adaptation**
Cash payments in India, prayer time considerations in Middle East and [Female driver options](https://techcrunch.com/2025/07/23/uber-is-finally-bringing-a-feature-to-the-u-s-that-lets-women-riders-match-with-women-drivers/?utm_source=chatgpt.com) where culturally significant.

## Common Myths

**"English Is Universal"**  
[76% of consumers](https://csa-research.com/Blogs-Events/CSA-in-the-Media/Press-Releases/Consumers-Prefer-their-Own-Language?utm_source=chatgpt.com) won't buy in another language.

**"Google Translate Is Good Enough"**  
Google Translate, while advanced, often struggles to produce accurate translations because it lacks the ability to fully understand the context or cultural nuances of the text. As a result, Google Translate frequently produces translations that are [funny or confusing](https://www.indigoextra.com/blog/google-translate-funny-fails) rather than reliable, making it unsuitable when accuracy and clarity are critical.

## The Technical Checklist

### **URLs and SEO**

Internationalized Domain Names (IDN) allow non-Latin URLs like https://例え.jp or https://مثال.السعودية. But your regex validation probably breaks on these. Your sitemap generator might crash. Your analytics will show garbage.

[Hreflang tags](https://developers.google.com/search/docs/advanced/crawling/localized-versions) tell Google which language version to show where. Get them wrong and German users see English results while Americans get Dutch pages.  
Format: `<link rel="alternate" hreflang="de-DE" href="https://example.com/de/">`.

Don't assume Google. [Baidu](https://www.baidu.com/) dominates China (70% market share). [Yandex](https://yandex.com/) owns Russia (60%). [Naver](https://www.naver.com/) rules South Korea. Each has different SEO requirements—Baidu requires ICP license, Yandex favors .ru domains.

### **Legal Requirements**

[GDPR](https://gdpr.eu/) isn't just cookie banners. It requires EU data to stay in EU, user deletion rights, and consent for everything. Fines: up to 4% of global revenue.

[China's PIPL](https://personalinformationprotectionlaw.com/) blocks data export without government approval. Your AWS us-east-1 setup? Illegal. Need local hosting or approved cross-border transfer mechanism.

[Brazil's LGPD](https://lgpd-brazil.info/) is another local data protection.  

[Russia's law](https://captaincompliance.com/education/russia-data-localization-law/#:~:text=Protection%20Law%20Explained-,Federal%20Law%20No.,specific%20purposes%20stated%20in%20advance.) demands Russian citizen data stays in Russia. Your centralized database architecture just became legally impossible.

Cookie banners need different text per region. California wants opt-out, EU demands opt-in, and your single checkbox won't satisfy either.

### **Performance Geography**

Chinese fonts contain 20,000+ characters and typically weigh 10-20MB. Your fancy web font? It just killed mobile users' data plans.  
Solution: concider [dynamic subsetting](https://web.dev/reduce-webfont-size/) or system fonts.

Network speeds vary wildly. Indian mobile averages 12 Mbps, Myanmar 4 Mbps. Your 5MB JavaScript bundle takes 40 seconds to load. Users would probably leave after 10.  
Have a look at : https://www.speedtest.net/global-index

CDN presence matters. [CloudFlare has 310 cities](https://www.cloudflare.com/network/), but weak in Africa. Fastly strong in developed markets, absent in emerging ones. Your millisecond optimizations in San Francisco mean nothing if your CDN serves the cities of Central Africa from London.
Check out that rule about CDN and Interalization: https://www.ssw.com.au/rules/use-a-cdn/

We also have a set of rule about internalization and China that might interest you: https://www.ssw.com.au/rules/search/?keyword=chinafy

## The Mindset Shift

Before writing any code, challenge every assumption:

**"What if this text was 3x longer?"**  
Finnish word for "not even with the help of his unintentionalness": "epäjärjestelmällistyttämättömyydelläänsäkään". Your fixed-width button just exploded. Design with elastic containers, never pixel-perfect layouts.

**"What if there were no spaces?"**  
Thai, Lao, and Khmer don't use spaces between words. Your word-wrap algorithm fails. Line breaks happen mid-word. Text selection becomes impossible. [CSS word-break](https://developer.mozilla.org/en-US/docs/Web/CSS/word-break) and proper Unicode segmentation required.

**"What if everything read right-to-left?"**  
Not just text—entire mental models flip. Timelines flow right-to-left. "Next" buttons move left. Carousels swipe opposite. Even emoji directions change in RTL contexts.

**"What if numbers use different symbols?"**  
[Eastern Arabic numerals](https://en.wikipedia.org/wiki/Eastern_Arabic_numerals): ٠١٢٣٤٥٦٧٨٩. Your regex `/[0-9]/` just failed. Your parseInt() broke. Credit card validation rejected legitimate cards.

**"What if this color means death?"**  
White = death in China, red = danger in the West but luck in Asia. Your "friendly" yellow warning might mean cowardice in some cultures. [Color psychology varies dramatically](https://www.shutterstock.com/blog/color-symbolism-and-meanings-around-the-world).

## The Bottom Line

Every market has its digital giants. WeChat dominates China, Line owns Japan,WhatsApp rules Brazil and India. They succeeded by understanding that global software isn't about translation—it's about architecture that respects fundamental differences in how humans organize information, express meaning, and interact with technology.

When PowerGen Italia became powergenitalia.com, it revealed a truth: our assumptions are so deep we can't even see them. When HSBC lost $10 million, when German patients needed repeat surgeries, when [Walmart retreated from Germany](https://www.theguardian.com/business/2006/jul/28/retail.money#:~:text=The%20world%27s%20largest%20retailer%2C%20Wal,price%2C%20American%2Dstyle%20trading.)—these weren't localization failures. They were architectural failures baked in from day one.

The internet's infrastructure—[UTF-8](https://en.wikipedia.org/wiki/UTF-8), [Unicode](https://home.unicode.org/), [IANA time zones](https://www.iana.org/time-zones), [ISO standards](https://www.iso.org/)—exists because engineers understood that people compute differently depending on where they live. The [W3C's Internationalization Activity](https://www.w3.org/International/) continues this work, creating standards like [Internationalized Resource Identifiers (IRIs)](https://www.w3.org/International/articles/idn-and-iri/) that allow web addresses in any script, and guidelines that help developers avoid these costly mistakes.

Build systems that assume nothing, adapt to everything, and treat edge cases as first-class citizens. Because in global software, there's no such thing as an edge case—just use cases you haven't encountered yet.