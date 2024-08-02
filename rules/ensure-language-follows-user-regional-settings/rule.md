---
type: rule
archivedreason:
title: Internationalization - Do you make sure your language follows the user's regional settings?
guid: ea1e46de-369e-4b4b-bb41-18ee507f56ec
uri: ensure-language-follows-user-regional-settings
created: 2024-08-02T11:08:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

Developers too often change the 'Language' settings on reports in order to make it look ok for how they want to see it. Without realizing that they are now not supporting multiple cultures.

<!--endintro-->

To do this, you need to set the 'Language' to **"=User!Language"**. Then the report will recognize user client's culture settings, e.g. IE's languages settings.

Now you can specify this on either the culture sensitive controls or the whole report. Generally, is better specify this property on the whole report.

::: bad  
![Figure: Bad example - Here the 'Language' setting is set to a specific culture](RSRulesLanguage4.jpg)  
:::

::: good  
![Figure: Good example - Here the 'Language' setting is set to '=User!Language' to detect user's culture automatically](RSRulesLanguage3.jpg)
:::

::: good  
![Figure: Good example - Now the data respects user's Language preference of IE in this case English (Australia)](RSRulesLanguage1.jpg)
:::

::: good  
![Figure: Good example - Likewise the data also respects user's Language preference of IE in this case Chinese (China)](RSRulesLanguage2.jpg)
:::

**Warning: Adding the 'User' who printed the report, stops all data-driven subscriptions**
When you try to add the 'User' your data-driven subscriptions fail with the following error:
'The '/GroupHealth' report has user profile dependencies and cannot be run unattended. (rsHasUserProfileDependencies)'.
The reason is the report doesn't know which language to choose
the workaround is to add a user function to fallback the error to a default language, like: "en-AU"

```
Public Function Language()
    Try
        Return Report.User!Language
    Catch
        Return "en-AU"
    End Try
End Function   
```

::: good  
Good example - Use above function to replace your reference to Report.User!Language it allow the subscription to work correctly
:::
