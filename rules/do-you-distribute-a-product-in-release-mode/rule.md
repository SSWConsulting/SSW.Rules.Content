---
type: rule
archivedreason: 
title: Do you distribute a product in Release mode?
guid: fe6201ba-9b95-420c-80f5-9e02b14d12b2
uri: do-you-distribute-a-product-in-release-mode
created: 2009-05-05T06:48:04.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee
related: []

---

We like to have debugging information in our application, so that we can view the line number information in the stack trace. However, we won't release our product in Debug mode, for example if we use "#if Debug" statement in our code we don't want them to be compiled in the release version. If we want line numbers, we simply need  **Debugging Information** . You can change an option in the project settings so these will be generated in when using Release build.   
<!--endintro-->
<dl class="goodCode">    &lt;dt&gt;
    <pre>#if DEBUG MessageBox.Show("Application started"); #endif</pre>
    &lt;/dt&gt;</dl>**Figure: Code that should only run in Debug mode, we certainly don't want this in the release version.** <dl class="goodImage">    &lt;dt&gt;<img style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" alt="Debug configuration" src="DebugConfiguration.gif"> &lt;/dt&gt;</dl>**Figure: Set "Generate Debugging Information" to True on the project properties page (VS 2003).** <dl class="goodImage">    &lt;dt&gt;<img style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" alt="Advanced Build Settings" src="VS2005AdvancedBuildSettings.gif"> &lt;/dt&gt;</dl>**Figure: Set "Debug Info" to "pdb-only" on the Advanced Build Settings page (VS 2005).** 

| We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor/Default.aspx) to check for this rule. |
| --- |
