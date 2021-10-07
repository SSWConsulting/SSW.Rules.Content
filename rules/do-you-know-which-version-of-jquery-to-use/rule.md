---
type: rule
archivedreason: Can’t keep it up-to-date + we don't use jQuery. Approved by Anthony N
title: Do you know which version of jQuery to use?
guid: 7cef792d-fa7f-429c-a002-5328196286f7
uri: do-you-know-which-version-of-jquery-to-use
created: 2013-04-29T06:20:48.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related:
- do-you-use-the-ready-function
- do-you-use-bundling-and-or-amd
- do-you-treat-javascript-like-a-real-language
- do-you-use-hyperlinks-instead-of-javascript-to-open-pages
redirects: []

---

New jQuery versions are released regularly, but you shouldn't always use the latest version.

<!--endintro-->

If your site needs to support Internet Explorer 6, 7, and 8, you should not use the latest version of jQuery.  You should use the latest version 1.9.x instead.

The jQuery authors made a decision to deprecate support for older versions of IE from version 2.0 onwards.  Even though support for these browsers has been discontinued, the authors have commited to maintaining version 1.9 so it's safe to keep using it.

For more information about the changes, see the [jQuery blog post about the version 2.0 release](https://blog.jquery.com/).
