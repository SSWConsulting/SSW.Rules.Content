---
seoDescription: Implement multilingual support in an Angular project using Internationalization (i18n), ngx-translate, or angular-gettext, each with its pros and cons
type: rule
title: Do you add multilingual support (Angular)?
uri: add-multilingual-support-on-angular
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Shane Ye
    url: https://ssw.com.au/people/shane-ye
  - title: Gabriel George
    url: https://ssw.com.au/people/gabriel-george
  - title: Sebastien Boissiere
    url: https://ssw.com.au/people/sebastien-boissiere
related: []
redirects:
  - do-you-add-multilingual-support-angular
  - do-you-add-multilingual-support-(angular)
created: 2018-11-13T22:06:41.000Z
archivedreason: null
guid: 6a959062-c8cf-419d-adbd-97aed99ea3e1
---

### How to implement multilingual support in an Angular project?

There are several ways of implementing multilingual support in an Angular project, the following libraries are popular:

**[Internationalization (i18n)](https://angular.dev/guide/i18n):** the standard Angular built-in module to help the application dealing with multilingual. It creates multiple language versions of your application.

**[ngx-translate](https://github.com/ngx-translate/core):** a library enhanced the Angular built-in feature, it supports not only template translations but can also be used in the code by APIs.


<!--endintro-->

`https://www.youtube.com/watch?v=KNTN-nsbV7M`  
**Video: Introduction to Internationalization in Angular (13mn)**

The following table shows the pros and cons of the 2 libraries:

|                                     | **Pros (+)**                                                                                                                                       | **Cons (-)**                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Internationalization** **(i18n)** | <ul class="p3"><li>Better support of displaying dates,</li><li>Better support for handling plural forms of words, and alternative text. </li><li>Runtime language switching support (since Angular 9+)</li></ul> | <ul class="ul1"><li class="li2">More complex setup initially</li><li class="li2">You can see the language in the URL.</li></ul>  |
| **ngx-translate**                   | <ul><li>It provides more powerful API support</li><li>It supports JSON files by default to store the translation resources</li><li>Simple runtime language switching</li></ul>               | <ul class="ul1"><li class="li2">It doesn't provide good support for plural forms and dates.</li><li class="li2">Third-party dependency that may not keep up with Angular updates.</li></ul> |

**Ngx-translate** provides the APIs which you can use to translate the resources in the code:

Angular's built-in i18n has significantly improved since Angular 9 with runtime language switching capabilities. Both solutions are viable, with **Angular i18n** being the recommended approach for new projects due to its official support and comprehensive features, while **ngx-translate** remains a good option for projects requiring simpler setup or existing implementations.