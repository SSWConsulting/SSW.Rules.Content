---
seoDescription: Code Analysis Tools to Improve Code Quality and Efficiency
type: rule
archivedreason:
title: Do you use the best Code Analysis tools?
guid: 48fb228d-a09e-4c52-9c6a-eddfff34f08f
uri: do-you-use-the-best-code-analysis-tools
created: 2012-03-16T08:43:44.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
  - title: Eric Phan
    url: https://ssw.com.au/people/eric-phan
related: []
redirects: []
---

Whenever you are writing code, you should always make sure it conforms to your team's standards. If everyone is following the same set of rules; someone else’s code will look more familiar and more like your code - ultimately easier to work with.

No matter how good a coder you are, you will always miss things from time to time, so it's a really good idea to have a tool that automatically scans your code and reports on what you need to change in order to improve it.

<!--endintro-->

Visual Studio has a great Code Analysis tool to help you look for problems in your code. Combine this with Jetbrains' ReSharper and your code will be smell free.

![Figure: You wouldn't play cricket without protective gear and you shouldn't code without protective tools](CricketHelmet.jpg)

The levels of protection are:

### Level 1

Get ReSharper to green on each file you touch. You want the files you work on to be left better than when you started. See [Do you follow the boyscout rule?](/follow-boy-scout-rule/)

You can run through a file and tidy it very quickly if you know 2 great keyboard shortcuts:

* Alt + [Page Down/Page Up] : Next/Previous Resharper Error / Warning
* Alt + Enter: Smart refactoring suggestions

![Figure: ReSharper will show Orange when it detects that there is code that could be improved](48bc81_image001.png)

![Figure: ReSharper will show green when all code is tidy](ReSharper-green.png)

### Level 2

Use [SSW CodeAuditor](https://codeauditor.com).

![Figure: CodeAuditor shows a lot of warnings in this test project](CodeAuditor.png)

**Note:** Document any rules you've turned off.

### Level 3

Use StyleCop to check that your code has consistent style and formatting.

![Figure: StyleCop shows a lot of warnings in this test project](StyleCopInVS2010.png)

### Level 4

Run Code Analysis (was FxCop) with the default settings or ReSharper with Code Analysis turned on.

![Figure: Run Code Analysis in Visual Studio](CodeAnalysisVS11.png)

![Figure: The Code Analysis results indicate there are 17 items that need fixing](codeanalysis.png)

### Level 5

Ratchet up your Code Analysis Rules until you get to 'Microsoft All Rules'.

![Figure: Start with the Minimum Recommended Rules, and then ratched up.](image003.png)

### Level 6

Document any rules you've turned off.

All of these rules allow you to disable rules that you're not concerned about. There's nothing wrong with disabling rules you don't want checked, but you should make it clear to developers why those rules were removed.

Create a **GlobalSuppressions.cs** file in your project with the rules that have been turned off and why.

![Figure: The suppressions file tells Code Analysis which rules it should disable for specific code blocks](suppressions-file.png)

**More Information:** [Do you make instructions at the beginning of a project and improve them gradually?](/do-you-make-instructions-at-the-beginning-of-a-project-and-improve-them-gradually) and <https://docs.microsoft.com/en-us/visualstudio/code-quality/in-source-suppression-overview>

### Level 7

The gold standard is to use [SonarQube](https://www.sonarqube.org/), which gives you the code analysis that the previous levels give you as wells as the ability to analyze technical debt and to see which code changes had the most impact to technical debt

![Figure: SonarQube workflow with Visual Studio and Azure DevOps](2016-06-08_12-59-38.png)

![Figure: SonarQube gives you the changes in code analysis results between each check-in](2016-06-08_12-59-53.png)
