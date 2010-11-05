---
type: rule
title: Do you Add SSW Code Auditor, NUnit and Microsoft FxCop project files to your Solution
uri: do-you-add-ssw-code-auditor-nunit-and-microsoft-fxcop-project-files-to-your-solution
created: 2009-05-06T09:26:46.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> 
  <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a>, <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/netTools.aspx#NUnit">NUnit</a> and <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/netTools.aspx#FxCop">Microsoft FxCop</a> are tools to keep your code &quot;healthy&quot;. That is why they should be easily accessible in every solution so that they can be run with a double click of a mouse button. 
 </span>


  <p>&#160;</p>
<dl class="goodImage">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" alt="Code Auditor Project File" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/CodeAuditorProjectFile.gif" border="0" /> </dt>
</dl>
<p>To add a <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> file to your solution&#58; </p>
<ol>
    <li>Start up SSW Code Auditor </li>
    <li>Add a <b>new Job</b> </li>
    <li>Add a the solution file to be scanned </li>
    <li>Select the rules to be run </li>
    <li>Configure email (not required) </li>
    <li>Select <b>File &gt; Save As</b> (into the solution's folder as &quot;c<b>odeauditor.SSWCodeAuditor</b>&quot;) </li>
    <li>Open your Solution in Visual Studio </li>
    <li>Right click and <b>add existing file</b> </li>
    <li>Select the <b>SSW Code Auditor project file</b> </li>
    <li>&#160;Right click the newly added file and select &quot;<b>Open With</b>&quot;<br>
    <dl class="goodImage">
        <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" alt="Open With" src="/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/OpenWith.gif" border="0" /> </dt>
    </dl>
    </li>
    <li>&#160;Point it to the SSW Code Auditor executable </li>
</ol>
<br>
See <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBeingSoftwareConsultantsWorkingInATeam.aspx#CodeAuditor">Do you run SSW Code Auditor?</a> <br>
See <a shape="rect" href="/Management/RulesToSuccessfulProjects/Pages/CheckCodeByCodeAuditorBeforeCheckIn.aspx" id="Do you check your code by Code Auditor before check-in?">Do you check your code by Code Auditor before check-in?</a> <br>
To add a <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/netTools.aspx#FxCop">Microsoft FxCop</a> file to your solution&#58;
<ol>
    <li>Stat up <b>Microsoft FxCop</b> </li>
    <li>Create a <b>New Project</b> </li>
    <li>Right click the project and <b>Add Target</b> </li>
    <li>Select the Assembly (DLL/EXE) for the project </li>
    <li>Select <b>File &gt; Save Project As </b>(into the solution's folder as &quot;<b>fxcop.FxCop</b>&quot;) </li>
    <li>Open your Solution in Visual Studio </li>
    <li>Right click and <b>add existing file</b> </li>
    <li>Select the <b>Microsoft FxCop project file</b> </li>
    <li><b>Right click</b> the newly added file and select &quot;<b>Open With</b>&quot; </li>
    <li>Point it to the Microsoft FxCop executable </li>
</ol>
<br>
To add a <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/DeveloperGeneral/netTools.aspx#NUnit">NUnit</a> file to your solution&#58;
<ol>
    <li>Stat up <b>NUnit</b> </li>
    <li>Create a New Project by selecting <b>File &gt; New Project</b> and save it to your solution directory as &quot;<b>nunit.NUnit</b>&quot; </li>
    <li>From the <b>Project</b> menu select <b>Add Assembly</b> </li>
    <li>Select the Assembly (DLL/EXE) for the project that contains unit tests </li>
    <li>Select <b>File &gt; Save Project</b> </li>
    <li>Open your Solution in Visual Studio </li>
    <li>Right click and <b>add existing file</b> </li>
    <li>Select the <b>NUnit project file</b> </li>
    <li><b>Right click</b> the newly added file and select &quot;<b>Open With</b>&quot; </li>
    <li>Point it to the NUnit executable </li>
</ol>
<p>Now you can simply double click these project files to run the corresponding applications.</p>
<table class="clsSSWProductTable" id="table42" cellspacing="2" cellpadding="2" summary="Code Auditor">
    <tbody>
        <tr>
            <td>We have a program called <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Default.aspx">SSW Code Auditor</a> that implements this rule.</td>
        </tr>
    </tbody>
</table>



