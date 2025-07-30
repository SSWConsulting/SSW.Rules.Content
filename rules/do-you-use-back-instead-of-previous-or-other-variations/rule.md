---
seoDescription: Use "&lt; Back" instead of "Previous" or other variations to navigate through records and follow Microsoft's design specifications for consistency.
type: rule
archivedreason:
title: Do you use "Back" instead of "Previous" (or other variations)?
guid: cd64ef97-75d9-4158-b732-f319de35069b
uri: do-you-use-back-instead-of-previous-or-other-variations
created: 2009-12-04T09:16:18.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
related: []
redirects:
  - do-you-use-＂-back＂-instead-of-＂-previous＂-or-other-variations
---

According to [Design Specifications and Guidelines - User Assistance](https://docs.microsoft.com/en-us/previous-versions/ms997609%28v=msdn.10%29?WT.mc_id=DT-MVP-33518), the commands for navigating through a wizard should be "&lt; Back" and "Next &gt;".

<!--endintro-->

When your site needs a link to iterate backward through records we recommend that you use "&lt; Back" instead of "&lt; Previous".

There are a few reasons for this:

1. This is the standard used in Microsoft Installation files. MSIs are the most widely used installation package available today.
2. Internet Explorer and several other lesser-known browsers use a Back button to iterate back through webpages, so your visitors will automatically know what your "&lt; Back" link does.
3. It is important to keep consistency on your pages.

Below is an example of a Good "&lt; Back" link versus some Bad variations.

::: bad  
![Figure: This is Bad because it says "Previous" instead of "Back"](badpreviouslink.gif)  
:::

::: bad  
![Figure: This is bad because it has too many "<"s or it has no space between the "<" and the "Back"](badbacklink.gif)  
:::

::: good  
![Figure: A Good example of a "< Back" link](textboxeswithshowbutton.gif)  
:::
