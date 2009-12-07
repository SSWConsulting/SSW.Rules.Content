---
type: rule
title: Do you distribute a product in Release mode?
uri: do-you-distribute-a-product-in-release-mode
created: 2009-05-05T06:48:04.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> We like to have debugging information in our application, so that we can view the line number information in the stack trace. However, we won't release our product in Debug mode, for example if we use &quot;#if Debug&quot; statement in our code we don't want them to be compiled in the release version. If we want line numbers, we simply need <b>Debugging Information</b>. You can change an option in the project settings so these will be generated in when using Release build. 
 </span>


  <dl class="goodCode">
    <dt>
    <pre>#if DEBUG MessageBox.Show(&quot;Application started&quot;); #endif</pre>
    </dt>
</dl>
<b>Figure&#58; Code that should only run in Debug mode, we certainly don't want this in the release version.</b>
<dl class="goodImage">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Debug configuration" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/DebugConfiguration.gif" /> </dt>
</dl>
<b>Figure&#58; Set&#160;&quot;Generate Debugging Information&quot; to True on the project properties page (VS 2003).</b>
<dl class="goodImage">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Advanced Build Settings" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/VS2005AdvancedBuildSettings.gif" /> </dt>
</dl>
<b>Figure&#58; Set&#160;&quot;Debug Info&quot; to &quot;pdb-only&quot; on the Advanced Build Settings page (VS 2005).</b>
<table id="table30" class="clsSSWProductTable" cellspacing="2" summary="Code Auditor" cellpadding="2">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx#Release">SSW Code Auditor</a> to check for this rule.</td>
        </tr>
    </tbody>
</table>



