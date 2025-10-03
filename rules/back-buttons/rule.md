---
seoDescription: Always include a Back button in multi-step wizards to improve usability, reduce frustration, and let users safely navigate between steps.
type: rule
archivedreason:
title: Do you have a "Back" button?
guid: cd64ef97-75d9-4158-b732-f319de35069b
uri: back-buttons
created: 2009-12-04T09:16:18.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: 
  - label-buttons-consistently
redirects:
  - do-you-use-＂-back＂-instead-of-＂-previous＂-or-other-variations
  - do-you-use-back-instead-of-previous-or-other-variations
---

When building multi-step wizards (e.g. forms, onboarding flows, or setup processes), always provide a Back button—unless there's a very good reason not to.

A "Back" button gives users confidence that they can safely navigate through the steps without fear of losing progress. It helps reduce frustration and increases completion rates, especially when users need to review or correct something in earlier steps.

<!--endintro-->

::: good img-medium
![Figure: Good example Back button is clearly visible](back-button-bad.png)
:::

::: bad img-medium
![Figure: Bad example - User hits "Next" and can't go back to change their answer](back-button-good.png)
:::

## Implementation tips

* Place the "Back" button **to the left** of the "Next" or "Submit" button
* [Use consistent labels](/label-buttons-consistently/) (don't use “Previous" or other variations).
   ::: info
   According to [Design Specifications and Guidelines - User Assistance](https://learn.microsoft.com/en-us/previous-versions/ms997609%28v=msdn.10%29#window-design?WT.mc_id=DT-MVP-33518), the commands for navigating through a wizard should be **"&lt; Back"** and **"Next &gt;"**.
   :::
* [Use icons to enforce the action meaning](/enforce-the-text-meaning-with-icons-and-emojis)
  
::: info
**Note:** Disabling or hiding the Back button is OK when:

* The previous step doesn’t exist (e.g. it's the first step)
* It's a single-step flow with no navigation needed
:::
