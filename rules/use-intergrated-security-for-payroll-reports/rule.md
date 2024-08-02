---
type: rule
archivedreason:
title: Admin - Do you take advantage of 'Integrated Security' to do Payroll reports?
guid: 3a7d4544-16e8-46fe-aff4-b2161e216420
uri: use-intergrated-security-for-payroll-reports
created: 2024-08-02T14:42:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

<!--endintro-->

Payroll report should only show the records of the current user, Reporting Services support "Integrated Security" which you can use to identify the user who is running the report and only return relevant result for the current user.

::: bad  
![Figure: Bad example - Everyone can see others' rate changing history (maybe useful for administrative, but not for your employees)](RSRulesPayRollByUserIDT1.jpg)  
:::

::: good  
![Figure: Good example - The current employee can only see his own record](RSRulesPayRollByUserIDT2.jpg)
:::

To generate such a report, you need to use the filter on the data table:

![Figure: Specify the filters on your data table and select Globals->User!UserID](RSRulesPayRollByUserIDT3.jpg)

Note: 'Edit Expression' dialog is only available on RS 2005, but the UserID global variable is available on RS 2000.
