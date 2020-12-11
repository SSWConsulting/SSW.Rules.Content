---
type: rule
archivedreason: 
title: Do you use comments not exclusion files when you ignore a Code Analysis rule?
guid: 2733b6f3-1374-41eb-ba4e-d8188eaa1098
uri: do-you-use-comments-not-exclusion-files-when-you-ignore-a-code-analysis-rule
created: 2012-06-12T14:17:49.0000000Z
authors:
- id: 3
  title: Eric Phan
related: []

---

When running code analysis you may need to ignore some rules that aren't relevant to your application. Visual Studio has a handy way of doing thing. 
<!--endintro-->

[[goodExample]]
| ![The Solution and Projects are named consistently](code-analysis-bad-example.jpg)
![](code-analysis-good-example.jpg)<dl class="goodCode">    &lt;dt&gt;
    <pre>public partial class Account
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors", Justification="Gold Plating")]
        public Account()
        {
            this.Centres = new HashSet();
            this.AccountUsers = new HashSet();
            this.Campaigns = new HashSet();</pre>
    &lt;/dt&gt;</dl>Figure: Good Example - The Solution and Projects are named consistently
