---
type: rule
archivedreason: 
title: Do you use comments not exclusion files when you ignore a Code Analysis rule?
guid: 2733b6f3-1374-41eb-ba4e-d8188eaa1098
uri: do-you-use-comments-not-exclusion-files-when-you-ignore-a-code-analysis-rule
created: 2012-06-12T14:17:49.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects: []

---


When running code analysis you may need to ignore some rules that aren't relevant to your application. Visual Studio has a handy way of doing thing.
<br><excerpt class='endintro'></excerpt><br>
<img alt="code-analysis-bad-example" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/code-analysis-bad-example" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureBad">Figure&#58; Good Example - The Solution and Projects are named consistently</span>
<img alt="code-analysis-good-example" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/code-analysis-good-example" class="ms-rteCustom-ImageArea" />
<dl class="goodCode">
    <dt>
    <pre>public partial class Account
    &#123;
        [System.Diagnostics.CodeAnalysis.SuppressMessage(&quot;Microsoft.Usage&quot;, &quot;CA2214&#58;DoNotCallOverridableMethodsInConstructors&quot;, Justification=&quot;Gold Plating&quot;)]
        public Account()
        &#123;
            this.Centres = new HashSet();
            this.AccountUsers = new HashSet();
            this.Campaigns = new HashSet();</pre>
    </dt>
</dl>
<span class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - The Solution and Projects are named consistently</span>


