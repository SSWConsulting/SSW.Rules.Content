---
type: rule
archivedreason:
title: Do you print and display your report on the web correctly?
guid: cc62742e-d48b-4f76-a4b4-49bfd5232ffd
uri: print-and-display-report-on-web
created: 2023-12-11T14:38:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- customization-do-you-know-which-version-of-sql-reporting-services-and-visual-studio-you-are-using
redirects: []

---

<!--endintro-->

A lot of the time, you will want a hard copy of your reports. Obviously reports are different sizes on screen and on paper, so you need to format your report so it exports to PDF and prints properly. Here's how.

1. Change the report's page width to 28cm (or 11in) and top and bottom margins to 0.5cm.

::: good  
![Figure: Good example - For proper printing, first change the Report's Page Width to 28cm (or 11in) and top and bottom margins to 0.5cm](reportpagewidth.gif)
:::

2. Change the Body width to 25.4cm (or 10in)

::: good  
![Figure: Good example - Then change the Report's Body Width to 25.4cm (or 10in)](reportbodywidth.gif)
:::

::: bad  
![Figure: Bad example - PDF page with 1cm margin (wasted much space on top and bottom)](RulesSQLRS7.jpg)  
:::

::: good  
![Figure: Good example - PDF page with 0.5cm margin (you have more room for content)](RSRuleMoreTopBottomPDF.png)
:::

You can see the 0.5cm margin looks much better than 1cm, and you have more space to organize your content, especailly for a landscape print view.

3. Resize report items (tables and charts) to fit the page. The easiest way to do this is to select (Ctrl+click) all report items that should span the whole width of the page, and set their Width property to 25.4cm (or 10in).

**Tip**: Export your report to PDF and do a print preview, so you don't have to print a lot of testing pages to find out the best page settings.

**Tip**: Remove top and bottom paddings in header and footer text can also give you more space.

**Note**: Reporting Services reports accept both inches and cm, so you can use either.

We have a program called [SSW Code Auditor](https://codeauditor.com/) to check for this rule.
