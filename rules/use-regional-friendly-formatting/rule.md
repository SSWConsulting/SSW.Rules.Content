---
type: rule
archivedreason:
title: Internationalization - Do you use regional friendly formatting?
guid: 5dbeac8d-d20e-44b4-9efd-f7acd2184bda
uri: use-regional-friendly-formatting
created: 2023-12-11T14:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

Currency formatting is not universal - therefore, it's crucial to adapt the formatting to match regional conventions.

<!--endintro-->

In Australia, one million is written this way: $1,000,000.00.
But in Brazil, one million is written that way: $1.000.000,00. 

So, in order to be culturally sensitive, try and use regional friendly formatting.

::: bad  
![Figure: Bad example - Bad Number Format](RSNumberFormatBad.jpg)  
:::

::: good  
![Figure: Good example - Good Number Format](RSNumberFormatGood.jpg) 
:::

::: bad  
![Figure: Bad example - Bad Currency Format](RSCurrencyFormatBad.jpg)  
:::

::: good  
![Figure: Good example - Good Currency Format](RSCurrencyFormatGood.jpg) 
:::

::: bad  
![Figure: Bad example - Bad Percentage Format](RSPercentageFormatBad.jpg)  
:::

::: good  
![Figure: Good example - Good Percentage Format](RSPercentageFormatGood.jpg) 
:::
