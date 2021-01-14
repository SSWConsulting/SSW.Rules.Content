---
type: rule
archivedreason: 
title: Do you make external links open on a new tab?
guid: 92984462-7d50-4817-82b9-2db9685fa720
uri: do-you-make-external-links-open-on-a-new-tab
created: 2016-08-22T21:22:08.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- external-links-open-on-a-new-tab

---

External links should  **open in a new tab**  (a.k.a. use target="\_blank") - since browsers implemented tabs (replacing new window), it's considered a good practice to open external links in a different tab.

Main reasons are:

* Avoid 'Back-Button Fatigue';
* Keep 'User Flow';
* and keep a good track of Analytics




```
<a href="http://support.microsoft.com/support">Support</a>
```


Figure: Bad example - External link opening on the same tab



```
<a href="http://support.microsoft.com/support" target="_blank">Support</a>
```


Figure: Good example - External link opening in a new tab 

<!--endintro-->

### Related Rule


* [Do you make external links clear?](/do-you-make-external-links-clear)
