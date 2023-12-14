---
type: rule
archivedreason:
title: Do you design your webpages for SEO with an SEO checklist?
guid: d4e70213-7272-4470-8b93-8a2c54a7b60c
uri: seo-checklist
created: 2023-06-14T00:00:00.000Z
authors:
- title: Seth Daily
  url: https://www.ssw.com.au/people/seth-daily
related:
- how-google-ranks-pages
- make-title-h1-and-h2-tags-descriptive
- use-dashes-in-urls
- html-meta-tags

---

Do you find yourself reworking pages on your website that weren't created with SEO in mind?

One of the key challenges for a business is ensuring that its webpages are favored by search engines. It's a delicate balance between providing value to your audience and ticking the right boxes for search engine algorithms.

The best way to make sure your website has good SEO is to ensure that every webpage you create starts with solid SEO. To do this, you should use an SEO components checklist. The checklist below is tailored to incorporate best SEO practices for a new webpage. If you are creating a webpage, you should make sure your page includes all of the elements on the list.

However, not everybody who wants to create a webpage is actually doing the creation (sometimes they will give the task to a developer). Therefore, to make sure that content does not get lost in the creation process, it is important to have a streamlined procedure. Creating a GitHub Issue is the best way for non-developers to send the request for a new webpage to their developers. So, the best place to keep your checklist is in a GitHub Issue template that exists specifically for requesting a new page on your website. [See this rule about GitHub issue templates.](/github-issue-templates/)

The example below is the text in a GitHub Issue template for requesting a new webpage. The user replaces all the placeholders with their information, and when a developer creates the page they will know to include the important SEO components.

<!--endintro-->

::: greybox

Replace all the placeholders with information about the new page:

Template: if the page should follow an existing template, put it here (if not, write N/A). If you don't know where the template is but you have an example you'd like to follow (e.g. another Consulting page), put the link here.

{{ PAGE TEMPLATE }}<br><br>

Page Title: Must be descriptive and include primary keywords (Google-able). It should be no more than 60 characters.

{{ PAGE TITLE }}<br><br>

Meta Description: This is the preview that users see on Google (or other search engines). It must be a unique and clear summary of the page. It should also incorporate the primary keyword and other secondary keywords. It should be under 150 characters. If you have trouble making this, give ChatGPT your content and ask it to write one for you!

{{ META DESCRIPTION }}<br><br>

URI: Must be concise, clear, and should include the primary keywords. Use kebab case (e.g. use-dashes-and-lowercase)

{{ URI }}<br><br>

Internal Links (If applicable, include related links on the page):

{{ RELATED URLS }}<br><br>

Content guidelines:

* Headings - include an HTML title tag for each heading, with H1 for the main title H2 for subheadings, H3 for smaller subheadings

  * Only one H1 per page
  * The H1 should summarize the main content
  * Each heading must include keywords
  * Example:
    * H1 – SSW Educational
    * H2 - How SSW can help: Customized technology solutions

* Images - must include both alt text and descriptive captions
  * Alt text describes the image to search engines
  * Example:
    * <cat-flying.jpg>
    * Alt text - cat flying above city
    * Caption - Figure: A cat soars majestically above New York City.

* Content - where possible, add links and/or hyperlinks to other relevant pages on the website
  * Called 'internal linking', this gives pages credibility in the eyes of search engines
  * Example:
    * We are experts in Power BI. Our developers are also experienced in [database development](https://www.ssw.com.au/consulting/database-development).

Write/paste the content here, following the above guidelines:

{{ CONTENT }}
:::
::: good
Figure: A comprehensive SEO checklist for a GitHub Issue template
:::
