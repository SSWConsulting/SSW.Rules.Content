---
seoDescription: Ensure your reports display currency consistently across cultures by setting specific language rules for each currency field.
type: rule
archivedreason:
title: Internationalization - Do you make sure your language rule has an exception for Currency Fields?
guid: c54613d1-1e07-4cc1-9284-b34a34f3c376
uri: language-rule-exception-for-currency-fields
created: 2024-08-02T11:27:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

Currency formatting can vary significantly across cultures, and it's important to manage this effectively in your reports.

<!--endintro-->

Although we can make the report support multiple cultures (as per [Do you make sure your language follows the users regional settings?](https://www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLReportingServices.aspx#LanguageSetting)), we suggest you don't do this for currency fields. Instead:

1. Have the Language set specifically to the culture you want.
e.g. If you do a report for Australian Dollars, then it should be "English(Australia)"; if for Chinese Yuan, it should be "Chinese(People's Republic of China)". Because the format of currency should not change as per user's culture setting as $100 AUD <> 100 CNY !

2. Have the currency column header set include the currency.
Because $100 USD <> $100 AUD !

::: bad  
![Figure: Bad example - Using default language for currency field](RSCurrency_bad.gif)  
:::

::: good  
![Figure: Good example - This currency field stores Australian Dollars and will always display it that way](RSCurrency_good_au.gif)
:::

![Figure: AUD currency](RSCurrency_sample_au.gif)

::: good  
![Figure: Good example - This currency field stores Chinese Yuan and will always display it that way](RSCurrency_good_cn.gif)
:::

![Figure: Chinese Yuan currency](RSCurrency_sample_cn.gif)

If you don't want to get currency fields hard coded in reports, you can use an expression to read settings from your database.

::: good  
![Figure: Good example - Using specified language as per value of column CurrencyType in table SystemValue](RSCurrency_good_expression.gif)
:::
