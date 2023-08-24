---
type: rule
title: Do you use comments not exclusion files when you ignore a Code Analysis rule?
uri: do-you-use-comments-not-exclusion-files-when-you-ignore-a-code-analysis-rule
authors:
  - title: Eric Phan
    url: https://ssw.com.au/people/eric-phan
related: []
redirects: []
created: 2012-06-12T14:17:49.000Z
archivedreason: null
guid: 2733b6f3-1374-41eb-ba4e-d8188eaa1098
---

When running code analysis you may need to ignore some rules that aren't relevant to your application. Visual Studio has a handy way of doing thing. 
<!--endintro-->

::: bad
![Figure: Bad example -](code-analysis-bad-example.jpg)
:::

::: good
![Figure: Good example - The Solution and Projects are named consistently](code-analysis-good-example.jpg)
:::

```cs
public partial class Account
{
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors", Justification="Gold Plating")]
    public Account()
    {
        this.Centres = new HashSet();
        this.AccountUsers = new HashSet();
        this.Campaigns = new HashSet();
    }
}
```
::: good
Figure: Good example - The Solution and Projects are named consistently
:::
